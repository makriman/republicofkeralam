# ഇന്നത്തെ കേരളത്തിന്റെ ഭൂപ്രദേശത്തിന്റെ ചരിത്രം

പതിപ്പ് 0.1.0: പ്രാരംഭ ഗവേഷണ ശേഖരം. ഈ പതിപ്പിലെ തെളിവുകളുടെ പരിശോധനാതീയതി: 2026 ഒക്ടോബർ 11.

ഇന്ന് കേരളത്തിന്റെ ഭരണപരിധിക്കുള്ളിലുള്ള ഭൂഭാഗത്തിന്റെ ചരിത്രം ശേഖരിക്കുന്ന പദ്ധതിയാണിത്. പാറകളുടെ രൂപീകരണം, പഴയ പരിസ്ഥിതികൾ, മനുഷ്യവാസത്തിന്റെ തെളിവുകൾ, സമൂഹങ്ങൾ, ഇന്നത്തെ സംഭവങ്ങൾ എന്നിവ ഇതിൽ ഉൾപ്പെടുന്നു. ഒരു സ്രോതസ്സിൽ “കേരളം” എന്ന വാക്കില്ലെങ്കിലും ഈ ഭൂഭാഗത്തെക്കുറിച്ചുള്ള തെളിവുണ്ടാകാം. ആ വാക്ക് ഉണ്ടെന്നതുകൊണ്ടുമാത്രം ഒരു രേഖ പദ്ധതിയുടെ പരിധിയിൽ വരണമെന്നില്ല.

ഈ ശേഖരത്തിലെ ഗവേഷണം പ്രാരംഭ ഘട്ടത്തിലാണ്. 2,326 വാർഷിക പേജുകളിൽ 18 എണ്ണത്തിലാണ് വർഷവുമായി ബന്ധപ്പെട്ട പ്രാരംഭ രേഖകളിലേക്കുള്ള കണ്ണികളുള്ളത്. ശേഷിക്കുന്ന 2,308 പേജുകൾ ഗവേഷണം നടത്താനുള്ളവയായി അടയാളപ്പെടുത്തിയിട്ടുണ്ട്. 31 അടിസ്ഥാന തെളിവുരേഖകളിൽ പഴയ സംഭവങ്ങളെക്കുറിച്ചുള്ള രേഖകൾക്കൊപ്പം ഗവേഷണവും പ്രസിദ്ധീകരണവും സംബന്ധിച്ച വിവരങ്ങളുമുണ്ട്. സ്വതന്ത്ര മനുഷ്യവിദഗ്ധരുടെ ചരിത്രപരിശോധനയും ഏതെങ്കിലും സമ്പൂർണ രേഖാശേഖരത്തിന്റെ ഇനംതിരിച്ചുള്ള പരിശോധനയും പൂർത്തിയായിട്ടില്ല. ഇവ 0.1.0 പതിപ്പിന്റെ കണക്കുകളാണ്; പിന്നീട് ചേർക്കുന്ന രേഖകൾക്കായി [കവറേജ് വിവരങ്ങൾ](coverage/README.md) പരിശോധിക്കുക.

## വായന തുടങ്ങാൻ

- [മുൻ മറുപടികളുടെ പരിശോധന](audit/CHAT_AUDIT.md), [പദ്ധതിയുടെ ലക്ഷ്യവും പരിധിയും](docs/PROJECT_CHARTER.md), [ഗവേഷണ പുരോഗതി](coverage/README.md)
- [കാലഘട്ടങ്ങൾ](periods/README.md), [വർഷങ്ങൾ](years/README.md), [തെളിവുരേഖകൾ](records/README.md), [സ്രോതസ്സുകൾ](sources/README.md)
- [സംഭാവന നൽകാനുള്ള മാർഗങ്ങൾ](CONTRIBUTING.md), [ഗവേഷണ പദ്ധതി](docs/ROADMAP.md)

