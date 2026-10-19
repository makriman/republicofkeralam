# മുകൾത്തല രേഖകളുടെ പരിശോധന / Top-level document review

അടിസ്ഥാന revision: `570f665e25480380e6be361627cf5cfb1285c093` (`main`). പരിശോധിച്ചത്: AI മോഡൽ (model review). ഇത് മനുഷ്യ ഭാഷാപരിശോധനയോ വിഷയവിദഗ്ധപരിശോധനയോ അല്ല. ഈ ഫയലുകൾ Project B/പദ്ധതി ഉടമയുടെ ഉത്തരവാദിത്തത്തിലാണ്; ഇവിടെ നിർദേശങ്ങൾ മാത്രം. ഒരു ഫയലും നേരിട്ട് മാറ്റിയിട്ടില്ല.

Base revision as above. Reviewed by: AI model (model review), not a human language or subject review. These files are owned by Project B or the project owner; this page only proposes changes. No file was edited.

## README.md (TR-B1-001), ഇതിനകം ദ്വിഭാഷ / already bilingual

Malayalam-first ക്രമം, സംഖ്യകൾ (2,326 / 18 / 2,308 / 31 / 12 / 7 / ക്രി.മു. 300 മുതൽ ക്രി.വ. 2026), കണ്ണികൾ, commands എന്നിവ ഇംഗ്ലീഷുമായി ഒത്തുനോക്കി; പൊരുത്തക്കേടില്ല. Em dash ഇല്ല. Order, numbers, links and commands match the English. No em dashes.

നിർദേശങ്ങൾ / Proposed wording changes:

| # | വരി / Line | നിലവിൽ / Current | നിർദേശം / Proposed | കാരണം / Reason |
|---|---|---|---|---|
| R1 | 3 | “തെളിവുകളുടെ പരിശോധനാതീയതി: 2026 ഒക്ടോബർ 11” | “തെളിവുപരിശോധനയുടെ അവസാനതീയതി: 2026 ഒക്ടോബർ 11” | EN says “inspection cutoff”; “പരിശോധനാതീയതി” reads as the single date of inspection, not a cutoff. |
| R2 | 15 | “ഭൂമിശാസ്ത്രപരമായ ദീർഘകാല ചരിത്രത്തിനും” | “ദീർഘ ഭൂകാലത്തിനും (deep time)” | ഭൂമിശാസ്ത്രം usually means geography; EN is “deep-time”. See glossary. Language reviewer to confirm. |
| R3 | 25 | “ഈ രേഖ മാത്രം വായിച്ച് ഒരു സ്രോതസ്സ് മുഴുവനായി പരിശോധിച്ചതായി കരുതരുത്” | “ഒരു സ്രോതസ്സ് ഉദ്ധരിച്ചിട്ടുണ്ട് എന്നതുകൊണ്ട് അതിന്റെ പൂർണപാഠം വായിച്ചു എന്നർത്ഥമില്ല” | EN: “a citation does not mean its full text was read”. “ഈ രേഖ” is ambiguous. |

## CONTRIBUTING.md (TR-B1-002), ഇതിനകം ദ്വിഭാഷ / already bilingual

ഘടനയും ഉള്ളടക്കവും ഇംഗ്ലീഷുമായി ഒത്തുനോക്കി. Sections, commands and links match. No em dashes.

| # | ഭാഗം / Section | നിലവിൽ / Current | നിർദേശം / Proposed | കാരണം / Reason |
|---|---|---|---|---|
| C1 | കോഡ് അറിയാത്തവർക്കും | “ജീവനുള്ള വ്യക്തിയുടെ അനുഭവം” | “ജീവിച്ചിരിക്കുന്ന വ്യക്തിയുടെ അനുഭവം” | More natural for “living person”; matches the staged RIGHTS_AND_ETHICS translation. |
| C2 | ചരിത്രവിവരം ചേർക്കുമ്പോൾ | links to `docs/EVIDENCE_POLICY.md`, `docs/CHRONOLOGY.md` labelled in Malayalam | No text change. After integration, these targets can point to Malayalam-first versions staged in `batch-1/docs/`. | Integration dependency, Project B. |

## docs/work-packages/translation.md (TR-B1-003, branch file from 1e8d0ef)

ദ്വിഭാഷ, Malayalam-first. Scope and acceptance terms are reflected in this staging area. No change proposed.

## ഇംഗ്ലീഷിൽ മാത്രമുള്ള മുകൾത്തല ഫയലുകൾ / English-only top-level files

ഇവ ഈ batch-ൽ പരിഭാഷപ്പെടുത്തിയിട്ടില്ല (batch 3). വസ്തുതാപരമായ കാലഹരണം ശ്രദ്ധയിൽപ്പെട്ടു; ഉടമ തീരുമാനിക്കണം. Not translated in this batch (deferred to batch 3). Possible staleness found, for the owner to decide; no change made:

| ID | Path | കണ്ടെത്തൽ / Finding |
|---|---|---|
| TR-B1-013 | `NOTICE.md` | “No remote repository has been created” reads as stale now that the GitHub repository exists. Historical statement about the original package may be intended; owner to decide whether to date-qualify it. |
| TR-B1-014 | `RELEASE_NOTES.md` | Title contains an em dash (`Release 0.1.0 — research foundation`); house style would use a colon. “No remote repository has been published” has the same staleness question. |
| TR-B1-015 | `IMPORT_PROVENANCE.md` | Future tense (“will be proposed in one draft import pull request”) is stale since the import PR has merged. |
| TR-B1-016 | `VALIDATION.md` | Records Python 3.13.5 results for the original package. Accurate as a historical report; translation should keep it dated rather than restate it as current. |
| TR-B1-017 | `LICENSE.md` | Legal text. A Malayalam explanatory summary may be added later, but must be labelled non-authoritative; the English license text stays controlling. |

Generated പേജുകളിലെ em dash-കൾ (`sources/README.md` 84, `periods/README.md` 19, `audit/CHAT_AUDIT.md` 80, ഓരോ `sources/S*.md`-ലും 1) `scripts/build.py`-ലെ templates-ൽനിന്ന് വരുന്നു. അവ Project B-യുടെ generator-ൽ മാത്രമേ മാറ്റാവൂ; [INTEGRATION_NOTES.md](../INTEGRATION_NOTES.md) കാണുക.
Em dashes in generated views come from `scripts/build.py` templates and must be changed only in the generator (Project B).
