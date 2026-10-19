> 2026-10-19: താഴെയുള്ളത് ആദ്യ ബാച്ചിന്റെ ചരിത്രക്കുറിപ്പാണ്. നിലവിലെ തിരുത്തലുകളും പരിശോധനയുടെ പരിധിയും [അവലോകനക്കുറിപ്പിൽ](REVIEW_CORRECTIONS_2026-10-19.md) കാണാം.
> 2026-10-19: This is the initial batch record. The [review correction note](REVIEW_CORRECTIONS_2026-10-19.md) supersedes its dates, coverage and merge gate.

# Integration batch 1: തെളിവുതിരുത്തലുകളും മലയാള കാറ്റലോഗുകളും / Integration batch 1: evidence corrections and Malayalam catalogues

> നില: AI സഹായത്തോടെ തയ്യാറാക്കിയ സംയോജനക്കരട്. മനുഷ്യ പണ്ഡിതപരിശോധനയും മലയാള ഭാഷാപരിശോധനയും ബാക്കി. മോഡൽ പരിശോധന അംഗീകാരമല്ല. / Status: AI-assisted integration draft. Human scholarly review and human Malayalam-language review are pending. Model checking is not approval.

## മലയാളം

### ആശ്രയങ്ങൾ

ഈ ബ്രാഞ്ച് (`work/integration-batch-1`) PR #5-ന്റെ `e82cb82` എന്ന head-ൽനിന്ന് തുടങ്ങുന്നു. PR #4 (`153e2e2`), PR #7 (`457d8f6`; അതിൽ PR #6 `e8dfacb`, PR #3 `ee2d600` ഉൾപ്പെടുന്നു) എന്നിവ സാധാരണ merge commit-കളായി ചേർത്തിരിക്കുന്നു. ആ PR-കളും മനുഷ്യപരിശോധനയും പൂർത്തിയാകുന്നതിന് മുമ്പ് ഇത് merge ചെയ്യരുത്. ആദ്യ import commit `166214f` ചരിത്രത്തിൽ മാറ്റമില്ലാതെ തുടരുന്നു.

### PR #4 തിരുത്തലുകൾ

ഓരോ മാറ്റവും PR #4 രേഖപ്പെടുത്തിയ `current_value`-മായി ഒത്തുനോക്കിയ ശേഷമാണ് പ്രയോഗിച്ചത് (`scripts/integration/apply_evidence_corrections.py`).