ഭൂമിശാസ്ത്രപരമായ ദീർഘകാല ചരിത്രത്തിനും ചരിത്രാതീതകാലത്തിനുമായി 12 പഠനരേഖകളും രേഖാമൂലമുള്ള ചരിത്രകാലത്തിനായി ഏഴ് പഠനരേഖകളുമുണ്ട്. വാർഷിക സൂചിക ക്രി.മു. 300 മുതൽ ക്രി.വ. 2026 വരെയാണ്. പൂജ്യം എന്ന വർഷമില്ല. ക്രി.മു. 300 എന്നത് സൂചികയുടെ തുടക്കമാണ്; ഈ ഭൂഭാഗത്തിന്റെ രേഖാമൂലമുള്ള ചരിത്രം അന്നാണ് ആരംഭിച്ചതെന്ന നിഗമനമല്ല.

## ഫയലുകൾ എങ്ങനെ ക്രമീകരിച്ചിരിക്കുന്നു

- `data/records.json`, `data/sources.json`, `data/periods.json`: അടിസ്ഥാന വിവരങ്ങൾ. ഇവയിൽനിന്നാണ് `records/`, `sources/`, `periods/` എന്നിവയിലെ വായനാപേജുകൾ തയ്യാറാക്കുന്നത്.
- `years/BCE/`, `years/CE/`: വർഷങ്ങൾക്കനുസരിച്ചുള്ള കണ്ണികളും ഗവേഷണനിലയും.
- `geography/scope.json`: ഭൗമപരിധി സംബന്ധിച്ച താൽക്കാലിക ക്രമീകരണം. നിലവിലെ ഭരണപരിധിയുടെ ഉപയോഗാനുമതിയുള്ളതും പരിശോധിച്ചതുമായ ഭൂപട ഡാറ്റ ഇനിയും ചേർത്തിട്ടില്ല. സ്വയമേവയുള്ള ഭൗമപരിധി പരിശോധന പ്രവർത്തനക്ഷമമാക്കിയിട്ടില്ല.
- `docs/`, `templates/`, `schemas/`: ഗവേഷണനയം, മാതൃകകൾ, ഡാറ്റയുടെ ഘടന.
- `notes/`: പ്രവർത്തനക്കുറിപ്പുകൾ. `scripts/`, `tests/`: പേജുകൾ നിർമ്മിക്കാനും ഘടന പരിശോധിക്കാനുമുള്ള കോഡ്.

ഈ പതിപ്പിൽ മൂന്നാംകക്ഷികളുടെ പുസ്തകങ്ങളുടെ പൂർണപാഠങ്ങളോ സ്കാൻ ശേഖരങ്ങളോ ഉൾപ്പെടുത്തിയിട്ടില്ല. സ്വയമേവ വെബ് ശേഖരണം നടത്തുന്ന സംവിധാനവും തയ്യാറായ വെബ്സൈറ്റും ഇതിന്റെ ഭാഗമല്ല. ഈ രേഖ മാത്രം വായിച്ച് ഒരു സ്രോതസ്സ് മുഴുവനായി പരിശോധിച്ചതായി കരുതരുത്; അതിന്റെ സ്രോതസ്സ് കാർഡിൽ പരിശോധനയുടെ പരിധി നൽകിയിട്ടുണ്ട്.

## തീയതികളും തെളിവുകളും

ഒരു സംഭവം നടന്ന കാലം, അതിനെക്കുറിച്ചുള്ള രേഖ എഴുതിയ കാലം, ഗവേഷണം പ്രസിദ്ധീകരിച്ച വർഷം എന്നിവ വേർതിരിച്ച് സൂക്ഷിക്കുന്നു. ഒരു ഫോസിലിന്റെ പ്രായം അതിനെക്കുറിച്ചുള്ള ലേഖനത്തിന്റെ പ്രസിദ്ധീകരണവർഷമല്ല. നൂറ്റാണ്ട് മാത്രം അറിയുന്ന തീയതി അത്രത്തോളം കൃത്യതയോടെ രേഖപ്പെടുത്തണം. വർഷപ്പേജ് നിറയ്ക്കാനായി കൃത്യമായ വർഷം അനുമാനിക്കരുത്.

