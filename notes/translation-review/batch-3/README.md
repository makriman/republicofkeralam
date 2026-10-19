# ബാച്ച് 3: ഓഡിറ്റ്, കോർപ്പസുകൾ, താരതമ്യപട്ടിക, പരിധി, generator ലേബലുകൾ / Batch 3

ആശ്രയം: ബാച്ച് 2 (`work/malayalam-first-translation-batch-2`). Depends on batch 2, which depends on batch 1 (PR #3).

Source revision: `570f665e25480380e6be361627cf5cfb1285c093`.

## പരിധി / Scope

| ഫയൽ / File | ID-കൾ / IDs | ഫീൽഡുകൾ / Fields | Strings |
|---|---|---|---:|
| [audit.ml.json](audit.ml.json) | A001–A080 (80) | earlier_claim, corrected_treatment | 160 |
| [corpora.ml.json](corpora.ml.json) | C001–C031 (31) | name, next_task | 62 |
| [prior_chapter_crosswalk.ml.json](prior_chapter_crosswalk.ml.json) | chapters 1–46 | title, assessment | 92 |
| [scope.ml.json](scope.ml.json) | `geography/scope.json` | inclusion_rule, offshore_rule, exclusions_and_context[0–2] | 5 |
| [generator-labels.ml.json](generator-labels.ml.json) | `scripts/build.py#<label>` | headings, field labels, register intros, coverage labels; 36 verdict display labels | 125 |

Previews: [audit](audit.ml-en.preview.md), [corpora](corpora.ml-en.preview.md), [crosswalk](prior_chapter_crosswalk.ml-en.preview.md), [scope](scope.ml-en.preview.md).

## ശ്രദ്ധിക്കേണ്ടവ / Notes

- Crosswalk keys use the chapter number (`#1.title`), because those rows have no `id` field.
- Generator labels are checked by finding the English literal in `scripts/build.py` at the pinned revision. A `{placeholder}` marks a value the generator inserts; only the fixed fragments are compared. `proposed_en` appears where the current English uses an em dash; that is a proposal for Project B, not an edit.
- Verdict labels translate how enum values are displayed. The enum values in `data/audit.json` do not change.
- Chapter titles in the crosswalk are titles of an earlier draft of this project, not published works; they are translated. Source titles in `data/sources.json` remain untranslated by design.

## പരിശോധന / Review

AI-assisted. Model self-check (not human approval) as in batch 2. Human Malayalam review: pending. Specialist review: pending. Questions Q27–Q32 in [GLOSSARY.md](../GLOSSARY.md). What remains untranslated: [GAP_INVENTORY.md](../GAP_INVENTORY.md).