- പ്രയോഗിച്ചത്: PC-01 മുതൽ PC-19 വരെ, താഴെ പറയുന്ന രണ്ട് വരികൾ ഒഴികെ. ആറ് പുതിയ സ്രോതസ്സ് കാർഡുകൾ: NEW-SRC-01 മുതൽ 06 വരെ S043 മുതൽ S048 വരെ. ബദൽ വർഷങ്ങൾ (R010: ക്രി.മു. 257, ഏകദേശം ക്രി.മു. 252; R019: 1894, 1895, ഏകദേശം 1896) ആരുടേതെന്ന് പറഞ്ഞ് caveat-ൽ മാത്രം; ഒന്നും സ്വീകരിച്ചിട്ടില്ല.
- പ്രയോഗിക്കാത്തത്: PC-04-ലെ `date.precision` മാറ്റം (നിർദേശിത മൂല്യം schema-യിലെ historical precision പട്ടികയിലില്ല; PC-21 ഘടനാതീരുമാനം വേണം). PC-15-ലെ Pliny രേഖ (രചനാകാലത്തിന് ഉദ്ധരിച്ച സ്രോതസ്സില്ല; PR #4 തന്നെ അത് വ്യവസ്ഥയാക്കുന്നു). PC-20 (വാക്കുകൾ ഉടമ തീരുമാനിക്കണം; `docs/proposals/current-status-correction.md`-ൽ നിർദേശമായി തുടരുന്നു; NOTICE, RELEASE_NOTES, LICENSE മാറ്റിയിട്ടില്ല). PC-21-ലെ ബദൽവർഷഫീൽഡും വേറിട്ട സ്ഥല ID-കളും (ഘടനാമാറ്റം; ഉടമ തീരുമാനിക്കണം).
- PC-21-ൽനിന്ന് ഭാഗികമായി: ഈ തിരുത്തലുകൾക്ക് ആവശ്യമായ അഞ്ച് പരിശോധനാമൂല്യങ്ങൾ (`abstract_and_preview`, `relevant_passages_translation`, `relevant_passages_ocr_text`, `relevant_passages_secondary_copy`, `full_text`) source schema-യിലും `INSPECTION_DEPTH`-ലും ചേർത്തു.
- 2026-10-18-ന് പരിശോധനയുടെ ആഴം പുതുക്കിയ S002, S003, S009, S015, S017, S018, S020 എന്നിവയുടെ `accessed` തീയതി 2026-10-18 ആക്കി. S023-ന്റെ ആ ദിവസത്തെ ശ്രമം പരാജയപ്പെട്ടതിനാൽ അതിന്റെ തീയതി മാറ്റിയില്ല.
- പുതിയ പ്രവേശനതീയതികൾ കാരണം `project.json`-ലെ `as_of` 2026-10-18 ആക്കി. അതുകൊണ്ട് എല്ലാ വാർഷിക പേജുകളുടെയും front matter മാറുന്നു.

### മലയാള പരിഭാഷ

- `notes/translation-review`-ലെ 869 കരടുകൾ `data/i18n/ml/`-ലേക്ക് മാറ്റി (`scripts/integration/import_ml_staging.py`). PR #4 ഇംഗ്ലീഷ് മാറ്റിയ 17 കരടുകൾ പഴയതായതിനാൽ ഒഴിവാക്കി; ഒരു verdict ലേബൽ ഇനി നിലവിലില്ല.
- പുതിയ മലയാളം 53 എണ്ണം: മാറിയ 17 ഫീൽഡുകൾ, പുതിയ verdict ലേബൽ, 23 `date.calendar` പാഠങ്ങൾ, S043 മുതൽ S048 വരെയുള്ള കാർഡുകളുടെ 12 കുറിപ്പുകളും അവകാശവരികളും.
- എല്ലാ entry-യിലും `ai_assisted: true`, `human_language_review: "pending"`, `specialist_review: "pending"`.
- കവറേജ്: 845-ൽ 797 ഡാറ്റാഫീൽഡുകൾ, 139-ൽ 139 ലേബലുകൾ. ശേഷിക്കുന്ന 48 എണ്ണം സ്രോതസ്സ് തലക്കെട്ടുകളാണ്. അതിനാൽ `validate.py --require-translation ml` ഇപ്പോഴും പരാജയപ്പെടുന്നു; അത് പ്രതീക്ഷിതമാണ്.
- തലക്കെട്ടുകളിലെ em dash വേർതിരിവ് `: ` ആക്കി. ഒരു generated പേജിലും ഇനി em dash ഇല്ല.
- `primary_language: "en"` തുടരുന്നു. അടിസ്ഥാന ഡാറ്റ ഇംഗ്ലീഷിലാണ്; മലയാളം ആദ്യം കാണിക്കുന്നത് rendering മാത്രമാണ്; മനുഷ്യ ഭാഷാപരിശോധന ഇല്ല. മാറ്റം ഉടമയുടെ തീരുമാനമാണ്.

### ശേഷിക്കുന്നവ

`notes/evidence-review/UNRESOLVED.md`-ലെ U-01 മുതൽ U-15 വരെ എല്ലാം തുറന്നുകിടക്കുന്നു. batch 1-ലെ കൈയെഴുത്തുരേഖകളുടെ മലയാളം (`docs/*.md`, templates, GitHub templates) ഈ ബാച്ചിൽ ചേർത്തിട്ടില്ല. സ്ഥലപരമായ ഉൾപ്പെടുത്തൽ നിർജീവമായി തുടരുന്നു. ഘടനാപരിശോധന വിജയിക്കുന്നത് ചരിത്രസത്യത്തിന്റെ സ്ഥിരീകരണമല്ല.

---

## English

### Dependencies

This branch (`work/integration-batch-1`) starts at PR #5's head `e82cb82`. PR #4 (`153e2e2`) and PR #7 (`457d8f6`, which contains PR #6 `e8dfacb` and PR #3 `ee2d600`) are brought in with regular merge commits so the dependency is visible in history. Do not merge this before those PRs, and not before human review. The original import commit `166214f` is unchanged in history.

### PR #4 corrections

Each change was applied only after checking the `current_value` recorded by PR #4 (`scripts/integration/apply_evidence_corrections.py`).

| Correction | Target | Applied |
|---|---|---|
| PC-01, PC-02 | R008 caveat; support adds S044, S043, S045 | yes |
| PC-03 | NEW-SRC-01 to 06 become S043 to S048 | yes |
| PC-04 | R019 caveat with 1894, 1895 and about 1896 attributed | caveat yes; `date.precision` no |
| PC-05, PC-06 | S009 full text; R006 claim, caveat, support | yes |
| PC-07, PC-08 | S015 passages in OCR; A011 witness forms | yes |
| PC-09 | R010 caveat with 257 BCE (Dhammika) and about 252 BCE (Hultzsch) attributed; support adds S015 | yes |
| PC-10 | A012 Edict XIII absence; A013 adds S015 | yes |
| PC-11, PC-12, PC-13 | S002 depth and note; S003 issue 10(1–2); R005 caveat | yes |
| PC-14 | R011 caveat on Pliny and the Periplus | yes |
| PC-15 | A017 verdict, treatment, source S046 | yes; optional Pliny record no |
| PC-16 | A018 treatment; adds S047 | yes |
| PC-17 | S017 `metadata_only`; S018 `full_text` | yes |
| PC-18 | S023 404 note and alternate URL | yes |
| PC-19 | R013 funded period; S020 locator | yes |
| PC-20 | Current-status wording | no |
| PC-21 | Inspection vocabulary; alternative-year field; place IDs | vocabulary values used here only |

Not applied, and why:

- PC-04 `date.precision: attributed_year_conflicting_sources`: not a value the record schema allows for historical dates. It needs the PC-21 decision on how alternative years are modelled. The conflicting years are attributed in the caveat instead and none is adopted.
- PC-15 optional Pliny record: PR #4 makes it conditional on a cited source for the composition date, and none has been checked.
- PC-20: wording and the private reporting route are owner decisions. It stays a proposal in `docs/proposals/current-status-correction.md`. NOTICE.md, RELEASE_NOTES.md and LICENSE.md are not edited.
- PC-21 alternative-year field and separate place IDs for Pattanam and Muziris: structural changes to the record model that need an owner decision. Places are free-text strings today.

Related changes:

- The five inspection values these corrections use (`abstract_and_preview`, `relevant_passages_translation`, `relevant_passages_ocr_text`, `relevant_passages_secondary_copy`, `full_text`) were added to `schemas/source.schema.json` and to `INSPECTION_DEPTH`, as the schema description requires.
- `accessed` is 2026-10-18 for S002, S003, S009, S015, S017, S018 and S020, whose depth or locator was re-established that day (access log in `notes/evidence-review/claim-reviews.json`). S023 keeps its earlier date because that day's access failed.
- `project.json` `as_of` moved from 2026-10-11 to 2026-10-18 because the new evidence was accessed on that date and the validator rejects access dates after the cutoff. Every annual page's front matter changes for that reason only.
- Changed records carry `updated: 2026-10-18`.
- Some wording carried over from PR #4 needs a human look, for example A018 still says local passages "remain unverified" while the appended sentence records that they were read in an 1885 translation.

### Malayalam

- 869 staged drafts were converted into `data/i18n/ml/` by `scripts/integration/import_ml_staging.py`: 867 whose English is unchanged since `570f665` and 2 labels whose English now equals the staging's `proposed_en`. 17 drafts became stale because PR #4 changed their English and were left out rather than re-hashed. One verdict label no longer exists.
- 53 new Malayalam entries (`scripts/integration/ml_supplement.json`): the 17 changed fields, the new verdict label, the 23 `date.calendar` strings (3 distinct values) and the 12 inspection notes and rights lines of S043 to S048.
- Every entry has `ai_assisted: true`, `human_language_review: "pending"` and `specialist_review: "pending"`. No reviewer record was added.
- Coverage: 797 of 845 data fields and 139 of 139 generator labels are current. The 48 missing are source titles, which stay as published, so `validate.py --require-translation ml` still fails as expected.
- The em-dash separator in generated headings and lists is now `: `. No generated view contains an em dash.
- `primary_language` stays `"en"`. The canonical data is English, Malayalam-first is a rendering choice, and no Malayalam has had human review. Changing it is an owner decision.
- Hand-maintained document translations from batch 1 (`docs/*.md`, templates, GitHub templates) are not integrated here.

### Regenerated views

All views are rebuilt by `scripts/build.py`. Changes come from: the corrected data and six new source pages; Malayalam-first rendering where a current translation exists; the separator; and `as_of` in annual pages. `MANIFEST.sha256` is re-hashed for files this branch changes and extended with its new files. `notes/translation-review/` and `notes/evidence-review/` stay outside the manifest as working notes owned by their PRs, as do `IMPORT_PROVENANCE.md`, `docs/work-packages/` and `docs/proposals/`.

### Readiness limits

All of U-01 to U-15 in `notes/evidence-review/UNRESOLVED.md` remain open. Spatial inclusion stays disabled; there is no licensed boundary dataset. Passing the structural checks does not verify historical truth, translation quality or rights. This batch is not ready to merge until PRs #3, #6, #7, #4 and #5 are reviewed and merged and a human has reviewed the evidence changes and the Malayalam.
