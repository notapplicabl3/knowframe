# References compression — Codex-implemented, two-track A/B, 2026-07-18

**Question:** can the three reference files (`project-mode.md` 7.4K, `advanced.md` 2.8K, `examples.md` 12.0K) be compressed without behavioral loss?

**Method — full trio × swarm composition:** Fable (main loop) wrote the compression contract (preserve every threshold, imperative, gate, path; rationale to ≤1 clause per rule; cut examples.md's redundant Example 2); **Codex GPT 5.5 xhigh implemented** the compression in a scratchpad (trio coder leg — judged for fidelity and attribution before any testing; the dispatch zombied per the known backgrounded-job behavior and was resolved by the quiet-tree probe); a **separate Fable instance designed the exam** from the installed contracts, blind to the candidates. Two tracks: **A (procedural)** — 6 mid-run scenarios with MUST/MUST-NOT action keys over project-mode + advanced (confirm gate, graduation/ownership trap, stale auto-pull self-heal, LOG split at session close, fork-check converge/diverge, loop-pass validity); **B (exemplar)** — 2 item-mode framing tasks where only the examples.md variant differs, artifacts judged on `rubric.md` (/30). 32 producers + 16 blind judges, seeded anonymization, 2 judges per unit, MUST-NOT cap.

## Result

| track | current | compressed | note |
|---|---|---|---|
| A /10 (n=24) | 9.46 ± 0.91 | **9.58 ± 0.64** | compressed wins/ties 5 of 6 incl. the trap; better on the hardest scenario (loop validity 8.5 vs 7.75) |
| B /30 (n=8) | 26.63 ± 1.93 | **26.75 ± 2.11** | parity within judge noise (vague case +1.25, decision case −1.0) |

Zero MUST-NOT violations in either variant. Installed: 16,716 bytes vs 22,241 (−25%).

## Reading

- Third consecutive campaign confirming the pattern: rules carry behavior; rationale compression is safe when every threshold/imperative survives verbatim-in-meaning.
- Cutting a whole worked example (Example 2) cost nothing measurable — the remaining exemplars carry the depth model (Track B parity; the vague-item case even improved).
- Caveats: n=2 reps per cell; Track B's decision case slightly favored the fuller examples (−1.0, sub-noise) — if decision-framing quality ever drifts, restore a decision-flavored example first.

**Action taken:** all three compressed files installed under `references/`; filenames unchanged so every route and link held without edits.
