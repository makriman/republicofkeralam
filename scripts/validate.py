#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Offline structural checks. Passing does NOT verify historical truth."""
from __future__ import annotations
import datetime as dt
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse, unquote
from build import ROOT, load, years, year_path, make_outputs, ROLES

RELATIONS={'core','regional_context','global_context','external_reference','external_action_affecting_core','external_custody_or_research'}

def validate_data(cfg,ss,pp,rr,aa):
    errors=[]
    def require(ok,msg):
        if not ok: errors.append(msg)
    for name,items in [('sources',ss),('periods',pp),('records',rr),('audit',aa)]:
        ids=[x.get('id') for x in items]
        require(len(ids)==len(set(ids)),f'Duplicate ID in {name}')
        require(all(isinstance(x,str) and re.fullmatch(r'[A-Z][0-9]{2,}',x) for x in ids),f'Invalid ID in {name}')
    sid={x['id'] for x in ss}; pid={x['id'] for x in pp}
    valid_years=set(years(cfg['annual_start'],cfg['annual_end']))
    cutoff=dt.date.fromisoformat(cfg['as_of'])
    require(cfg['annual_end']<=cutoff.year,'Annual range extends beyond release year')
    for s in ss:
        require(urlparse(s['url']).scheme in {'https','http'},f'{s["id"]}: bad source URL')
        require(bool(s['inspection']) and bool(s['inspected_locator']),f'{s["id"]}: missing inspection provenance')
        require(bool(s['rights']),f'{s["id"]}: missing rights statement')
        if s.get('local_copy'):
            require(bool(s.get('sha256')),f'{s["id"]}: local copy missing checksum')
            require(bool(s.get('redistribution_basis')),f'{s["id"]}: local copy missing explicit rights basis')
    for p in pp:
        require(all(s in sid for s in p['sources']),f'{p["id"]}: unknown source')
        if p['annual_span']:
            a,b=p['annual_span']; require(a!=0 and b!=0 and a<=b,f'{p["id"]}: bad annual span')
    for r in rr:
        tag=r['id']; d=r['date']
        require(bool(r['claim']) and bool(r['caveat']),f'{tag}: missing claim or limitation')
        require(r['scope_relation'] in RELATIONS,f'{tag}: unknown geography relation')
        require(bool(r['support']),f'{tag}: missing support')
        for c in r['support']:
            require(c['source'] in sid,f'{tag}: dangling source {c["source"]}')
            require(bool(c['locator']),f'{tag}: source without locator')
        require(all(p in pid for p in r['periods']),f'{tag}: unknown period')
        require(r['human_review'] in {'pending','approved','rejected'},f'{tag}: invalid human review state')
        if r['human_review']=='approved':
            require(bool(r.get('reviewers')),f'{tag}: approval without named review record')
        if d['kind']=='historical':
            a,b=d['start_year'],d['end_year']
            require(type(a)==int and type(b)==int and a!=0 and b!=0 and a<=b,f'{tag}: invalid historical interval')
            require(b<=cfg['annual_end'],f'{tag}: future date')
            if d.get('date'):
                try:
                    day=dt.date.fromisoformat(d['date'])
                    require(day<=cutoff,f'{tag}: day after release cutoff')
                    require(a==b==day.year,f'{tag}: day/year mismatch')
                except ValueError: errors.append(f'{tag}: invalid day date')
        elif d['kind']=='geological':
            require(d['older_ma']>=d['younger_ma']>=0,f'{tag}: inverted geological interval')
            require(not r['year_links'],f'{tag}: geological claim forced into a BCE/CE year')
        elif d['kind']=='undated':
            require(not r['year_links'],f'{tag}: undated claim given a calendar year')
        else: errors.append(f'{tag}: unknown date kind')
        for l in r['year_links']:
            y=l['year']; role=l['role']
            require(y in valid_years,f'{tag}: link to missing year {y}')
            require(role in ROLES,f'{tag}: invalid year role')
            if d['kind']=='historical':
                require(d['start_year']<=y<=d['end_year'],f'{tag}: year link outside date range')
                if d['start_year']!=d['end_year']:
                    require(role=='proposed_date',f'{tag}: interval forced into an exact year role')
            if role=='exact_date': require(d.get('precision')=='day',f'{tag}: exact-day role without day precision')
    for a in aa:
        require(all(s in sid for s in a['sources']),f'{a["id"]}: unknown audit source')
    return errors

def local_link_errors():
    errors=[]
    for p in ROOT.rglob('*.md'):
        # Generated/local documentation uses ordinary file links; URL links are skipped.
        for link in re.findall(r'\]\(([^\s)]+)\)',p.read_text(encoding='utf-8')):
            if urlparse(link).scheme or link.startswith('#'): continue
            target=unquote(link.split('#',1)[0])
            if target and not (p.parent/target).exists():
                errors.append(f'Broken local link: {p.relative_to(ROOT)} -> {target}')
    return errors

def main():
    errors=validate_data(load('project.json'),load('data/sources.json'),load('data/periods.json'),load('data/records.json'),load('data/audit.json'))
    out,_=make_outputs()
    errors.extend(f'Stale/missing view: {p}' for p,t in out.items() if not (ROOT/p).exists() or (ROOT/p).read_text(encoding='utf-8')!=t)
    cfg=load('project.json'); expected={year_path(y).as_posix() for y in years(cfg['annual_start'],cfg['annual_end'])}
    actual={p.relative_to(ROOT).as_posix() for p in (ROOT/'years').rglob('*.md') if p.stem.isdigit()}
    if expected!=actual: errors.append('Annual filenames do not exactly match configured nonzero range')
    errors.extend(local_link_errors())
    if errors:
        print('\n'.join(errors)); return 1
    print('PASS: IDs, provenance, dates, year-zero exclusion, annual coverage, generated views and local links.')
    print('This is structural validation only; all seed records still require independent human review.')
    return 0
if __name__=='__main__': raise SystemExit(main())
