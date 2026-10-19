# പരിഭാഷാ staging ഭാഗം / Translation review staging area

ശേഖരത്തിലെ വായനാപാഠങ്ങൾ മലയാളം ആദ്യം, ഇംഗ്ലീഷ് തുടർന്ന് എന്ന ക്രമത്തിൽ ലഭ്യമാക്കാനുള്ള നിർദിഷ്ട പരിഭാഷകളും പരിശോധനാക്കുറിപ്പുകളും ഇവിടെയാണ്. ഇവിടെയുള്ളതൊന്നും അടിസ്ഥാന ഡാറ്റയിലോ generated പേജുകളിലോ ചേർത്തിട്ടില്ല. എല്ലാ മലയാളപാഠവും AI സഹായത്തോടെ തയ്യാറാക്കിയ കരടാണ്. യോഗ്യതയുള്ള ഒരു മനുഷ്യനും ഇതുവരെ മലയാളഭാഷാപരിശോധന നടത്തിയിട്ടില്ല; വിഷയവിദഗ്ധപരിശോധനയും ബാക്കിയാണ്. മോഡൽ നടത്തിയ സ്വയംപരിശോധന മനുഷ്യാംഗീകാരമല്ല.

Proposed Malayalam-first translations and review notes for the archive's reader-facing text. Nothing here has been integrated into canonical data or generated pages. All Malayalam is an AI-assisted draft. No qualified human has performed Malayalam-language review yet, and specialist review is pending. Model self-checks are labelled as such and are not human approval.

## ഉള്ളടക്കം / Contents

- [manifest.json](manifest.json): ഓരോ ഇനത്തിന്റെയും source path/ID, source revision, നില, AI സഹായം, പദപ്രശ്നങ്ങൾ, പരിശോധനാനില. One entry per item with source path or stable ID, revision, status, AI disclosure, terminology questions and review state.
- [INVENTORY.md](INVENTORY.md), [inventory.json](inventory.json): hand-maintained ഗദ്യം, generated പാഠം, ഡാറ്റയിലെ ഗദ്യം എന്നിവ വേർതിരിച്ച പൂർണപട്ടികയും ബാച്ച് പദ്ധതിയും. Full inventory and batch plan.
- [GLOSSARY.md](GLOSSARY.md): പദാവലിയും തുറന്ന പദപ്രശ്നങ്ങളും. Terminology and open questions.
- [INTEGRATION_NOTES.md](INTEGRATION_NOTES.md): Project B-യ്ക്കുള്ള നിർദേശങ്ങൾ. Proposals for the integration owner.
- [batch-1/](batch-1/TOP_LEVEL_REVIEW.md): മുകൾത്തല രേഖാപരിശോധനയും സംഭാവന/ഗവേഷണനയ രേഖകളുടെ പരിഭാഷയും. Top-level review and contributor/research-policy translations.
- [batch-2/](batch-2/README.md): കാലഘട്ടങ്ങൾ, തെളിവുരേഖകൾ, സ്രോതസ്സുകുറിപ്പുകൾ. Periods, records and source notes keyed by ID.
- [batch-3/](batch-3/README.md): ഓഡിറ്റ്, കോർപ്പസുകൾ, താരതമ്യപട്ടിക, പരിധി, generator ലേബലുകൾ. Audit, corpora, crosswalk, scope and generator labels.
- [GAP_INVENTORY.md](GAP_INVENTORY.md): ഇനിയും ബാക്കിയുള്ളവ. What is still untranslated or unreviewed.
- `tools/`: staging ഫയലുകൾ നിർമ്മിക്കാനും പരിശോധിക്കാനുമുള്ള ചെറിയ scripts (standard library മാത്രം). Small helper scripts; read-only outside this folder.

## പരിശോധന / Checks

```bash
python notes/translation-review/tools/inventory.py
python notes/translation-review/tools/check_staging.py
python notes/translation-review/tools/check_staging.py --target-revision HEAD
python -m unittest discover -s notes/translation-review/tools -p 'test_*.py'
```

## നിലകൾ / Status values

- `draft_translation`: AI സഹായത്തോടെയുള്ള പരിഭാഷാകരട്, മനുഷ്യപരിശോധന ബാക്കി. AI-assisted draft, human review pending.
- `already_bilingual_reviewed_by_model`: നിലവിലുള്ള ദ്വിഭാഷാപാഠം; മോഡൽ നിർദേശങ്ങൾ മാത്രം. Existing bilingual text with model suggestions only.
- `untranslated`, `untranslated_reviewed_for_staleness`: ഇനിയും പരിഭാഷപ്പെടുത്താത്തത്. Not yet translated; kept visible.
- `stale`: മൂലപാഠം മാറിയതിനാൽ പുതുക്കേണ്ടത്. Source changed after translation.

ഒരു മനുഷ്യപരിശോധകൻ യഥാർത്ഥത്തിൽ പരിശോധിച്ച് പേര്/ID, പരിശോധിച്ച കാര്യങ്ങൾ, revision എന്നിവ രേഖപ്പെടുത്തുമ്പോൾ മാത്രമേ `human_language_review` മാറ്റാവൂ. Change `human_language_review` only when a real reviewer records their identifier, what they checked and the revision.

The default checker validates pinned snapshots only. The optional target check conservatively compares complete source files against an explicit revision, failing on any difference or missing revision/path. It does not automatically update source revisions or approve translations.
