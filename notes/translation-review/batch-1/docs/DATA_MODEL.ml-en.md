<!--
source_path: docs/DATA_MODEL.md
source_revision: 570f665e25480380e6be361627cf5cfb1285c093
manifest_id: TR-B1-004
ai_assistance: Malayalam draft prepared with AI assistance; English retained from source.
human_language_review: pending
specialist_review: pending
model_review: model self-check only (see manifest); not human approval
-->

# തെളിവുകൾ, സ്രോതസ്സുകൾ, വായനാപേജുകൾ

> പരിഭാഷാ കരട്. AI സഹായത്തോടെ തയ്യാറാക്കിയത്. മലയാള ഭാഷാപരിശോധനയും വിഷയവിദഗ്ധപരിശോധനയും ബാക്കിയുണ്ട്. മൂലപാഠം: `docs/DATA_MODEL.md` @ `570f665`.

## ഘടന

ഈ പതിപ്പിൽ തിരുത്താവുന്ന അടിസ്ഥാന ഡാറ്റ JSON ആണ്. Markdown പൊതുവായനയ്ക്കുള്ള അടരാണ്. ഓരോ വർഷവും ഒരു Markdown ഫയലായി നിലനിർത്തുമ്പോൾത്തന്നെ വസ്തുതകളുടെ ആവർത്തനവും പൊരുത്തമില്ലാതെ പകർത്തിയ citation-കളും ഇതുവഴി ഒഴിവാക്കുന്നു. ഒരു സ്രോതസ്സ് ഒരിക്കൽ മാത്രം രജിസ്റ്റർ ചെയ്യുന്നു; ഓരോ അവകാശവാദവും സ്ഥാനസൂചന സഹിതം അതിനെ ഉദ്ധരിക്കുന്നു; വാർഷിക പേജുകളും കാലഘട്ടപേജുകളും ആ അവകാശവാദത്തിലേക്ക് കണ്ണി നൽകുന്നു.

```text
സ്രോതസ്സ് / പതിപ്പ് / ഭാഗം
           ↓ പിന്തുണയ്ക്കുന്നു, എതിർക്കുന്നു, പരിമിതപ്പെടുത്തുന്നു
അടിസ്ഥാന തെളിവുരേഖ
           ↓ തീയതിയുടെ ധർമ്മവും ഭൂമിശാസ്ത്രബന്ധവും
കാലഘട്ടപഠനരേഖ ← വാർഷിക Markdown സൂചിക
```

ഡാറ്റാബേസ് സെർവർ, knowledge-graph സംവിധാനം, വെബ് തിരയൽ സമ്പർക്കമുഖം, സ്വയമേവയുള്ള GIS അരിക്കൽ, പരിഭാഷാസംവിധാനം എന്നിവ ഈ പ്രാരംഭശേഖരം ഇനിയും നടപ്പാക്കിയിട്ടില്ല. സംഭാവകർക്ക് ഈ സംവിധാനങ്ങൾ മുൻവ്യവസ്ഥയാക്കാതെ JSON പിന്നീട് മാറ്റിസ്ഥാപിക്കാം.

## ഫയലുകളും ഉത്തരവാദിത്തവും

`data/sources.json`-ൽ ഗ്രന്ഥസൂചികാപരമായ തിരിച്ചറിയൽ, ലഭ്യമാകുന്ന വഴി, പരിശോധനയുടെ ആഴം, അവകാശങ്ങൾ, പകർപ്പ്/hash നില എന്നിവയുണ്ട്. `data/records.json`-ൽ ആരോപിത അവകാശവാദങ്ങൾ, തീയതികൾ, സ്രോതസ്സുകൾ, പരിമിതികൾ, വഴികാട്ടൽ എന്നിവയുണ്ട്. `data/periods.json`-ൽ സമ്പാദകീയ ഗവേഷണജാലകങ്ങളുണ്ട്. `data/audit.json` മുൻ സംഭാഷണത്തിലെ മറുപടികൾക്കുള്ള തിരുത്തലുകൾ സൂക്ഷിക്കുന്നു. `data/corpora.json` കണ്ടെത്തലിന്റെ ലക്ഷ്യങ്ങളും പട്ടികപ്പെടുത്തൽ നിലയും നിർവചിക്കുന്നു.

