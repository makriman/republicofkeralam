#!/usr/bin/env python3
"""Assemble a Malayalam-first staging file: header + Malayalam draft + retained English.

Usage: assemble.py MANIFEST_ID SOURCE_PATH ML_FRAGMENT OUT_PATH
Relative Markdown links in the retained English are rewritten so they resolve
from the staging location; the manifest records this. Text is otherwise unchanged.
Run from the repository root.
"""
import os, re, subprocess, sys

mid, src, frag, out = sys.argv[1:5]
rev = subprocess.check_output(["git", "rev-parse", "origin/main"], text=True).strip()
english = subprocess.check_output(["git", "show", f"{rev}:{src}"], text=True)
ml = open(frag, encoding="utf-8").read().rstrip() + "\n"

def rewrite(text):
    def fix(m):
        target = m.group(2)
        if re.match(r"^[a-z]+:|^#|^/", target):
            return m.group(0)
        path, _, anchor = target.partition("#")
        absolute = os.path.normpath(os.path.join(os.path.dirname(src), path))
        rel = os.path.relpath(absolute, os.path.dirname(out))
        return f"{m.group(1)}({rel}{'#' + anchor if anchor else ''})"
    return re.sub(r"(\[[^\]]*\])\(([^)\s]+)\)", fix, text)

header = f"""<!--
source_path: {src}
source_revision: {rev}
manifest_id: {mid}
ai_assistance: Malayalam draft prepared with AI assistance; English retained from source.
human_language_review: pending
specialist_review: pending
model_review: model self-check only (see manifest); not human approval
-->

"""
note_ml = f"> പരിഭാഷാ കരട്. AI സഹായത്തോടെ തയ്യാറാക്കിയത്. മലയാള ഭാഷാപരിശോധനയും വിഷയവിദഗ്ധപരിശോധനയും ബാക്കിയുണ്ട്. മൂലപാഠം: `{src}` @ `{rev[:7]}`.\n\n"
note_en = f"> Retained English source text from `{src}` @ `{rev[:7]}`. Wording unchanged; relative links rewritten to resolve from this staging path.\n\n"
lines = ml.split("\n", 1)
body = lines[0] + "\n\n" + note_ml + lines[1].lstrip("\n")
elines = english.split("\n", 1)
ebody = elines[0] + "\n\n" + note_en + elines[1].lstrip("\n")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w", encoding="utf-8") as f:
    f.write(header + rewrite(body) + "\n---\n\n" + rewrite(ebody))
