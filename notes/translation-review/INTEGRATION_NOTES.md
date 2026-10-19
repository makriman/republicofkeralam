# Project B-യ്ക്കുള്ള integration കുറിപ്പുകൾ / Integration notes for Project B

ഈ കുറിപ്പുകൾ നിർദേശങ്ങൾ മാത്രമാണ്. ഈ staging ഭാഗം `data/`, `project.json`, `scripts/`, `schemas/`, `tests/`, `coverage/`, generated പേജുകൾ, root README/CONTRIBUTING എന്നിവ തിരുത്തുന്നില്ല. Proposals only; this staging area does not edit canonical data, generators, schemas, tests, coverage, generated views or the root README/CONTRIBUTING. Owner of these files: Project B (draft PR #5, `work/schema-validation`).

Base revision: `570f665e25480380e6be361627cf5cfb1285c093`.

## I1. ഹാൻഡ്-മെയിന്റെയ്ൻഡ് ഡോക്യുമെന്റുകൾ / Hand-maintained documents

`batch-1/docs/*.ml-en.md`, `batch-1/notes/`, `batch-1/templates/`, `batch-1/github/` are complete replacement candidates: Malayalam section, `---`, retained English. To integrate one:

1. Remove the HTML comment header and the two `>` staging notices.
2. Restore the original relative link prefixes (the staged copies rewrite `../sources/S027.md` to resolve from the staging folder; `tools/assemble.py` shows the exact rewrite).
3. Confirm the source file has not changed since `570f665`; if it has, mark the manifest entry `stale` and retranslate the diff.
4. Keep human-review status pending in the integrated text until a recorded human review exists.

For the GitHub templates, front-matter `name`/`about` changes are proposals; GitHub shows them in its template picker.

## I2. Canonical-data prose / ഡാറ്റയിലെ ഗദ്യം (batch 2 and 3)

Batch 2 and 3 stage translations keyed by stable ID and JSON field (for example `data/periods.json#E01.central_question`), never by array position. A backward-compatible schema option that would avoid touching existing keys:

```json
"i18n": { "ml": { "title": "…", "claim": "…", "caveat": "…" } }
```

with the English fields unchanged as the fallback, and per-field `source_revision` or a hash of the English string so the validator can flag stale Malayalam. The exact shape is Project B's decision. Translation will adapt the staging format to it.

Fields that should **not** be translated: `id`, enum values (`status`, `precision`, `kind`, `inspection`, `scope_relation`, `evidence_type`), `url`, `doi`, `support[].locator`, `inspected_locator`, `sources`, dates, `tags`. Original source `title` values stay as published; a Malayalam gloss, if any, must be rendered as an explanatory translation, not as the title.

## I3. Generator-supplied labels / generator-ലെ ലേബലുകൾ

Reader-facing strings in `scripts/build.py` (page headings such as “Year attested; day not normalized”, `Wider-period evidence — not an event assigned to this year`, coverage table labels, register introductions) are generated text. Batch 3 will stage Malayalam strings for them in a key/value list. They need a rendering mechanism in the generator; translation will not edit generated pages.

Em dashes in generated views (for example `sources/README.md`, `periods/README.md`, `audit/CHAT_AUDIT.md`, every `sources/S###.md` heading) come from generator templates of the form `ID — title`. Suggest `ID: title`. Changing this alters all generated files, so it belongs with the generator work.

## I4. Line-ending observation

`coverage/year-status.csv` is committed with CRLF line endings while `.gitattributes` declares `*.csv text eol=lf`, so a fresh clone shows the file as modified (`git status`) without any edit. Translation has not staged or committed that file. Suggest renormalizing it in the generator PR.

## I5. `project.json` primary language

`project.json` declares `primary_language: en`. The work package asks that this not change until rendering support exists. No change proposed here beyond the dependency.
