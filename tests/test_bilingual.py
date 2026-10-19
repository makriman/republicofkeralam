# SPDX-License-Identifier: MIT
"""Malayalam-first, English-second rendering and translation freshness.

Uses the small catalogues in tests/fixtures/bilingual/. These are test data,
not integrated translations.
"""
import copy
import datetime as dt
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import bilingual  # noqa: E402
from build import make_outputs, load_data, label_texts  # noqa: E402
from validate import review_record_errors  # noqa: E402

FIX = ROOT / 'tests' / 'fixtures' / 'bilingual'
AS_OF = json.loads((ROOT / 'project.json').read_text(encoding='utf-8'))['as_of']
CUTOFF = dt.date.fromisoformat(AS_OF)


def fixture_catalogues():
    return bilingual.load_catalogues(FIX)


def errors_for(cats, data=None):
    data = data or load_data()
    return bilingual.catalogue_errors(cats, data, label_texts(data), CUTOFF, review_record_errors)


def entry(cats, key):
    for c in cats:
        for e in c['entries']:
            if e['key'] == key:
                return e
    raise KeyError(key)


class BilingualRenderingTests(unittest.TestCase):
    def test_fixture_catalogues_are_valid(self):
        self.assertEqual(errors_for(fixture_catalogues()), [])

    def test_without_catalogues_output_is_english_only(self):
        # Since integration batch 1 the committed views include Malayalam, so the
        # no-catalogue fallback is checked for English-only output instead of
        # byte equality with the committed files.
        plain, _ = make_outputs(catalogues=[])
        for path in ['records/R014.md', 'years/CE/1498.md', 'sources/S001.md', 'audit/CHAT_AUDIT.md']:
            self.assertNotIn('translation_ml', plain[path], path)
            self.assertIsNone(bilingual.MALAYALAM.search(plain[path]), path)

    def test_committed_views_match_integrated_catalogues(self):
        full, _ = make_outputs()
        for path in ['records/R014.md', 'years/CE/1498.md', 'sources/S001.md', 'audit/CHAT_AUDIT.md']:
            self.assertEqual(full[path], (ROOT / path).read_text(encoding='utf-8'), path)

    def test_malayalam_first_english_second(self):
        out, _ = make_outputs(catalogues=fixture_catalogues())
        page = out['records/R014.md']
        ml_title = 'യാത്രാഡയറി 1498-ൽ Calicut-ലെ വരവ് രേഖപ്പെടുത്തുന്നു'
        en_title = 'Voyage journal places arrival at Calicut in 1498'
        heading = next(l for l in page.splitlines() if l.startswith('# '))
        self.assertLess(heading.index(ml_title), heading.index(en_title))
        ml_claim = 'യാത്രാഡയറി ഉദ്ധരണി'
        en_claim = 'The voyage-journal extract describes'
        self.assertLess(page.index(ml_claim), page.index(en_claim))
        self.assertIn('## പരിമിതികൾ / Limitations', page)
        self.assertIn('**തെളിവിന്റെ തരം: / Evidence type:**', page)

    def test_page_discloses_ai_assistance_and_pending_review(self):
        out, _ = make_outputs(catalogues=fixture_catalogues())
        page = out['records/R014.md']
        self.assertIn('translation_ml: "ai_assisted_human_review_pending"', page)
        self.assertIn('AI', page)
        self.assertIn('human language review is pending', page)
        self.assertNotIn('translation_ml', out['sources/S002.md'])
        self.assertNotIn('Malayalam first', out['sources/S002.md'])

    def test_year_page_labels_and_templates(self):
        out, _ = make_outputs(catalogues=fixture_catalogues())
        y = out['years/CE/1498.md']
        self.assertIn('## വർഷം സാക്ഷ്യപ്പെടുത്തിയിരിക്കുന്നു; ദിവസം ഏകീകരിച്ചിട്ടില്ല / Year attested; day not normalized', y)
        self.assertIn('[വർഷസൂചിക / Year index](../README.md)', y)
        last = out['years/CE/2026.md']
        self.assertIn(f'{AS_OF}-ൽ അവസാനിക്കുന്നു', last)
        self.assertLess(last.index('ഭാഗിക വർഷം'), last.index('Partial year'))

    def test_table_header_joined_cell_by_cell(self):
        out, _ = make_outputs(catalogues=fixture_catalogues())
        self.assertIn('| അധ്യായം / Chapter | നിർദേശിച്ച വിഷയം / Proposed subject |', out['audit/CHAT_AUDIT.md'])

    def test_source_title_gloss_is_not_presented_as_title(self):
        out, _ = make_outputs(catalogues=fixture_catalogues())
        page = out['sources/S001.md']
        heading = next(l for l in page.splitlines() if l.startswith('# '))
        self.assertNotIn('ഭൂമിയുടെ പ്രായം', heading)
        self.assertIn('Explanatory translation, not the source title', page)
        self.assertIn('ഭൂമിയുടെ പ്രായം', page)

    def test_generation_with_catalogues_is_deterministic(self):
        a, _ = make_outputs(catalogues=fixture_catalogues())
        b, _ = make_outputs(catalogues=fixture_catalogues())
        self.assertEqual(a, b)


