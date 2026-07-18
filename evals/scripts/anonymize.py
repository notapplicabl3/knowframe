#!/usr/bin/env python3
"""Anonymize a /knowframe eval run: shuffle each case's artifacts into anon/<case>/NN.md,
scrub literal variant labels, and record label->variant maps. Usage: anonymize.py <run_dir>"""
import os, re, sys, csv, random, glob

run = sys.argv[1] if len(sys.argv) > 1 else "."
OUT, ANON, MAPS = f"{run}/out", f"{run}/anon", f"{run}/maps"
random.seed(42)
scrub = re.compile(r"variant[:\s]+[a-z0-9_-]+", re.IGNORECASE)

if not os.path.isdir(OUT):
    sys.exit(f"no out/ dir at {OUT}")
os.makedirs(MAPS, exist_ok=True)

cases = sorted(d for d in os.listdir(OUT) if os.path.isdir(f"{OUT}/{d}"))
for case in cases:
    files = sorted(glob.glob(f"{OUT}/{case}/*.md"))
    # filename convention: <variant>_r<rep>.md
    parsed = []
    for p in files:
        m = re.match(r"(.+)_r(\d+)\.md$", os.path.basename(p))
        if m:
            parsed.append((m.group(1), m.group(2), p))
    random.shuffle(parsed)
    d = f"{ANON}/{case}"
    os.makedirs(d, exist_ok=True)
    rows = []
    for i, (variant, rep, p) in enumerate(parsed, start=1):
        label = f"{i:02d}"
        txt = scrub.sub("this submission", open(p).read())
        open(f"{d}/{label}.md", "w").write(txt)
        rows.append((label, variant, rep))
    with open(f"{MAPS}/{case}.csv", "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["label", "variant", "rep"]); w.writerows(rows)
    print(f"{case}: {len(rows)} anonymized")
print(f"cases: {len(cases)}")
