#!/usr/bin/env python3
"""Import a browser research export into a new local deal, without inventing retained files."""
import argparse
from datetime import date,datetime,timezone
import hashlib,json,re,uuid
from pathlib import Path
from urllib.parse import urlsplit

def bounded(value,limit,required=False):
    if not isinstance(value,str) or len(value)>limit or (required and not value.strip()):
        raise ValueError('Invalid or oversized text field')
    return value

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace',type=Path,required=True)
    parser.add_argument('--file',type=Path,required=True)
    parser.add_argument('--slug',required=True)
    args=parser.parse_args()
    root=args.workspace.expanduser().resolve()
    if not (root/'FIRM.json').is_file() or not (root/'deals').is_dir() or (root/'deals').is_symlink():
        parser.error('Choose an initialized firm workspace with a regular deals directory')
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',args.slug) or len(args.slug)>80:
        parser.error('Use a lowercase deal slug up to 80 characters')
    source=args.file.expanduser()
    if source.is_symlink() or not source.is_file() or source.stat().st_size>2*1024*1024:
        parser.error('Choose a regular browser-export JSON file up to 2 MB')
    original=source.read_bytes();raw=json.loads(original)
    if raw.get('version')!=1 or raw.get('kind')!='underwriter-browser-workspace':
        parser.error('Unsupported browser export')
    deal=raw['deal'];browser_id=str(uuid.UUID(deal['id']))
    name=bounded(deal['name'],160,True);address=bounded(deal['address'],400,True)
    notes={key:bounded(deal.get(key,''),limit) for key,limit in [('question',5000),('facts',15000),('assumptions',15000)]}
    sources=deal.get('sources');records=[];ids=set()
    if not isinstance(sources,list) or len(sources)>200:parser.error('Invalid source collection')
    for item in sources:
        identity=str(uuid.UUID(item['id']))
        if identity in ids:parser.error('Duplicate source identity')
        ids.add(identity)
        title=bounded(item['title'],200,True);url=bounded(item.get('url',''),2000)
        if url:
            parsed=urlsplit(url)
            if parsed.scheme not in ['http','https'] or not parsed.netloc or parsed.username or parsed.password:
                parser.error('Invalid source URL')
        published=bounded(item.get('published',''),10)
        if published and date.fromisoformat(published).isoformat()!=published:parser.error('Invalid publication date')
        recorded=bounded(item['recorded'],40,True);datetime.fromisoformat(recorded.replace('Z','+00:00'))
        entry={'browser_source_id':identity,'title':title,'origin':url,'source_as_of':published or 'unknown','browser_recorded_at':recorded,'claims_verified':False,'original_retained':False}
        if 'sha256' in item:
            digest=item['sha256'];size=item.get('bytes')
            if not isinstance(digest,str) or not re.fullmatch('[a-f0-9]{64}',digest) or type(size) is not int or not 0<=size<=20*1024*1024:parser.error('Invalid original-file fingerprint')
            entry.update(sha256=digest,bytes=size,file_name=bounded(item['fileName'],255,True))
        records.append(entry)
    destination=root/'deals'/args.slug
    destination.mkdir() # Exclusive. Never merge into or overwrite an existing deal.
    (destination/'research').mkdir()
    now=datetime.now(timezone.utc).isoformat()
    def write(name,value):
        with (destination/name).open('x') as file:json.dump(value,file,indent=2)
    write('deal.json',{'id':str(uuid.uuid4()),'browser_id':browser_id,'slug':args.slug,'name':name,'address':address,'stage':'intake','created_at':now,'verified':False})
    write('sources.json',[])
    write('browser-source-records.json',records)
    write('browser-import.json',{'imported_at':now,'sha256':hashlib.sha256(original).hexdigest(),'bytes':len(original),'original_files_included':False})
    with (destination/'browser-workspace.json').open('xb') as file:file.write(original)
    (destination/'00-summary.md').write_text(f'# {name}\n\nLocation: {address}\n\nImported author-supplied research; not independently verified.\n\n## Research question\n{notes["question"]}\n\n## Known facts (author supplied)\n{notes["facts"]}\n\n## Assumptions and open questions\n{notes["assumptions"]}\n\nOriginal files are not embedded. Use the source command to retain originals. Browser fingerprints remain in browser-source-records.json until the corresponding bytes are retained.\n')
    print(json.dumps({'deal':str(destination),'browser_source_records':len(records),'retained_originals':0}))

if __name__=='__main__':
    try:main()
    except (OSError,ValueError,KeyError,TypeError) as error:
        raise SystemExit('Import failed; any partially created new deal directory is retained for inspection: '+str(error))
