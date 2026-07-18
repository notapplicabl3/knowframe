# Benchmark: knowframe × mode (2×2) — prompt vs loop

**Date:** 2026-06-27 · **Model:** opus (fixed) · **n:** 3 reps × 3 tasks = 9 per cell · **Judge:** 1 blind opus grader per task, /30 rubric (`../rubric.md`)

## Question

Does grounding in a project knowframe (`.know/PROJECT.md`) improve framing+plan quality, and does that differ between a **single prompt** and an **investigation-driven loop**?

## Method

2×2 design — knowframe {ignore · use} × mode {prompt single-pass · loop ≤4 investigation passes} = 4 variants, each run on 3 shopify-tools tasks (vague / crisp / complex), n=3. 36 artifacts, blind-anonymized and judged /30. Target repo: `~/shopify-tools` (has a built `.know/PROJECT.md`). Loop variants iterate (drive a load-bearing unknown via a real probe each pass) then emit only the final artifact.

## Results — per variant (n=9)

| variant | mean /30 | mean % | stddev /30 | stddev % |
|---|---|---|---|---|
| baseline_prompt | 25.11 | 83.7% | 1.83 | 6.1 |
| grounded_prompt | 24.89 | 83.0% | 2.32 | 7.7 |
| baseline_loop | 25.78 | 85.9% | 1.86 | 6.2 |
| **grounded_loop** | **27.00** | **90.0%** | 1.87 | 6.2 |

### 2×2 cell means

**/30**
| | prompt | loop |
|---|---|---|
| ignore knowframe | 25.11 | 25.78 |
| use knowframe | 24.89 | **27.00** |

**%**
| | prompt | loop |
|---|---|---|
| ignore knowframe | 83.7% | 85.9% |
| use knowframe | 83.0% | **90.0%** |

### Contrasts

| contrast | Δ /30 | Δ (percentage points) |
|---|---|---|
| knowframe effect **in prompts** | −0.22 | −0.74pp |
| knowframe effect **in loops** | +1.22 | +4.07pp |
| loop effect (ignore knowframe) | +0.67 | +2.22pp |
| loop effect (use knowframe) | **+2.11** | **+7.04pp** |
| MAIN effect — knowframe (use − ignore) | +0.50 | +1.67pp |
| MAIN effect — loop (loop − prompt) | +1.39 | +4.63pp |
| **INTERACTION (knowframe × loop)** | **+1.44** | **+4.81pp** |

### Per-case means (/30 and %)

| task | baseline_prompt | grounded_prompt | baseline_loop | grounded_loop |
|---|---|---|---|---|
| t1_vague | 24.0 / 80.0% | 22.7 / 75.6% | 25.0 / 83.3% | 27.3 / 91.1% |
| t2_crisp | 26.7 / 88.9% | 25.3 / 84.4% | 24.7 / 82.2% | 27.0 / 90.0% |
| t3_complex | 24.7 / 82.2% | 26.7 / 88.9% | 27.7 / 92.2% | 26.7 / 88.9% |

## Findings

1. **The knowframe is ~flat in a single prompt (−0.22 / −0.7pp), but pays off in a loop (+1.22 / +4.1pp).** The story is the **positive interaction (+1.44 / +4.8pp)**: grounding's value is unlocked by iteration, not one-shot priming.
2. **Best config is knowframe + loop** (27.0 / 90.0%), beating grounded single-pass by +2.11 (+7.0pp) — the one contrast that clears ~2σ.
3. **Looping helps overall** (+1.39 / +4.6pp main effect) and **helps more when grounded** (+2.11 vs +0.67).
4. **Loop artifacts were shorter yet scored higher** (grounded_loop 85 lines vs grounded_prompt 91), i.e. investigation distilled, not padded — the convergence-by-migration design working.

## Caveats

- Only the **+2.11 (loop helps when grounded)** clears ~2σ. The **+1.22 knowframe-in-loops** and **+1.44 interaction** are suggestive (~1.4σ) at n=9 / single judge / opus-only.
- The interaction is **carried by 2 of 3 tasks**: on `t3_complex` it reverses (baseline_loop 27.7 > grounded_loop 26.7) — on a richly-specified hard task the agent investigates deeply regardless and the knowframe adds little.
- The **single-prompt knowframe came out flat**, weaker than the prior 96-run pooled +2.1 — that earlier figure pooled both models and concentrated on low-complexity/bad-clarity cells; this is opus-only on different tasks, where opus's strong solo framing leaves little headroom. Not a clean replication.
- Grades **framing/plan quality, not shipped-code correctness**.

## Implication

Validates **loop-mode as substance, not packaging**: it is the mode where grounding compounds. Supports recommending **grounded + loop** for deep/consequential work, while treating single-pass grounding as near-neutral on a strong model.