class FreshnessAndContractTests(unittest.TestCase):
    def test_stale_translation_detected_and_not_rendered(self):
        data = load_data()
        r = next(x for x in data['records'] if x['id'] == 'R014')
        r['claim'] = r['claim'] + ' Edited after translation.'
        errs = errors_for(fixture_catalogues(), data)
        self.assertTrue(any('R014.claim' in e and 'stale' in e for e in errs), errs)
        out, _ = make_outputs(data=data, catalogues=fixture_catalogues())
        self.assertNotIn('യാത്രാഡയറി ഉദ്ധരണി', out['records/R014.md'])
        self.assertIn('Edited after translation.', out['records/R014.md'])

    def test_stored_english_copy_must_match(self):
        cats = fixture_catalogues()
        entry(cats, 'data/records.json#R014.claim')['en'] = 'Something else'
        self.assertTrue(any('R014.claim' in e and 'stale' in e for e in errors_for(cats)))

    def test_unknown_item_or_field_rejected(self):
        cats = fixture_catalogues()
        entry(cats, 'data/records.json#R014.title')['key'] = 'data/records.json#R999.title'
        self.assertTrue(any('R999' in e and 'no such' in e for e in errors_for(cats)))

    def test_machine_fields_cannot_be_translated(self):
        for key in ['data/records.json#R014.id', 'data/records.json#R014.support[0].locator',
                    'data/sources.json#S001.url', 'data/records.json#R014.date.precision']:
            cats = fixture_catalogues()
            entry(cats, 'data/records.json#R014.title')['key'] = key
            self.assertTrue(any(key in e and 'not translatable' in e for e in errors_for(cats)), key)

    def test_malayalam_text_required(self):
        cats = fixture_catalogues()
        entry(cats, 'data/records.json#R014.title')['ml'] = 'Voyage journal 1498'
        self.assertTrue(any('R014.title' in e and 'Malayalam script' in e for e in errors_for(cats)))

    def test_em_dash_rejected_in_new_malayalam(self):
        cats = fixture_catalogues()
        e = entry(cats, 'data/records.json#R014.title'); e['ml'] = e['ml'] + ' \u2014 1498'
        self.assertTrue(any('R014.title' in x and 'em dash' in x for x in errors_for(cats)))

    def test_numbers_must_survive_translation(self):
        cats = fixture_catalogues()
        entry(cats, 'data/records.json#R014.caveat')['ml'] = 'വർഷം നിലനിർത്തിയിരിക്കുന്നു.'
        self.assertTrue(any('R014.caveat' in e and 'number' in e for e in errors_for(cats)))

    def test_label_placeholders_and_markup_must_match(self):
        cats = fixture_catalogues()
        entry(cats, 'scripts/build.py#year.partial')['ml'] = '**ഭാഗിക വർഷം:** ഈ പതിപ്പ് അവസാനിക്കുന്നു.'
        entry(cats, 'scripts/build.py#record.h_limitations')['ml'] = 'പരിമിതികൾ'
        errs = errors_for(cats)
        self.assertTrue(any('year.partial' in e and 'placeholder' in e for e in errs), errs)
        self.assertTrue(any('record.h_limitations' in e and 'heading' in e for e in errs), errs)

    def test_unknown_label_rejected(self):
        cats = fixture_catalogues()
        entry(cats, 'scripts/build.py#year.coverage')['key'] = 'scripts/build.py#year.no_such_label'
        self.assertTrue(any('year.no_such_label' in e and 'no such' in e for e in errors_for(cats)))

    def test_duplicate_key_rejected(self):
        cats = fixture_catalogues()
        cats[0]['entries'].append(copy.deepcopy(cats[0]['entries'][0]))
        self.assertTrue(any('duplicate' in e for e in errors_for(cats)))

    def test_approved_translation_needs_human_review_record(self):
        cats = fixture_catalogues()
        entry(cats, 'data/records.json#R014.title')['human_language_review'] = 'approved'
        self.assertTrue(any('R014.title' in e and 'approval without' in e for e in errors_for(cats)))
        e = entry(cats, 'data/records.json#R014.title')
        e['reviewers'] = [{'reviewer': 'model-check', 'reviewer_type': 'model', 'checked': 'wording', 'date': '2026-10-11'}]
        self.assertTrue(any('R014.title' in x and 'cannot approve' in x for x in errors_for(cats)))

    def test_rejected_translation_not_rendered(self):
        cats = fixture_catalogues()
        e = entry(cats, 'data/records.json#R014.claim')
        e['human_language_review'] = 'rejected'
        e['reviewers'] = [{'reviewer': 'contributor-ml-1', 'reviewer_type': 'human', 'checked': 'wording against English', 'date': '2026-10-11'}]
        self.assertEqual(errors_for(cats), [])
        out, _ = make_outputs(catalogues=cats)
        self.assertNotIn('യാത്രാഡയറി ഉദ്ധരണി', out['records/R014.md'])

    def test_specialist_rejection_is_not_rendered_or_counted_current(self):
        cats = fixture_catalogues()
        key = 'data/records.json#R014.claim'
        e = entry(cats, key)
        e['specialist_review'] = 'rejected'
        e['reviewers'] = [{'reviewer': 'specialist-1', 'reviewer_type': 'human',
                           'checked': 'historical terminology', 'date': '2026-10-11'}]
        self.assertEqual(errors_for(cats), [])
        out, _ = make_outputs(catalogues=cats)
        self.assertNotIn(e['ml'], out['records/R014.md'])
        data = load_data()
        coverage = bilingual.coverage(data, cats, label_texts(data))
        self.assertEqual(coverage['data_fields_rejected'], 1)
        self.assertEqual(coverage['data_fields_current'], 5)
        self.assertIn(key, bilingual.missing_fields(data, cats, label_texts(data)))

    def test_complete_format_syntax_checked_and_unsafe_labels_not_rendered(self):
        key = 'scripts/build.py#year.partial'
        for suffix in ('{UNKNOWN}', '{', '}', '{}', '{0}', '{as_of.bad}',
                       '{as_of[bad]}', '{as_of!q}', '{as_of:bad}',
                       '{as_of:{UNKNOWN}}', '{as_of:{'):
            with self.subTest(suffix=suffix):
                cats = fixture_catalogues()
                e = entry(cats, key)
                e['ml'] += suffix
                self.assertTrue(any('year.partial' in x and ('format' in x or 'placeholder' in x)
                                    for x in errors_for(cats)))
                # Direct builds also fall back safely when validation is skipped.
                out, _ = make_outputs(catalogues=cats)
                self.assertNotIn(e['ml'], out['years/CE/2026.md'])
        self.assertEqual(bilingual._format_errors('{value}', '{{literal}} {value}'), [])
        self.assertEqual(bilingual._format_errors('{first} {second}', '{second} {first}'), [])

    def test_catalogue_schema_enforced(self):
        cats = fixture_catalogues()
        del entry(cats, 'data/records.json#R014.title')['ai_assisted']
        self.assertTrue(any('ai_assisted' in e and 'required' in e for e in errors_for(cats)))

    def test_missing_fields_reported_not_counted_complete(self):
        data = load_data()
        cats = fixture_catalogues()
        missing = bilingual.missing_fields(data, cats, label_texts(data))
        total = bilingual.coverage(data, cats, label_texts(data))
        self.assertEqual(total['data_fields_current'], 6)
        self.assertEqual(len([k for k in missing if not k.startswith('scripts/')]), total['data_fields_total'] - 6)
        self.assertIn('data/records.json#R001.title', missing)
        self.assertNotIn('data/records.json#R014.title', missing)

    def test_translatable_denominator(self):
        # The translation staging inventory lists 804 strings; it did not count the 23
        # human-readable date.calendar strings (3 distinct values), which are translatable here.
        data = load_data()
        keys = [k for k, _ in bilingual.iter_translatable(data)]
        self.assertEqual(len(keys), 845)  # 827 plus title, inspection_note and rights for S043-S048
        self.assertEqual(len(set(keys)), 845)
        self.assertEqual(sum('.date.calendar' in k for k in keys), 23)

    def test_english_hash_scheme(self):
        self.assertEqual(bilingual.en_hash('Planetary age as context'), '2b5b911668171420')


if __name__ == '__main__':
    unittest.main()
