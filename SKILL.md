---
name: knowframe
description: Metacognition-first framing — externalize and calibrate the LLM's own understanding on the 2x2 known/unknown (Rumsfeld) matrix before acting. Item mode (/knowframe <task | idea | decision>) maps one NEW item into a transient knowframe — off when .know/PROJECT.md exists. Project mode (bare /knowframe in a repo) builds and maintains a persisting whole-project understanding at .know/PROJECT.md, auto-pulled before non-trivial work. The knowframe is understanding only, never a plan; it feeds forward to planning and gets corrected by user or loop reflection. Invoke via /knowframe, or on "map the knowns and unknowns", "what do we know vs not know", "frame this before we start", "known unknowns", "what am I not seeing", "map this project".
---

## Info / Help command

**If this skill is invoked with the argument `info` (or `help` / `?`) and nothing else, do NOT run the skill's normal workflow.** Instead print a compact overview of this skill, then stop:

- **Name & one-liner** — the skill name and one sentence on what it does.
- **When to use** — 1–2 lines on the situations or triggers it's for.
- **Commands / usage** — every subcommand, flag, or invocation form this skill supports, one line each with a short description. If it has no subcommands, give the basic usage form(s).
- **Key inputs / outputs** — what it expects and what it produces, when not obvious.

Draw the details from this SKILL.md's own contents (plus the `references/` file for project mode), keep it scannable (headers + tight lines), and take no other action.

# Knowframe — the known/unknown matrix

**Purpose.** Externalize the LLM's own understanding of an item — what's grasped, what's guessed, what's invisible — so it can be corrected *before* anything is built on it. A plan holds only the top row (steps + risks it sees); the knowframe's unique value is the bottom row: the assumptions you don't notice you're making and the blind spots you don't know exist. It is **understanding only, never a plan** — it feeds planning. The map is a **worklist, not a deliverable**: reduce the load-bearing unknowns with cheap probes before presenting; a tidy matrix that ends the investigation is the core failure mode. Its value comes from being challenged — **don't start the task until the user gives a go-ahead.**

## Gates — run first; mandatory even on explicit invocation

1. **`.know/PROJECT.md` exists → item mode OFF**, even when invoked with a subject. Stacking a task matrix on a project knowframe measurably *dilutes* it — hard switch. Lean on the project knowframe and go straight to planning; if the task is genuinely ambiguous, surface the one load-bearing question there.
2. **Ambiguity gate.** Full framing *only* when the request hides assumptions or has contested framing. Crisp, well-specified, or reversible → say *"this is unambiguous — going straight to plan"* and hand to plan mode. Borderline → short inline matrix, never the full artifact. The default for a clear task is plan mode, not this skill. (Project mode is exempt from both gates.)

## Modes

- **Item — `/knowframe <task | idea | decision>`:** frame one **new** item with no standing project understanding (a repo with no `.know/PROJECT.md`, or anything outside a repo). Transient `.know/<slug>.md`, or inline for small items.
- **Project — bare `/knowframe` inside a repo:** one persisting `.know/PROJECT.md`, auto-pulled before non-trivial work. **READ `references/project-mode.md` before acting — never run project mode from memory of this file.**

## The matrix

|                          | **We know it**                     | **We don't know it**                |
| ------------------------ | ---------------------------------- | ----------------------------------- |
| **We know it matters**   | **Known knowns** — foundational commitments | **Known unknowns** — open questions |
| **We don't know it matters** | **Unknown knowns** — silent assumptions | **Unknown unknowns** — blind spots |

- **Known knowns — what the item fundamentally *is*.** Trace each to a source; untraceable → demote to assumption. **A wrong known-known is the deadliest error — nothing downstream questions it.**
- **Known unknowns — open questions,** conceptual first (scope, framing, un-considered adjacents), then technical. Route each to its cheapest resolver: ask / research / **check yourself** — resolve the trivially-checkable ones instead of punting them upward.
- **Unknown knowns — the assumptions you don't notice,** framing first (chosen representation, "how it's done", who it's for, static-vs-evolving). Give each a **falsifier**: a cheap self-check you can actually run (`→ check:` grep / read / run / lookup). Only-the-user-can-settle-it = `→ ask` — an open question, not a falsifier; hunt for a self-check first.
- **Unknown unknowns — blind spots you must *generate*,** not recall: smarter/more malleable approach? growth direction? unsurfaced pain points? existing tool already does part of this? what would I regret not knowing? Force a **pre-mortem** ("assume this failed or was the wrong frame — what did we miss?") and an **adjacent-expert** check. Several (aim ≥3) distinct, specific blind spots, not one generic caveat; name each one's degree (hunch vs. total void) and run the cheapest probe now — a blind spot merely listed is still a blind spot.

**No confidence scores** — an LLM confabulates its own knowledge provenance; a cheap external check beats any self-rated certainty. **Depth bar:** "It's a REST API" is inert trivia; "it's a **public** API with no existing limiter, so failure-mode and bypass outrank the limit value" is a real known-known. Dig to that level or mark the box honestly empty — never invent unknowns to fill the grid.

