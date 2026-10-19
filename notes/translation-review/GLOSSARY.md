# പദാവലി / Terminology glossary

നില: AI സഹായത്തോടെ തയ്യാറാക്കിയ കരട്. മലയാള ഭാഷാപരിശോധന ബാക്കി (pending). ഭൂവിജ്ഞാനീയം, പുരാവസ്തുശാസ്ത്രം, ലിഖിതശാസ്ത്രം, കാലഗണന എന്നിവയിലെ പദങ്ങൾക്ക് വിഷയവിദഗ്ധപരിശോധനയും ബാക്കി. അടിസ്ഥാന revision: `570f665e25480380e6be361627cf5cfb1285c093`.

Status: AI-assisted draft. Human Malayalam-language review pending. Specialist review pending for geology, archaeology, epigraphy and chronology terms. Base revision as above.

## ഉപയോഗരീതി / How to use

- ഈ പദാവലിയിലെ മലയാളപദം സ്ഥിരമായി ഉപയോഗിക്കുക. ആദ്യ പ്രയോഗത്തിൽ വ്യക്തതയ്ക്കായി ഇംഗ്ലീഷ് പദം ബ്രാക്കറ്റിൽ നൽകാം.
- Code, ID, JSON key, enum മൂല്യങ്ങൾ (`seed_index`, `pending`, `interval` തുടങ്ങിയവ), ഫയൽപാതകൾ, DOI എന്നിവ പരിഭാഷപ്പെടുത്തരുത്. വായനക്കാരന് വിശദീകരണം വേണമെങ്കിൽ ബ്രാക്കറ്റിൽ മലയാളം ചേർക്കുക.
- “Q” നിരയിലെ ചോദ്യങ്ങൾ മനുഷ്യപരിശോധകർ തീരുമാനിക്കേണ്ടവയാണ്.
- Use the Malayalam term consistently; give the English in brackets on first use where helpful. Never translate code, IDs, keys, enum values, paths or DOIs. Questions in the “Q” column await human reviewers.

## ശേഖരവും പ്രക്രിയയും / Archive and workflow

| English | മലയാളം | Q / കുറിപ്പ് |
|---|---|---|
| archive / repository | ശേഖരം | “repository” സാങ്കേതികാർത്ഥത്തിൽ (Git) വരുമ്പോൾ repository എന്നുതന്നെ നിലനിർത്തി. |
| research foundation | പ്രാരംഭ ഗവേഷണശേഖരം | README ഉപയോഗിക്കുന്ന രൂപം. |
| canonical data | അടിസ്ഥാന ഡാറ്റ | “ആധികാരിക ഡാറ്റ” എന്നത് ഉള്ളടക്കം സ്ഥിരീകരിച്ചതാണെന്ന് തോന്നിപ്പിക്കും; ഒഴിവാക്കി. |
| generated view / page | generated പേജ് (സ്വയമേവ നിർമ്മിക്കുന്ന പേജ്) | Q1: “generated” മലയാളത്തിൽ സ്ഥിരപ്പെടുത്തണോ? |
| seed record | പ്രാരംഭരേഖ | |
| evidence record | തെളിവുരേഖ | |
| source card | സ്രോതസ്സ് കാർഡ് | |
| period dossier | കാലഘട്ടപഠനരേഖ | README “പഠനരേഖ” എന്ന് ചുരുക്കുന്നു. |
| annual page / year file | വാർഷിക പേജ് / വർഷഫയൽ | |
| unresearched | ഗവേഷണം നടത്താത്തത് | “ശൂന്യം” എന്ന് പരിഭാഷപ്പെടുത്തരുത്: ചരിത്രം ശൂന്യമാണെന്ന അർത്ഥം വരും. |
| coverage | കവറേജ് / ഗവേഷണവ്യാപ്തി | Q2: README “കവറേജ് വിവരങ്ങൾ” ഉപയോഗിക്കുന്നു; തദ്ദേശീയപദം വേണോ? |
| corpus / collection | രേഖാസമുച്ചയം / ശേഖരം | Q3: “corpus”-ന് സ്ഥിരമായ ഒരൊറ്റ പദം തിരഞ്ഞെടുക്കണം. |
| inventory | ഇനംതിരിച്ചുള്ള പട്ടിക | |
| gap ledger / gap inventory | വിടവുപട്ടിക | |
| contributor identifier | സംഭാവകന്റെ തിരിച്ചറിയൽ | |
| maintainer / project owner | പരിപാലകൻ / പദ്ധതി ഉടമ | |
| human review | മനുഷ്യപരിശോധന | |
| model review / self-check | മോഡൽ പരിശോധന (മനുഷ്യാംഗീകാരമല്ല) | എപ്പോഴും വേർതിരിച്ച് അടയാളപ്പെടുത്തണം. |
| specialist review | വിഷയവിദഗ്ധപരിശോധന | |
| pending | ബാക്കി / തീർപ്പാകാത്തത് | enum `pending` മാറ്റരുത്. |
| structural validation | ഘടനാപരിശോധന | ചരിത്രസ്ഥിരീകരണമല്ലെന്ന് എപ്പോഴും വ്യക്തമാക്കണം. |

