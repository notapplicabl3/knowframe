# `/knowframe` evaluation harness

Measures whether `/knowframe` actually improves downstream framing+plan quality over not using it, in the two scopes the skill operates in. Output is judgment-quality, so this is a **qualitative + benchmark** eval (blind LLM judge on a /30 rubric, reported as mean ± stddev with a delta vs baseline) — not deterministic assertions.

## What it measures (two tracks)

| Track | Compares | Question |
|---|---|---|
| `project_mode` | `baseline` vs `grounded` | Does grounding in a repo's `.know/PROJECT.md` beat an ungrounded pass? |
| `item_mode` | `baseline` vs `know-item` | On a genuinely new, ungrounded item, does running the matrix beat going straight to plan — and does the gate correctly *skip* a crisp item? |

These mirror the skill's two modes. Note there is deliberately **no "both" variant** — the skill forbids stacking item-mode on an existing project knowframe, so the harness doesn't test it.

## Cases

See `evals.json`. `project_mode` prompts are **repo-agnostic** (they self-bind to whatever target repo you point them at — no hardcoded paths). `item_mode` prompts are self-contained (idea / decision / crisp task) and need no repo.

## How to run (agent-orchestrated)

1. **project_mode setup:** pick a `TARGET_REPO` that has a built `.know/PROJECT.md` (run bare `/knowframe` in it first if not). 
2. **Generate.** For each case × variant × `default_n` reps, spawn an *independent* sub-agent (so reps are real samples) with the variant file (`variants/<variant>.md`) + the case prompt. The `know-item` variant applies the skill at `../SKILL.md`. Write each artifact to `runs/<label>/out/<case_id>/<variant>_r<rep>.md`. Keep reps independent and variants blind to each other.
3. **Anonymize:** `python3 scripts/anonymize.py runs/<label>` → shuffles + scrubs variant labels into `anon/`, writes `maps/`.
4. **Judge:** for each case, spawn one blind grader (prompt: `grader.md` + `rubric.md`) over its anonymized artifacts → `scores/<case_id>.md`.
5. **Aggregate:** `python3 scripts/aggregate.py runs/<label>` → `benchmark.md` (per-variant mean ± stddev, delta vs baseline).

## Generalization / overfitting check (important)

The skill's behavioral rules were tuned on **one** repo. Before trusting them, run the `project_mode` track against **≥2 different repos** and confirm the `grounded − baseline` delta holds. A delta that appears on repo A but vanishes on repo B means the rule is overfit, not real.

## Caveats (read before believing a result)

- **Judge noise ≈ 1–2 points** on /30. Sub-1-point deltas are nothing; trust aggregates (many samples), not single cases.
- **Low n is noisy.** `default_n: 3` per cell still has real spread; bump it for a number you'd stake a claim on.
- **One judge per case** here — inter-judge variance is not captured. For a stronger result, use multiple graders and average.
- This grades *framing/plan quality*, not shipped-code correctness.

## Recorded results

- [`results/loop-vs-prompt-2x2_2026-06-27.md`](results/loop-vs-prompt-2x2_2026-06-27.md) — 2×2 knowframe × mode (prompt vs loop), opus, n=9/cell. Headline: grounding is ~flat in a single prompt but compounds in a loop (best = grounded+loop, 90.0%).
- [`results/concise-vs-current_2026-07-17.md`](results/concise-vs-current_2026-07-17.md) — item-mode A/B of a ~31% smaller SKILL.md, n=3/cell, 2 judges/case. Headline: concise wins 27.5 vs 25.2 (/30) — interim-default + flip-condition rule drives it; extra rationale prose cost signal-to-noise. Concise installed.
