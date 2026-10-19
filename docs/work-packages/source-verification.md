# സ്രോതസ്സുകളും തെളിവുകളും പരിശോധിക്കുന്ന PR

നില: നിർദേശിക്കുന്ന പരിശോധന; ചരിത്രവിദഗ്ധരുടെ അംഗീകാരം ലഭിച്ചതായി കരുതരുത്.

`audit/CHAT_AUDIT.md`, `data/records.json`, `data/sources.json`, `docs/EVIDENCE_POLICY.md`, `docs/CHRONOLOGY.md` എന്നിവയിൽനിന്ന് തുടങ്ങുക. നിലവിലെ ID-കൾ നിലനിർത്തുക. ഈ worker പുതിയ `notes/evidence-review/` ഭാഗം മാത്രം തിരുത്തണം. അടിസ്ഥാന ഡാറ്റയിൽ തിരുത്തലുകൾ integration worker ചേർക്കും.

## ആദ്യം പരിശോധിക്കേണ്ടത്

1. ഇടയ്ക്കലിലെ ചിത്രങ്ങൾക്ക് പറയുന്ന “6000 BCE” തീയതിയുടെ അടിസ്ഥാനവും പരിമിതികളും.
2. വടക്കൻ കേരളത്തിലെ ആദ്യകാല മനുഷ്യവാസത്തെക്കുറിച്ചുള്ള പഠനം: സാരാംശത്തിനപ്പുറം തെളിവും dating രീതിയും.
3. അശോകശാസനങ്ങൾ: കൃത്യപാഠം, പരിഭാഷ, നിർദേശിച്ച തീയതി, സ്ഥലബന്ധം. ഒരു ഏകവർഷത്തെ ചരിത്രത്തിന്റെ തുടക്കമായി പ്രഖ്യാപിക്കരുത്.
4. Trivandrum Block പഠനത്തിന്റെ തിരുത്തൽ: `S002`-നൊപ്പം `S003` പരിശോധിച്ച് സംഖ്യാഫലങ്ങൾ വിലയിരുത്തുക.
5. Quilon Formation പഠനത്തിലെ സാമ്പിളുകളും dating രീതിയും. സാമ്പിളിന്റെ പ്രായം മുഴുവൻ തീരത്തിന്റെ പ്രായമാക്കരുത്.
6. Periplus, Pliny, Ptolemy: പ്രസക്തമായ ഭാഗങ്ങൾ. പട്ടണം എന്ന പുരാവസ്തുസ്ഥലവും Muziris എന്ന പാഠത്തിലെ സ്ഥലനാമവും വേർതിരിക്കുക.
7. 1956-ലെ നിയമത്തിലെ പ്രദേശമാറ്റങ്ങളും ഇപ്പോഴത്തെ ഭരണപരിധി ഡാറ്റയും പ്രത്യേകം പരിശോധിക്കുക.
8. `S020`-ലെ Kollam plates ഗവേഷണ നിർദേശവും അന്തിമഫലവും വേർതിരിക്കുക. `S017`, `S018` എന്നിവയിലെ യഥാർത്ഥ പ്രസിദ്ധീകരണവും പിന്നീടുള്ള hosting തീയതികളും പരിശോധിക്കുക.

## ഓരോ പരിശോധനയിലും വേേണ്ടത്

അവകാശവാദം, സ്ഥിര ID, സ്രോതസ്സ്, പതിപ്പ്, പേജ്/ഭാഗം, പരിശോധിച്ച ആഴം, ഭൂഭാഗബന്ധം, തീയതികളുടെ വ്യത്യസ്ത അർത്ഥങ്ങൾ, വിരുദ്ധ തെളിവ്, അവകാശനില, നിർദേശിച്ച മാറ്റം, ശേഷിക്കുന്ന സംശയം എന്നിവ മലയാളം ആദ്യം ഇംഗ്ലീഷ് തുടർന്ന് രേഖപ്പെടുത്തുക. കാറ്റലോഗോ abstract-ഓ മാത്രം കണ്ടാൽ അതു വ്യക്തമാക്കുക. ഒരേ മൂലസ്രോതസ്സിന്റെ പകർപ്പുകൾ സ്വതന്ത്ര തെളിവായി എണ്ണരുത്.

## സ്വീകരിക്കാനുള്ള വ്യവസ്ഥകൾ

പരിശോധിച്ചു എന്ന എല്ലാ വാദത്തിനും കൃത്യമായ locator-ഉം inspection depth-ഉം വേണം. ലഭിക്കാത്ത പൂർണപാഠം unresolved ആയി തുടരണം. യഥാർത്ഥ പരിശോധനയില്ലാതെ human_review മാറ്റരുത്. പകർപ്പവകാശമുള്ള പൂർണപാഠങ്ങളോ സ്കാനുകളോ കൂട്ടത്തോടെ ചേർക്കരുത്. കണ്ണികളും സ്വന്തം സംഗ്രഹങ്ങളും ഉപയോഗിക്കുക. Draft PR-ൽ തീർന്നതും ബാക്കിയുള്ളതും വ്യക്തമാക്കുക; merge/publish ചെയ്യരുത്.

# Source verification and provenance PR

Status: proposed research; not scholarly approval.

Start with `audit/CHAT_AUDIT.md`, `data/records.json`, `data/sources.json`, `docs/EVIDENCE_POLICY.md` and `docs/CHRONOLOGY.md`. Keep existing IDs. This worker owns only a new `notes/evidence-review/` staging area. The integration worker applies canonical-data changes.

## Priority checks

1. Evidence and limitations behind Edakkal's “6000 BCE” attribution.
2. North-Kerala early-occupation study beyond its abstract, including context and dating methods.
3. Ashokan passages, translation, proposed dates and geographical identification. Do not invent one exact beginning of recorded history.
4. Trivandrum Block erratum: inspect `S003` alongside `S002` before adopting numerical findings.
5. Quilon Formation samples and dating methods. Do not generalize sampled-strata ages to the entire coast.
6. Relevant Periplus, Pliny and Ptolemy passages. Keep the Pattanam site and the textual place name Muziris separate.
7. The 1956 Act's territorial provisions separately from a checked current-boundary dataset.
8. `S020`'s Kollam-plates proposal versus final outcomes; `S017`/`S018` original publication versus later hosting dates.

## Each review record

Provide the claim, stable IDs, source edition, precise locator, inspection depth, geographical relationship, date roles, contrary evidence, rights status, proposed correction and unresolved questions in Malayalam first and English second. State when only metadata or an abstract was inspected. Track dependent copies rather than counting them as independent evidence.

## Acceptance

Every verification claim has a locator and inspection depth. Missing full text remains unresolved. Do not change human_review without actual qualified human review. Do not bulk-copy copyrighted texts or scans; use references and original summaries. The draft PR lists resolved and unresolved items without claiming complete verification. Do not merge or deploy. Return changes on this assigned draft PR branch.
