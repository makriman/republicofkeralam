#!/usr/bin/env python3
"""Checks for staged translation files. Run from repo root. Exit 1 on failure.

UTF-8 decode; relative Markdown links resolve; manifest source revisions exist
and source paths exist at that revision; staged *.ml-en.md files put Malayalam
before English; every digit run and S### citation in the retained English also
appears in the Malayalam section; no em dash in Malayalam sections or in
staging prose; changed files limited to notes/translation-review/ (plus the
existing assignment document).
"""
import argparse, json, re, subprocess, sys
from freshness import source_freshness_errors
from pathlib import Path

parser = argparse.ArgumentParser(description="Validate pinned staging snapshots; optionally compare whole source files against a target revision.")
parser.add_argument("--target-revision", help="Explicit git revision to check for source-file changes (conservative; any change needs review).")
args = parser.parse_args()

STAGE = Path("notes/translation-review")
ML = re.compile(r"[\u0D00-\u0D7F]")
fails = []
def fail(m): fails.append(m)

for f in sorted(STAGE.rglob("*")):
    if not f.is_file() or "__pycache__" in f.parts: continue
    try:
        text = f.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        fail(f"{f}: not UTF-8"); continue
    if f.suffix == ".md":
        for target in re.findall(r"\]\(([^)\s]+)\)", text):
            if re.match(r"^[a-z]+:|^#", target): continue
            if not (f.parent / target.split("#")[0]).resolve().exists():
                fail(f"{f}: broken link {target}")
        body = re.sub(r"```.*?```|`[^`\n]*`", "", text, flags=re.S)
        if "\u2014" in body:
            fail(f"{f}: em dash outside retained source text or code") if ".ml-en." not in f.name else None
    if f.name.endswith(".ml-en.md"):
        ml_part, sep, en_part = text.partition("\n---\n")
        if not sep: fail(f"{f}: missing ML/EN separator"); continue
        h1 = re.search(r"^# (.+)$", ml_part, re.M)
        if not h1 or not ML.search(h1.group(1)): fail(f"{f}: first heading is not Malayalam")
        if ML.search(en_part): fail(f"{f}: Malayalam found in English section")
        if "\u2014" in ml_part: fail(f"{f}: em dash in Malayalam section")
        strip = lambda s: re.sub(r"<!--.*?-->|`[0-9a-f]{7,40}`|\]\([^)]*\)", "", s, flags=re.S)
        en_nums = set(re.findall(r"\d+(?:[.,]\d+)*", strip(en_part)))
        ml_nums = set(re.findall(r"\d+(?:[.,]\d+)*", strip(ml_part)))
        missing = sorted(en_nums - ml_nums)
        if missing: fail(f"{f}: numbers missing in Malayalam: {missing}")
        en_cites = set(re.findall(r"S\d{3}", en_part)); ml_cites = set(re.findall(r"S\d{3}", ml_part))
        if en_cites - ml_cites: fail(f"{f}: citations missing in Malayalam: {sorted(en_cites - ml_cites)}")

for f in sorted(STAGE.rglob("*.ml.json")):
    doc = json.loads(f.read_text(encoding="utf-8"))
    raw = subprocess.check_output(["git", "show", f"{doc['source_revision']}:{doc['source_path']}"], text=True)
    if doc["source_path"].endswith(".py"):
        for e in doc["entries"]:
            if e["key"].split("#")[1].startswith("verdict."):
                k = e["key"].split("verdict.")[1]
                if e["en"] != k.replace("_", " "): fail(f"{f}: {e['key']} label mismatch")
            else:
                frags = [x for x in re.split(r"\{\w+\}", e["en"]) if x.strip()]
                if any(x not in raw for x in frags): fail(f"{f}: {e['key']} English literal not found in generator (stale)")
            if not ML.search(e["ml"]): fail(f"{f}: {e['key']} has no Malayalam")
            if "\u2014" in e["ml"] or "\u2014" in e.get("proposed_en", ""): fail(f"{f}: {e['key']} em dash")
        continue
    src = json.loads(raw)
    if isinstance(src, dict): src = [dict(src, id="scope")]
    byid = {str(r.get("id", r.get("chapter"))): r for r in src}
    for e in doc["entries"]:
        m = re.match(r"(.+?)#(\w+)\.([\w.]+?)(?:\[(\d+)\])?$", e["key"])
        v = byid[m.group(2)]
        for k in m.group(3).split("."): v = v[k]
        if m.group(4) is not None: v = v[int(m.group(4))]
        if v != e["en"]: fail(f"{f}: {e['key']} English differs from source (stale)")
        if not ML.search(e["ml"]): fail(f"{f}: {e['key']} has no Malayalam")
        if "\u2014" in e["ml"]: fail(f"{f}: {e['key']} em dash in Malayalam")
        miss = set(re.findall(r"\d+(?:[.,]\d+)*", e["en"])) - set(re.findall(r"\d+(?:[.,]\d+)*", e["ml"]))
        if miss: fail(f"{f}: {e['key']} numbers missing in Malayalam: {sorted(miss)}")
        cm = set(re.findall(r"S\d{3}", e["en"])) - set(re.findall(r"S\d{3}", e["ml"]))
        if cm: fail(f"{f}: {e['key']} citations missing: {sorted(cm)}")

man = json.loads((STAGE / "manifest.json").read_text(encoding="utf-8"))
if args.target_revision:
    fails.extend(source_freshness_errors(man["entries"], args.target_revision))

for e in man["entries"]:
    rev = e["source_revision"]
    if subprocess.run(["git", "cat-file", "-e", f"{rev}:{e['source_path']}"], capture_output=True).returncode:
        fail(f"manifest {e['id']}: {e['source_path']} not found at {rev}")
    if e.get("staged_file") and not (STAGE / e["staged_file"]).exists():
        fail(f"manifest {e['id']}: staged file missing")
    if e["human_language_review"] != "pending" and not e.get("reviewer"):
        fail(f"manifest {e['id']}: human review marked without reviewer")
    for field in ("source_path", "source_revision", "ai_assistance", "status", "terminology_questions", "human_language_review"):
        if field not in e: fail(f"manifest {e['id']}: missing {field}")
    if e.get("staged_file") and e["staged_file"].endswith(".ml-en.md"):
        head = (STAGE / e["staged_file"]).read_text(encoding="utf-8")[:600]
        if f"source_revision: {rev}" not in head or f"source_path: {e['source_path']}" not in head:
            fail(f"manifest {e['id']}: staged header does not match manifest")

changed = subprocess.check_output(["git", "diff", "--name-only", "origin/main...HEAD"], text=True).split()
changed += subprocess.check_output(["git", "diff", "--cached", "--name-only"], text=True).split()
changed += subprocess.check_output(["git", "ls-files", "--others", "--exclude-standard"], text=True).split()
allowed = ("notes/translation-review/", "docs/work-packages/translation.md")
outside = sorted({c for c in changed if not c.startswith(allowed)})
if outside: fail(f"changes outside ownership: {outside}")

print("\n".join(fails) if fails else f"PASS: {len(man['entries'])} manifest entries; pinned snapshots checked" + (f"; whole-source freshness checked against {args.target_revision}" if args.target_revision else "; target freshness NOT checked") + "; staging files UTF-8, links, revisions, Malayalam-first order, numbers/citations, ownership.")
sys.exit(1 if fails else 0)
