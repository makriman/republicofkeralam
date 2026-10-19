#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Malayalam-first, English-second translation catalogues. Standard library only.

Contract (documented in docs/BILINGUAL_DATA.md):

* English stays in the canonical JSON fields. Translations live in optional
  catalogues under data/i18n/ml/*.json, so canonical keys, IDs and enum values
  never change.
* Each entry is keyed by file, stable ID and field path, for example
  ``data/records.json#R014.claim``, ``data/periods.json#E01.research_tasks[2]``,
  ``data/prior_chapter_crosswalk.json#7.title``, ``geography/scope.json#scope.offshore_rule``
  or ``scripts/build.py#record.h_limitations`` for generator labels.
* ``en_sha256`` is the first 16 hex digits of SHA-256 of the exact UTF-8
  English text that was translated. If the English changes, the entry is stale:
  validation fails and the generator falls back to English for that field.
* A rejected translation is never rendered. Missing translations are counted
  and listed, never treated as complete.
"""
from __future__ import annotations
import hashlib
import json
import re
from pathlib import Path

from schema_check import check as schema_errors

ROOT = Path(__file__).resolve().parents[1]
LANG = 'ml'
CATALOGUE_DIR = ROOT / 'data' / 'i18n' / LANG
FILES = {
    'data/records.json': 'records', 'data/sources.json': 'sources', 'data/periods.json': 'periods',
    'data/audit.json': 'audit', 'data/corpora.json': 'corpora',
    'data/prior_chapter_crosswalk.json': 'crosswalk', 'geography/scope.json': 'scope',
    'scripts/build.py': 'labels',
}
# Human-readable fields only. IDs, enums, URLs, DOIs, locators, dates, source
# lists and tags are machine keys or evidence locators and are never translated.
TRANSLATABLE = {
    'records': ['title', 'claim', 'caveat', 'date.original_expression', 'date.datum', 'date.calendar', 'authoring', 'rights'],
    'sources': ['title', 'inspection_note', 'rights'],
    'periods': ['title', 'display_window', 'central_question', 'established_in_this_pass', 'limitations', 'research_tasks[]'],
    'audit': ['earlier_claim', 'corrected_treatment'],
    'corpora': ['name', 'next_task'],
    'crosswalk': ['title', 'assessment'],
    'scope': ['inclusion_rule', 'offshore_rule', 'exclusions_and_context[]'],
}
# A published source title keeps its original wording. A Malayalam entry for it
# is rendered as an explanatory translation, never as the title.
GLOSS_ONLY = {('sources', 'title')}
MALAYALAM = re.compile('[\u0d00-\u0d7f]')
NUMBER = re.compile(r'\d+(?:[.,]\d+)*')
PLACEHOLDER = re.compile(r'\{[a-z_]+\}')
LINK_TARGET = re.compile(r'\]\(([^)]*)\)')
EM_DASH = '\u2014'


def en_hash(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()[:16]


def load_catalogues(directory: Path | str | None = None) -> list[dict]:
    d = Path(directory) if directory is not None else CATALOGUE_DIR
    if not d.is_dir():
        return []
    cats = []
    for p in sorted(d.glob('*.json')):
        c = json.loads(p.read_text(encoding='utf-8'))
        if isinstance(c, dict):
            c = dict(c)
            c['_file'] = p.name
        cats.append(c)
    return cats


def parse_key(key: str):
    """Return (source_path, selector, field_path) or None."""
    if '#' not in key:
        return None
    path, rest = key.split('#', 1)
    if path == 'scripts/build.py':
        return path, None, rest
    if '.' not in rest:
        return None
    sel, field = rest.split('.', 1)
    return path, sel, field


def _generic(field: str) -> str:
    return re.sub(r'\[\d+\]', '[]', field)


def _get(obj, field: str):
    cur = obj
    for part in field.split('.'):
        m = re.fullmatch(r'([A-Za-z_][A-Za-z0-9_]*)((?:\[\d+\])*)', part)
        if not m or not isinstance(cur, dict) or m.group(1) not in cur:
            return None
        cur = cur[m.group(1)]
        for idx in re.findall(r'\[(\d+)\]', m.group(2)):
            i = int(idx)
            if not isinstance(cur, list) or i >= len(cur):
                return None
            cur = cur[i]
    return cur


def _item(data: dict, coll: str, sel: str):
    if coll == 'scope':
        return data.get('scope') if sel == 'scope' else None
    key = 'chapter' if coll == 'crosswalk' else 'id'
    for x in data.get(coll) or []:
        if isinstance(x, dict) and str(x.get(key)) == sel:
            return x
    return None


def iter_translatable(data: dict):
    """Yield (key, english) for every translatable field present in canonical data."""
    path_of = {v: k for k, v in FILES.items()}
    for coll, fields in TRANSLATABLE.items():
        items = [data.get('scope')] if coll == 'scope' else (data.get(coll) or [])
        for x in items:
            if not isinstance(x, dict):
                continue
            sel = 'scope' if coll == 'scope' else str(x.get('chapter' if coll == 'crosswalk' else 'id'))
            for f in fields:
                if f.endswith('[]'):
                    vals = _get(x, f[:-2])
                    if isinstance(vals, list):
                        for i, v in enumerate(vals):
                            if isinstance(v, str) and v.strip():
                                yield f'{path_of[coll]}#{sel}.{f[:-2]}[{i}]', v
                else:
                    v = _get(x, f)
                    if isinstance(v, str) and v.strip():
                        yield f'{path_of[coll]}#{sel}.{f}', v


def english_for(key: str, data: dict, labels: dict):
    """Return (english, error). labels maps label key -> (kind, english)."""
    parsed = parse_key(key)
    if not parsed or parsed[0] not in FILES:
        return None, 'key must look like <file>#<ID>.<field> for a known canonical file'
    path, sel, field = parsed
    coll = FILES[path]
    if coll == 'labels':
        if field not in labels:
            return None, 'no such generator label'
        return labels[field][1], None
    if _generic(field) not in TRANSLATABLE[coll]:
        return None, 'field is not translatable (IDs, enums, URLs, locators, dates and tags stay as they are)'
    item = _item(data, coll, sel)
    if item is None:
        return None, f'no such item {sel} in {path}'
    v = _get(item, field)
    if not isinstance(v, str) or not v.strip():
        return None, f'no such text field {field} on {sel}'
    return v, None


def _label_form_errors(kind: str, en: str, ml: str) -> list[str]:
    out = []
    if sorted(PLACEHOLDER.findall(en)) != sorted(PLACEHOLDER.findall(ml)):
        out.append(f'template placeholders differ (English {sorted(PLACEHOLDER.findall(en))}, Malayalam {sorted(PLACEHOLDER.findall(ml))})')
    if sorted(LINK_TARGET.findall(en)) != sorted(LINK_TARGET.findall(ml)):
        out.append('link targets differ from the English label')
    if kind == 'heading':
        h = re.match(r'#+ ', en).group(0)
        if not ml.startswith(h) or ml.startswith(h + '#'):
            out.append(f'heading label must start with {h.strip()!r} like the English')
    elif kind == 'bold':
        if not (ml.startswith('**') and ml.endswith('**')):
            out.append('bold label must be wrapped in ** like the English')
    elif kind == 'bracket':
        if not (ml.startswith('[') and ml.endswith(']')):
            out.append('bracketed link text must be wrapped in [ ] like the English')
    elif kind == 'table_row':
        if ml.count('|') != en.count('|'):
            out.append('table row must have the same number of cells as the English')
    return out


def catalogue_errors(catalogues: list, data: dict, labels: dict, cutoff, review_fn) -> list[str]:
    errors = []
    seen = {}
    for c in catalogues:
        name = f"translation catalogue {c.get('_file', '?') if isinstance(c, dict) else '?'}"
        if not isinstance(c, dict):
            errors.append(f'{name}: must be a JSON object'); continue
        body = {k: v for k, v in c.items() if k != '_file'}
        errs = schema_errors(body, 'translation-catalogue.schema.json')
        errors.extend(f'{name}: {e}' for e in errs)
        if errs:
            continue
        for e in c['entries']:
            key = e['key']; tag = f'{name}: {key}'
            if key in seen:
                errors.append(f'{tag}: duplicate translation key (also in {seen[key]})'); continue
            seen[key] = name
            if not key.startswith(c['source_path'] + '#'):
                errors.append(f'{tag}: key does not belong to source_path {c["source_path"]}')
            en, err = english_for(key, data, labels)
            if err:
                errors.append(f'{tag}: {err}'); continue
            if e['en_sha256'] != en_hash(en) or ('en' in e and e['en'] != en):
                errors.append(f'{tag}: stale Malayalam translation; the English changed after source_revision {e["source_revision"][:12]} '
                              f'(en_sha256 {e["en_sha256"]}, current {en_hash(en)}). Retranslate and update en_sha256, or remove the entry.')
            ml = e['ml']
            if not MALAYALAM.search(ml):
                errors.append(f'{tag}: ml contains no Malayalam script')
            if EM_DASH in ml:
                errors.append(f'{tag}: ml contains an em dash; use a colon, semicolon or full stop in new writing')
            lost = sorted(set(NUMBER.findall(en)) - set(NUMBER.findall(ml)))
            if lost:
                errors.append(f'{tag}: number(s) {lost} from the English are missing in the Malayalam')
            if key.startswith('scripts/build.py#'):
                kind = labels[key.split('#', 1)[1]][0]
                errors.extend(f'{tag}: {x}' for x in _label_form_errors(kind, en, ml))
            errors.extend(review_fn(tag, e, cutoff))
            if e.get('specialist_review') in {'approved', 'rejected'} and not any(
                    isinstance(r, dict) and r.get('reviewer_type') == 'human' for r in e.get('reviewers') or []):
                errors.append(f'{tag}: specialist review {e["specialist_review"]} without a human review record')
    return errors


class Translations:
    """Lookup of renderable Malayalam text. Stale or rejected entries are skipped."""

    def __init__(self, catalogues=None):
        self.entries = {}
        for c in catalogues or []:
            if not isinstance(c, dict) or not isinstance(c.get('entries'), list):
                continue
            for e in c['entries']:
                if isinstance(e, dict) and isinstance(e.get('key'), str) and isinstance(e.get('ml'), str):
                    self.entries.setdefault(e['key'], e)

    def get(self, key: str, english: str):
        e = self.entries.get(key)
        if not e or e.get('en_sha256') != en_hash(english) or ('en' in e and e['en'] != english):
            return None
        if e.get('human_language_review') == 'rejected':
            return None
        return e


def _status(key: str, english: str, tr: Translations) -> str:
    e = tr.entries.get(key)
    if e is None:
        return 'missing'
    if e.get('human_language_review') == 'rejected':
        return 'rejected'
    if tr.get(key, english) is None:
        return 'stale'
    return 'current'


def coverage(data: dict, catalogues: list, labels: dict) -> dict:
    tr = Translations(catalogues)
    out = {}
    for prefix, pairs in [('data_fields', list(iter_translatable(data))),
                          ('generator_labels', [(f'scripts/build.py#{k}', v[1]) for k, v in sorted(labels.items())])]:
        st = [(k, _status(k, en, tr)) for k, en in pairs]
        out[f'{prefix}_total'] = len(st)
        for s in ('current', 'stale', 'rejected', 'missing'):
            out[f'{prefix}_{s}'] = sum(1 for _, x in st if x == s)
        out[f'{prefix}_human_reviewed'] = sum(1 for k, x in st if x == 'current' and tr.entries[k].get('human_language_review') == 'approved')
    return out


def missing_fields(data: dict, catalogues: list, labels: dict) -> list[str]:
    tr = Translations(catalogues)
    pairs = list(iter_translatable(data)) + [(f'scripts/build.py#{k}', v[1]) for k, v in sorted(labels.items())]
    return [k for k, en in pairs if _status(k, en, tr) != 'current']
