#!/usr/bin/env python3
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
path = Path(__file__).resolve().parents[1] / 'skills/stylemoth/scripts/inspect_bundle.py'
spec = importlib.util.spec_from_file_location('inspector', path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
class BundleTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / 'DESIGN.md').write_text('# System')
        (self.root / 'reference.css').write_text(':root {}')
    def tearDown(self): self.tmp.cleanup()
    def check_tokens(self, data):
        (self.root / 'tokens.json').write_text(json.dumps(data))
        return module.inspect(self.root)['errors']
    def test_valid_alias(self):
        self.assertEqual(self.check_tokens({'a': {'$value': '#fff'}, 'b': {'$value': '{a}'}}), [])
    def test_missing_file(self):
        self.assertIn('Missing tokens.json', module.inspect(self.root)['errors'])
    def test_missing_alias(self):
        self.assertTrue(self.check_tokens({'a': '{missing}'}))
    def test_cycle(self):
        self.assertTrue(self.check_tokens({'a': '{b}', 'b': '{a}'}))
    def test_invalid_json(self):
        (self.root / 'tokens.json').write_text('{bad')
        self.assertTrue(module.inspect(self.root)['errors'])
    def test_symlink(self):
        (self.root / 'tokens.json').symlink_to(self.root / 'DESIGN.md')
        self.assertTrue(module.inspect(self.root)['errors'])
if __name__ == '__main__': unittest.main()
