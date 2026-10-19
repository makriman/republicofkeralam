#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Offline structural checks. Passing does NOT verify historical truth.

Order of checks:
1. Every canonical item is checked against its JSON Schema in schemas/
   (executed by scripts/schema_check.py, standard library only). Malformed
   items are reported and skipped, so missing or wrong-typed fields produce
   messages instead of KeyError or TypeError.
2. Cross-references, review records, cutoffs and date/year-link rules run on
   the well-formed items.
3. Generated views, annual filenames and local links.
"""
from __future__ import annotations
import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse, unquote
from build import ROOT, load, years, year_path, make_outputs, ROLES, INSPECTION_DEPTH
from schema_check import check as schema_errors

RELATIONS={'core','regional_context','global_context','external_reference','external_action_affecting_core','external_custody_or_research'}
REVIEW_STATES={'pending','approved','rejected'}
SINGLE_YEAR_PRECISION={'day','year','conventional_year'}
# Which year-link roles each historical precision may carry. A conventional or
# reconstructed year must not be relabelled as an attested or exact one.
ROLE_PRECISION={'exact_date':{'day'},'year_attested':{'day','year'}}
COLLECTIONS=[  # name, schema, label
    ('sources','source.schema.json'),('periods','period.schema.json'),('records','record.schema.json'),
    ('audit','audit.schema.json'),('corpora','corpus.schema.json'),('crosswalk','crosswalk.schema.json'),
]


def _tag(name,item,i):
    if isinstance(item,dict):
        for k in ('id','chapter'):
            v=item.get(k)
            if isinstance(v,(str,int)) and not isinstance(v,bool):
                return f'{name} {v}'
    return f'{name} #{i}'


def review_record_errors(tag,item,cutoff):
    """One rule for records, sources and translation entries.

    approved or rejected needs at least one human review record naming the
    reviewer identifier, what was checked and the date. A model check can be
    recorded, but it can never be the basis of approval.
    """
    errors=[]
    state=item.get('human_review') if 'human_review' in item else item.get('human_language_review')
    revs=item.get('reviewers')
    if revs is not None and not isinstance(revs,list):
        return [f'{tag}: reviewers must be a list of review records']
    revs=revs or []
    for i,r in enumerate(revs):
        ok=(isinstance(r,dict) and isinstance(r.get('reviewer'),str) and r['reviewer'].strip()
            and r.get('reviewer_type') in {'human','model'} and isinstance(r.get('checked'),str) and r['checked'].strip()
            and isinstance(r.get('date'),str))
        if not ok:
            errors.append(f'{tag}: reviewers[{i}] is not a valid review record (needs reviewer, reviewer_type human|model, checked, date)')
            continue
        try:
            if dt.date.fromisoformat(r['date'])>cutoff:
                errors.append(f'{tag}: reviewers[{i}] dated after release cutoff')
        except ValueError:
            errors.append(f'{tag}: reviewers[{i}] has an invalid date')
    if state in {'approved','rejected'}:
        humans=[r for r in revs if isinstance(r,dict) and r.get('reviewer_type')=='human' and isinstance(r.get('reviewer'),str)
                and r['reviewer'].strip() and isinstance(r.get('checked'),str) and r['checked'].strip()]
        if not revs:
            errors.append(f'{tag}: approval without named review record' if state=='approved' else f'{tag}: rejection without named review record')
        elif not humans:
            errors.append(f'{tag}: {state} without a valid human review record; a model check cannot approve or reject')
    return errors


def validate_data(cfg,ss,pp,rr,aa,corpora=None,scope=None,crosswalk=None):
    """Return a list of error strings. Never raises for malformed data.

    The first five arguments keep the original signature. corpora, scope,
    and crosswalk are optional so older callers keep working.
    """
    errors=[]
    def require(ok,msg):
        if not ok: errors.append(msg)
    if not isinstance(cfg,dict):
        return ['project: project.json must be a JSON object']
    errors.extend(f'project: {e}' for e in schema_errors(cfg,'project.schema.json'))
    if errors:
        return errors  # dates and ranges below depend on a well-formed config
    given={'sources':ss,'periods':pp,'records':rr,'audit':aa,'corpora':corpora,'crosswalk':crosswalk}
    good={}; ids={}
    for name,schema in COLLECTIONS:
        items=given[name]
        if items is None:
            good[name]=[]; continue
        if not isinstance(items,list):
            errors.append(f'{name}: expected a JSON array'); good[name]=[]; continue
        ok=[]
        for i,x in enumerate(items):
            errs=schema_errors(x,schema)
            errors.extend(f'{_tag(name,x,i)}: {e}' for e in errs)
            if not errs: ok.append(x)
        good[name]=ok
        key='chapter' if name=='crosswalk' else 'id'
        seen=[x.get(key) for x in items if isinstance(x,dict) and isinstance(x.get(key),(str,int))]
        dup=sorted({str(v) for v in seen if seen.count(v)>1})
        require(not dup,f'Duplicate ID in {name}: {", ".join(dup)}')
        ids[name]={x.get(key) for x in items if isinstance(x,dict)}
    if scope is not None:
        if isinstance(scope,dict):
            errs=schema_errors(scope,'scope.schema.json')
            errors.extend(f'scope: {e}' for e in errs)
            if not errs:
                require(all(s in ids['sources'] for s in scope['sources']),'scope: unknown source')
        else:
            errors.append('scope: geography/scope.json must be a JSON object')
    sid=ids.get('sources',set()); pid=ids.get('periods',set())
    valid_years=set(years(cfg['annual_start'],cfg['annual_end'])) if cfg['annual_start']<=cfg['annual_end'] else set()
    require(bool(valid_years),'project: annual_start must precede annual_end')
    cutoff=dt.date.fromisoformat(cfg['as_of'])
    require(cfg['annual_end']<=cutoff.year,'Annual range extends beyond release year')
    for s in good['sources']:
        tag=s['id']
        require(urlparse(s['url']).scheme in {'https','http'},f'{tag}: bad source URL')
        require(bool(s['inspection']) and bool(s['inspected_locator']),f'{tag}: missing inspection provenance')
        require(s['inspection'] in INSPECTION_DEPTH,f'{tag}: inspection {s["inspection"]!r} has no inspection-depth tier')
        require(bool(s['rights']),f'{tag}: missing rights statement')
        require(s['human_review'] in REVIEW_STATES,f'{tag}: invalid human review state')
        errors.extend(review_record_errors(tag,s,cutoff))
        if s.get('local_copy'):
            require(bool(s.get('sha256')),f'{tag}: local copy missing checksum')
            require(bool(s.get('redistribution_basis')),f'{tag}: local copy missing explicit rights basis')
        if s['publication_year'] is not None:
            require(s['publication_year']<=cutoff.year,f'{tag}: publication year after release cutoff')
        require(dt.date.fromisoformat(s['accessed'])<=cutoff,f'{tag}: access date after release cutoff')
    for p in good['periods']:
        require(all(s in sid for s in p['sources']),f'{p["id"]}: unknown source')
        if p['annual_span']:
            a,b=p['annual_span']; require(a!=0 and b!=0 and a<=b,f'{p["id"]}: bad annual span')
    for r in good['records']:
        tag=r['id']; d=r['date']
        require(bool(r['claim']) and bool(r['caveat']),f'{tag}: missing claim or limitation')
        require(r['scope_relation'] in RELATIONS,f'{tag}: unknown geography relation')
        require(bool(r['support']),f'{tag}: missing support')
        for c in r['support']:
            require(c['source'] in sid,f'{tag}: dangling source {c["source"]}')
            require(bool(c['locator']),f'{tag}: source without locator')
        require(all(p in pid for p in r['periods']),f'{tag}: unknown period')
        require(r['human_review'] in REVIEW_STATES,f'{tag}: invalid human review state')
        errors.extend(review_record_errors(tag,r,cutoff))
        if d['kind']=='historical':
            a,b=d['start_year'],d['end_year']
            require(a!=0 and b!=0 and a<=b,f'{tag}: invalid historical interval')
            require(b<=cfg['annual_end'],f'{tag}: future date')
            if d['precision'] in SINGLE_YEAR_PRECISION:
                require(a==b,f'{tag}: single-year precision {d["precision"]!r} on a multi-year range; use precision interval')
            elif d['precision']=='interval':
                require(a<b,f'{tag}: precision interval needs start_year before end_year')
            if d.get('date'):
                day=dt.date.fromisoformat(d['date'])
                require(day<=cutoff,f'{tag}: day after release cutoff')
                require(a==b==day.year,f'{tag}: day/year mismatch')
        elif d['kind']=='geological':
            require(d['older_ma']>=d['younger_ma']>=0,f'{tag}: inverted geological interval')
            require(not r['year_links'],f'{tag}: geological claim forced into a BCE/CE year')
        elif d['kind']=='undated':
            require(not r['year_links'],f'{tag}: undated claim given a calendar year')
        linked=[l['year'] for l in r['year_links']]
        dups=sorted({y for y in linked if linked.count(y)>1})
        require(not dups,f'{tag}: duplicate year link {dups[:5]}; one record counts once per year')
        if d['kind']=='historical' and d['start_year']!=d['end_year']:
            require(len(r['year_links'])<=1,f'{tag}: one interval record linked to {len(r["year_links"])} years; one interval is not that many independently evidenced annual events')
        for l in r['year_links']:
            y=l['year']; role=l['role']
            require(y in valid_years,f'{tag}: link to missing year {y}')
            require(role in ROLES,f'{tag}: invalid year role')
            if d['kind']=='historical':
                require(d['start_year']<=y<=d['end_year'],f'{tag}: year link outside date range')
                if d['start_year']!=d['end_year']:
                    require(role=='proposed_date',f'{tag}: interval forced into an exact year role')
                allowed=ROLE_PRECISION.get(role)
                if role=='year_attested' and d['precision'] not in allowed:
                    errors.append(f'{tag}: year link role {role!r} not allowed for precision {d["precision"]!r}; a conventional_year or interval is not an attested year')
            if role=='exact_date': require(d.get('precision')=='day',f'{tag}: exact-day role without day precision')
        for i,o in enumerate(r['other_dates']):
            otag=f'{tag}: other_dates[{i}] ({o["role"]})'
            if 'year' in o:
                require(o['year']<=cutoff.year,f'{otag}: year after release cutoff')
            if 'date' in o:
                require(dt.date.fromisoformat(o['date'])<=cutoff,f'{otag}: date after release cutoff')
    for a in good['audit']:
        require(all(s in sid for s in a['sources']),f'{a["id"]}: unknown audit source')
    for c in good['corpora']:
        bad=[s for s in c['source_ids'] if s not in sid]
        require(not bad,f'{c["id"]}: unknown corpus source {", ".join(bad)}')
    for c in good['crosswalk']:
        bad=[x.strip() for x in re.split(r'[;,]',c['dossiers']) if re.fullmatch(r'\s*[EP][0-9]{2,}\s*',x) and x.strip() not in pid]
        require(not bad,f'crosswalk {c["chapter"]}: unknown dossier {", ".join(bad)}')
    return errors


def local_link_errors():
    errors=[]
    for p in sorted(ROOT.rglob('*.md')):
        if '.git' in p.parts: continue
        # Generated/local documentation uses ordinary file links; URL links are skipped.
        for link in re.findall(r'\]\(([^\s)]+)\)',p.read_text(encoding='utf-8')):
            if urlparse(link).scheme or link.startswith('#'): continue
            target=unquote(link.split('#',1)[0])
            if target and not (p.parent/target).exists():
                errors.append(f'Broken local link: {p.relative_to(ROOT)} -> {target}')
    return errors


def _load_all():
    names={'project':'project.json','sources':'data/sources.json','periods':'data/periods.json','records':'data/records.json',
           'audit':'data/audit.json','corpora':'data/corpora.json','crosswalk':'data/prior_chapter_crosswalk.json','scope':'geography/scope.json'}
    data={}; errors=[]
    for k,f in names.items():
        try:
            data[k]=load(f)
        except (OSError,json.JSONDecodeError) as e:
            errors.append(f'{f}: cannot be read as UTF-8 JSON ({e})')
    return data,errors


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    args=parser.parse_args(argv)
    data,errors=_load_all()
    if errors:
        print('\n'.join(errors)); return 1
    errors=validate_data(data['project'],data['sources'],data['periods'],data['records'],data['audit'],
                         corpora=data['corpora'],scope=data['scope'],crosswalk=data['crosswalk'])
    if errors:
        print('\n'.join(errors)); return 1  # views cannot be compared reliably from malformed data
    out,stats=make_outputs()
    errors.extend(f'Stale/missing view: {p}' for p,t in out.items() if not (ROOT/p).exists() or (ROOT/p).read_text(encoding='utf-8')!=t)
    cfg=data['project']; expected={year_path(y).as_posix() for y in years(cfg['annual_start'],cfg['annual_end'])}
    actual={p.relative_to(ROOT).as_posix() for p in (ROOT/'years').rglob('*.md') if p.stem.isdigit()}
    if expected!=actual: errors.append('Annual filenames do not exactly match configured nonzero range')
    errors.extend(local_link_errors())
    if errors:
        print('\n'.join(errors)); return 1
    print('PASS: schemas, IDs, provenance, review records, dates, year-zero exclusion, annual coverage, generated views and local links.')
    print('This is structural validation only; all seed records still require independent human review.')
    return 0
if __name__=='__main__': raise SystemExit(main())
