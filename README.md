# History of the present-day Kerala territory

**Version 0.1.0 — research foundation · evidence cutoff: 11 October 2026**

An open, geographically defined history of the material territory now administered as Kerala, from its geological ancestry through human occupation to the contemporary record. The name is a modern locator, not an eligibility test. A source can concern this land without using “Kerala,” and a source using that word is not automatically about this land.

> **This is not an exhaustive history or a completed archival collection.** It is a working repository structure, a claim audit, a limited source register and carefully qualified seeds. It contains 2,326 annual pages, but only 18 have year-specific seed links; the other 2,308 are labelled unresearched. Thirty-one canonical records include publication and research milestones as well as past-event evidence. No independent human scholarly review or complete collection inventory has yet been completed.

## Start here

[Audit of the previous conversation](audit/CHAT_AUDIT.md) · [Project charter](docs/PROJECT_CHARTER.md) · [Coverage](coverage/README.md)

[Deep-time and period dossiers](periods/README.md) · [Annual navigation](years/README.md) · [Evidence records](records/README.md) · [Source cards](sources/README.md)

There are twelve deep-time/prehistory dossiers and seven documentary-period dossiers. The annual index runs from **300 BCE to 2026 CE, without a year zero**. The start of that century is an editorial container for an early documentary horizon, not a claim that an event occurred in 300 BCE or that no earlier writing could be relevant. The index can be extended.

## What is in this release

| Component | Purpose |
|---|---|
| `audit/CHAT_AUDIT.md` | 80 claim, implication, omission and method checks; crosswalk of all 46 earlier proposed chapters |
| `data/records.json` → `records/` | 31 canonical, attributed evidence records and readable Markdown views |
| `data/sources.json` → `sources/` | 42 sources and discovery routes, with inspection depth and rights status |
| `data/periods.json` → `periods/` | 19 open research dossiers, including explicit unanswered questions |
| `years/BCE/`, `years/CE/` | 2,326 year files: navigation, not fabricated annual narratives |
| `geography/scope.json` | Proposed geographic rules; licensed current boundary geometry still pending |
| `coverage/` | Counts and year statuses; no invented whole-internet completion percentage |
| `docs/`, `templates/`, `schemas/` | Research, chronology, evidence, rights and contribution conventions |
| `scripts/`, `tests/` | Offline generation and structural validation using Python’s standard library |

**Not included:** copyrighted full texts, bulk image scans, a verified current boundary polygon, an automatic scraper, automatic calendar conversion, a deployed website, a remote GitHub repository, or a claim that catalogue-only sources have been read in full.

## Use locally

The included code uses Python 3.10+ language features and was tested with Python 3.13.5. No third-party packages or network access are needed to build the Markdown.

```bash
python scripts/build.py
python scripts/build.py --check
python scripts/validate.py
python -m unittest discover -s tests -v
```

Generated Markdown contains a warning marker. Edit canonical JSON in `data/`, then rebuild. Put working notes in `notes/`; do not edit generated annual pages and expect those changes to survive regeneration. The builder refuses to overwrite unmarked hand-authored Markdown at generated paths.

## The central evidence rule

**A fact about the past, the source that attests it, and a later interpretation are different objects.** The annual pages are views onto the evidence; they are not the primary database. An uncertain century stays uncertain. A fossil’s geological age is not the year its paper was published. A digital scan’s upload year is not the manuscript’s age.

[Chronology rules](docs/CHRONOLOGY.md) · [Data model](docs/DATA_MODEL.md) · [Evidence and review](docs/EVIDENCE_POLICY.md)

## Geographic scope

The target is the modern administrative territory as a fixed research frame. Historical kingdoms, districts, watersheds, language areas and offshore basins overlap it in different ways. Related external evidence is allowed, but must state the relationship. The current polygon has **not** been acquired or legally/geographically crosschecked; automated spatial inclusion is disabled.

[Geographic policy](geography/README.md) · [Provisional scope configuration](geography/scope.json)

## Exhaustiveness as a research programme

The ambition is exhaustive discovery and indexing of relevant digital material. Each bounded collection must have an inventory, acquisition date, item count, missing ranges, access failures and rights assessment. An index of everything in a declared collection snapshot is a defensible milestone. “All history on the internet is complete” is not a result asserted here.

[Corpus plan](docs/CORPUS_PLAN.md) · [Collection registry](data/corpora.json) · [Research roadmap](docs/ROADMAP.md)

## Reuse and collaboration

Original code is MIT-licensed. Original explanatory prose, editorial arrangement and copyrightable original database contributions are offered under CC BY 4.0 to the extent contributors hold rights in them. Facts are not claimed as exclusive property. **Source books, scans, translations, images, metadata exports and third-party databases keep their own rights.** They do not acquire the repository’s license by being cited.

[License](LICENSE.md) · [Rights policy](docs/RIGHTS_AND_ETHICS.md) · [Contributing](CONTRIBUTING.md) · [Release limitations](RELEASE_NOTES.md)

This initial draft is AI-assisted. Sources were inspected only to the depths declared on their cards. Specialist review, multilingual verification and primary-source acquisition remain open work, not completed achievements.