## Workflow (item mode)

1. **Decompose into aspects** along **≥2 lenses** (stakeholder, lifecycle, abstraction layer, failure mode) — different aspects land in different boxes, and second-lens aspects are where blind spots live. The most important step.
2. **Map aspects onto the matrix.** Splits across boxes are fine; assumptions go in unknown-knowns, never known-knowns.
3. **Interrogate, then reduce.** *"How do I actually know this?"* — "seems true" demotes to assumption. Thin box → *"am I dodging work?"* Run the cheapest probe on each load-bearing unknown **before presenting**. Name the single **load-bearing belief** — the one that, if wrong, collapses the most.
4. **Render** — file for consequential/ambiguous items, inline matrix for small ones.
5. **Present: lead with exactly ONE yes/no question** (the load-bearing assumption: "I'm assuming X — right?"). Never two, never bundled with "and"; the matrix sits below as backup. Apply corrections in place, logging quadrant migrations (e.g. unknown-known → known-known, verified via X). **No go-ahead → no start.**
6. **Feed forward.** Corrected understanding → the plan/spec: "What this implies" seeds it; residual unknowns + unverified assumptions become its named risks. Derive it fully — every load-bearing open item gets its resolution pointer, and a *decision* item also gets an **interim default** (the cheapest reversible choice) plus the evidence that would flip it: reversibility asymmetry is often the load-bearing frame. Then delete the slug file (death trigger).

**Advanced passes** — genuinely ambiguous item, or iterating a knowframe to convergence: read `references/advanced.md` (fork-check · loop mode) before step 5.

## Output format

Sections in order; a **comprehension** document — pointers ("settle the scope boundary first"), never execution steps.

```markdown
# Understanding: <item in a line>
<!-- knowframe · comprehension layer · revise in place -->

- **Captured:** <date>  ·  **Status:** draft -> (reflected / confirmed)

## 1. What I think you're actually asking for
<one honest paragraph — the gestalt, not a feature list>

## 2. Decomposed aspects
<numbered list of distinct sub-questions>

## 3. The matrix

|                            | We know it               | We don't know it            |
| -------------------------- | ------------------------ | --------------------------- |
| **We know it matters**     | <glance>                 | <glance>                    |
| **We don't know it matters** | <glance>               | <glance>                    |

### Known knowns — established
- <foundational commitment>

### Known unknowns — open questions (conceptual first)
- <question> -> ask / research / check yourself

### Unknown knowns — assumptions I'm making (flag any that are wrong)
- *Assuming* <assumption> `[load-bearing]` → check: <self-check>   ·   → ask: <if only the user can settle it>

### Unknown unknowns — blind spots & directions to probe
- <blind spot> -> probe / research

**Load-bearing assumption:** <the one belief that, if wrong, breaks the most>

## 4. What this implies (feed-forward — pointers, not steps)
*Derived, not hand-picked: load-bearing items still open = what to resolve first, each with its cheapest resolution route. Decisions also get an interim default + what would flip it.*
- <highest-leverage gap -> how to resolve it>

## Revision log
*Quadrant migrations only, ~1 line per refresh. (Item-mode only; project mode splits it — see references/project-mode.md.)*
- <date> — initial draft (pre-reflection)
```

Rank the feed-forward by **load-bearing + still unresolved**. Tag `[load-bearing]` sparingly (≤3 — if everything is load-bearing you haven't found the spine); the single most load-bearing one gets the callout. Glance-table = map; subsections = depth.

## Mechanics

- Write to `.know/<slug>.md`; create `.know/` if absent; gitignore `.know/` in repos.
- One file per item, overwritten in place on correction; never versioned copies.
- **Death trigger:** once fed forward (plan approved / spec landed / abandoned), delete the slug file same session, folding residual unknowns into the spec's risks.
- File for non-trivial/ambiguous/loop items; inline matrix otherwise — match depth to stakes, never turn a quick request into ceremony.
- Dates: `Captured` / revision-log dates are the freshness mechanism (exempt from any no-timestamps house rule); nothing else carries dates or activity narrative.

## References & measurement

- [references/project-mode.md](references/project-mode.md) — **mandatory read for project mode**.
- [references/advanced.md](references/advanced.md) — fork-check · loop mode.
- [references/examples.md](references/examples.md) — worked knowframes; read when unsure whether a box is deep enough (the depth model lives there, not in the depth-bar line above).
- [evals/README.md](evals/README.md) — blind /30 harness; run project-mode track on ≥2 repos.

## Activation: explicit only (by design)

No auto-triggering for item mode — broad per-task framing dilutes more than it protects, and knowing when to SKIP is the hard part. The single automatic trigger is project-mode auto-pull (CLAUDE.md reads `.know/PROJECT.md` before non-trivial work). Don't add item-mode auto-triggering.
