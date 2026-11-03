#!/usr/bin/env python3
"""Create deterministic skill ZIP and checksum manifest from an explicit allowlist."""
import hashlib
import json
import subprocess
import zipfile
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
subprocess.run(['python3', str(ROOT / 'scripts/check_release.py')], check=True)
version = (ROOT / 'VERSION').read_text().strip()
out = ROOT / 'dist'
out.mkdir(exist_ok=True)
archive = out / 'stylemoth-skill.zip'
files = [(ROOT / 'README.md', 'README.md')]
files += [(p, str(p.relative_to(ROOT / 'skills'))) for p in sorted((ROOT / 'skills/stylemoth').rglob('*'))
          if p.is_file() and not p.is_symlink() and '__pycache__' not in p.parts and p.suffix != '.pyc']
with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
    for p, name in files:
        info = zipfile.ZipInfo(name, (2026, 1, 1, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        z.writestr(info, p.read_bytes())
manifest = {'version': version, 'repository': 'https://github.com/devdsgnn/stylemoth-skills',
            'sha256': hashlib.sha256(archive.read_bytes()).hexdigest()}
(out / 'stylemoth-skill.json').write_text(json.dumps(manifest, indent=2) + '\n')
print(archive)
