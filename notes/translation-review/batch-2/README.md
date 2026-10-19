# ബാച്ച് 2: കാലഘട്ടപഠനരേഖകൾ, തെളിവുരേഖകൾ, സ്രോതസ്സുകുറിപ്പുകൾ / Batch 2

ആശ്രയം: ബാച്ച് 1 (`work/malayalam-first-translation`, PR #3). ഈ ബാച്ച് ബാച്ച് 1-ലെ പദാവലി, manifest, tools എന്നിവ ഉപയോഗിക്കുന്നു. Depends on batch 1 for the glossary, manifest format and tools.

Source revision: `570f665e25480380e6be361627cf5cfb1285c093`.

## പരിധി / Scope

| ഫയൽ / File | ID-കൾ / IDs | ഫീൽഡുകൾ / Fields | Strings |
|---|---|---|---:|
| [periods.ml.json](periods.ml.json) | E01–E12, P01–P07 (19) | title, display_window, central_question, established_in_this_pass, limitations, research_tasks[] | 171 |
| [records.ml.json](records.ml.json) | R001–R031 (31) | title, claim, caveat, date.original_expression, date.datum (where present), authoring, rights | 188 |
| [sources.ml.json](sources.ml.json) | S001–S042 (42) | inspection_note, rights | 84 |

Readable previews (Malayalam first, retained English second): [periods](periods.ml-en.preview.md), [records](records.ml-en.preview.md), [sources](sources.ml-en.preview.md).

ഓരോ entry-യും `data/<file>.json#<ID>.<field>[index]` എന്ന സ്ഥിരമായ key ഉപയോഗിക്കുന്നു; array സ്ഥാനമല്ല. `en_sha256` മൂലവാക്യം മാറിയാൽ stale ആണെന്ന് കണ്ടെത്താനാണ്. Every entry is keyed by stable ID and field, never by array position; `en_sha256` lets an integrator detect stale Malayalam.

## പരിഭാഷപ്പെടുത്താത്തവ / Deliberately not translated

IDs, enum values, URLs, DOIs, `support[].locator`, `inspected_locator`, dates, tags, `sources` arrays. Source `title` values in `data/sources.json` stay as published (42 titles). No explanatory Malayalam gloss of source titles is offered in this batch; if one is added later it must be labelled as an explanatory translation, never as the title.

## ഇപ്പോഴും ബാക്കിയുള്ളവ / Still open after this batch

Generated pages in `periods/`, `records/`, `sources/` also contain fixed generator labels (headings, field names, `ID — title` lines). Those labels are batch 3 material and need generator support from Project B. See [INTEGRATION_NOTES.md](../INTEGRATION_NOTES.md).

## പരിശോധന / Review

AI-assisted. Model self-check (not human approval): every digit run and S### citation in each English string also appears in its Malayalam; no em dash in Malayalam; English matches the source at the pinned revision; qualifiers such as “approximately”, “proposed”, “not inspected”, “pending”, “attributed” kept. Human Malayalam review: pending. Specialist review (geology, archaeology, epigraphy, law): pending. Terminology questions Q13–Q26 in [GLOSSARY.md](../GLOSSARY.md).
