# പരിഭാഷാവിടവുകൾ / Translation gap inventory

Source revision `570f665e25480380e6be361627cf5cfb1285c093`. Batches 1 to 3 together. Counts come from [INVENTORY.md](INVENTORY.md) and [manifest.json](manifest.json).

## 1. ഇനിയും പരിഭാഷപ്പെടുത്താത്ത രേഖകൾ / Hand-maintained files not yet translated

| Path | Words (approx.) | Reason / note |
|---|---:|---|
| `docs/PROJECT_CHARTER.md` | 913 | Not reached. Highest priority next, because it defines scope. |
| `docs/CORPUS_PLAN.md` | 997 | Not reached. Overlaps with staged corpus names and next tasks. |
| `docs/ROADMAP.md` | 590 | Not reached. Contains 6 em dashes in English; changes over time, so translate after Project B work settles. |
| `docs/KNOWN_GAPS.md` | 328 | Not reached. |
| `docs/LINK_AUDIT.md` | 194 | Not reached. Mostly URLs and status; low value. |
| `geography/README.md` | 561 | Not reached. Scope rules are staged from `geography/scope.json`. |
| `schemas/README.md` | 117 | Not reached. Technical. |
| `NOTICE.md`, `RELEASE_NOTES.md`, `IMPORT_PROVENANCE.md`, `VALIDATION.md` | 632 | Reviewed for staleness only (batch 1). |
| `LICENSE.md` | 227 | Legal text. A non-binding Malayalam summary at most; never a replacement. |
| `templates/record.json` | 106 | Example placeholders; translate with the schema work in Project B. |

## 2. ബോധപൂർവം നിലനിർത്തിയ ഇംഗ്ലീഷ് / Retained English by design

- 42 source titles in `data/sources.json` (original titles are never translated).
- IDs, enum values, URLs, DOIs, locators, dates, tags, file paths, quotations.

## 3. Generator support ആവശ്യമുള്ളവ / Needs generator support (Project B)

All 2,428 generated files remain English. Malayalam for their inputs is staged: data prose (762 of 804 strings, the remainder being the 42 retained titles) and 125 generator labels. Rendering needs the bilingual generator described in [INTEGRATION_NOTES.md](INTEGRATION_NOTES.md) I2 and I3. Year pages (2,328 files) are built entirely from labels and staged titles, so no per-page translation is needed.

Generator strings not yet staged: rare error or empty-state messages and any literal added after the pinned revision. The checker reports staged literals that disappear from `scripts/build.py`.

## 4. അവലോകനം / Review still required

Every Malayalam string in batches 1 to 3 is an AI-assisted draft. Human Malayalam review: pending for all. Specialist review needed for geology, archaeology, epigraphy, law and place names. Open terminology questions: Q1 to Q32 in [GLOSSARY.md](GLOSSARY.md).
