# SPDX-License-Identifier: MIT
"""Integration imports must preserve the English actually translated."""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SupplementImportTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for name in ('scripts', 'data', 'geography', 'notes/translation-review'):
            shutil.copytree(ROOT / name, self.root / name)
        shutil.copy2(ROOT / 'project.json', self.root / 'project.json')

    def run_import(self):
        return subprocess.run([sys.executable, 'scripts/integration/import_ml_staging.py'],
                              cwd=self.root, text=True, capture_output=True)

    def catalogues(self):
        return {p.name: p.read_bytes() for p in (self.root / 'data/i18n/ml').glob('*.json')}

    def test_changed_english_is_rejected_without_catalogue_writes(self):
        before = self.catalogues()
        path = self.root / 'data/records.json'
        data = json.loads(path.read_text())
        record = next(r for r in data if r['id'] == 'R006')
        record['claim'] = record['claim'].replace('Lower Palaeolithic', 'Upper Palaeolithic')
        path.write_text(json.dumps(data))
        result = self.run_import()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('stale or invalid supplement', result.stderr)
        self.assertEqual(before, self.catalogues())

    def test_bad_hash_is_rejected_without_catalogue_writes(self):
        before = self.catalogues()
        path = self.root / 'scripts/integration/ml_supplement.json'
        data = json.loads(path.read_text())
        data['entries'][-1]['en_sha256'] = '0' * 16
        path.write_text(json.dumps(data))
        self.assertNotEqual(self.run_import().returncode, 0)
        self.assertEqual(before, self.catalogues())

    def test_matching_supplement_is_repeatable(self):
        first = self.run_import()
        self.assertEqual(first.returncode, 0, first.stderr)
        before = self.catalogues()
        second = self.run_import()
        self.assertEqual(second.returncode, 0, second.stderr)
        self.assertEqual(before, self.catalogues())

    def test_existing_review_decisions_are_not_reset_by_reimport(self):
        path = self.root / 'data/i18n/ml/records.json'
        for field in ('specialist_review', 'human_language_review'):
            for status in ('rejected', 'approved'):
                with self.subTest(field=field, status=status):
                    data = json.loads(path.read_text())
                    entry = next(e for e in data['entries'] if e['key'] == 'data/records.json#R006.claim')
                    entry[field] = status
                    entry['reviewers'] = [{'reviewer': 'Test reviewer', 'reviewer_type': 'human',
                                           'checked': 'claim', 'date': '2026-10-18'}]
                    path.write_text(json.dumps(data, ensure_ascii=False))
                    result = self.run_import()
                    self.assertEqual(result.returncode, 0, result.stderr)
                    actual = next(e for e in json.loads(path.read_text())['entries'] if e['key'] == entry['key'])
                    self.assertEqual(actual, entry)

    def test_changed_reviewed_translation_requires_resolution_without_writes(self):
        path = self.root / 'data/i18n/ml/records.json'
        data = json.loads(path.read_text())
        entry = next(e for e in data['entries'] if e['key'] == 'data/records.json#R006.claim')
        entry['specialist_review'] = 'rejected'
        entry['ml'] += ' test'
        path.write_text(json.dumps(data, ensure_ascii=False))
        before = self.catalogues()
        result = self.run_import()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('review resolution required', result.stderr)
        self.assertEqual(before, self.catalogues())
