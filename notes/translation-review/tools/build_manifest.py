#!/usr/bin/env python3
"""Write manifest.json for staged translation entries. Run from repo root."""
import json, subprocess
from pathlib import Path

REV = subprocess.check_output(["git", "rev-parse", "origin/main"], text=True).strip()
BRANCH_REV = "1e8d0ef3e16b5b1032d02cb0caf6931fa2309895"
AI = "Malayalam drafted with AI assistance (language model). No human translator. English retained verbatim from source except staging-relative link paths."
MODEL = {"by": "AI model (self-check, not human approval)",
         "checked": ["UTF-8", "relative links resolve", "Malayalam-first order", "digits and S### citations preserved",
                     "no em dash in Malayalam editorial text", "qualifiers (approximately, proposed, not inspected, pending) retained"],
         "against_revision": REV}
PENDING = {"human_language_review": "pending", "specialist_review": "pending", "reviewer": None}

def entry(mid, path, kind, staged, status, terms, rev=REV, extra=None):
    e = {"id": mid, "source_path": path, "source_id": None, "source_revision": rev, "kind": kind,
         "staged_file": staged, "malayalam": "staged_file: Malayalam section first" if staged else None,
         "retained_english": "staged_file: English section second, verbatim" if staged else None,
         "ai_assistance": AI if staged else None, "status": status, "terminology_questions": terms,
         "model_review": MODEL if staged else None, **PENDING}
    if extra: e.update(extra)
    return e

E = [
 entry("TR-B1-001", "README.md", "hand_maintained", "batch-1/TOP_LEVEL_REVIEW.md", "already_bilingual_reviewed_by_model", ["R1 cutoff wording", "R2 ഭൂമിശാസ്ത്രം vs ഭൂവിജ്ഞാനീയം", "R3 citation sentence"],
       extra={"ai_assistance": "Existing bilingual text is an AI-assisted draft (stated in README). This entry adds model review notes only."}),
 entry("TR-B1-002", "CONTRIBUTING.md", "hand_maintained", "batch-1/TOP_LEVEL_REVIEW.md", "already_bilingual_reviewed_by_model", ["C1 ജീവനുള്ള vs ജീവിച്ചിരിക്കുന്ന"],
       extra={"ai_assistance": "Existing bilingual text is an AI-assisted draft (stated in CONTRIBUTING). Model review notes only."}),
 entry("TR-B1-003", "docs/work-packages/translation.md", "hand_maintained", "batch-1/TOP_LEVEL_REVIEW.md", "already_bilingual_reviewed_by_model", [], rev=BRANCH_REV,
       extra={"ai_assistance": "Existing bilingual assignment document. Model review notes only."}),
 entry("TR-B1-004", "docs/DATA_MODEL.md", "hand_maintained", "batch-1/docs/DATA_MODEL.ml-en.md", "draft_translation", ["Q1 generated", "manifestation/edition terms (Q5)", "knowledge-graph left in English"]),
 entry("TR-B1-005", "docs/EVIDENCE_POLICY.md", "hand_maintained", "batch-1/docs/EVIDENCE_POLICY.ml-en.md", "draft_translation", ["Q4 ആരോപിത", "Q9 Kollam plates", "errata/corrigenda left in English"]),
 entry("TR-B1-006", "docs/RIGHTS_AND_ETHICS.md", "hand_maintained", "batch-1/docs/RIGHTS_AND_ETHICS.ml-en.md", "draft_translation", ["license laundering idiom rendered as ലൈസൻസ് “വെളുപ്പിക്കൽ”; confirm register", "paywall/rate limit left in English with gloss"]),
 entry("TR-B1-007", "docs/CHRONOLOGY.md", "hand_maintained", "batch-1/docs/CHRONOLOGY.ml-en.md", "draft_translation", ["Q6 ക്രി.വ./പൊ.യു.", "Q7 calibration", "Q8 stratigraphic", "Q11 detrital", "Q12 chronostratigraphic"]),
 entry("TR-B1-008", "notes/README.md", "hand_maintained", "batch-1/notes/README.ml-en.md", "draft_translation", []),
 entry("TR-B1-009", "templates/research-note.md", "hand_maintained", "batch-1/templates/research-note.ml-en.md", "draft_translation", ["'pending' placeholder rendered ബാക്കി (pending); confirm"]),
 entry("TR-B1-010", ".github/ISSUE_TEMPLATE/correction.md", "hand_maintained", "batch-1/github/ISSUE_TEMPLATE/correction.ml-en.md", "draft_translation", ["front-matter name/about change needs owner decision"]),
 entry("TR-B1-011", ".github/ISSUE_TEMPLATE/source.md", "hand_maintained", "batch-1/github/ISSUE_TEMPLATE/source.ml-en.md", "draft_translation", []),
 entry("TR-B1-012", ".github/PULL_REQUEST_TEMPLATE.md", "hand_maintained", "batch-1/github/PULL_REQUEST_TEMPLATE.ml-en.md", "draft_translation", []),
]
for mid, p in [("TR-B1-013", "NOTICE.md"), ("TR-B1-014", "RELEASE_NOTES.md"), ("TR-B1-015", "IMPORT_PROVENANCE.md"), ("TR-B1-016", "VALIDATION.md"), ("TR-B1-017", "LICENSE.md")]:
    E.append(entry(mid, p, "hand_maintained", None, "untranslated_reviewed_for_staleness", [], extra={"notes": "See batch-1/TOP_LEVEL_REVIEW.md; translation deferred to batch 3.", "model_review": {"by": "AI model", "checked": ["staleness", "em dashes"], "against_revision": REV}}))

out = Path("notes/translation-review/manifest.json")
old = json.loads(out.read_text(encoding="utf-8")) if out.exists() else {"entries": []}
keep = [e for e in old["entries"] if not e["id"].startswith("TR-B1-")]
data = {"schema": "translation-staging-manifest/0.1",
        "note": "Staging only. Nothing here is integrated into canonical data or generated pages. Human Malayalam review: none performed.",
        "base_revision": REV, "entries": E + keep}
out.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(len(data["entries"]), "entries")
