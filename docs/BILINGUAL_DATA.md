# മലയാളം ആദ്യം, ഇംഗ്ലീഷ് തുടർന്ന്: പരിഭാഷാ ഡാറ്റയും rendering-ഉം / Malayalam first, English second: translation data and rendering

> നില: AI സഹായത്തോടെ എഴുതിയ സാങ്കേതിക രേഖ. മലയാള ഭാഷാപരിശോധന ബാക്കി. / Status: AI-assisted technical document. Human Malayalam-language review pending.

## മലയാളം

### അടിസ്ഥാനതത്വം

ഇംഗ്ലീഷ് പാഠം ഇപ്പോഴും `data/*.json`-ലെയും `geography/scope.json`-ലെയും അടിസ്ഥാന ഫീൽഡുകളിലാണ്. മലയാളപരിഭാഷ `data/i18n/ml/*.json` എന്ന വേറിട്ട കാറ്റലോഗുകളിലാണ്. അതിനാൽ ID-കൾ, JSON keys, enum മൂല്യങ്ങൾ, നിലവിലുള്ള സ്ഥാനസൂചനകൾ എന്നിവ മാറുന്നില്ല; പഴയ ഡാറ്റയ്ക്ക് migration ആവശ്യമില്ല. ഒരു ഫീൽഡിന് നിലവിലുള്ള (stale അല്ലാത്ത, നിരസിക്കാത്ത) പരിഭാഷയുണ്ടെങ്കിൽ മാത്രം generator മലയാളം ആദ്യവും ഇംഗ്ലീഷ് തുടർന്നും നൽകും. കാറ്റലോഗ് ഇല്ലെങ്കിൽ പേജുകൾ മുമ്പത്തെപ്പോലെ ഇംഗ്ലീഷിൽ മാത്രം.

### കാറ്റലോഗ് ഘടന

ഓരോ ഫയലിനും `catalogue: "translation-catalogue/1"`, `language: "ml"`, `source_path`, `entries` എന്നിവ വേണം. ഓരോ entry-ക്കും:

- `key`: ഫയൽ, സ്ഥിര ID, ഫീൽഡ്. ഉദാ: `data/records.json#R014.claim`, `data/periods.json#E01.research_tasks[2]`, `data/prior_chapter_crosswalk.json#7.title` (അധ്യായ നമ്പർ), `geography/scope.json#scope.offshore_rule`, generator ലേബലിന് `scripts/build.py#record.h_limitations`.
- `ml`: മലയാളപാഠം.
- `en_sha256`: പരിഭാഷപ്പെടുത്തിയ കൃത്യമായ ഇംഗ്ലീഷ് പാഠത്തിന്റെ UTF-8 SHA-256-ലെ ആദ്യ 16 hex അക്കങ്ങൾ.
- `source_revision`: ആ ഇംഗ്ലീഷ് ഉണ്ടായിരുന്ന commit (40 അക്കം).
- `ai_assisted`: true അല്ലെങ്കിൽ false.
- `human_language_review`: `pending`, `approved`, `rejected`.
- ഐച്ഛികം: `en` (പരിശോധകർക്കുള്ള ഇംഗ്ലീഷ് പകർപ്പ്; നിലവിലെ ഇംഗ്ലീഷുമായി ഒന്നായിരിക്കണം), `specialist_review`, `reviewers`, `terminology_questions`, `note`.

`approved` അല്ലെങ്കിൽ `rejected` ആക്കാൻ `reviewers`-ൽ `reviewer_type: "human"` ഉള്ള ഒരു രേഖ വേണം (`reviewer`, `checked`, `date`). മോഡൽ പരിശോധന രേഖപ്പെടുത്താം; അത് അംഗീകാരമല്ല.

### പരിഭാഷപ്പെടുത്താവുന്ന ഫീൽഡുകൾ

