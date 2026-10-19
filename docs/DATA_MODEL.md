# Evidence, sources and views

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

Production location, place described, findspot, modern repository and proposed ancient identification must become separate place relations. Pattanam and Muziris must have separate identifiers until a specific claim states their proposed relationship; silently merging their names would erase the question being researched [S017](../sources/S017.md), [S018](../sources/S018.md).

## Dates and annual links

A record may be geological, historical or undated. An annual link has an explicit role: exact date, attested year, conventional date, proposed date, or research/access history. Undated and geological claims cannot be forced into annual event entries. A separately dated modern publication can have a separate research-history record.

## Review states

The seed has no independently approved human reviews. Approval requires identifiable review provenance, not merely a generated confidence adjective. Review should be claim-specific: someone may check a translation but not the radiocarbon model or geographical identification.

Use contributor identifiers rather than unnecessary personal contact details. Proposed extensions include reviewer role, reviewed source passages, unresolved objections, decision, timestamp and superseded decisions. A source check, a method check and an editorial merge are different acts.

## Validation limits

`validate.py` checks references, date structures, year-zero exclusion, future cutoffs, required provenance, generated views and local file links. It cannot establish the truth of an ancient claim, interpret an inscription, adjudicate rights or verify an unseen page. The JSON schema files document the basic structure; the included standard-library validator performs the operational checks and is not a general-purpose JSON Schema engine.
