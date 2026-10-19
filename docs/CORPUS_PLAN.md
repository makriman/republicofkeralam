# Building an auditable digital corpus

## Two connected products

The repository is both an evidence index and an eventual public history. Discovery must therefore be wider than the currently accepted facts. Catalogue a relevant document even when it is untranslated, inaccessible, disputed or not licensed for republication. Do not elevate its contents to an accepted event until the appropriate passages have been inspected.

“Publicly accessible” means a person can access material under some conditions. It does not mean that redistribution, automated harvesting, text mining or republication is authorized. Rights and access are separate fields [S027](../sources/S027.md).

## Verified starting routes

The source cards distinguish actual inspected landing pages from search-index-only discoveries. None of these collections is declared completely inventoried.

| Corpus family | Starting source cards | Next bounded task |
|---|---|---|
| Local geology and palaeontology | S002–S008 | Acquire corrections, sample tables and citation networks; map each local sample |
| Prehistory and excavation reports | S009–S013, S019, S039 | Enumerate journal volumes, site reports and original laboratory references |
| Epigraphy and ancient texts | S014–S018, S020, S041 | Register physical witnesses, editions, translation passages and dating arguments |
| Early modern voyage manuscripts | S021, S022, S040 | Compare the critical edition and surviving witness; distinguish narrative and edition dates |
| Statutory history | S023 | Extract the relevant sections, amendments, schedules and operative dates |
| State archival holdings and printed series | S028–S030 | Enumerate fonds/series/volumes before asserting digital coverage |
| Legislative documentation | S031 | Inventory debates, bills and reports by institution, session and date |
| University historical collections | S032, S033 | Build item lists, dates, languages and rights records |
| Manuscript preservation projects | S034–S037 | Enumerate catalogue items and manifests; preserve custodial and ethical restrictions |
| Audiovisual and public-information collections | S038 | Separate recording, publication, digitization and subject dates |

See the [source register](../sources/README.md) for the actual URLs and inspection limitations. `data/corpora.json` separates these located routes from families awaiting reconnaissance.

## Additional families to survey — not claimed as inspected holdings

The next inventory should cover national and state archaeological publications, inscription series, museum catalogues and coin finds; university theses and institutional repositories; national and regional archives; gazettes, district manuals, settlement reports, censuses and land records; newspapers and periodicals; legal proceedings; religious and community repositories; school, labour, cooperative and local-government records; oral-history collections; and environmental, demographic and statistical series.

External repositories require equal attention. Portuguese, Dutch, French, British, West Asian, Chinese, Jewish and Syriac sources can contain evidence about the same territory. Maritime documentation, commercial correspondence, missionary records and manuscript custody abroad should be searched by places and relationships, not only by the modern name.

These are research targets. No claim is made here about complete digital availability, current endpoints, licenses or item counts for uninspected collections.

## Multilingual discovery

Use place aliases and historical administrative names alongside themes and genres. Search relevant languages and scripts where the source corpus warrants them: Malayalam, Tamil, Kannada, Tulu, Sanskrit, Prakrit, Arabic and Arabi-Malayalam, Syriac, Hebrew, Persian and Judaeo-Persian, Portuguese, Dutch, French, Greek, Latin, Chinese, English and German, among others. This is a discovery checklist, not a statement that every language has an equally extensive local corpus.

Do not auto-normalize a historical language label to a modern political identity. Preserve a source’s classification and a reviewer’s revised classification as separate assertions. Preserve both original spelling and transliteration. Record transliteration uncertainty rather than silently “correcting” names.

## From collection to year file

1. **Register the collection.** Give it an ID, custodian, scope, snapshot date, access method, terms and catalogue structure. Define what counts as an item and whether a manifest is complete.
2. **Enumerate items.** Record identifiers, duplicates, parent volumes, page/image extents, languages, dates and rights. Distinguish the same work on several sites from several independent sources.
3. **Triage relevance.** Identify places, periods and themes. Retain uncertainty and record exclusions with reasons.
4. **Inspect evidence.** Read relevant passages continuously, check page images where needed, retain precise locators, and identify versions/corrections.
5. **Extract bounded claims.** Separate event, object, text and research dates. Preserve alternative readings and geographic relationships.
6. **Review and publish.** Check factual support, translation, date normalization, rights and sensitive information. Only then promote from lead to approved evidence.

A scraper must never jump from catalogue discovery directly to approved annual prose.

## Coverage ledger

For each declared collection snapshot, track the total catalogue items enumerated; items deemed relevant; items accessible; relevant passages inspected; items requiring OCR or specialist translation; extracted claims; review outcomes; rights-cleared assets; and missing or inaccessible ranges. Keep `unknown` distinct from zero.

The denominator must be the same unit as the numerator. “200 images processed” is not “200 manuscripts read.” A catalogue’s total TIFF count is not this repository’s extraction count. A 92-manuscript announcement does not mean 92 manuscripts were inspected [S036](../sources/S036.md).

Separate content completeness from source quality. A complete newspaper year can still contain erroneous reports. A single surviving inscription can be historically important even when it supplies only one record.

## Negative searches and failures

Log the collection, query or item range, date, language, filters, result count if actually known, and whether catalogue pages or full content were searched. Access denial, broken link, missing OCR and no matching text are different outcomes. Do not claim “no record exists” from one failed query.

This release provides a concise successful-source and gap log. It does not contain a complete raw log of every search performed during the chat. No hidden query total or total-pages-read claim is fabricated.

## Storage and growth

Keep metadata, citations and original summaries in Git. Store only rights-cleared binary assets, with source and integrity metadata; a large-scale asset store is a separate future decision. Where distribution is not permitted, link to the holder and retain only allowed metadata and analysis.

The current flat JSON arrays are appropriate to a seed. At larger scale, shard records by stable ID and sources by collection or identifier range; keep generated year pages stable. Avoid manually maintaining millions of duplicate citations in annual prose. A search index or database can be generated without replacing the plain-text source of truth.