വായനക്കാർക്കുള്ള ഗദ്യം മാത്രം: records-ൽ `title`, `claim`, `caveat`, `date.original_expression`, `date.datum`, `date.calendar`, `authoring`, `rights`; sources-ൽ `title` (വിശദീകരണ പരിഭാഷയായി മാത്രം), `inspection_note`, `rights`; periods-ൽ `title`, `display_window`, `central_question`, `established_in_this_pass`, `limitations`, `research_tasks[]`; audit-ൽ `earlier_claim`, `corrected_treatment`; corpora-യിൽ `name`, `next_task`; crosswalk-ൽ `title`, `assessment`; scope-ൽ `inclusion_rule`, `offshore_rule`, `exclusions_and_context[]`. ID, enum, URL, DOI, locator, തീയതി, source പട്ടിക, tag എന്നിവയ്ക്കുള്ള entry validator നിരസിക്കും.

### പുതുമ (freshness)

ഇംഗ്ലീഷ് മാറിയാൽ `en_sha256` പൊരുത്തപ്പെടില്ല. അപ്പോൾ `validate.py` പിശക് നൽകും; generator ആ ഫീൽഡിന് ഇംഗ്ലീഷ് മാത്രം കാണിക്കും. വീണ്ടും പരിഭാഷപ്പെടുത്തി hash പുതുക്കുക, അല്ലെങ്കിൽ entry നീക്കുക. ഇല്ലാത്ത പരിഭാഷകൾ എണ്ണി പട്ടികപ്പെടുത്തും; പൂർത്തിയായതായി കണക്കാക്കില്ല. `python scripts/validate.py --require-translation ml` ഏതെങ്കിലും ഫീൽഡിന് നിലവിലുള്ള പരിഭാഷ ഇല്ലെങ്കിൽ പരാജയപ്പെടും.

### Rendering

മലയാളം ആദ്യം, തുടർന്ന് ഇംഗ്ലീഷ്. തലക്കെട്ടുകളും ചെറിയ ലേബലുകളും `മലയാളം / English` എന്ന രൂപത്തിൽ; ഖണ്ഡികകൾ മലയാള ഖണ്ഡിക, തുടർന്ന് ഇംഗ്ലീഷ് ഖണ്ഡിക. പട്ടികയുടെ തലവരി ഓരോ കള്ളിയിലും ചേർക്കും. മലയാളം ഉപയോഗിക്കുന്ന ഓരോ പേജിലും AI സഹായവും പരിശോധനാനിലയും പറയുന്ന ഒരു അറിയിപ്പും front matter-ൽ `translation_ml`-ഉം ഉണ്ടാകും. പ്രസിദ്ധീകരിച്ച സ്രോതസ്സ് തലക്കെട്ട് മാറ്റില്ല; മലയാളം "വിശദീകരണ പരിഭാഷ, ഔദ്യോഗിക തലക്കെട്ടല്ല" എന്ന വരിയായി മാത്രം വരും.

### കവറേജ്

`coverage/stats.json`-ലെ `translation.ml` ഭാഗം അടിസ്ഥാന ഡാറ്റയിലെ 845 പാഠഫീൽഡുകളും (integration batch 1-ലെ S043–S048 കാർഡുകൾക്ക് മുമ്പ് 827) 139 generator ലേബലുകളും (103 സ്ഥിരം, audit verdict-കൾക്ക് 36) എണ്ണുന്നു. പരിഭാഷയുടെ വ്യാപ്തി സ്രോതസ്സുപരിശോധനയോ പണ്ഡിതപരിശോധനയോ അല്ല.

### Integration batch 1

`notes/translation-review/`-ലെ കരടുകൾ `scripts/integration/import_ml_staging.py` വഴി `data/i18n/ml/`-ലേക്ക് മാറ്റി. ഇംഗ്ലീഷ് മാറാത്ത entries മാത്രം ചേർത്തു; PR #4 തിരുത്തലുകൾ ഇംഗ്ലീഷ് മാറ്റിയ 17 ഫീൽഡുകൾക്കും, 23 `date.calendar` പാഠങ്ങൾക്കും, പുതിയ S043–S048 കാർഡുകളുടെ കുറിപ്പുകൾക്കും അവകാശവരികൾക്കും പുതിയ മലയാളം എഴുതി (`scripts/integration/ml_supplement.json`). എല്ലാം AI സഹായത്തോടെ; മനുഷ്യ ഭാഷാപരിശോധന ബാക്കി. ഇപ്പോൾ 845-ൽ 797 ഡാറ്റാഫീൽഡുകളും 139-ൽ 139 ലേബലുകളും നിലവിലുള്ളതാണ്. ശേഷിക്കുന്ന 48 എണ്ണം സ്രോതസ്സ് തലക്കെട്ടുകളാണ്; പ്രസിദ്ധീകരിച്ച രൂപത്തിൽ തുടരുന്നു. തലക്കെട്ടുകളിലെ em dash വേർതിരിവ് `: ` ആക്കി. `project.json`-ൽ `primary_language: "en"` തുടരുന്നു: അടിസ്ഥാന ഡാറ്റ ഇംഗ്ലീഷിലാണ്, മലയാളം ഇതുവരെ മനുഷ്യർ പരിശോധിച്ചിട്ടില്ല; മാറ്റം ഉടമയുടെ തീരുമാനമാണ്. വിശദാംശങ്ങൾ: [INTEGRATION_BATCH_1.md](INTEGRATION_BATCH_1.md).

