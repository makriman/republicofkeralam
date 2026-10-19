# SPDX-License-Identifier: MIT
"""Regression tests for validator hardening.

Each file in tests/fixtures/invalid/ applies one targeted mutation to a copy of
the canonical data and names the error the validator must report. The test
fails if validation raises an exception instead of reporting, or if the
expected error is missing.
"""
import copy
import json
import hashlib
import tempfile
import subprocess
from unittest.mock import patch
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

    def test_garbage_collections_do_not_raise(self):
        data = seed()
        data['records'] = 'not a list'
        data['sources'][0] = 5
        errors = run(data)
        self.assertTrue(any('records: expected a JSON array' in e for e in errors))
        self.assertTrue(any('sources #0' in e for e in errors))

    def test_required_collections_cannot_be_null(self):
        for name in ('sources', 'periods', 'records', 'audit'):
            with self.subTest(collection=name):
                data = seed()
                data[name] = None
                self.assertTrue(any(f'{name}: expected a JSON array' in e for e in run(data)))

    def test_malformed_ids_and_reviewers_report_errors(self):
        for value in ([], {}, True, None):
            with self.subTest(value=value):
                data = seed()
                data['sources'][0]['id'] = value
                self.assertTrue(run(data))
                data = seed()
                data['records'][0]['reviewers'] = [{
                    'reviewer': 'tester', 'reviewer_type': value,
                    'checked': 'claim', 'date': '2026-10-11'}]
                self.assertTrue(run(data))

    def test_direct_review_checker_tolerates_bad_types(self):
        import datetime as dt
        from validate import review_record_errors
        for value in ([], {}, None, 0):
            errors = review_record_errors('test', {'human_review': [], 'reviewers': [{
                'reviewer': 'tester', 'reviewer_type': value,
                'checked': 'claim', 'date': '2026-10-11'}]}, dt.date(2026, 10, 11))
            self.assertTrue(errors)

    def test_malformed_urls_report_errors(self):
        for url in ('https://[', 'https://', 'https://host:bad', 'https://host:99999'):
            with self.subTest(url=url):
                data = seed()
                data['sources'][0]['url'] = url
                self.assertTrue(any('bad source URL' in e for e in run(data)))

    def test_geometry_requires_existing_matching_local_file(self):
        data = seed()
        scope = data['scope']
        scope.update(spatial_filtering_enabled=True, geometry_file='missing.geojson',
                     geometry_license='CC0', geometry_sha256='0' * 64, boundary_status='verified')
        with tempfile.TemporaryDirectory() as directory, patch('validate.ROOT', Path(directory)):
            self.assertTrue(any('existing regular file' in e for e in run(data)))
            geometry = Path(directory) / 'boundary.geojson'
            geometry.write_bytes(b'{"type":"FeatureCollection","features":[]}')
            scope['geometry_file'] = geometry.name
            self.assertTrue(any('does not match' in e for e in run(data)))
            scope['geometry_sha256'] = hashlib.sha256(geometry.read_bytes()).hexdigest()
            self.assertEqual(run(data), [])
            geometry.write_bytes(b'changed')
            self.assertTrue(any('does not match' in e for e in run(data)))
            for path in ('../outside.geojson', str(geometry), '.'):
                scope['geometry_file'] = path
                self.assertTrue(run(data))
            scope['geometry_file'] = 'escape.geojson'
            (Path(directory) / 'escape.geojson').symlink_to(ROOT / 'project.json')
            self.assertTrue(any('inside the repository' in e for e in run(data)))

    def test_json_equality_does_not_conflate_booleans_and_numbers(self):
        from schema_check import Validator
        for keyword in ('const', 'enum'):
            for expected, value in ((False, 0), (True, 1), ([False], [0]), ({'a': True}, {'a': 1})):
                schema = {keyword: expected if keyword == 'const' else [expected]}
                self.assertTrue(Validator(schema).errors(value))
                self.assertEqual(Validator(schema).errors(expected), [])
            schema = {keyword: 1 if keyword == 'const' else [1]}
            self.assertEqual(Validator(schema).errors(1.0), [])
        data = seed()
        data['project']['year_zero'] = 0
        self.assertTrue(any('year_zero' in e for e in run(data)))

    def test_manifest_covers_tracked_files_except_itself(self):
        result = subprocess.run(['git', 'ls-files', '-z'], cwd=ROOT, capture_output=True)
        if result.returncode:
            self.skipTest('Git inventory unavailable in exported release')
        tracked = set(result.stdout.decode().rstrip('\0').split('\0')) - {'MANIFEST.sha256'}
        entries = [line.split('  ', 1)[1] for line in (ROOT / 'MANIFEST.sha256').read_text().splitlines()]
        self.assertEqual(len(entries), len(set(entries)), 'duplicate manifest entries')
        self.assertEqual(set(entries), tracked)

    def test_original_five_argument_signature_still_works(self):
        d = seed()
        self.assertEqual(validate_data(d['project'], d['sources'], d['periods'], d['records'], d['audit']), [])

    def test_schema_executor_refuses_unknown_keyword(self):
        from schema_check import Validator, SchemaError
        with self.assertRaises(SchemaError):
            Validator({'type': 'object', 'dependentRequired': {}}).errors({})

    def test_schemas_agree_with_reference_engine_if_installed(self):
        try:
            import jsonschema
        except ImportError:
            self.skipTest('jsonschema not installed; the standard-library executor is the operational check')
        d = seed()
        pairs = [('record', d['records']), ('source', d['sources']), ('period', d['periods']), ('audit', d['audit']),
                 ('corpus', d['corpora']), ('crosswalk', d['crosswalk'])]
        for name, items in pairs:
            schema = json.loads((ROOT / 'schemas' / f'{name}.schema.json').read_text(encoding='utf-8'))
            v = jsonschema.Draft202012Validator(schema)
            for item in items:
                self.assertEqual(list(v.iter_errors(item)), [], f'{name} {item.get("id")}')

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
