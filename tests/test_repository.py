# SPDX-License-Identifier: MIT
import copy
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from build import years, label, year_path, load, make_outputs
from validate import validate_data

class RepositoryTests(unittest.TestCase):
    def data(self):
        return [load(x) for x in ['project.json','data/sources.json','data/periods.json','data/records.json','data/audit.json']]
    def test_no_year_zero(self): self.assertEqual(years(-2,2),[-2,-1,1,2])
    def test_zero_rejected(self):
        with self.assertRaises(ValueError): year_path(0)
    def test_labels(self): self.assertEqual(label(-257),'257 BCE')
    def test_count(self): self.assertEqual(len(years(-300,2026)),2326)
    def test_paths(self): self.assertEqual(year_path(-1).as_posix(),'years/BCE/0001.md')
    def test_seed_data_valid(self): self.assertEqual(validate_data(*self.data()),[])
    def test_unknown_source_fails(self):
        x=self.data(); x[3][0]['support'][0]['source']='S999'
        self.assertTrue(any('dangling source' in e for e in validate_data(*x)))
    def test_geological_year_link_fails(self):
        x=self.data(); x[3][0]['year_links']=[{'year':2000,'role':'year_attested'}]
        self.assertTrue(any('geological claim' in e for e in validate_data(*x)))
    def test_undated_year_link_fails(self):
        x=self.data(); x[3][1]['year_links']=[{'year':2006,'role':'research_history'}]
        self.assertTrue(any('undated claim' in e for e in validate_data(*x)))
    def test_interval_cannot_become_exact_event(self):
        x=self.data(); r=next(r for r in x[3] if r['id']=='R010'); r['year_links'][0]['role']='year_attested'
        self.assertTrue(any('interval forced' in e for e in validate_data(*x)))
    def test_approval_needs_reviewer(self):
        x=self.data(); x[3][0]['human_review']='approved'
        self.assertTrue(any('approval without' in e for e in validate_data(*x)))
    def test_current_year_cutoff(self):
        x=self.data(); r=next(r for r in x[3] if r['id']=='R031'); r['date']['date']='2026-12-01'
        self.assertTrue(any('after release cutoff' in e for e in validate_data(*x)))
    def test_bce_ce_navigation(self):
        out,_=make_outputs()
        self.assertIn('../CE/0001.md',out['years/BCE/0001.md'])
        self.assertIn('../BCE/0001.md',out['years/CE/0001.md'])
    def test_generation_deterministic(self):
        a,_=make_outputs(); b,_=make_outputs(); self.assertEqual(a,b)
    def test_empty_year_not_no_history(self):
        out,_=make_outputs(); t=out['years/CE/0123.md']
        self.assertIn('unresearched',t); self.assertIn('not proof that nothing happened',t)

if __name__=='__main__': unittest.main()