### Migration

ആവശ്യമില്ല. നിലവിലെ ഡാറ്റ മാറ്റമില്ലാതെ സാധുവാണ്. പഴയ validator സ്വീകരിച്ചിരുന്നതും ഇപ്പോൾ നിരസിക്കുന്നതുമായ നിയമങ്ങൾ ഓരോന്നിനും `tests/fixtures/invalid/`-ൽ fixture ഉണ്ട്.

---

## English

### Principle

English stays in the canonical fields of `data/*.json` and `geography/scope.json`. Malayalam lives in separate catalogues under `data/i18n/ml/*.json`, so IDs, JSON keys, enum values and existing locators never change and existing data needs no migration. The generator puts Malayalam first and English second only where a current translation exists (not stale, not rejected). Without catalogues the pages are English only, exactly as before.

### Catalogue format

Each file has `catalogue: "translation-catalogue/1"`, `language: "ml"`, `source_path` and `entries` (schema: `schemas/translation-catalogue.schema.json`). Each entry has:

| Field | Required | Meaning |
|---|---|---|
| `key` | yes | File, stable ID and field path. Examples: `data/records.json#R014.claim`, `data/periods.json#E01.research_tasks[2]`, `data/prior_chapter_crosswalk.json#7.title` (chapter number), `geography/scope.json#scope.offshore_rule`, and `scripts/build.py#record.h_limitations` for generator labels. |
| `ml` | yes | Malayalam text. |
| `en_sha256` | yes | First 16 hex digits of SHA-256 over the exact UTF-8 English that was translated. |
| `source_revision` | yes | 40-character commit where that English was read. Provenance only; freshness uses the hash. |
| `ai_assisted` | yes | Whether a model drafted the Malayalam. |
| `human_language_review` | yes | `pending`, `approved` or `rejected`. |
| `en` | no | Copy of the English for reviewers. If present it must equal the current English. |
| `specialist_review` | no | `pending`, `approved`, `rejected` or `not_required`. |
| `reviewers` | no | Review records: `reviewer` (contributor identifier), `reviewer_type` (`human` or `model`), `checked`, `date`. |
| `terminology_questions`, `note` | no | Free text for reviewers. |

```json
{
  "key": "data/records.json#R014.claim",
  "ml": "യാത്രാഡയറി ഉദ്ധരണി അതിന്റെ 1498 ഭാഗത്ത് Calicut-ന് (കോഴിക്കോട്) സമീപം നങ്കൂരമിട്ടതിനെ വിവരിക്കുന്നു.",
  "en_sha256": "8a48f174e994c033",
  "source_revision": "570f665e25480380e6be361627cf5cfb1285c093",
  "ai_assisted": true,
  "human_language_review": "pending",
  "specialist_review": "pending"
}
```

Compute the hash with `python3 -c "import hashlib,sys; print(hashlib.sha256(sys.argv[1].encode()).hexdigest()[:16])" "<English text>"`.

`approved` or `rejected` needs a `reviewers` entry with `reviewer_type: "human"`, the same rule used for records and sources. A model check can be recorded but never counts as approval.

### Translatable fields

Reader-facing prose only:

