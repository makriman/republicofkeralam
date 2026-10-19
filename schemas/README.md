# Schemas

`record.schema.json` documents the basic record shape. The included `scripts/validate.py` applies additional cross-reference, date and view checks using Python’s standard library. It is not a full JSON Schema validation engine and does not promise every conceivable malformed input produces a friendly diagnostic.

Identifiers are stable and expandable: the structural checker accepts a letter followed by at least two digits; record identifiers follow the more specific R-plus-three-or-more-digits convention documented in the schema. The starter uses 31 record IDs and 42 source IDs. Do not renumber existing records when the corpus grows. Date unions are deliberately simple; disjoint alternatives and detailed laboratory measurements require a reviewed schema extension rather than ambiguous free-form additions.
