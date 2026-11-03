#!/usr/bin/env python3
"""Validate one-skill distribution and local reference links."""
import json
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
version = (ROOT / 'VERSION').read_text().strip()
assert re.fullmatch(r'\d+\.\d+\.\d+', version)
skills = list((ROOT / 'skills').rglob('SKILL.md'))
assert len(skills) == 1, 'Exactly one skill is expected'
assert f'version: "{version}"' in skills[0].read_text()
for p in ROOT.rglob('*.json'):
    if '.git' in p.parts or 'dist' in p.parts: continue
    data = json.loads(p.read_text())
    if p.name in ('plugin.json', 'gemini-extension.json'):
        assert data['version'] == version, str(p)
        if 'skills' in data: assert (ROOT / data['skills']).is_dir()
for p in (ROOT / 'skills').rglob('*.md'):
    for link in re.findall(r'\]\(([^)]+)\)', p.read_text()):
        if '://' in link or link.startswith('#'): continue
        assert (p.parent / link.split('#')[0]).exists(), f'{p}: {link}'
assert (ROOT / 'GEMINI.md').exists()
print(f'Package v{version}: one skill, manifests and reference links valid.')