| File | Fields |
|---|---|
| `data/records.json` | `title`, `claim`, `caveat`, `date.original_expression`, `date.datum`, `date.calendar`, `authoring`, `rights` |
| `data/sources.json` | `title` (explanatory translation only), `inspection_note`, `rights` |
| `data/periods.json` | `title`, `display_window`, `central_question`, `established_in_this_pass`, `limitations`, `research_tasks[]` |
| `data/audit.json` | `earlier_claim`, `corrected_treatment` |
| `data/corpora.json` | `name`, `next_task` |
| `data/prior_chapter_crosswalk.json` | `title`, `assessment` |
| `geography/scope.json` | `inclusion_rule`, `offshore_rule`, `exclusions_and_context[]` |
| `scripts/build.py` | every key in `LABELS`, plus `verdict.<value>` for each audit verdict |

Entries for IDs, enums, URLs, DOIs, locators, dates, source lists or tags are refused.

### Checks

`scripts/validate.py` checks every catalogue: schema; one entry per key; the key resolves to an existing item and a translatable field; `en_sha256` (and `en`, if present) matches the current English; the Malayalam contains Malayalam script, keeps every number from the English, contains no em dash, and for labels keeps the same `{placeholders}`, link targets and heading, bold, bracket or table form; review records follow the shared rule.

A stale entry fails validation and is not rendered. A rejected entry is not rendered. Missing translations are counted and listed, never treated as complete. `python scripts/validate.py --require-translation ml` fails while any field or label lacks a current translation; the default run only reports the counts.

### Rendering

| Unit | Rendering |
|---|---|
| Heading label or title | `## മലയാളം / English` |
| Bold label | `**മലയാളം: / English:**` |
| Link label with one target | `[മലയാളം / English](../README.md)`, keeping the original target |
| Paragraph | Malayalam paragraph, then the English paragraph |
| Label followed by text on one line | Malayalam, hard line break, English |
| Research task list item | Malayalam, hard line break, indented English |
| Table header row | each cell `മലയാളം / English` |
| Template label | both versions formatted with the same values |

A page that renders any Malayalam gets a notice after its first heading stating that the Malayalam is AI-assisted (or human-translated) and whether human language review is pending or recorded, plus a `translation_ml` front-matter value when the page has front matter. A published source title is never replaced; its Malayalam appears on a separate line marked "Explanatory translation, not the source title". Malayalam for date wording appears under the JSON date block, which stays unchanged.

With no catalogues the generated views are English only (checked by `tests/test_bilingual.py`). Before integration batch 1 they were byte-identical to the earlier views; that batch also changed the heading separator.

### Coverage measures

`coverage/stats.json` keeps every earlier key and adds separate measures: year links, records with year links, annual pages with a past-event link versus only research, publication or access history, source cards cited by records, source cards by inspection-depth tier (`INSPECTION_DEPTH` in `scripts/build.py`), human-reviewed source cards, and `translation.ml`. The translation denominators are the 845 non-empty translatable strings in canonical data (827 before the six source cards S043–S048 added in integration batch 1) and the 139 generator labels (103 fixed labels and 36 audit verdicts). The translation staging inventory counts 804 data strings because it did not include the 23 `date.calendar` strings (3 distinct values). Translation coverage is not source inspection or scholarly review. No internet-wide percentage is calculated.

### Integration batch 1

`scripts/integration/import_ml_staging.py` converted the drafts staged under `notes/translation-review/` into `data/i18n/ml/`. Only entries whose English is unchanged were imported. New Malayalam was written for the 17 fields whose English the PR #4 corrections changed, the 23 `date.calendar` strings, and the inspection notes and rights of the new cards S043–S048 (`scripts/integration/ml_supplement.json`). All of it is AI-assisted with human language review pending. Current coverage: 797 of 845 data fields and 139 of 139 labels. The 48 missing strings are source titles, which stay as published.

The em-dash separator in generated headings (translation note I3) is now `: `. `project.json` keeps `primary_language: "en"` (note I5): the canonical data is English and no Malayalam has had human review, so changing it is an owner decision. Details: [INTEGRATION_BATCH_1.md](INTEGRATION_BATCH_1.md).

### Migration

None needed. Existing data validates unchanged. Rules that now reject data the old validator accepted: namespace ID patterns, the schema-level required fields and precision values per date kind, the shared human review record, at most one year link per interval, no duplicate year links, no `conventional_year` labelled `year_attested`, checked `other_dates`, mapped inspection labels, and the spatial-filtering guard. Each is covered by a fixture in `tests/fixtures/invalid/`.
