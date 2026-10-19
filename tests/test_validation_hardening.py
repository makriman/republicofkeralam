# SPDX-License-Identifier: MIT
"""Regression tests for validator hardening.

Each file in tests/fixtures/invalid/ applies one targeted mutation to a copy of
the canonical data and names the error the validator must report. The test
fails if validation raises an exception instead of reporting, or if the
expected error is missing.
"""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from build import load  # noqa: E402
from validate import validate_data  # noqa: E402

FIXTURES = ROOT / 'tests' / 'fixtures' / 'invalid'
EXTRA = ('corpora', 'scope', 'crosswalk')


def seed():
    return {
        'project': load('project.json'), 'sources': load('data/sources.json'),
        'periods': load('data/periods.json'), 'records': load('data/records.json'),
        'audit': load('data/audit.json'), 'corpora': load('data/corpora.json'),
        'scope': load('geography/scope.json'), 'crosswalk': load('data/prior_chapter_crosswalk.json'),
    }


def run(data, extras=EXTRA):
    kwargs = {k: data[k] for k in extras}
    return validate_data(data['project'], data['sources'], data['periods'], data['records'], data['audit'], **kwargs)


def _target(data, fixture):
    coll = data[fixture['collection']]
    if fixture['target'] is None:
        return coll
    return next(x for x in coll if x.get('id') == fixture['target'])


def apply(data, fixture):
    obj = _target(data, fixture)
    for m in fixture['mutations']:
        op = m['op']
        if op == 'fill_year_links':
            obj['year_links'] = [{'year': y, 'role': m['role']} for y in range(m['start'], m['end'] + 1) if y != 0]
            continue
        *parent, last = m['path']
        cur = obj
        for p in parent:
            cur = cur[p]
        if op == 'set':
            cur[last] = copy.deepcopy(m['value'])
        elif op == 'delete':
            del cur[last]
        elif op == 'append':
            cur[last].append(copy.deepcopy(m['value']))
        else:
            raise ValueError(f'unknown fixture op {op}')
    return data


class InvalidFixtureTests(unittest.TestCase):
    def test_seed_data_valid_with_all_collections(self):
        self.assertEqual(run(seed()), [])

    def test_fixture_set_is_not_empty(self):
        self.assertGreaterEqual(len(list(FIXTURES.glob('*.json'))), 30)


def _make(path):
    fixture = json.loads(path.read_text(encoding='utf-8'))

    def test(self):
        data = apply(seed(), fixture)
        extras = tuple(k for k in EXTRA if k == fixture['collection'])
        errors = run(data, extras)  # must not raise
        self.assertIsInstance(errors, list)
        hit = [e for e in errors if all(s in e for s in fixture['expect'])]
        self.assertTrue(hit, f"{fixture['bug']}: expected an error containing {fixture['expect']}; got {errors[:8]}")
    test.__doc__ = f"[{fixture['bug']}] {fixture['description']}"
    return test


for _p in sorted(FIXTURES.glob('*.json')):
    setattr(InvalidFixtureTests, f'test_invalid_{_p.stem}', _make(_p))


if __name__ == '__main__':
    unittest.main()
