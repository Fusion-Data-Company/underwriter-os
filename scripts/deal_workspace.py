#!/usr/bin/env python3
"""Create deal folders and retain source evidence without network access."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import uuid


def stamp():
    return datetime.now(timezone.utc).isoformat()


def write_json(path, value):
    temporary = path.with_name(path.name + '.' + uuid.uuid4().hex + '.tmp')
    temporary.write_text(json.dumps(value, indent=2) + '\n')
    os.replace(temporary, path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, required=True)
    commands = parser.add_subparsers(dest='command', required=True)
    create = commands.add_parser('create')
    create.add_argument('--name', required=True)
    create.add_argument('--slug', required=True)
    add = commands.add_parser('source')
    add.add_argument('--slug', required=True)
    add.add_argument('--file', required=True, type=Path)
    add.add_argument('--title', required=True)
    add.add_argument('--origin', required=True, help='Original source URL or document provenance')
    add.add_argument('--as-of', required=True, help='Source publication date YYYY-MM-DD; use unknown when absent')
    commands.add_parser('list')
    args = parser.parse_args()
    workspace = args.workspace.expanduser().resolve()
    if not (workspace / 'FIRM.json').is_file() or not (workspace / 'deals').is_dir():
        parser.error('Choose an initialized firm workspace')
    if args.command == 'list':
        deals = []
        for path in sorted((workspace / 'deals').glob('*/deal.json')):
            if path.is_symlink() or path.parent.is_symlink():
                continue
            record = json.loads(path.read_text())
            record['source_count'] = len(json.loads((path.parent / 'sources.json').read_text()))
            deals.append(record)
        print(json.dumps({'deals': deals}, indent=2))
        return
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', args.slug) or len(args.slug) > 80:
        parser.error('Use a lowercase alphanumeric deal slug with hyphens, maximum 80 characters')
    deal = workspace / 'deals' / args.slug
    if deal.is_symlink():
        parser.error('Deal symlinks are not supported')
    if args.command == 'create':
        name = args.name.strip()
        if not name or len(name) > 200 or any(ord(c) < 32 for c in name):
            parser.error('Supply a deal name of 1 to 200 characters')
        deal.mkdir()  # Exclusive: never overwrite an existing deal.
        (deal / 'research').mkdir()
        write_json(deal / 'deal.json', {'id': str(uuid.uuid4()), 'slug': args.slug, 'name': name, 'stage': 'intake', 'created_at': stamp(), 'verified': False})
        write_json(deal / 'sources.json', [])
        (deal / '00-summary.md').write_text('# ' + name + '\n\nStage: intake. No research or underwriting has been verified.\n\n## Objective\nNot supplied.\n\n## Next decision\nNot supplied.\n\n## Missing information\nProperty identity, strategy, financial records, market evidence and decision criteria.\n')
        for template, dest in [('site-one-pager.md', 'site-one-pager.md'), ('market-study.md', 'market-study.md'), ('investment-memo.md', 'ic-memo.md')]:
            source = workspace / 'templates' / template
            if source.is_file():
                (deal / dest).write_text('<!-- UNFILLED TEMPLATE: not a completed analysis -->\n' + source.read_text().replace('{{DEAL_NAME}}', name))
        print(json.dumps({'deal': str(deal), 'stage': 'intake'}))
        return
    if not (deal / 'deal.json').is_file():
        parser.error('Create the deal before adding evidence')
    source = args.file.expanduser()
    if source.is_symlink() or not source.is_file() or source.name.startswith('.') or source.suffix.lower() in {'.env', '.pem', '.key'}:
        parser.error('Choose a regular source document, not a hidden or credential file')
    if args.as_of != 'unknown':
        datetime.strptime(args.as_of, '%Y-%m-%d')
    if not args.title.strip() or not args.origin.strip():
        parser.error('Source title and provenance are required')
    lock = deal / '.source-import.lock'
    fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    staging = deal / 'research' / (uuid.uuid4().hex + '.partial')
    try:
        os.close(fd)
        shutil.copyfile(source, staging)
        digest = hashlib.sha256()
        with staging.open('rb') as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b''):
                digest.update(chunk)
        registry = json.loads((deal / 'sources.json').read_text())
        sha = digest.hexdigest()
        existing = next((entry for entry in registry if entry['sha256'] == sha), None)
        if existing:
            print(json.dumps({'source': existing, 'already_present': True}))
            return
        name = sha + source.suffix.lower()
        os.replace(staging, deal / 'research' / name)
        entry = {'id': 'S' + str(len(registry) + 1), 'title': args.title.strip(), 'origin': args.origin.strip(), 'source_as_of': args.as_of, 'retained_at': stamp(), 'sha256': sha, 'bytes': (deal / 'research' / name).stat().st_size, 'file': 'research/' + name, 'claims_verified': False}
        registry.append(entry)
        write_json(deal / 'sources.json', registry)
        print(json.dumps({'source': entry, 'already_present': False}))
    finally:
        staging.unlink(missing_ok=True)
        lock.unlink(missing_ok=True)

if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError) as error:
        print('Deal operation failed: ' + str(error), file=sys.stderr)
        sys.exit(1)
