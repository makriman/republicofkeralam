"""Regression tests for explicit target checks versus frozen source snapshots."""
import subprocess
import unittest
from freshness import source_freshness_errors


class FreshnessTests(unittest.TestCase):
    entries = [{'source_revision': 'pinned', 'source_path': 'scripts/build.py', 'staged_file': 'labels.ml.json'}]

    def test_identical_source_passes(self):
        self.assertEqual([], source_freshness_errors(self.entries, 'HEAD', lambda _: b'label'))

    def test_removed_literal_fails_without_rewriting_revision(self):
        data = {'pinned:scripts/build.py': b'label', 'HEAD:scripts/build.py': b''}
        self.assertIn('translation review required', source_freshness_errors(self.entries, 'HEAD', data.__getitem__)[0])
        self.assertEqual('pinned', self.entries[0]['source_revision'])

    def test_missing_target_fails_closed(self):
        def read(spec):
            if spec.startswith('missing:'):
                raise subprocess.CalledProcessError(128, ['git', 'show', spec])
            return b'label'
        self.assertIn('cannot read', source_freshness_errors(self.entries, 'missing', read)[0])

    def test_unstaged_sources_are_not_freshness_claims(self):
        self.assertEqual([], source_freshness_errors([dict(self.entries[0], staged_file=None)], 'HEAD'))


if __name__ == '__main__':
    unittest.main()
