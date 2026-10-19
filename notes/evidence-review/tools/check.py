#!/usr/bin/env python3
"""Local checks for notes/evidence-review. Run from the repository root with python3."""
import json, re, sys, pathlib, subprocess

ROOT = pathlib.Path(__file__).resolve().parents[3]
HERE = ROOT / "notes" / "evidence-review"
errors = []

def load_at_base(path, base):
    try:
        out = subprocess.run(["git", "show", f"{base}:{path}"], cwd=ROOT, capture_output=True, check=True)
        return json.loads(out.stdout.decode("utf-8"))
    except (subprocess.CalledProcessError, OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"Cannot load declared base {base!r}, path {path!r}: {exc}") from exc

def main():
    global errors
    errors = []
    files = sorted(p for p in HERE.rglob("*") if p.is_file() and "__pycache__" not in p.parts)
    for p in files:
        raw = p.read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            errors.append(f"{p}: not UTF-8"); continue
        if "\u2014" in text:
            errors.append(f"{p}: contains an em dash")
        if p.suffix == ".json":
            try: json.loads(text)
            except ValueError as e: errors.append(f"{p}: invalid JSON ({e})")
        if p.suffix == ".md":
            for target in re.findall(r"\]\(([^)#\s]+)", text):
                if re.match(r"[a-z]+://", target): continue
                if not (p.parent / target).exists():
                    errors.append(f"{p}: broken relative link {target}")

    reviews = json.loads((HERE / "claim-reviews.json").read_text(encoding="utf-8"))
    corr = json.loads((HERE / "proposed-corrections.json").read_text(encoding="utf-8"))
    base = reviews["base_revision"]
    if corr["base_revision"] != base:
        errors.append("Claim reviews and corrections declare different base revisions")
    known = {}
    for name, path in (("records", "data/records.json"), ("sources", "data/sources.json"), ("audit", "data/audit.json"), ("periods", "data/periods.json")):
        try:
            data = load_at_base(path, base)
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 1
        if isinstance(data, dict):
            data = next((v for v in data.values() if isinstance(v, list)), [])
        known[name] = {x["id"] for x in data if isinstance(x, dict) and "id" in x}
    proposed = {s["key"] for s in reviews["proposed_sources"]}
    pc_ids = {c["id"] for c in corr["corrections"]}
    unresolved = set(re.findall(r"^\| (U-\d+) \|", (HERE / "UNRESOLVED.md").read_text(encoding="utf-8"), re.M))
    for c in reviews["claims"]:
        for kind, ids in c["stable_ids"].items():
            pool = proposed if kind == "proposed_sources" else known.get(kind, set())
            for i in ids:
                if i not in pool: errors.append(f"{c['id']}: unknown {kind} id {i}")
        for k in ("title", "claim_under_review", "finding"):
            if list(c[k].keys())[:2] != ["ml", "en"]: errors.append(f"{c['id']}: {k} not Malayalam first")
        for r in c["proposed_corrections"]:
            if r not in pc_ids: errors.append(f"{c['id']}: unknown correction {r}")
        for u in c["unresolved"]:
            if u not in unresolved: errors.append(f"{c['id']}: unknown unresolved item {u}")
    for c in corr["corrections"]:
        for ch in c["changes"]:
            f, t = ch["file"], ch.get("target_id")
            kind = {"data/records.json": "records", "data/sources.json": "sources", "data/audit.json": "audit"}.get(f)
            if kind and ch["op"] not in ("add_entry", "proposal") and t not in known[kind]:
                errors.append(f"{c['id']}: unknown target {t} in {f}")

    if errors:
        print("\n".join(errors)); return 1
    print(f"ok: {len(files)} files, {len(reviews['claims'])} claims, {len(pc_ids)} corrections, {len(unresolved)} unresolved items")
    return 0

if __name__ == "__main__":
    sys.exit(main())
