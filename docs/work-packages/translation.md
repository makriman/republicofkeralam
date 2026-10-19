# മലയാളം ആദ്യം വരുന്ന പരിഭാഷാ PR

നില: നിർദേശിക്കുന്ന ജോലി. ഭാഷാവിദഗ്ധരുടെ പരിശോധന ബാക്കിയുണ്ട്.

## പരിധി

നിലവിലെ Pro ശേഖരം നിലനിർത്തുക. README, CONTRIBUTING, `docs/`, `audit/`, `geography/`, `coverage/`, `notes/`, `templates/research-note.md`, കൂടാതെ ഡാറ്റയിൽനിന്ന് നിർമ്മിക്കുന്ന വായനാപാഠങ്ങൾ എന്നിവയുടെ ഭാഷാപട്ടിക തയ്യാറാക്കുക. `project.json` ഇപ്പോൾ `primary_language: en` എന്നാണ് പറയുന്നത്; ഇത് മാറ്റുന്നതിന് മുൻപ് schema worker-നൊപ്പം rendering രീതി തീരുമാനിക്കുക. പ്രത്യേക ഇംഗ്ലീഷ് ലാൻഡിങ് പേജ് മാറ്റരുത്.

## ഫയൽ ഉത്തരവാദിത്തം

ഈ worker `notes/translation-review/` എന്ന പുതിയ staging ഭാഗം മാത്രം തിരുത്തണം. README, CONTRIBUTING നിർദേശങ്ങൾ അവിടെ സൂക്ഷിക്കുക. `data/*.json`, `project.json`, `scripts/`, generated പേജുകൾ എന്നിവ integration worker മാത്രം തിരുത്തണം. ഫയൽപ്പട്ടികയും commit-ഉം പങ്കുവെച്ചശേഷം ജോലി തുടങ്ങുക.

## ഫലങ്ങൾ

- ഓരോ വായനാപാഠത്തിന്റെയും ഉറവിടപാത/ID, source revision, പരിഭാഷ, പരിശോധനാനില ഉൾപ്പെടുത്തിയ manifest.
- മലയാളം ആദ്യം, ഇംഗ്ലീഷ് തുടർന്ന് വരുന്ന കരടുകൾ; സാങ്കേതികപദങ്ങളുടെ പദാവലി.
- പരിഭാഷയില്ലാത്തതും സംശയമുള്ളതുമായ ഭാഗങ്ങളുടെ പട്ടിക.
- AI സഹായം, ഭാഷാപരിശോധകൻ, വിഷയപരിശോധകൻ എന്നിവ വേർതിരിച്ച നിലകൾ.

## സ്വീകരിക്കാനുള്ള വ്യവസ്ഥകൾ

തീയതി, സംഖ്യ, citation, URL, uncertainty എന്നിവ മൂലപാഠവുമായി ഒത്തിരിക്കണം. JSON key-കളും ID-കളും മാറ്റരുത്. ചരിത്രശാസ്ത്രപരമായ അർത്ഥം പരിഭാഷയിൽ ശക്തിപ്പെടുത്തരുത്. UTF-8, Markdown കണ്ണികൾ, മലയാളം ആദ്യം എന്ന ക്രമം പരിശോധിക്കുക. മലയാളം അറിയുന്ന വ്യക്തിയുടെ വായനയും സാങ്കേതികപദങ്ങളുടെ വിഷയപരിശോധനയും കഴിഞ്ഞതുവരെ human review pending എന്ന് സൂചിപ്പിക്കുക. Schema support ലഭിച്ചശേഷം മാത്രമേ generated പേജുകളിലേക്ക് ചേർക്കാവൂ. നേരിട്ട് merge/publish ചെയ്യരുത്.

# Malayalam-first translation PR

Status: proposed work; human language review pending.

## Scope

Preserve the Pro archive. Inventory README, CONTRIBUTING, `docs/`, `audit/`, `geography/`, `coverage/`, `notes/`, `templates/research-note.md` and reader-facing text generated from canonical data. `project.json` currently declares `primary_language: en`; agree on rendering support before changing it. Leave the separate English landing page untouched.

## Ownership

This worker writes only to a new `notes/translation-review/` staging area, including proposed README and CONTRIBUTING replacements. The integration worker alone edits `data/*.json`, `project.json`, scripts and generated views. Agree on file ownership and base commit before work starts.

## Deliverables

- A manifest recording source path/ID, source revision, translation and review status.
- Malayalam-first, English-second drafts and a technical glossary.
- A list of untranslated content and unresolved wording.
- Separate AI-assistance, language-review and specialist-review statuses.

## Acceptance

Dates, numbers, citations, URLs and uncertainty match the source. Keys and IDs remain stable. Translation does not strengthen historical claims. Check UTF-8, links and Malayalam-first ordering. Human review remains pending until a competent Malayalam reader and relevant subject specialist perform the required checks. Integrate generated pages only after schema/rendering support is ready. Do not merge or deploy. Return changes on this assigned draft PR branch.
