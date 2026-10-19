# Contributing

Start with an identified source or a clearly bounded unanswered question. Do not begin by asking a model to invent the contents of an empty year file.

## A source contribution

Register the title, creator, edition, identifier, URL or shelfmark, language, dates, relevant place relationship, access conditions and rights. State exactly what you inspected: catalogue, abstract, passage, selected page images or full text. Preserve the locator and distinguish a hosted version from original publication. Search for corrections and duplicates.

## A historical claim contribution

Add one bounded claim in `data/records.json`, using [the record template](templates/record.json). Cite at least one source with the smallest sufficient locator. State date precision and geographic relation. Record limitations and contrary evidence. Uncertain intervals belong in dossiers; they do not become exact events simply because annual files exist.

The template is an example structure and is not automatically loaded as a source record. Replace placeholders and validate. IDs must be unique. Generated pages are not the source of truth. A future large-scale dataset can be sharded while preserving stable IDs.

## A correction

Keep the record’s identity where practical, state the old and new readings, cite the new evidence and explain whether the change affects date, place, wording, interpretation or rights. Do not silently erase a contested interpretation. Material privacy or safety removals may require different treatment and should be documented without republishing the sensitive content.

## Checks before submission

```bash
python scripts/build.py
python scripts/build.py --check
python scripts/validate.py
python -m unittest discover -s tests -v
```

Passing these commands is not historical peer review. Proposed factual acceptance needs a person with appropriate source/language/method competence. Approval must name a reviewer identifier and what was checked; do not flip `human_review` to `approved` merely because a source sounds plausible.

## Rights and conduct

Submit only material you are entitled to submit under the repository’s applicable licenses. Keep third-party restrictions attached to assets. Avoid unnecessary personal data and sensitive site coordinates. Discuss evidence and interpretation respectfully; no community’s history is to be excluded because it does not match a modern identity narrative.

The initial package has no configured remote repository or real maintainer contact. Those must be set by the project owner before launch; this file does not imply a review team already exists.