Generated ആയ `sources/`, `records/`, `periods/`, `years/`, `audit/CHAT_AUDIT.md`, `coverage/`-ന്റെ ചില ഭാഗങ്ങൾ എന്നിവ അടിസ്ഥാന ഡാറ്റയിൽനിന്ന് വീണ്ടും നിർമ്മിക്കണം. കൈയെഴുത്തുകുറിപ്പുകൾ `notes/`-ലാണ് വേണ്ടത്. എഴുതുന്നതിനുമുമ്പ് generator ഔട്ട്‌പുട്ട് പാതകൾ മുൻകൂട്ടി പരിശോധിക്കുന്നു. അത് ഇന്റർനെറ്റ് അഭ്യർത്ഥനകൾ നടത്തുന്നില്ല; സംരക്ഷിതരേഖകൾ നിശ്ശബ്ദമായി കൈക്കലാക്കാനും അതിന് കഴിയില്ല.

## സ്രോതസ്സുരേഖയുടെ കുറഞ്ഞ ആവശ്യങ്ങൾ

ഒരു സ്രോതസ്സിന് സ്ഥിരമായ പ്രാദേശിക തിരിച്ചറിയൽ (identifier), ശീർഷകം, യഥാർത്ഥത്തിൽ സ്ഥിരീകരിച്ച രചയിതാവ്/സ്ഥാപനം, URL അല്ലെങ്കിൽ കാറ്റലോഗ് സ്ഥാനസൂചന, സ്രോതസ്സിന്റെ തരം, അറിയാമെങ്കിൽ പ്രസിദ്ധീകരണതീയതി, പ്രവേശിച്ച തീയതി, പരിശോധിച്ച ഭാഗം, പരിശോധനയുടെ പരിമിതി, അവകാശനില എന്നിവ വേണം. DOI ഉപകാരപ്രദമാണ്; പക്ഷേ അത് സംഭവത്തിന്റെ തീയതിയല്ല. URL ലഭ്യമാകാനുള്ള വഴിയാണ്; അത് നിർബന്ധമായും ഒരു കൃതിയുടെ അനന്യ തിരിച്ചറിയൽ ആകണമെന്നില്ല.

കാറ്റലോഗ് മാത്രം, സാരാംശം മാത്രം എന്നീ പരിശോധനകൾ വായനക്കാർക്ക് കാണാനാകണം. നിയമപരമായി സൂക്ഷിച്ച സ്രോതസ്സുഫയൽ നിലവിലുള്ളപ്പോൾ മാത്രമേ checksum-ന് അർത്ഥമുള്ളൂ. ലഭിക്കാത്ത സ്രോതസ്സിന് hash കെട്ടിച്ചമയ്ക്കരുത്. വേർതിരിച്ചെടുത്ത കുറിപ്പിന്റെ hash മൂലരേഖയുടെ hash അല്ല.

ഭാവിയിൽ സ്രോതസ്സുരേഖകൾ ആശയതലത്തിലുള്ള കൃതി, പതിപ്പ് (edition), പ്രകാശനരൂപം (manifestation), ഭൗതിക സാക്ഷ്യപ്രതി, ഡിജിറ്റൽ വസ്തു, പ്രത്യേക version എന്നിവ വേർതിരിക്കണം. ഏത് പരിഭാഷയോ പകർത്തിയെഴുത്തോ ഉപയോഗിച്ചു എന്ന് രേഖപ്പെടുത്തുക. ഒരേ രചയിതാവിനെ പകർത്തുന്ന പല സൈറ്റുകളെ സ്വതന്ത്ര സ്ഥിരീകരണങ്ങളായി എണ്ണാതിരിക്കാൻ സ്രോതസ്സുകളുടെ ആശ്രയബന്ധവിവരം സൂക്ഷിക്കുക.

