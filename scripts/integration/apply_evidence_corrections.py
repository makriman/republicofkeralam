#!/usr/bin/env python3
"""Apply the evidence-backed proposed corrections from PR #4 to canonical data.
Run from the repository root. Every change asserts the PR #4 current_value first
(the conflict rule in proposed-corrections.json), so nothing is overwritten blindly."""
import json, sys
from pathlib import Path

PC = json.loads(Path('notes/evidence-review/proposed-corrections.json').read_text())
CR = json.loads(Path('notes/evidence-review/claim-reviews.json').read_text())
files = {f: json.loads(Path(f).read_text()) for f in ('data/records.json','data/sources.json','data/audit.json')}
NEWID = {f'NEW-SRC-0{i}': f'S{42+i:03d}' for i in range(1, 7)}  # NEW-SRC-01 -> S043 ... NEW-SRC-06 -> S048
TODAY = '2026-10-18'

APPLY = {'PC-01','PC-02','PC-03','PC-04','PC-05','PC-06','PC-07','PC-08','PC-09','PC-10','PC-11',
         'PC-12','PC-13','PC-14','PC-15','PC-16','PC-17','PC-18','PC-19'}
# Individual change rows not applied (reason recorded in docs/INTEGRATION_BATCH_1.md).
SKIP_ROWS = {('PC-04','date.precision'), ('PC-15','NEW-RECORD-PLINY')}

def remap(v):
    if isinstance(v, str): return NEWID.get(v, v)
    if isinstance(v, list): return [remap(x) for x in v]
    if isinstance(v, dict): return {k: remap(x) for k, x in v.items()}
    return v

def item(f, i):
    for x in files[f]:
        if x['id'] == i: return x
    raise SystemExit(f'missing {f}#{i}')

# New source cards first (PC-03), so later rows can reference S043-S048.
NOTES = {
 'NEW-SRC-01': ("research_article", 1901,
   "OCR text of the Digital Library of India scan read at pp. 412 and 420–421; pp. 409–411 were not located in the OCR and page images and plates were not checked. Page 412 quotes a report placing Fawcett's visit at about the beginning of 1896 and gives Fawcett's reply that residents had known the cave for at least 12 or 15 years. Fawcett reports a trench that found no habitation deposit. Edition details: The Indian Antiquary, vol. 30 (1901), pp. 409–421."),
 'NEW-SRC-02': ("conference_paper", None,
   "Full paper read (6 pages). The 'Date of the engravings' section proposes a megalithic or early historic date and treats the earliest inscriptions as a later limit; it is a relative argument, not an absolute date. The paper gives 1894 for Fawcett's visit. Edition: XXV Valcamonica Symposium 2013 papers, pp. 337–342; the publication year of the papers volume was not checked, so none is registered."),
 'NEW-SRC-03': ("tourism_claim", None,
   "State tourism page read in full. It shares wording with S011, gives 1895 for the discovery and cites no evidence for its dates. Recorded as a claim to audit, not as dating evidence."),
 'NEW-SRC-04': ("primary_text_translation", 1855,
   "Book 6, chapter 26 read in the 1855 Bostock and Riley translation as encoded by Perseus. The publication year is that of the translation, not of Pliny's composition; no source for the composition date has been checked. The Latin text and a modern translation remain to be compared. Muziris stays a textual name."),
 'NEW-SRC-05': ("primary_text_translation", 1885,
   "OCR text read at Geography 7.1.8 with commentary pp. 50–52 and 7.1.86 with commentary p. 181. McCrindle's identifications, following Yule, of Mouziris with Kodungallur and Karoura with Karur are attributed arguments. Ptolemy's coordinates are not modern positions. The publication year is that of the translation, not of the Geography."),
 'NEW-SRC-06': ("primary_legislation", None,
   "Sections 4 and 5 read in a consolidated republication of the India Code text. Consolidated text as in force on the page date is not the 1956 Gazette text; the republisher's commentary was not used. Used only because the recorded official copy for S023 returned HTTP 404 on 2026-10-18. Statutory provisions are not a boundary dataset."),
}
applied, skipped = [], []
for c in PC['corrections']:
    if c['id'] != 'PC-03': continue
    for p in CR['proposed_sources']:
        kind, year, note = NOTES[p['key']]
        files['data/sources.json'].append({
            'id': NEWID[p['key']], 'title': p['title'], 'creator': p['creator'], 'url': p['url'],
            'source_kind': kind, 'inspection': p['inspected_depth'], 'inspected_locator': p['locator'],
            'inspection_note': note, 'publication_year': year, 'doi': None, 'alternative_urls': [],
            'accessed': TODAY, 'rights': p['rights'], 'local_copy': None, 'sha256': None, 'human_review': 'pending'})
    applied.append(('PC-03', 'add 6 source cards', ', '.join(f'{k}->{v}' for k, v in NEWID.items())))

for c in PC['corrections']:
    if c['id'] not in APPLY or c['id'] == 'PC-03': continue
    for ch in c['changes']:
        if (c['id'], ch['field'] or ch['target_id']) in SKIP_ROWS:
            skipped.append((c['id'], ch['target_id'], ch['field'])); continue
        f, i, fld, op = ch['file'], ch['target_id'], ch['field'], ch['op']
        x = item(f, i)
        path = fld.split('.')
        parent = x
        for k in path[:-1]: parent = parent[k]
        cur = parent.get(path[-1])
        assert cur == ch['current_value'], (c['id'], i, fld, cur, ch['current_value'])
        val = remap(ch['proposed_value'])
        if op == 'replace': new = val
        elif op == 'append': new = cur + [v for v in val if v not in cur]
        elif op == 'append_sentence':
            new = cur.rstrip() + ('' if cur.rstrip().endswith(('.', '?', '!')) else '.') + ' ' + val
        else: raise SystemExit(f'unhandled op {op}')
        parent[path[-1]] = new
        if f == 'data/records.json': x['updated'] = TODAY
        applied.append((c['id'], i, fld))

# Access dates for sources whose depth or locator was re-established on 2026-10-18 (access log in claim-reviews.json).
for sid in ('S002','S003','S009','S015','S017','S018','S020'):
    item('data/sources.json', sid)['accessed'] = TODAY

for f, d in files.items():
    Path(f).write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
for a in applied: print('applied', *a)
for s in skipped: print('skipped', *s)
