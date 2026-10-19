# തെളിവ് പരിശോധന: ആദ്യ ബാച്ച്

**നില:** AI സഹായത്തോടെ തയ്യാറാക്കിയ കരട്. മനുഷ്യ പണ്ഡിതപരിശോധനയും മലയാളം ഭാഷാപരിശോധനയും ശേഷിക്കുന്നു. മോഡൽ നടത്തിയ പരിശോധന പണ്ഡിതാംഗീകാരമല്ല.

**അടിസ്ഥാന പതിപ്പ്:** `570f665e25480380e6be361627cf5cfb1285c093` (main). പരിശോധിച്ച തീയതി: 2026-10-18 (America/Los_Angeles).

## ഈ ഫോൾഡറിൽ എന്ത്

| ഫയൽ | ഉള്ളടക്കം |
|---|---|
| [claim-reviews.json](claim-reviews.json) | 16 അവകാശവാദങ്ങളുടെ (EV-01 മുതൽ EV-16 വരെ) ഘടനാപരമായ അവലോകനം: സ്ഥിര ഐഡികൾ, പതിപ്പ്, സ്ഥാനസൂചന, പരിശോധനയുടെ ആഴം, ഭൂമിശാസ്ത്രബന്ധം, തീയതിയുടെ പങ്ക്, അനുകൂലവും വിരുദ്ധവുമായ തെളിവ്, സ്രോതസ്സുകളുടെ പരസ്പരാശ്രയം, അവകാശങ്ങൾ, കണ്ടെത്തൽ. പ്രവേശനരേഖയും (access log) നിർദേശിത പുതിയ സ്രോതസ്സുകളും ഇതിലുണ്ട്. |
| [proposed-corrections.json](proposed-corrections.json) | PC-01 മുതൽ PC-21 വരെ നിർദേശിത തിരുത്തലുകൾ; ഓരോന്നും ഐഡി, ഫീൽഡ്, അടിസ്ഥാന പതിപ്പ്, ഫയൽ ബ്ലോബ് SHA, നിലവിലെ മൂല്യം എന്നിവയോടെ. ഒന്നും canonical ഡാറ്റയിൽ പ്രയോഗിച്ചിട്ടില്ല. |
| [UNRESOLVED.md](UNRESOLVED.md) | പരിഹരിക്കാത്ത 15 പ്രശ്നങ്ങളും (U-01 മുതൽ U-15 വരെ) അവകാശങ്ങളിലെ വിടവുകളും. |
| [tools/check.py](tools/check.py) | UTF-8, JSON സാധുത, ഐഡികൾ അടിസ്ഥാന ഡാറ്റയിൽ ഉണ്ടോ, ആപേക്ഷിക കണ്ണികൾ, em dash ഇല്ലായ്മ എന്നിവ പരിശോധിക്കുന്ന ചെറിയ സ്ക്രിപ്റ്റ്. |

## എങ്ങനെ വായിക്കാം

- "പരിശോധനയുടെ ആഴം" വ്യത്യസ്ത തലങ്ങളാണ്: ഗ്രന്ഥസൂചി മാത്രം, സാരാംശം, നിർദിഷ്ട ഭാഗങ്ങൾ, പൂർണപാഠം. അവ കൂട്ടിക്കലർത്തരുത്. പദാവലി claim-reviews.json-ലെ `inspection_depth_vocabulary`-ൽ.
- തീയതികൾക്ക് പങ്കുണ്ട്: സംഭവം, നിർമാണം, രചന, പ്രസിദ്ധീകരണം, ഓൺലൈൻ ലഭ്യത. ഒന്ന് മറ്റൊന്നിന് പകരമല്ല.
- പട്ടണം ഒരു പുരാവസ്തുസ്ഥലം; മുസിരിസ് ഒരു ഗ്രന്ഥനാമം. ഇവയെ ബന്ധിപ്പിക്കുന്നത് ആരോപിത തിരിച്ചറിയൽവാദങ്ങൾ മാത്രം.
- 1956-ലെ നിയമത്തിലെ വകുപ്പുകൾ ഒരു അതിർത്തി ഡാറ്റാസെറ്റല്ല. സ്ഥലപരമായ ഉൾപ്പെടുത്തൽ നിർജീവമായി തുടരുന്നു.
- ഏതെങ്കിലും ഒറ്റ വർഷം കേരളത്തിന്റെ ലിഖിതചരിത്രത്തിന്റെ തുടക്കമായി ഈ കുറിപ്പുകൾ അവതരിപ്പിക്കുന്നില്ല.

## പരിധികൾ

ഈ ബാച്ച് `notes/evidence-review/` മാത്രം ചേർക്കുന്നു. `data/*.json`, സ്കീമകൾ, സ്ക്രിപ്റ്റുകൾ, ടെസ്റ്റുകൾ, ജനറേറ്റ് ചെയ്ത കാഴ്ചകൾ, പരിഭാഷാ കുറിപ്പുകൾ, ചരിത്രപരമായ റിലീസ് രേഖകൾ എന്നിവ മാറ്റുന്നില്ല. പണമതിലുകൾ മറികടന്നിട്ടില്ല. ദീർഘമായ പകർപ്പവകാശപാഠം ഇല്ല: ചെറു ഉദ്ധരണികളും കണ്ണികളും സ്വന്തം സംഗ്രഹങ്ങളും മാത്രം. ഉത്ഖനനസ്ഥലങ്ങൾക്ക് കൃത്യ നിർദേശാങ്കങ്ങൾ ചേർത്തിട്ടില്ല.

---

# Evidence review: first batch

**Status:** AI-assisted draft. Human scholarly review and Malayalam language review are pending. Model-assisted checking is not scholarly approval.

**Base revision:** `570f665e25480380e6be361627cf5cfb1285c093` (main). Checked on 2026-10-18 (America/Los_Angeles).

## Contents

| File | What it holds |
|---|---|
| [claim-reviews.json](claim-reviews.json) | Structured review of 16 claims (EV-01 to EV-16): stable IDs, edition, locator, inspection depth, geographical relationship, date roles, supporting and conflicting evidence, source dependencies, rights and finding. Also the access log and the proposed new source cards. |
| [proposed-corrections.json](proposed-corrections.json) | Proposed corrections PC-01 to PC-21, each keyed by ID, field, base revision, file blob SHA and current value. None is applied to canonical data. |
| [UNRESOLVED.md](UNRESOLVED.md) | Fifteen open items (U-01 to U-15) and the rights gaps. |
| [tools/check.py](tools/check.py) | Small script that checks UTF-8, JSON validity, that referenced IDs exist in the base data, relative links, and the absence of em dashes. |

## How to read it

- Inspection depths are distinct levels: metadata only, abstract, named passages, full text. Do not merge them. The vocabulary is in `inspection_depth_vocabulary` in claim-reviews.json.
- Dates carry roles: event, production, composition, publication, online availability. One does not stand in for another.
- Pattanam is an archaeological site and Muziris is a textual name. Only attributed identification arguments link them.
- The provisions of the 1956 Act are not a boundary dataset. Spatial inclusion stays disabled.
- These notes do not present any single year as the start of Kerala's recorded history.

## Limits

This batch adds only `notes/evidence-review/`. It does not change `data/*.json`, schemas, scripts, tests, generated views, translation notes or historical release documents. No paywall was bypassed. No bulk copyrighted text is included: short quotations, links and original summaries only. No precise coordinates are added for excavation sites.

Run the local check with `python3 notes/evidence-review/tools/check.py` from the repository root.