[കാലക്രമനയം](docs/CHRONOLOGY.md), [ഡാറ്റ മാതൃക](docs/DATA_MODEL.md), [തെളിവുകളും പരിശോധനയും](docs/EVIDENCE_POLICY.md), [ഭൗമപരിധി](geography/README.md).

ലഭ്യമായ ഡിജിറ്റൽ രേഖകൾ കഴിയുന്നത്ര കണ്ടെത്തി സൂചികപ്പെടുത്തുകയാണ് ലക്ഷ്യം. ഓരോ രേഖാശേഖരത്തിന്റെയും പരിശോധനാതീയതി, ഇനങ്ങൾ, ലഭ്യമാകാത്ത ഭാഗങ്ങൾ, പരിശോധിച്ച ഉള്ളടക്കം, ഉപയോഗാവകാശം എന്നിവ രേഖപ്പെടുത്തണം. [ശേഖരണ പദ്ധതി](docs/CORPUS_PLAN.md), [ശേഖരങ്ങളുടെ പട്ടിക](data/corpora.json).

## കമ്പ്യൂട്ടറിൽ ഉപയോഗിക്കാൻ

Python 3.10 അല്ലെങ്കിൽ അതിനുശേഷമുള്ള പതിപ്പ് വേണം. അടിസ്ഥാന പാക്കേജ് Python 3.13.5-ൽ പരിശോധിച്ചതായി രേഖപ്പെടുത്തിയിട്ടുണ്ട്. Markdown പേജുകൾ നിർമ്മിക്കാൻ പുറത്തുനിന്നുള്ള Python പാക്കേജുകളോ ഇന്റർനെറ്റ് ബന്ധമോ ആവശ്യമില്ല.

```bash
python scripts/build.py
python scripts/build.py --check
python scripts/validate.py
python -m unittest discover -s tests -v
```

അടിസ്ഥാന JSON ഫയലുകൾ തിരുത്തിയശേഷം പേജുകൾ വീണ്ടും നിർമ്മിക്കുക. സ്വയമേവ നിർമ്മിക്കുന്ന പേജുകളിൽ നേരിട്ട് വരുത്തുന്ന മാറ്റങ്ങൾ അടുത്ത നിർമ്മാണത്തിൽ നഷ്ടപ്പെടാം. കൈയെഴുത്ത് ഗവേഷണക്കുറിപ്പുകൾ `notes/`-ൽ സൂക്ഷിക്കുക. ഈ പരിശോധനകൾ ഡാറ്റയുടെ ഘടന പരിശോധിക്കുന്നു; ചരിത്രവസ്തുതകളുടെ ശരിതെറ്റുകൾ തീരുമാനിക്കുന്നില്ല.

## ഭാഷയും പുനരുപയോഗവും

ശേഖരത്തിലെ വായനയ്ക്കുള്ള ഉള്ളടക്കം മലയാളം ആദ്യം, ഇംഗ്ലീഷ് തുടർന്ന് എന്ന രീതിയിലാക്കുകയാണ് ലക്ഷ്യം. ഈ README-യും സംഭാവനാമാർഗരേഖയും AI സഹായത്തോടെ തയ്യാറാക്കിയ പരിഭാഷകളാണ്. മലയാള ഭാഷാപരിശോധനയും വിഷയവിദഗ്ധരുടെ പരിശോധനയും ബാക്കിയുണ്ട്. മറ്റ് ഫയലുകളുടെ പരിഭാഷ പൂർത്തിയായതായി ഇതിലൂടെ അവകാശപ്പെടുന്നില്ല. പ്രത്യേക ലാൻഡിങ് പേജ് ഇംഗ്ലീഷിൽ തുടരും.

സ്വന്തമായി എഴുതിയ കോഡിന് MIT ലൈസൻസും അവകാശമുള്ള സ്വന്തം വിവരണങ്ങൾക്കും ബാധകമായ സമ്പാദകീയ സംഭാവനകൾക്കും CC BY 4.0 ലൈസൻസുമാണ്. മൂന്നാംകക്ഷികളുടെ പുസ്തകങ്ങൾ, പരിഭാഷകൾ, ചിത്രങ്ങൾ, സ്കാനുകൾ, ഡാറ്റാബേസുകൾ എന്നിവയുടെ അവകാശങ്ങൾ അതത് ഉടമകൾക്കുതന്നെയാണ്. [ലൈസൻസ്](LICENSE.md), [അവകാശങ്ങളും നൈതികതയും](docs/RIGHTS_AND_ETHICS.md), [പതിപ്പിന്റെ പരിമിതികൾ](RELEASE_NOTES.md).

