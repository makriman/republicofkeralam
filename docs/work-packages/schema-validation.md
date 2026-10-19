# ഘടനയും കണക്കുകളും പരിശോധിക്കുന്ന PR

നില: നിർദേശിക്കുന്ന സാങ്കേതിക ജോലി. ടെസ്റ്റുകൾ ചരിത്രസത്യത്തിനുള്ള അംഗീകാരമല്ല.

## ഫയൽ ഉത്തരവാദിത്തം

ഈ worker integration-ന്റെ ഉത്തരവാദിത്തം വഹിക്കും. `project.json`, `schemas/`, `scripts/`, `tests/`, `data/`, generated views, `coverage/` എന്നിവയിൽ മറ്റ് worker-കൾ ഒരേസമയം മാറ്റം വരുത്തരുത്. `notes/translation-review/`, `notes/evidence-review/` എന്നിവയിൽനിന്നുള്ള അംഗീകരിച്ച നിർദേശങ്ങൾ മാത്രമേ ചേർക്കാവൂ. നിലവിലെ Pro ഘടന നിലനിർത്തുക. ലാൻഡിങ് പേജ് മാറ്റരുത്.

## ജോലി

നിലവിലുള്ള build, validation, tests പ്രവർത്തിപ്പിച്ച് യഥാർത്ഥ ഫലങ്ങൾ രേഖപ്പെടുത്തുക. ഇപ്പോഴുള്ള canonical inputs-ഉം generated outputs-ഉം പട്ടികപ്പെടുത്തുക. മലയാളം ആദ്യം ഇംഗ്ലീഷ് തുടർന്ന് render ചെയ്യാനുള്ള ഏറ്റവും ചെറിയ backward-compatible മാറ്റം തയ്യാറാക്കുക. Translation, source inspection, historical review, rights review എന്നിവ വേർതിരിക്കുക. പുതിയ status മൂല്യങ്ങൾ ഉപയോഗിക്കുന്നതിന് മുൻപ് schema-യും validator-ഉം പരിശോധിക്കുക.

## ടെസ്റ്റുകൾ

- ID-കൾ വേറിട്ടതും references സാധുവുമായിരിക്കണം.
- പൂജ്യം വർഷമില്ല; BCE/CE ക്രമവും കാലപരിധികളും ശരിയായിരിക്കണം.
- കൃത്യമല്ലാത്ത തീയതി കൃത്യവർഷ സംഭവമാകരുത്; ഒരു site phase പല സ്വതന്ത്ര സംഭവങ്ങളായി എണ്ണരുത്.
- സംഭവകാലം, കണ്ടെത്തൽ, പ്രസിദ്ധീകരണം, ഡിജിറ്റൈസേഷൻ എന്നിവ വേർതിരിക്കണം.
- ശൂന്യ വർഷങ്ങൾ unresearched ആയി തുടരണം. Research milestones-ഉം ചരിത്രസംഭവങ്ങളും കവറേജിൽ വേർതിരിക്കണം.
- unique records, annual links, sources, inspected sources എന്നിവ പ്രത്യേകം എണ്ണണം. മലയാളപരിഭാഷയുടെ കവറേജ് ചരിത്രപരിശോധനയുടെ കവറേജല്ല.
- generated output ആവർത്തിച്ച build-കളിൽ ഒരുപോലെയായിരിക്കണം; stale files, broken links, missing bilingual fields കണ്ടെത്തണം.
- `notes/`-ലെ കൈയെഴുത്ത് ഫയലുകൾ overwrite ചെയ്യരുത്.
- പരിശോധിച്ച boundary geometry ഇല്ലാതെ spatial filtering പ്രവർത്തനക്ഷമമാകരുത്.
- current-year cutoff, ഭാവിയിലെ തീയതികൾ, മാറിയ source revision-ന്റെ പഴയ പരിഭാഷ എന്നിവയ്ക്ക് വ്യക്തമായ പരിശോധന വേണം.

## സ്വീകരിക്കാനുള്ള വ്യവസ്ഥകൾ

Migration ആവശ്യമെങ്കിൽ ആവർത്തിക്കാവുന്ന നിർദേശങ്ങൾ നൽകുക. തെറ്റായ fixture-കൾക്ക് tests പരാജയപ്പെടണം. README-യിലെ കണക്കുകളും coverage output-ഉം യഥാർത്ഥ ഡാറ്റയോട് ഒത്തിരിക്കണം. താഴെക്കൊടുത്ത commands-ന്റെ ഫലങ്ങൾ PR-ൽ ചേർക്കുക. പുതിയ release തയ്യാറാക്കുമ്പോൾ manifest/checksum നയം അനുസരിക്കുക. മനുഷ്യപരിശോധന ബാക്കിയുള്ളവ അതേ നിലയിൽ തുടരണം. Draft PR മാത്രം; merge/publish ചെയ്യരുത്.

# Schema, validation and coverage PR

Status: proposed technical work. Passing tests does not establish historical truth.

## Ownership

This worker owns integration into `project.json`, `schemas/`, `scripts/`, `tests/`, `data/`, generated views and `coverage/`. Other workers must not edit those files concurrently. Integrate reviewed proposals from `notes/translation-review/` and `notes/evidence-review/`. Preserve the Pro structure and leave the landing page untouched.

## Work

Run the current build, validation and tests; record actual results. Map canonical inputs to generated outputs. Add the smallest backward-compatible Malayalam-first, English-second rendering support. Keep translation, source inspection, historical review and rights review separate. Inspect schema and validator constraints before adding status values.

## Tests

- Unique IDs and valid references.
- No year zero; correct BCE/CE ordering and interval boundaries.
- Uncertain dates never become exact-year events; a site phase is not counted as multiple independent events.
- Separate event, discovery, publication and digitization dates.
- Empty years stay unresearched; distinguish research milestones from past-event coverage.
- Count unique records, annual links, sources and inspected sources separately. Translation coverage is distinct from scholarly review.
- Deterministic output; detect stale files, broken links and missing bilingual fields.
- Preserve hand-maintained files in `notes/`.
- Keep spatial filtering disabled without checked boundary geometry.
- Test current-year cutoffs, future dates and translations stale after source revision.

## Acceptance

Document reproducible migrations where needed. Invalid fixtures must fail. README counts and coverage output must agree with actual data. Include actual command results. Follow manifest/checksum policy when preparing a release. Human-review-pending items must retain that status. Draft PR only; do not merge or deploy.

```bash
python scripts/build.py
python scripts/build.py --check
python scripts/validate.py
python -m unittest discover -s tests -v
```
