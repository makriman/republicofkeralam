# Schemas / സ്കീമകൾ

> നില: AI സഹായത്തോടെ എഴുതിയ സാങ്കേതിക കുറിപ്പ്. മലയാള ഭാഷാപരിശോധന ബാക്കി. / Status: AI-assisted technical note. Human Malayalam-language review pending.

## മലയാളം

ഓരോ അടിസ്ഥാന ഡാറ്റാഫയലിനും ഇവിടെ ഒരു JSON Schema ഉണ്ട്: `record`, `source`, `period`, `audit`, `corpus`, `crosswalk`, `project`, `scope`. `scripts/validate.py` ഓരോ ഇനവും ആദ്യം അതിന്റെ സ്കീമയുമായി ഒത്തുനോക്കുന്നു. ഇതിനായി പുറത്തുനിന്നുള്ള പാക്കേജ് ആവശ്യമില്ല; `scripts/schema_check.py` എന്ന ചെറിയ standard-library executor ഉപയോഗിക്കുന്നു. അത് നടപ്പാക്കാത്ത ഒരു schema keyword കണ്ടാൽ നിശ്ശബ്ദമായി ഒഴിവാക്കാതെ `SchemaError` നൽകും. അതുകൊണ്ട് പ്രയോഗിക്കാത്ത നിയമം പ്രയോഗിച്ചതായി തോന്നില്ല.

ഘടന തെറ്റിയ ഇനം (ഫീൽഡ് ഇല്ലാത്തത്, തെറ്റായ തരം) ഒരു പിശകുസന്ദേശമായി രേഖപ്പെടുത്തി ഒഴിവാക്കും. പിന്നീടുള്ള cross-reference, തീയതി പരിശോധനകൾ ശരിയായ ഘടനയുള്ള ഇനങ്ങളിൽ മാത്രം നടക്കും. അതിനാൽ `KeyError`, `TypeError` പോലുള്ള തകർച്ചകൾക്ക് പകരം വായിക്കാവുന്ന സന്ദേശം ലഭിക്കും.

ID-കൾ സ്ഥിരമാണ്; പുനർനമ്പറിടരുത്. ഓരോ വിഭാഗത്തിനും സ്വന്തം namespace ഉണ്ട്: സ്രോതസ്സ് `S` + മൂന്നോ അതിലധികമോ അക്കം, തെളിവുരേഖ `R` + മൂന്നോ അതിലധികമോ അക്കം, കാലഘട്ടപഠനരേഖ `E` അല്ലെങ്കിൽ `P` + രണ്ടോ അതിലധികമോ അക്കം, audit `A` + മൂന്നോ അതിലധികമോ അക്കം, രേഖാസമുച്ചയം `C` + മൂന്നോ അതിലധികമോ അക്കം.

തീയതിക്ക് വ്യവസ്ഥാപിത നിയമങ്ങളുണ്ട്. `historical` തീയതിക്ക് പൂജ്യമല്ലാത്ത `start_year`, `end_year` വേണം; `precision` എന്നത് `day`, `year`, `conventional_year`, `interval` എന്നിവയിലൊന്നാകണം; `day` ആണെങ്കിൽ പരിശോധിച്ച `date` വേണം. `geological` തീയതിക്ക് `older_ma`, `younger_ma` വേണം; BCE/CE വർഷം പാടില്ല. `undated` അവകാശവാദത്തിന് വർഷമോ ദിവസമോ Ma മൂല്യമോ പാടില്ല. `other_dates`-ലെ ഓരോ തീയതിക്കും പ്രസിദ്ധീകരണം, കണ്ടെത്തൽ, ഡിജിറ്റൈസേഷൻ പോലുള്ള പേരുള്ള role വേണം; `event` എന്ന role പാടില്ല, കാരണം സംഭവകാലം `date`-ലാണ്. ഓരോന്നിനും `year` അല്ലെങ്കിൽ `date` ഇവയിൽ ഒന്ന് മാത്രം.

