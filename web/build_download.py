#!/usr/bin/env python3
"""Build the public blank starter ZIP using the canonical workspace creator."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'web' / 'downloads'

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='underwriter-public-') as temporary:
        workspace = Path(temporary) / 'underwriter-starter'
        subprocess.run([sys.executable, str(ROOT / 'scripts/create_workspace.py'), '--firm', 'Your firm - unconfigured starter', '--output', str(workspace)], check=True)
        manifest = json.loads((workspace / 'DELIVERY-MANIFEST.json').read_text())
        archive = OUT / 'underwriter-starter.zip'
        staged = Path(temporary) / archive.name
        with zipfile.ZipFile(staged, 'w', zipfile.ZIP_DEFLATED) as package:
            for path in sorted(workspace.rglob('*')):
                if path.is_file():
                    package.write(path, str(Path(workspace.name) / path.relative_to(workspace)))
            package.writestr('underwriter-starter/deals/', '')
        archive.write_bytes(staged.read_bytes())
        checksum = hashlib.sha256(archive.read_bytes()).hexdigest()
        (OUT / 'underwriter-starter.sha256').write_text(checksum + '  ' + archive.name + '\n')
        (OUT / 'release.json').write_text(json.dumps({'source_commit': manifest['source_commit'], 'sha256': checksum, 'bytes': archive.stat().st_size, 'customer_data_included': False, 'providers_configured': False}, indent=2) + '\n')
        print(json.dumps({'archive': str(archive), 'bytes': archive.stat().st_size, 'sha256': checksum}))

if __name__ == '__main__':
    main()
