# SPDX-License-Identifier: MIT
"""Generation safety and coverage counting, run against a temporary copy."""
import csv
import io
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from build import make_outputs, MARKER  # noqa: E402


def run(args, cwd):
    return subprocess.run([sys.executable, *args], cwd=cwd, capture_output=True, text=True, encoding='utf-8')


class TempRepo:
    def __enter__(self):
        self.tmp = tempfile.mkdtemp(prefix='rok-test-')
        self.root = Path(self.tmp) / 'repo'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__'))
        return self.root

    def __exit__(self, *exc):
        shutil.rmtree(self.tmp)


class GenerationSafetyTests(unittest.TestCase):
    def test_orphaned_generated_view_detected(self):
        with TempRepo() as root:
            (root / 'records' / 'R999.md').write_text(MARKER + '\n\n# R999 left over\n', encoding='utf-8')
            check = run(['scripts/build.py', '--check'], root)
            self.assertNotEqual(check.returncode, 0)
            self.assertIn('records/R999.md', check.stdout)
            val = run(['scripts/validate.py'], root)
            self.assertNotEqual(val.returncode, 0)
            self.assertIn('Orphaned generated view', val.stdout)

    def test_edited_generated_view_detected(self):
        with TempRepo() as root:
            p = root / 'years' / 'CE' / '0123.md'
            p.write_text(p.read_text(encoding='utf-8') + '\nHand edit.\n', encoding='utf-8')
            check = run(['scripts/build.py', '--check'], root)
            self.assertNotEqual(check.returncode, 0)
            self.assertIn('years/CE/0123.md', check.stdout)

    def test_notes_survive_regeneration_and_hand_files_are_not_overwritten(self):
        with TempRepo() as root:
            note = root / 'notes' / 'hand-note.md'
            note.write_text('# Hand note\n\nKeep me.\n', encoding='utf-8')
            built = run(['scripts/build.py'], root)
            self.assertEqual(built.returncode, 0, built.stderr)
            self.assertEqual(note.read_text(encoding='utf-8'), '# Hand note\n\nKeep me.\n')
            hand = root / 'records' / 'R001.md'
            hand.write_text('# Hand-written page\n', encoding='utf-8')
            before = (root / 'records' / 'R002.md').read_text(encoding='utf-8')
            refused = run(['scripts/build.py'], root)
            self.assertNotEqual(refused.returncode, 0)
            self.assertIn('Refusing to overwrite', refused.stderr + refused.stdout)
            self.assertEqual(hand.read_text(encoding='utf-8'), '# Hand-written page\n')
            self.assertEqual((root / 'records' / 'R002.md').read_text(encoding='utf-8'), before)

    def test_build_twice_is_byte_identical(self):
        with TempRepo() as root:
            self.assertEqual(run(['scripts/build.py'], root).returncode, 0)
            first = {p: p.read_bytes() for p in root.rglob('*') if p.is_file()}
            self.assertEqual(run(['scripts/build.py'], root).returncode, 0)
            second = {p: p.read_bytes() for p in root.rglob('*') if p.is_file()}
            self.assertEqual(first, second)


class CoverageCountTests(unittest.TestCase):
    def setUp(self):
        self.out, self.stats = make_outputs()
        self.records = json.loads((ROOT / 'data' / 'records.json').read_text(encoding='utf-8'))

    def test_links_records_and_pages_counted_separately(self):
        s = self.stats
        links = sum(len(r['year_links']) for r in self.records)
        self.assertEqual(s['annual_year_links_total'], links)
        self.assertEqual(sum(s['annual_year_links_by_role'].values()), links)
        self.assertEqual(s['records_with_annual_links'], sum(bool(r['year_links']) for r in self.records))
        self.assertEqual(s['canonical_records'], len(self.records))
        self.assertEqual(s['annual_pages_with_past_event_links'] + s['annual_pages_with_only_research_history_links'],
                         s['annual_pages_with_year_specific_seeds'])

    def test_research_milestones_separated_from_past_events(self):
        rows = self.out['coverage/year-status.csv'].splitlines()
        self.assertEqual(rows[0], 'era,year,file,year_specific_seed_links,status,past_event_links,research_history_links')
        r1819 = next(r for r in rows if r.startswith('CE,1819,'))
        self.assertTrue(r1819.endswith(',0,1'))
        r1956 = next(r for r in rows if r.startswith('CE,1956,'))
        self.assertTrue(r1956.endswith(',2,0'))

    def test_source_cards_and_inspection_depth_counted_separately(self):
        s = self.stats
        self.assertEqual(sum(s['sources_by_inspection_depth'].values()), s['source_records'])
        self.assertLessEqual(s['sources_cited_by_records'], s['source_records'])
        self.assertEqual(s['sources_inspected_at_passage_or_full_text'],
                         s['sources_by_inspection_depth'].get('passage', 0) + s['sources_by_inspection_depth'].get('full_text', 0))
        self.assertEqual(s['human_reviewed_sources'], 0)

    def test_translation_is_a_separate_measure(self):
        t = self.stats['translation']['ml']
        self.assertEqual(t['data_fields_total'], 845)  # 827 plus 3 fields for each of S043-S048
        self.assertEqual(t['data_fields_human_reviewed'], 0)
        self.assertNotIn('percent', json.dumps(self.stats))
        self.assertEqual(self.stats['whole_web_completeness'], 'not_claimed')

    def test_unresearched_years_stay_explicit(self):
        rows = list(csv.DictReader(io.StringIO(self.out['coverage/year-status.csv'])))
        unresearched = sum(1 for r in rows if r['status'] == 'unresearched' and r['year_specific_seed_links'] == '0')
        self.assertEqual(unresearched, self.stats['annual_pages_without_year_specific_seeds'])


if __name__ == '__main__':
    unittest.main()
