#!/usr/bin/env python3
"""Render readable Malayalam-first previews from batch-*/X.ml.json. Run from repo root.

The previews are review aids, not generated archive pages. Each record shows
the Malayalam block first and the retained English block second.
"""
import json, re, sys
from pathlib import Path

LABELS = {
 "title": ("ശീർഷകം", "Title"), "display_window": ("കാലജാലകം", "Display window"),
 "central_question": ("കേന്ദ്രചോദ്യം", "Central question"),
 "established_in_this_pass": ("ഈ ഘട്ടത്തിൽ സ്ഥാപിച്ചത്", "Established in this pass"),
 "limitations": ("പരിമിതികൾ", "Limitations"), "research_tasks": ("ഗവേഷണജോലികൾ", "Research tasks"),
 "claim": ("അവകാശവാദം", "Claim"), "caveat": ("മുന്നറിയിപ്പ്", "Caveat"),
 "date.original_expression": ("തീയതി (സ്രോതസ്സുപ്രയോഗത്തിന്റെ വിശദീകരണം)", "Date (original expression)"),
 "date.datum": ("ആധാരം", "Datum"), "authoring": ("രചനാരീതി", "Authoring"), "rights": ("അവകാശങ്ങൾ", "Rights"),
 "inspection_note": ("പരിശോധനാക്കുറിപ്പ്", "Inspection note"),
}
for path in sys.argv[1:]:
    doc = json.loads(Path(path).read_text(encoding="utf-8"))
    groups = {}
    for e in doc["entries"]:
        m = re.match(r"(.+?)#(\w+)\.([\w.]+?)(?:\[(\d+)\])?$", e["key"])
        groups.setdefault(m.group(2), []).append((m.group(3), e))
    src = doc["source_path"]
    L = [f"<!-- preview rendered by tools/render_data.py from {Path(path).name}; source_path: {src}; source_revision: {doc['source_revision']} -->", "",
         f"# മലയാളം ആദ്യം: `{src}` ദ്വിഭാഷാ കരട് / Malayalam-first preview",
         "", f"AI സഹായത്തോടെയുള്ള കരട്. മനുഷ്യ ഭാഷാപരിശോധന: ബാക്കി. വിഷയവിദഗ്ധപരിശോധന: ബാക്കി. Source revision `{doc['source_revision'][:7]}`.",
         "", "AI-assisted draft. Human language review: pending. Specialist review: pending. Canonical IDs are unchanged; the English below is the retained source text.", ""]
    for rid, fields in groups.items():
        L.append(f"## {rid}")
        L.append("")
        for lang, idx in (("ml", 0), ("en", 1)):
            L.append("**മലയാളം**" if lang == "ml" else "**English (retained)**")
            L.append("")
            last = None
            for f, e in fields:
                label = LABELS.get(f, (f, f))[idx]
                if f == "research_tasks":
                    if last != f: L.append(f"- {label}:")
                    L.append(f"  - {e[lang]}")
                else:
                    L.append(f"- {label}: {e[lang]}")
                last = f
            L.append("")
    out = Path(path).with_name(Path(path).name.replace(".ml.json", ".ml-en.preview.md"))
    out.write_text("\n".join(L), encoding="utf-8")
    print(out)