## തെളിവും സ്രോതസ്സും / Evidence and sources

| English | മലയാളം | Q / കുറിപ്പ് |
|---|---|---|
| claim / assertion | അവകാശവാദം / പ്രസ്താവന | |
| attributed statement | ആരോപിത പ്രസ്താവന (ആരുടേതെന്ന് വ്യക്തമാക്കിയത്) | Q4: “ആരോപിതം” ചിലപ്പോൾ കുറ്റാരോപണത്തിന്റെ ധ്വനി നൽകും. “ആരുടേതെന്ന് രേഖപ്പെടുത്തിയ” ആണോ നല്ലത്? |
| allegation | ആരോപണം | |
| primary source | പ്രാഥമിക സ്രോതസ്സ് | |
| critical edition | വിമർശനാത്മക പതിപ്പ് | |
| witness (textual) | സാക്ഷ്യപ്രതി | Q5: പാഠവിമർശനത്തിൽ സാധാരണ പദം? |
| locator | സ്ഥാനസൂചന | |
| inspection depth | പരിശോധനയുടെ ആഴം | |
| catalogue-only / abstract-only | കാറ്റലോഗ് മാത്രം / സാരാംശം മാത്രം | |
| erratum / corrigendum | erratum / corrigendum (തിരുത്തൽക്കുറിപ്പ്) | |
| retraction | പിൻവലിക്കൽ | |
| provenance | ഉദ്ഭവവിവരം | |
| independent corroboration | സ്വതന്ത്ര സ്ഥിരീകരണം | |
| superseded / challenged / unresolved | മറികടന്നത് / ചോദ്യം ചെയ്യപ്പെട്ടത് / തീർപ്പാകാത്തത് | |
| rights not cleared | അനുമതി ഉറപ്പാക്കിയിട്ടില്ല | നിയമലംഘന ആരോപണമല്ലെന്ന് നയം വ്യക്തമാക്കുന്നു. |
| public domain | പൊതുസഞ്ചയം | |
| custodian | സൂക്ഷിപ്പുകാർ | |

## കാലഗണന / Chronology

| English | മലയാളം | Q / കുറിപ്പ് |
|---|---|---|
| BCE / CE | ക്രി.മു. / ക്രി.വ. | Q6: “ക്രി.വ.” vs “ക്രി.പി.” vs “പൊ.യു.” (പൊതുയുഗം). README “ക്രി.വ.” ഉപയോഗിക്കുന്നു. മതനിരപേക്ഷമായ “പൊ.യു.മു./പൊ.യു.” വേണോ എന്ന് പരിശോധകർ തീരുമാനിക്കണം. |
| circa | ഏകദേശം | |
| precision | കൃത്യതാനില | |
| interval / range | കാലപരിധി | |
| proposed date | നിർദേശിച്ച തീയതി | |
| attested year | സാക്ഷ്യപ്പെടുത്തിയ വർഷം | |
| conventional year | കീഴ്‌വഴക്കപ്രകാരമുള്ള വർഷം | |
| reign / regnal year | ഭരണകാലം / ഭരണവർഷം | |
| Kollam Era | കൊല്ലവർഷം | |
| Saka | ശകവർഷം | |
| Hijri | ഹിജ്റ | |
| radiocarbon age / calibration | റേഡിയോകാർബൺ പ്രായം / കാലിബ്രേഷൻ | Q7: “അംശാങ്കനം” എന്ന സാങ്കേതികപദം വേണോ? |
| BP (before present, 1950) | BP (1950 ആധാരമാക്കി “വർത്തമാനത്തിന് മുമ്പ്”) | ചിഹ്നം മാറ്റരുത്. |
| stratigraphic | അടുക്കുക്രമപരമായ (stratigraphic) | Q8: “സ്തരവിന്യാസ” പോലുള്ള പദം വിദഗ്ധർ ഇഷ്ടപ്പെടുന്നുണ്ടോ? |
| palaeographic | ലിപിശാസ്ത്രപരമായ | |
| epigraphy / inscription | ലിഖിതശാസ്ത്രം / ലിഖിതം | |
| copper plates (Kollam plates) | ചെപ്പേടുകൾ (കൊല്ലം ചെപ്പേടുകൾ) | Q9: സ്രോതസ്സ് “Kollam plates” എന്ന് മാത്രം പറയുന്നു; “തരിസാപ്പള്ളി ചെപ്പേടുകൾ” എന്ന് പരിഭാഷയിൽ വ്യക്തമാക്കരുത്, അത് സ്രോതസ്സിൽ ഇല്ലാത്ത സ്ഥിരീകരണമാകും. |