## അവകാശവാദരേഖയുടെ കുറഞ്ഞ ആവശ്യങ്ങൾ

ഒരു അവകാശവാദത്തിന് തിരിച്ചറിയൽ, പരിധിയുള്ള ഒരൊറ്റ പ്രസ്താവന, തെളിവിന്റെ തരം, കൃത്യതാനില സഹിതമുള്ള തീയതി, ഭൂമിശാസ്ത്രബന്ധം, സ്ഥാനസൂചനകളോടെയുള്ള സ്രോതസ്സ് citation-കൾ, വ്യക്തമായ പരിമിതികൾ, വിഷയടാഗുകൾ, പരിശോധനാനില എന്നിവ വേണം. വ്യത്യസ്ത തെളിവുകൾ ആവശ്യമുള്ള സംയുക്ത പ്രസ്താവന സാധാരണയായി വിഭജിക്കണം.

നിലവിലെ `support` പട്ടിക അനുകൂല തെളിവുകൾ രേഖപ്പെടുത്തുന്നു. ഭാവിയിലെ സങ്കീർണമായ അഭിപ്രായഭിന്നതകൾക്ക് `supports`, `disputes`, `revises`, `supersedes`, `copies_from`, `alternative_identification` പോലുള്ള തരം തിരിച്ച ബന്ധങ്ങൾ ഉപയോഗിക്കണം. ന്യായീകരിക്കാവുന്ന മാതൃകയില്ലാതെ തർക്കമുള്ള കണ്ടെത്തലുകളെ സംഖ്യാരൂപത്തിലുള്ള ഉറപ്പുസ്കോറായി അവതരിപ്പിക്കരുത്.

## ഭൂമിശാസ്ത്രം

`scope_relation` കേന്ദ്രതെളിവിനെ പ്രാദേശിക/ആഗോള പശ്ചാത്തലം, ബാഹ്യ പാഠസൂചനകൾ, ഈ പ്രദേശത്തെ ബാധിക്കുന്ന ബാഹ്യ പ്രവൃത്തികൾ, ബാഹ്യ സൂക്ഷിപ്പ്/ഗവേഷണചരിത്രം എന്നിവയിൽനിന്ന് വേർതിരിക്കുന്നു. കൃത്യമായ നിർദേശാങ്കങ്ങൾ അറിയാമെന്ന് നടിക്കാതെ ഒരു സ്ഥലപ്പേര് നിലനിർത്താം. പ്രാരംഭ ജ്യാമിതി (geometry) മനഃപൂർവം null ആണ്.

നിർമ്മാണസ്ഥലം, വിവരിക്കുന്ന സ്ഥലം, കണ്ടെടുത്ത സ്ഥലം (findspot), ആധുനിക സൂക്ഷിപ്പുകേന്ദ്രം, നിർദേശിക്കപ്പെട്ട പ്രാചീന സ്ഥലനിർണയം എന്നിവ വേറിട്ട സ്ഥലബന്ധങ്ങളായി മാറണം. ഒരു പ്രത്യേക അവകാശവാദം അവ തമ്മിലുള്ള നിർദേശിത ബന്ധം പ്രസ്താവിക്കുന്നതുവരെ പട്ടണത്തിനും മുസിരിസിനും വേറിട്ട തിരിച്ചറിയലുകൾ ഉണ്ടായിരിക്കണം; അവയുടെ പേരുകൾ നിശ്ശബ്ദമായി ലയിപ്പിക്കുന്നത് ഗവേഷണം നടക്കുന്ന ചോദ്യത്തെത്തന്നെ മായ്ച്ചുകളയും [S017](../../../../sources/S017.md), [S018](../../../../sources/S018.md).

## തീയതികളും വാർഷിക കണ്ണികളും

