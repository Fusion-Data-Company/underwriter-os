#!/usr/bin/env python3
"""Package an operator-reviewed firm workspace. Does not configure or approve it."""
import argparse, hashlib, json, re, zipfile
from pathlib import Path

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--workspace',type=Path,required=True)
    p.add_argument('--order',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args(); root=a.workspace.resolve(); out=a.output.resolve()
    if a.workspace.is_symlink() or not root.is_dir() or out.exists() or root in out.parents:
        p.error('Use a regular reviewed workspace and a new archive path outside it')
    order=json.loads(a.order.read_text()); manifest=json.loads((root/'DELIVERY-MANIFEST.json').read_text()); firm=json.loads((root/'FIRM.json').read_text()); handoff=json.loads((root/'SERVICE-HANDOFF.json').read_text())
    if firm.get('name')!=order['request']['firm'] or handoff.get('engagementId')!=order['id'] or handoff.get('quoteRevision')!=order['accepted_revision'] or handoff.get('runtime')!=order['request']['runtime']:
        p.error('Workspace identity, runtime and accepted quote must match the paid engagement')
    if handoff.get('operatorReviewed') is not True or not isinstance(handoff.get('completedScope'),str) or len(handoff['completedScope'].strip())<20 or not isinstance(handoff.get('acceptanceEvidence'),list) or not handoff['acceptanceEvidence'] or any(not isinstance(x,str) or len(x.strip())<10 for x in handoff['acceptanceEvidence']):
        p.error('Supply actual operator-reviewed scope and acceptance evidence in SERVICE-HANDOFF.json')
    if (root/'INSTALL-INCOMPLETE').exists() or not re.fullmatch(r'[0-9a-f]{40}',manifest.get('source_commit','')):
        p.error('Workspace is incomplete or has no committed source provenance')
    selected=[]; seen=set()
    for record in manifest['files']:
        name=record['path']; rel=Path(name); path=root/rel
        if rel.is_absolute() or '..' in rel.parts or any(x.startswith('.') for x in rel.parts) or name in seen or path.suffix.lower() in {'.env','.key','.pem','.p12'} or any((root/Path(*rel.parts[:i])).is_symlink() for i in range(1,len(rel.parts)+1)) or not path.is_file():
            p.error('Invalid or duplicate manifest path: '+name)
        data=path.read_bytes()
        if len(data)!=record['bytes'] or hashlib.sha256(data).hexdigest()!=record['sha256']:
            p.error('Manifest hash does not match reviewed file: '+name)
        if re.search(rb'(?:sk_live_|sk_test_|sk-ant-|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY)',data):
            p.error('Credential-like content detected in '+name)
        seen.add(name);selected.append((name,data))
    if not {'LICENSE','FIRM.json','AGENTS.md','CLAUDE.md'}.issubset(seen):p.error('Required toolkit identity or license missing')
    if 'SERVICE-HANDOFF.json' not in seen:selected.append(('SERVICE-HANDOFF.json',(root/'SERVICE-HANDOFF.json').read_bytes()))
    selected.append(('DELIVERY-MANIFEST.json',(root/'DELIVERY-MANIFEST.json').read_bytes()))
    if sum(len(data) for _,data in selected)>15000000:p.error('Delivery exceeds the bounded 15 MB source limit')
    with zipfile.ZipFile(out,'x',zipfile.ZIP_DEFLATED) as archive:
        for name,data in selected:archive.writestr('underwriter-firm/'+name,data)
    data=out.read_bytes()
    if len(data)>4000000:p.error('Archive exceeds the hosted download limit; use a separately scoped delivery')
    print(json.dumps({'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'deliveryNote':handoff['completedScope'],'sourceCommit':manifest['source_commit']}))
if __name__=='__main__':main()
