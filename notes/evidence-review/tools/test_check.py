"""Regression checks for historical-base loading; no current-tree fallback."""
import importlib.util
import pathlib
import subprocess
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location('evidence_check', pathlib.Path(__file__).with_name('check.py'))
check = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(check)

class HistoricalBaseTests(unittest.TestCase):
    def test_missing_revision_fails_even_when_working_tree_file_exists(self):
        with self.assertRaisesRegex(ValueError, 'Cannot load declared base'):
            check.load_at_base('data/records.json', 'nonexistent-evidence-base-7193')

    def test_missing_path_fails(self):
        with self.assertRaises(ValueError):
            check.load_at_base('data/not-present.json', 'HEAD')

    def test_invalid_json_fails(self):
        with patch.object(check.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, b'{broken')):
            with self.assertRaises(ValueError):
                check.load_at_base('data/records.json', 'HEAD')

    def test_valid_base_reads_historical_json(self):
        value = check.load_at_base('data/records.json', '570f665e25480380e6be361627cf5cfb1285c093')
        self.assertIsInstance(value, (list, dict))

if __name__ == '__main__':
    unittest.main()