## ഭൂവിജ്ഞാനീയവും പ്രാക്‌ചരിത്രവും / Geology and prehistory

| English | മലയാളം | Q / കുറിപ്പ് |
|---|---|---|
| geology / geological | ഭൂവിജ്ഞാനീയം / ഭൂവിജ്ഞാനീയ | **ഭൂമിശാസ്ത്രം = geography.** README-യിലെ “ഭൂമിശാസ്ത്രപരമായ ദീർഘകാല ചരിത്രം” (deep time) തിരുത്തേണ്ടതാകാം; top-level review കാണുക. |
| deep time | ദീർഘ ഭൂകാലം | Q10 |
| prehistory | ചരിത്രാതീതകാലം / പ്രാക്‌ചരിത്രം | |
| Ma / Ga | Ma / Ga (ദശലക്ഷം / നൂറുകോടി വർഷം മുമ്പ്) | ഏകകം മാറ്റരുത്. |
| basement rock | അടിസ്ഥാനശില (basement) | |
| detrital grain | അപരദന ധാന്യം (detrital) | Q11 |
| metamorphic rim | കായാന്തരിത വലയം | |
| deposition / sediment | നിക്ഷേപം / അവസാദം | |
| geochronology | ഭൂകാലനിർണയം | |
| chronostratigraphic chart | chronostratigraphic ചാർട്ട് | Q12: മലയാളപദം? |
| Lower Palaeolithic | പ്രാചീന ശിലായുഗത്തിന്റെ ആദ്യഘട്ടം (Lower Palaeolithic) | |
| megalithic | മഹാശിലായുഗ | |
| excavation / findspot | ഉത്ഖനനം / കണ്ടെടുത്ത സ്ഥലം | |
| archaeological context | പുരാവസ്തു സന്ദർഭം | |

## ഭൂമിശാസ്ത്രവും ഭരണപരിധിയും / Geography and territory

| English | മലയാളം | Q / കുറിപ്പ് |
|---|---|---|
| territory now administered as Kerala | ഇന്ന് കേരളത്തിന്റെ ഭരണപരിധിയിലുള്ള ഭൂഭാഗം | “കേരളം” എന്ന പേര് പരിധിനിർണയത്തിന്റെ മാനദണ്ഡമല്ല. |
| geographic scope | ഭൗമപരിധി | |
| scope relation | പരിധിബന്ധം | |
| coordinates | നിർദേശാങ്കങ്ങൾ | |
| Pattanam / Muziris | പട്ടണം / മുസിരിസ് | ഇവ ഒന്നാണെന്ന് പരിഭാഷ സൂചിപ്പിക്കരുത്. |
| Quilon | Quilon (കൊല്ലം) | സ്രോതസ്സ് ശീർഷകങ്ങളിൽ Quilon നിലനിർത്തുക. |
| Calicut | Calicut (കോഴിക്കോട്) | |
| Mahe | മാഹി | പുതുച്ചേരിയുടെ ഭാഗം; പശ്ചാത്തലം മാത്രം. |

## ബാച്ച് 2-ൽ ഉയർന്ന ചോദ്യങ്ങൾ / Questions raised in batch 2

