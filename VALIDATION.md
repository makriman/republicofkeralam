# Structural validation report

Release: 0.1.0-research-foundation. Evidence cutoff: 2026-10-11.

Test environment: Python 3.13.5, standard library only.

`python scripts/build.py --check`: passed; 2,428 generated files match canonical data.

`python scripts/validate.py`: passed; IDs, provenance references, date structures, year-zero exclusion, configured annual-file coverage, generated views and local Markdown file links checked.

`python -m unittest discover -s tests -v`: 15 tests passed. Tests include BCE/CE transition, deterministic generation, invalid source links, inappropriate annual links, reviewer requirement and current-year cutoff.

This validates the implementation and internal consistency. It does **not** establish historical truth, translation accuracy, legal clearance, source independence, present boundary correctness, or exhaustive coverage. Independent human review remains pending for all 31 evidence records.
