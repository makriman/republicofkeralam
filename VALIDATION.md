# Structural validation report

Release: 0.1.0-research-foundation. Evidence cutoff: 2026-10-11.

Test environment: Python 3.13.5, standard library only.

`python scripts/build.py --check`: passed; 2,428 generated files match canonical data.

`python scripts/validate.py`: passed; IDs, provenance references, date structures, year-zero exclusion, configured annual-file coverage, generated views and local Markdown file links checked.

`python -m unittest discover -s tests -v`: 15 tests passed. Tests include BCE/CE transition, deterministic generation, invalid source links, inappropriate annual links, reviewer requirement and current-year cutoff.

This validates the implementation and internal consistency. It does **not** establish historical truth, translation accuracy, legal clearance, source independence, present boundary correctness, or exhaustive coverage. Independent human review remains pending for all 31 evidence records.

## Validation hardening recheck (19 October 2026)

Python 3.12.14. `python -m unittest discover -s tests -v`: 102 tests passed, including the installed optional JSON Schema reference comparison. `python scripts/build.py` and `python scripts/build.py --check`: 2,428 generated files match; no canonical or generated content changes. `python scripts/validate.py`: passed. `python scripts/validate.py --require-translation ml`: failed as expected with 952 missing current translations. A separate malformed-field probe tried 456 wrong-typed or empty values across canonical collections without a validator crash.

`sha256sum -c MANIFEST.sha256`: all 2,526 entries passed. Inventory comparison covers every tracked file except the manifest itself. Human and specialist review remain pending; 2,308 annual pages remain without year-specific seeds. Integrity checks for geometry do not replace boundary acquisition or legal/GIS review.
