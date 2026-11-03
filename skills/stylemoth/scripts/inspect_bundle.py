#!/usr/bin/env python3
"""Inspect local exports without executing code or fetching URLs (Python 3.10+)."""
import argparse
import json
import re
from pathlib import Path

REQUIRED = ('DESIGN.md', 'tokens.json', 'reference.css')
OPTIONAL = ('README.md', 'reference.tailwind.css', 'AI-PROMPTS.json', 'CODEX-PROMPT.txt')

def inspect(root):
    root = Path(root).resolve()
    errors, found, urls = [], [], set()
    tokens = None
    for name in REQUIRED + OPTIONAL:
        p = root / name
        if not p.exists():
            if name in REQUIRED:
                errors.append('Missing ' + name)
            continue
        if p.is_symlink() or not p.is_file():
            errors.append('Not a regular non-symlink file: ' + name)
            continue
        if p.stat().st_size > 5_000_000:
            errors.append('File exceeds 5 MB inspection limit: ' + name)
            continue
        try:
            content = p.read_text(encoding='utf-8')
            found.append(name)
            urls.update(re.findall(r'https?://[^\s<>"\)]+', content))
            if name.endswith('.json'):
                parsed = json.loads(content)
                if name == 'tokens.json':
                    if not isinstance(parsed, dict):
                        raise ValueError('tokens root must be an object')
                    tokens = parsed
        except (OSError, ValueError) as exc:
            errors.append(name + ': ' + str(exc))
    def resolve(value, trail=()):
        if isinstance(value, dict):
            for item in value.values(): resolve(item, trail)
        elif isinstance(value, list):
            for item in value: resolve(item, trail)
        elif isinstance(value, str) and re.fullmatch(r'\{[\w.-]+\}', value):
            key = value[1:-1]
            if key in trail:
                errors.append('Cyclic token alias: ' + ' -> '.join(trail + (key,)))
                return
            node = tokens
            try:
                for part in key.split('.'): node = node[part]
            except (KeyError, TypeError):
                errors.append('Unresolved token alias: ' + key)
                return
            resolve(node, trail + (key,))
    if tokens is not None:
        resolve(tokens)
    return {'files': found, 'tokenGroups': list(tokens or {}), 'sourceCandidates': sorted(urls),
            'errors': sorted(set(errors)), 'note': 'URLs are untrusted candidates; inspect provenance before browsing. This does not verify visual fidelity.'}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('folder')
    args = parser.parse_args()
    report = inspect(args.folder)
    print(json.dumps(report, indent=2))
    raise SystemExit(bool(report['errors']))