ഒരു രേഖ ഭൂവിജ്ഞാനീയമോ ചരിത്രപരമോ തീയതിയില്ലാത്തതോ ആകാം. ഒരു വാർഷിക കണ്ണിക്ക് വ്യക്തമായ ധർമ്മമുണ്ട്: കൃത്യമായ തീയതി, സാക്ഷ്യപ്പെടുത്തിയ വർഷം, കീഴ്‌വഴക്കപ്രകാരമുള്ള തീയതി, നിർദേശിച്ച തീയതി, അല്ലെങ്കിൽ ഗവേഷണ/ലഭ്യതാചരിത്രം. തീയതിയില്ലാത്തതും ഭൂവിജ്ഞാനീയവുമായ അവകാശവാദങ്ങളെ വാർഷിക സംഭവവിവരങ്ങളിലേക്ക് നിർബന്ധിച്ച് ചേർക്കാനാവില്ല. വേറിട്ട് തീയതിയുള്ള ഒരു ആധുനിക പ്രസിദ്ധീകരണത്തിന് പ്രത്യേക ഗവേഷണചരിത്രരേഖ ഉണ്ടാകാം.

## പരിശോധനാനിലകൾ

പ്രാരംഭശേഖരത്തിൽ സ്വതന്ത്രമായി അംഗീകരിച്ച മനുഷ്യപരിശോധനകളൊന്നുമില്ല. അംഗീകാരത്തിന് തിരിച്ചറിയാവുന്ന പരിശോധനാ-ഉദ്ഭവവിവരം വേണം; യന്ത്രം നിർമ്മിച്ച ഒരു ഉറപ്പുവിശേഷണം മതിയാകില്ല. പരിശോധന ഓരോ അവകാശവാദത്തിനും പ്രത്യേകമായിരിക്കണം: ഒരാൾ ഒരു പരിഭാഷ പരിശോധിച്ചേക്കാം, പക്ഷേ റേഡിയോകാർബൺ മാതൃകയോ ഭൂമിശാസ്ത്രപരമായ സ്ഥലനിർണയമോ പരിശോധിച്ചിട്ടുണ്ടാകണമെന്നില്ല.

അനാവശ്യമായ വ്യക്തിഗത ബന്ധപ്പെടൽവിവരങ്ങൾക്കുപകരം സംഭാവകരുടെ തിരിച്ചറിയലുകൾ ഉപയോഗിക്കുക. പരിശോധകന്റെ ധർമ്മം, പരിശോധിച്ച സ്രോതസ്സുഭാഗങ്ങൾ, തീർപ്പാകാത്ത എതിർപ്പുകൾ, തീരുമാനം, സമയമുദ്ര, മറികടന്ന തീരുമാനങ്ങൾ എന്നിവ നിർദേശിക്കപ്പെട്ട വിപുലീകരണങ്ങളിൽ ഉൾപ്പെടുന്നു. സ്രോതസ്സുപരിശോധന, രീതിപരിശോധന, സമ്പാദകീയ ലയനം (merge) എന്നിവ വ്യത്യസ്ത പ്രവൃത്തികളാണ്.

## പരിശോധനയുടെ പരിമിതികൾ

`validate.py` സൂചനകൾ, തീയതിഘടനകൾ, പൂജ്യംവർഷം ഒഴിവാക്കൽ, ഭാവിതീയതിപരിധികൾ, ആവശ്യമായ ഉദ്ഭവവിവരം, generated പേജുകൾ, പ്രാദേശിക ഫയൽക്കണ്ണികൾ എന്നിവ പരിശോധിക്കുന്നു. ഒരു പ്രാചീന അവകാശവാദത്തിന്റെ സത്യം സ്ഥാപിക്കാനോ ഒരു ലിഖിതം വ്യാഖ്യാനിക്കാനോ അവകാശങ്ങൾ തീർപ്പാക്കാനോ കാണാത്ത പേജ് സ്ഥിരീകരിക്കാനോ അതിന് കഴിയില്ല. JSON schema ഫയലുകൾ അടിസ്ഥാനഘടന രേഖപ്പെടുത്തുന്നു; ഉൾപ്പെടുത്തിയ standard-library validator പ്രവർത്തനപരിശോധനകൾ നടത്തുന്നു; അത് പൊതുവായ JSON Schema engine അല്ല.

---

# Evidence, sources and views

