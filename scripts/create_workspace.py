#!/usr/bin/env python3
"""Create a new firm workspace from the tracked toolkit; no network or provider setup."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
ROOTS = {'onboarding', 'reference', 'templates', 'plugins', 'docs', 'brand', 'catalog', 'memory'}
FILES = {'LICENSE', 'SECURITY.md', 'WALKTHROUGH.md', 'START-HERE.md', 'INSTALL.md', 'scripts/deal_workspace.py'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--firm', required=True)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    firm = args.firm.strip()
    if not firm or len(firm) > 160 or any(ord(c) < 32 for c in firm):
        parser.error('Supply a firm name of 1 to 160 characters without control characters')
    output = args.output.expanduser().resolve()
    if output == ROOT or ROOT in output.parents or output.exists() or not output.parent.is_dir():
        parser.error('Choose a new directory outside this repository with an existing parent')
    status = subprocess.check_output(['git', 'status', '--porcelain', '--untracked-files=no'], cwd=ROOT, text=True)
    if status.strip():
        parser.error('Commit tracked source changes first so the delivery matches one revision')
    commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    entries = subprocess.check_output(['git', 'ls-tree', '-r', '-z', 'HEAD'], cwd=ROOT).split(b'\0')
    selected = []
    for entry in filter(None, entries):
        metadata, raw_path = entry.split(b'\t', 1)
        mode, kind, blob = metadata.decode().split()
        name = raw_path.decode()
        path = Path(name)
        if path.parts[0] not in ROOTS and name not in FILES:
            continue
        if mode not in ('100644', '100755') or kind != 'blob':
            raise ValueError('Unsupported source entry: ' + name)
        if any(part.startswith('.') for part in path.parts) or path.suffix in {'.pem', '.key', '.env'}:
            continue
        selected.append((name, blob, mode))
    if not selected:
        raise ValueError('No tracked toolkit content found')
    output.mkdir(mode=0o700)
    marker = output / 'INSTALL-INCOMPLETE'
    marker.write_text('Workspace creation did not finish. Do not use as a delivery.\n')
    manifest = []
    for name, blob, mode in selected:
        content = subprocess.check_output(['git', 'cat-file', 'blob', blob], cwd=ROOT)
        dest = output / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(content)
        dest.chmod(0o700 if mode == '100755' else 0o600)
        manifest.append({'path': name, 'bytes': len(content), 'sha256': hashlib.sha256(content).hexdigest()})
    instructions = '''# Underwriter workspace\n\nRead FIRM.json for workspace identity, then reference/rigor-standard.md and reference/underwriting-model.md. Use templates/sources.md to retain evidence with dates and distinguish observations, assumptions and calculations.\n\nStart each engagement by completing onboarding/user-intake.md with the firm's actual objectives. Do not use example profiles as real people or assume a tool is connected because it is listed in catalog/TOOL-CATALOG.md. Check the current runtime's available tools before choosing a workflow.\n\nThe playbooks under plugins/underwriter-os/skills are reference instructions. Claude-specific commands are not executable Codex integrations; use only available, authorized equivalents and state any missing capability. Do not install connectors, send messages, incur costs or change external records merely because a playbook suggests it. Follow the firm's explicit authorization.\n\nKeep deal work under deals/, with separate source evidence and derived analysis. Never invent market data, identify sample output as real, or describe an unverified deal as investment-ready. Preserve source artifacts and log material assumptions. Optional voice and data providers require the firm's own configured access.\n'''
    (output / 'AGENTS.md').write_text(instructions)
    (output / 'CLAUDE.md').write_text(instructions)
    (output / 'FIRM.json').write_text(json.dumps({'name': firm, 'source_commit': commit, 'configured_providers': [], 'customer_acceptance_verified': False}, indent=2) + '\n')
    (output / 'deals').mkdir()
    for name in ('AGENTS.md', 'CLAUDE.md', 'FIRM.json'):
        content = (output / name).read_bytes()
        manifest.append({'path': name, 'bytes': len(content), 'sha256': hashlib.sha256(content).hexdigest()})
    (output / 'DELIVERY-MANIFEST.json').write_text(json.dumps({'source_commit': commit, 'files': manifest, 'provider_setup_performed': False, 'release_verified': False}, indent=2) + '\n')
    marker.rename(output / 'WORKSPACE-CREATED')
    print(json.dumps({'workspace': str(output), 'files': len(manifest), 'source_commit': commit, 'provider_setup_performed': False}))

if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print('Workspace creation failed: ' + str(error), file=sys.stderr)
        sys.exit(1)
