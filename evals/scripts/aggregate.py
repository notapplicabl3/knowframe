#!/usr/bin/env python3
"""Aggregate a /know eval run into a benchmark (mean +/- stddev, delta vs baseline).
Joins scores/<case>.md with maps/<case>.csv. Usage: aggregate.py <run_dir>"""
import os, re, sys, csv, glob, statistics

run = sys.argv[1] if len(sys.argv) > 1 else "."
SCORES, MAPS = f"{run}/scores", f"{run}/maps"

def parse_scores(path):
    res = {}
    for line in open(path):
        if "|" not in line:
            continue
        parts = [p.strip() for p in line.strip().strip("|").split("|")]
        if len(parts) < 8 or not re.fullmatch(r"\d{1,2}", parts[0]):
            continue
        try:
            res[parts[0].zfill(2)] = sum(int(parts[i]) for i in range(1, 7))
        except ValueError:
            continue
    return res

def parse_map(path):
    with open(path) as f:
        return {r["label"].zfill(2): r["variant"] for r in csv.DictReader(f)}

# variant -> list of per-rep totals (pooled across all cases)
pooled = {}
per_case = {}
for mp_path in sorted(glob.glob(f"{MAPS}/*.csv")):
    case = os.path.splitext(os.path.basename(mp_path))[0]
    sc_path = f"{SCORES}/{case}.md"
    if not os.path.exists(sc_path):
        print(f"!! missing scores for {case}"); continue
    scores, mp = parse_scores(sc_path), parse_map(mp_path)
    per_case[case] = {}
    for label, total in scores.items():
        v = mp.get(label)
        if v is None:
            continue
        pooled.setdefault(v, []).append(total)
        per_case[case].setdefault(v, []).append(total)

def line(vals):
    m = statistics.mean(vals)
    s = statistics.stdev(vals) if len(vals) > 1 else 0.0
    return m, s

variants = sorted(pooled)
base = "baseline" if "baseline" in variants else variants[0]
lines = ["# benchmark\n", f"baseline = `{base}`\n", "## per-case mean (/30)\n",
         "| case | " + " | ".join(variants) + " |", "|" + "---|" * (len(variants) + 1)]
for case in sorted(per_case):
    row = [f"{statistics.mean(per_case[case][v]):.1f}" if per_case[case].get(v) else "-" for v in variants]
    lines.append(f"| {case} | " + " | ".join(row) + " |")

lines += ["\n## treatment vs matched baseline (paired by case)\n",
          "| variant | mean | stddev | n | baseline (same cases) | delta |", "|---|---|---|---|---|---|"]
for v in variants:
    if v == base:
        continue
    cases_v = [c for c in per_case if per_case[c].get(v)]
    vvals = [x for c in cases_v for x in per_case[c][v]]
    bvals = [x for c in cases_v for x in per_case[c].get(base, [])]
    if not vvals or not bvals:
        continue
    vm, vs = line(vvals)
    bm = statistics.mean(bvals)
    lines.append(f"| {v} | {vm:.2f} | {vs:.2f} | {len(vvals)} | {bm:.2f} | {vm - bm:+.2f} |")
bm_all, bs_all = line(pooled[base])
lines.append(f"\nbaseline overall: {bm_all:.2f} ± {bs_all:.2f} (n={len(pooled[base])})")

out = "\n".join(lines) + "\n"
open(f"{run}/benchmark.md", "w").write(out)
print(out)