| # | English | ഉപയോഗിച്ചത് / Used | ചോദ്യം / Question |
|---|---|---|---|
| Q13 | Keralaputras | Keralaputras (കേരളപുത്രർ) | ലിപ്യന്തരണം നിലനിർത്തണോ, “കേരളപുത്രർ” മാത്രം മതിയോ? പരിഭാഷ ചേരരുമായുള്ള ബന്ധം ഉറപ്പിക്കരുത്. |
| Q14 | (Major) Rock Edict II | രണ്ടാം ശിലാശാസനം / പ്രധാന ശിലാശാസനം II | ഏത് രൂപം സ്ഥിരപ്പെടുത്തണം? |
| Q15 | hominin | hominin (ആദിമനുഷ്യവർഗം) | “മാനവവംശം” എന്നത് Homo sapiens എന്ന് തെറ്റിദ്ധരിപ്പിക്കും; വിദഗ്ധർ സ്ഥിരീകരിക്കണം. |
| Q16 | Trivandrum Block, Quilon Formation | ഇംഗ്ലീഷ് ഔപചാരിക നാമം നിലനിർത്തി | ഭൂവിജ്ഞാനീയ ഔപചാരിക നാമങ്ങൾ ലിപ്യന്തരണം ചെയ്യണോ? |
| Q17 | Ghats (E04) | ഘട്ടങ്ങൾ (Ghats) | “ഘട്ടം” = phase എന്ന അർത്ഥവുമായി കൂടിക്കുഴയും. “ഘട്ടമലനിരകൾ” / “പശ്ചിമഘട്ടം” ആണോ നല്ലത്? |
| Q18 | appointed day | നിശ്ചിതദിനം (appointed day) | ഔദ്യോഗിക മലയാള നിയമപദാവലിയിലെ പദം പരിശോധിക്കണം. |
| Q19 | Early Historic | ആദ്യകാല ചരിത്രഘട്ടം (Early Historic) | |
| Q20 | Mesolithic / microlithic | Mesolithic (മധ്യ ശിലായുഗം) / microlithic (സൂക്ഷ്മശിലായുധ) | |
| Q21 | Thenmala/Tenmala, Ankode, Rappal, Puthiyangadi | തെന്മല/Tenmala, അങ്കോട്, റാപ്പൽ (Rappal), പുതിയങ്ങാടി | സ്ഥലനാമങ്ങളുടെ പ്രാദേശിക രൂപം ഉറപ്പാക്കണം; പ്രത്യേകിച്ച് “അങ്കോട്”, “റാപ്പൽ”. |
| Q22 | Babington, Fawcett, Logan | ബാബിങ്ടൺ, ഫോസെറ്റ് (Fawcett), ലോഗൻ | വ്യക്തിനാമങ്ങളുടെ മലയാളരൂപം. |
| Q23 | Old Malayalam | പഴയ മലയാളം | ഭാഷാചരിത്രത്തിലെ സാങ്കേതികപദമായി “പ്രാചീന മലയാളം” ആണോ? |
| Q24 | inherited zircon core, overgrowth, model age | പാരമ്പര്യമായി ലഭിച്ച zircon കാമ്പ്, പുറംവളർച്ച, മാതൃകാപ്രായം | വിഷയവിദഗ്ധപരിശോധന ആവശ്യം. |
| Q25 | celt | celt (മിനുക്കിയ ശിലാമഴു) | |
| Q26 | date.original_expression | സ്രോതസ്സുപ്രയോഗത്തിന്റെ വിശദീകരണം | ഈ ഫീൽഡ് മിക്കപ്പോഴും സമ്പാദകീയ ചുരുക്കമാണ്, നേരിട്ടുള്ള ഉദ്ധരണിയല്ല. Integration-ൽ മലയാളം വിശദീകരണമായി മാത്രം കാണിക്കണം; മൂലപ്രയോഗം ഇംഗ്ലീഷിൽ നിലനിൽക്കും. |

## ബാച്ച് 3-ൽ ഉയർന്ന ചോദ്യങ്ങൾ / Questions raised in batch 3

| # | English | ഉപയോഗിച്ചത് / Used | ചോദ്യം / Question |
|---|---|---|---|
| Q27 | verdict (audit) | വിധി / തീർപ്പ് | Audit verdict labels-ൽ “പിന്തുണയുണ്ട്” ആവർത്തിക്കുന്നു. ചെറിയ ലേബലുകൾ വേണോ? ഉദാ. “ഭാഗിക പിന്തുണ”. |
| Q28 | qualify / qualified | നിബന്ധന ചേർക്കുക | “വ്യവസ്ഥ”, “പരിമിതി”, “നിബന്ധന” ഇവയിൽ ഏതാണ് സമ്പാദകീയ അർത്ഥത്തിന് ചേർന്നത്? |
| Q29 | corpus / corpora | കോർപ്പസ് / ശേഖരം | “ശേഖരം” വളരെ പൊതുവാണ്. സാങ്കേതികപദമായി “കോർപ്പസ്” നിലനിർത്തണോ? |
| Q30 | crosswalk | താരതമ്യപട്ടിക (crosswalk) | |
| Q31 | offshore | കടൽമേഖല | നിയമപരമായ “territorial waters” (സമുദ്രാതിർത്തി) എന്നതുമായി വേർതിരിക്കണം. |
| Q32 | Generator separator ` — ` | `ID: title` എന്ന് നിർദ്ദേശിച്ചു | INTEGRATION_NOTES I3 കാണുക. Project B തീരുമാനിക്കണം. |