# History of the present-day Kerala territory

Version 0.1.0: research foundation. Evidence inspection cutoff: 11 October 2026.

This project collects the history of the territory now administered as Kerala, from the formation of its rocks and past environments through human occupation to the contemporary record. A source can concern this land without using the name “Kerala.” Using that name does not automatically place a source within scope.

Research is at an early stage. Of 2,326 annual pages, 18 contain year-specific seed links; the remaining 2,308 are marked unresearched. The 31 canonical evidence records include research and publication milestones alongside evidence of past events. Independent human scholarly review and a complete item-level inventory of any collection remain unfinished. These are version 0.1.0 counts; see [coverage](coverage/README.md) for subsequent changes.

## Start reading

- [Audit of earlier answers](audit/CHAT_AUDIT.md), [project charter](docs/PROJECT_CHARTER.md), [coverage](coverage/README.md)
- [Period dossiers](periods/README.md), [annual navigation](years/README.md), [evidence records](records/README.md), [source cards](sources/README.md)
- [Contributing](CONTRIBUTING.md), [research roadmap](docs/ROADMAP.md)

There are 12 deep-time/prehistory dossiers and seven documentary-period dossiers. The annual index runs from 300 BCE to 2026 CE without a year zero. Its starting year is an indexing choice, not a finding that the territory's written history began then.

## Repository layout

- `data/records.json`, `data/sources.json`, `data/periods.json`: canonical inputs for the readable views in `records/`, `sources/` and `periods/`.
- `years/BCE/`, `years/CE/`: annual links and research statuses.
- `geography/scope.json`: provisional scope configuration. A licensed, checked current-boundary dataset is still missing; automatic spatial inclusion is disabled.
- `docs/`, `templates/`, `schemas/`: research policies, examples and data structures.
- `notes/`: working research notes. `scripts/`, `tests/`: generation and structural checks.

This release does not bundle third-party full texts or scan collections. It includes neither an automatic web scraper nor a deployed website. Each source card states the depth of inspection; a citation does not mean its full text was read.

## Dates and evidence

The time of an event, the date of its surviving record and the publication date of research are recorded separately. A fossil's age is not its paper's publication year. A date known only to a century must retain that precision. Do not infer an exact year to fill an annual page.

[Chronology](docs/CHRONOLOGY.md), [data model](docs/DATA_MODEL.md), [evidence policy](docs/EVIDENCE_POLICY.md), [geographic scope](geography/README.md).

The aim is to discover and index as much relevant digital material as possible. Each bounded collection needs a dated inventory, missing-item record, inspection status and rights assessment. See the [corpus plan](docs/CORPUS_PLAN.md) and [collection registry](data/corpora.json).

## Use locally

Python 3.10 or later is required. The original package records testing with Python 3.13.5. Building Markdown needs no third-party Python packages or network connection.

```bash
python scripts/build.py
python scripts/build.py --check
python scripts/validate.py
python -m unittest discover -s tests -v
```

Edit canonical JSON and rebuild the pages. Direct edits to generated pages may be lost at the next build. Keep hand-maintained research notes in `notes/`. These checks assess structural consistency, not historical truth.

## Language and reuse

Reader-facing archive content is being prepared in Malayalam first, followed by English. This README and the contribution guide are AI-assisted translation drafts, pending Malayalam-language and specialist review. This does not claim that the remaining repository has been translated. The separate landing page remains English-only.

Original code uses the MIT license. Original prose and applicable editorial contributions use CC BY 4.0 where contributors control the rights. Third-party books, translations, images, scans and databases retain their own rights. See [LICENSE.md](LICENSE.md), [rights and ethics](docs/RIGHTS_AND_ETHICS.md) and [release limitations](RELEASE_NOTES.md).
