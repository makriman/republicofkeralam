#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""One-off import of the staged Malayalam drafts into data/i18n/ml catalogues.

Reads notes/translation-review/batch-2 and batch-3 (Project A, draft PRs #3, #6
and #7, staged at revision 570f665) and writes entries in the format of
docs/BILINGUAL_DATA.md. An entry is imported only when its en_sha256 matches the
current English, or when the current English equals the staging file's own
proposed_en. Everything else is reported as stale and left out; nothing is
re-hashed to hide a change. Supplementary entries (new translations written in
the integration batch) are merged from scripts/integration/ml_supplement.json.

Usage, from the repository root: python3 scripts/integration/import_ml_staging.py
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
import bilingual  # noqa: E402
from build import load_data, label_texts  # noqa: E402

STAGED = {
    'records.json': ['batch-2/records.ml.json'], 'sources.json': ['batch-2/sources.ml.json'],
    'periods.json': ['batch-2/periods.ml.json'], 'audit.json': ['batch-3/audit.ml.json'],
    'corpora.json': ['batch-3/corpora.ml.json'],
    'prior_chapter_crosswalk.json': ['batch-3/prior_chapter_crosswalk.ml.json'],
    'scope.json': ['batch-3/scope.ml.json'], 'labels.json': ['batch-3/generator-labels.ml.json'],
}
SOURCE_PATH = {'records.json': 'data/records.json', 'sources.json': 'data/sources.json',
               'periods.json': 'data/periods.json', 'audit.json': 'data/audit.json',
               'corpora.json': 'data/corpora.json', 'prior_chapter_crosswalk.json': 'data/prior_chapter_crosswalk.json',
               'scope.json': 'geography/scope.json', 'labels.json': 'scripts/build.py'}
NOTE = ('AI-assisted Malayalam draft. Human Malayalam-language review and specialist review are pending; '
        'a model check is not approval. Imported from notes/translation-review (draft PRs #3, #6, #7) where the '
        'English is unchanged, plus integration-batch translations for English that changed or was not staged.')


def put_draft(have, draft):
    """A staging import cannot erase a recorded human review decision."""
    old = have.get(draft['key'])
    if old and (old.get('human_language_review', 'pending') != 'pending'
                or old.get('specialist_review', 'pending') != 'pending'
                or old.get('reviewers')):
        if any(old.get(k) != draft.get(k) for k in ('en', 'en_sha256', 'ml')):
            raise SystemExit(f"{draft['key']}: reviewed translation differs; explicit review resolution required")
        return
    have[draft['key']] = draft


def main():
    data = load_data(); labels = label_texts(data)
    supp = json.loads((ROOT / 'scripts/integration/ml_supplement.json').read_text(encoding='utf-8'))
    # Validate every supplement before writing any catalogue. Never attach a new
    # English hash to a translation prepared from a different source text.
    seen = set()
    for entry in supp['entries']:
        key = entry['key']
        if key in seen:
            raise SystemExit(f'{key}: duplicate supplement key')
        seen.add(key)
        en, err = bilingual.english_for(key, data, labels)
        if err or entry.get('en') != en or entry.get('en_sha256') != bilingual.en_hash(en):
            raise SystemExit(f'{key}: stale or invalid supplement English; translate and review the changed text')
        if entry.get('revision') not in supp['revisions']:
            raise SystemExit(f'{key}: missing supplement source revision')
    pending = {}
    out_dir = ROOT / 'data/i18n/ml'
    report = {'imported': 0, 'proposed_en_imported': 0, 'stale_left_out': [], 'supplement': 0}
    for name, staged in STAGED.items():
        target = out_dir / name
        cat = (json.loads(target.read_text(encoding='utf-8')) if target.exists() else
               {'catalogue': 'translation-catalogue/1', 'language': 'ml', 'source_path': SOURCE_PATH[name], 'entries': []})
        cat['note'] = NOTE
        have = {e['key']: e for e in cat['entries']}
        for rel in staged:
            doc = json.loads((ROOT / 'notes/translation-review' / rel).read_text(encoding='utf-8'))
            for s in doc['entries']:
                en, err = bilingual.english_for(s['key'], data, labels)
                if err:
                    report['stale_left_out'].append((s['key'], err)); continue
                if bilingual.en_hash(en) == s['en_sha256'] and en == s['en']:
                    rev = doc['source_revision']; report['imported'] += 1
                elif s.get('proposed_en') == en:
                    rev = supp['revisions']['separator']; report['proposed_en_imported'] += 1
                else:
                    report['stale_left_out'].append((s['key'], 'English changed after staging')); continue
                put_draft(have, {'key': s['key'], 'ml': s['ml'], 'en': en, 'en_sha256': bilingual.en_hash(en),
                                  'source_revision': rev, 'ai_assisted': True, 'human_language_review': 'pending',
                                  'specialist_review': doc.get('specialist_review', 'pending')})
        for s in supp['entries']:
            if not s['key'].startswith(SOURCE_PATH[name] + '#'):
                continue
            en, err = bilingual.english_for(s['key'], data, labels)
            if err:
                raise SystemExit(f"{s['key']}: {err}")
            put_draft(have, {'key': s['key'], 'ml': s['ml'], 'en': en, 'en_sha256': bilingual.en_hash(en),
                              'source_revision': supp['revisions'][s['revision']], 'ai_assisted': True,
                              'human_language_review': 'pending', 'specialist_review': 'pending',
                              **({'note': s['note']} if s.get('note') else {})})
            report['supplement'] += 1
        cat['entries'] = sorted(have.values(), key=lambda e: e['key'])
        pending[target] = json.dumps(cat, ensure_ascii=False, indent=2) + '\n'
    for target, text in pending.items():
        target.write_text(text, encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