> Retained English source text from `docs/DATA_MODEL.md` @ `570f665`. Wording unchanged; relative links rewritten to resolve from this staging path.

## Architecture

The canonical editable data in this release is JSON. Markdown is the public reading layer. This keeps every year as a Markdown file while avoiding duplicated facts and inconsistently copied citations. A source is registered once; each claim cites it with a locator; annual and era pages link to the claim.

```text
source / version / passage
           ↓ supports, disputes, qualifies
canonical evidence record
           ↓ date role and geographic relation
period dossier ← annual Markdown index
```

The starter does not yet implement a database server, a knowledge-graph engine, a web search UI, automatic GIS filtering or a translation system. JSON can be migrated later without making those systems a prerequisite for contributors.

## Files and ownership

`data/sources.json` contains bibliographic identity, access route, inspection depth, rights and copy/hash status. `data/records.json` contains attributed claims, dates, sources, limitations and navigation. `data/periods.json` contains editorial research windows. `data/audit.json` preserves corrections to the earlier conversation. `data/corpora.json` defines discovery targets and inventory status.

Generated `sources/`, `records/`, `periods/`, `years/`, `audit/CHAT_AUDIT.md` and parts of `coverage/` must be rebuilt from canonical data. Manual notes belong in `notes/`. The generator preflights output paths before writing. It makes no internet requests and cannot silently acquire protected documents.

## Minimum source record

A source needs a stable local identifier, title, creator as actually verified, URL or catalogue locator, source type, publication date if known, access date, inspected portion, inspection limitation and rights status. A DOI is useful but is not an event date. A URL is an access route, not necessarily a unique work identifier.

Catalogue-only and abstract-only inspection must be visible to readers. A checksum is meaningful only when the corresponding legally retained source file exists. Do not fabricate a hash of a source that was not obtained. A hash of an extracted note is not a hash of the original document.

Future source refinements should distinguish a conceptual work, edition, manifestation, physical witness, digital object and specific version. Record which translation or transcription was used. Keep source dependency information so multiple sites copying one author are not counted as independent corroboration.

## Minimum claim record

A claim needs an identifier, one bounded statement, evidence type, date with precision, geographic relationship, source citations with locators, explicit limitations, topic tags and review status. A compound statement that requires different evidence should normally be split.

The current `support` list records positive evidence. Complex future disagreements should use typed relations such as `supports`, `disputes`, `revises`, `supersedes`, `copies_from` and `alternative_identification`. Do not represent disputed findings as a numerical certainty score without a defensible model.

## Geography

`scope_relation` distinguishes core evidence from regional/global context, external textual references, external actions affecting the area and external custody/research history. A place string can be retained without pretending that exact coordinates are known. The initial geometry is deliberately null.

Production location, place described, findspot, modern repository and proposed ancient identification must become separate place relations. Pattanam and Muziris must have separate identifiers until a specific claim states their proposed relationship; silently merging their names would erase the question being researched [S017](../../../../sources/S017.md), [S018](../../../../sources/S018.md).

## Dates and annual links

A record may be geological, historical or undated. An annual link has an explicit role: exact date, attested year, conventional date, proposed date, or research/access history. Undated and geological claims cannot be forced into annual event entries. A separately dated modern publication can have a separate research-history record.

## Review states

The seed has no independently approved human reviews. Approval requires identifiable review provenance, not merely a generated confidence adjective. Review should be claim-specific: someone may check a translation but not the radiocarbon model or geographical identification.

Use contributor identifiers rather than unnecessary personal contact details. Proposed extensions include reviewer role, reviewed source passages, unresolved objections, decision, timestamp and superseded decisions. A source check, a method check and an editorial merge are different acts.

## Validation limits

`validate.py` checks references, date structures, year-zero exclusion, future cutoffs, required provenance, generated views and local file links. It cannot establish the truth of an ancient claim, interpret an inscription, adjudicate rights or verify an unseen page. The JSON schema files document the basic structure; the included standard-library validator performs the operational checks and is not a general-purpose JSON Schema engine.