സ്കീമയ്ക്ക് പ്രകടിപ്പിക്കാനാകാത്ത നിയമങ്ങൾ `validate.py`-ൽ ഉണ്ട്: references, release cutoff, ഒറ്റവർഷ precision-ഉം കാലപരിധിയും തമ്മിലുള്ള പൊരുത്തം, ഒരു interval-ന് ഒരു വർഷക്കണ്ണി മാത്രം, ഒരേ വർഷം രണ്ടുതവണ ബന്ധിപ്പിക്കരുത്, `conventional_year` തീയതിയെ `year_attested` ആക്കരുത്, ബൗണ്ടറി geometry ഇല്ലാതെ spatial filtering പാടില്ല. മനുഷ്യപരിശോധനയുടെ നിയമം തെളിവുരേഖ, സ്രോതസ്സ്, പരിഭാഷ എന്നിവയ്ക്ക് ഒന്നുതന്നെയാണ്: `approved` അല്ലെങ്കിൽ `rejected` ആക്കാൻ `reviewers`-ൽ കുറഞ്ഞത് ഒരു `reviewer_type: "human"` രേഖ വേണം. മോഡൽ പരിശോധന രേഖപ്പെടുത്താം; അത് അംഗീകാരമാകില്ല.

മലയാള പരിഭാഷാ കാറ്റലോഗുകളുടെ ഘടന [`docs/BILINGUAL_DATA.md`](../docs/BILINGUAL_DATA.md) വിശദീകരിക്കുന്നു. ഈ പരിശോധനകൾ ഘടന മാത്രമാണ് ഉറപ്പാക്കുന്നത്; ചരിത്രസത്യം, പരിഭാഷയുടെ കൃത്യത, അവകാശനില എന്നിവയല്ല.

---

## English

There is one JSON Schema per canonical data file: `record`, `source`, `period`, `audit`, `corpus`, `crosswalk`, `project` and `scope`. `scripts/validate.py` checks every item against its schema first. No third-party package is needed: `scripts/schema_check.py` is a small standard-library executor for the subset these files use. If a schema uses a keyword the executor does not implement, it raises `SchemaError` instead of skipping it, so an unenforced rule cannot look enforced. When the optional `jsonschema` package is installed, a test confirms that it agrees with the seed data.

A malformed item (missing field, wrong type) is reported and skipped. Cross-reference and date checks then run only on well-formed items, so bad input produces readable messages instead of `KeyError` or `TypeError`.

IDs are stable; do not renumber them. Each collection has its own namespace: sources `S` plus three or more digits, records `R` plus three or more digits, period dossiers `E` or `P` plus two or more digits, audit items `A` plus three or more digits, corpora `C` plus three or more digits.

Dates have conditional rules. A `historical` date needs nonzero `start_year` and `end_year`; `precision` is one of `day`, `year`, `conventional_year` or `interval`; `day` also needs a checked `date`. A `geological` date needs `older_ma` and `younger_ma` and may not carry BCE/CE years. An `undated` claim may not carry a year, a day or an Ma value. Each `other_dates` entry needs a named role such as publication, discovery or digitization; the role `event` is refused because the event date lives in `date`. Each entry has exactly one of `year` or `date`.

Rules a schema cannot express live in `validate.py`: references, the release cutoff, agreement between single-year precision and the range, at most one year link for an interval, no year linked twice by one record, no `conventional_year` relabelled as `year_attested`, and no spatial filtering without boundary geometry. Human review uses one rule for records, sources and translations: `approved` or `rejected` needs at least one `reviewer_type: "human"` entry in `reviewers`, with `reviewer`, `checked` and `date`. A model check can be recorded but never counts as approval.

The Malayalam translation catalogue format is described in [`docs/BILINGUAL_DATA.md`](../docs/BILINGUAL_DATA.md). These checks establish structure only, not historical truth, translation accuracy or rights status.
