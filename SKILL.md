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

## Core principle

This skill **externalizes the LLM's own understanding** of an item so it can be corrected *before* anything is built on it — a **knowframe**: what you grasp, what you're guessing, and what you can't yet see. It beats going straight to a plan because a plan lives entirely in the top row ("we know it matters") — it can hold steps and the risks it sees, but structurally *cannot* hold the bottom row: the assumptions it doesn't notice it's making and the blind spots it doesn't know exist. Surfacing that bottom row is the whole point. Where a tool like `/understand` maps *what's here*, this skill maps the opposite-facing half — *what's **not** here, and to what degree*: the unstated framing, the missing requirement, the approach you haven't considered.

**The map is for digging, not for closing — and only pays off if challenged.** A tidy matrix that *feels* like understanding and quietly ends the investigation is this skill's core failure mode; the bottom row is a worklist, not a confession. The knowframe is done when the load-bearing unknowns have actually been *reduced* (or honestly marked residual with their degree named), and its value comes entirely from you (or a loop pass) pushing back on it — rubber-stamped, it's ceremony. Map it, surface it, get it corrected, and **don't start the task until there's a go-ahead.**

## Gates — run these before anything below

**First gate — a pre-existing project knowframe turns item-mode OFF.** If `.know/PROJECT.md` exists, do **not** run a per-task matrix, *even when `/knowframe` is invoked with a subject*. The project knowframe is your grounding: lean on it and go straight to planning (surface the one load-bearing question there if the task is genuinely ambiguous). Item-mode is for **new** items only — no standing project understanding to draw on (a repo with no `.know/PROJECT.md`, or anything outside a repo). Stacking a task matrix on a project knowframe was measured to *dilute* it, never improve it — a hard switch, not a judgment call.

**Second gate — ambiguity (vs. plan mode); mandatory even on explicit invocation.** Run the full item-mode framing *only* when the request genuinely **hides assumptions or has contested framing** — you could read it several ways, the real goal is unstated, or you'd otherwise build on unexamined ground. If the task is crisp, well-specified, or reversible, **do not run the matrix**: say *"this is unambiguous — going straight to plan"* and hand to plan mode. Borderline cases get a short inline matrix, never the full artifact. `/knowframe` feeds *into* planning; it never replaces it — **the default for a clear task is plan mode, not this skill.** (Project mode is exempt from both gates: a bare `/knowframe` in a repo isn't framing a task.)

## Two modes

- **Item mode — `/knowframe <task | idea | decision>`.** Frames a single **new** forward-looking item. Writes a transient `.know/<slug>.md` (or inline for small items). Everything below through *Knowframe mechanics*.
- **Project mode — bare `/knowframe` inside a repo.** Builds and maintains one persisting understanding of the *whole project* at `.know/PROJECT.md`, auto-pulled before non-trivial work. **READ `references/project-mode.md` before doing anything in this mode — never run project mode from memory of this file alone.**

## The four quadrants

The matrix is a thinking tool, not a form to fill. Each box catches a different *kind* of thing:

|                          | **We know it**                                          | **We don't know it**                                         |
| ------------------------ | ------------------------------------------------------- | ------------------------------------------------------------ |
| **We know it matters**   | **Known knowns** — the foundational commitments the understanding rests on. | **Known unknowns** — open questions and undefined framing we're aware of. |
| **We don't know it matters** | **Unknown knowns** — framing/style/structure assumptions baked in silently. | **Unknown unknowns** — blind spots, smarter approaches, growth direction. |

- **Known knowns — what the item fundamentally *is*.** Honesty-check each: *genuinely established* or *assumed-but-feels-certain*? Anything you can't trace to a source is demoted to an assumption. **A wrong known-known is the deadliest error — nothing downstream questions it.**
- **Known unknowns — the open questions.** Lead with conceptual ones (undefined scope, open framing, un-considered adjacents), then technical. Route each to its cheapest resolver: ask the user when they hold the answer, research when it's discoverable — and **resolve the trivially-checkable ones yourself** (a grep, a file read) instead of punting them upward.
- **Unknown knowns — the assumptions you don't notice.** The dangerous box for an LLM. Lead with *framing* assumptions (chosen representation, "this is just how it's done," who the output is for, treating an evolving thing as static), then concrete ones. Give each a **falsifier** — but only a real one: a cheap *self-check you can actually run* (`→ check:` grep / read / run / lookup). If only the user can settle it, mark it `→ ask` — that's an open question, not a falsifier; hunt for a self-check before settling for an ask.
- **Unknown unknowns — the blind spots.** The highest-value box, and the one you can't fill by staring — *generate* it by probing several angles: a **smarter or more malleable approach**? Where will this **grow**? What **pain points haven't surfaced**? **Does an existing skill, tool, or product already do part of this?** What would I **regret not knowing**? Then force two prompts: a **pre-mortem** ("assume this went wrong, or was the wrong frame entirely — what did we miss?") and an **adjacent-expert** check ("what would a specialist from a neighbouring field ask first?"). Several distinct, specific blind spots, not one generic caveat — and for each, name *to what degree* it's unknown (hunch vs. total void) and run the cheapest probe to shrink it now. A blind spot merely *listed* is still a blind spot.

**Why falsifiers, not confidence scores:** you can't reliably inspect your own knowledge provenance — asked *how do I know this?*, an LLM confabulates a source as readily as it recalls one. A cheap external check beats any amount of self-rated certainty.

**Depth is the whole game — show it, don't pad it.** For "add rate limiting to our API": *shallow* known-known — "It's a REST API" (trivia; true but inert); *deep* — "It's a **public** API with no existing limiter, so this is the first line of abuse defense, not a tuning knob — failure-mode and bypass matter more than the limit value." If a box has no content at that level, dig until it does — or mark it honestly empty. Don't invent unknowns to fill the grid.

## Workflow (item mode)

1. **Decompose into aspects.** Break the item into distinct sub-questions — different aspects land in different boxes (scope = known known, data source = known unknown, the real goal = unknown known, an edge case = unknown unknown). The most important step; skipping it collapses a rich picture into one misleading label. Decompose along **more than one lens** (stakeholder, lifecycle, abstraction layer, failure mode) — aspects that surface only under a second lens are often where the blind spots live.
2. **Map each aspect onto the matrix.** One aspect may span two boxes — note the split rather than forcing it. An assumption goes in unknown-knowns, not known-knowns.
3. **Interrogate, then reduce.** For each known-known ask *"how do I actually know this?"* — "it just seems true" demotes it to an assumption. For any thin box ask *"am I dodging work here?"* — especially the bottom row. Then run the cheapest probe (grep / read / doc check) on the load-bearing unknowns **before presenting** — a tidy matrix you haven't tried to dent is the core failure (see *Core principle*). Name the single **load-bearing** belief: the one that, if wrong, collapses the most.
4. **Render** — a file for consequential/ambiguous/loop items (per *Output format* + *Knowframe mechanics*), an inline matrix for small ones.
5. **Present, then revise in place.** **Lead the hand-off with exactly ONE question** — the single load-bearing assumption, as a direct yes/no ("I'm assuming X — right?"). *One*, never two bundled with "and" — if several feel essential, ask the one that breaks the most and hold the rest in the matrix, which sits below as backup. Apply corrections directly, logging any **quadrant migration** (e.g. unknown-known → known-known, verified via X). **Do not start the task until there's a go-ahead.**
6. **Feed forward.** Derive the plan from the corrected understanding. For a non-trivial build the plan persists as a spec — `plans/SPEC-<topic>.md` where that convention exists: "What this implies" seeds the SPEC, residual known-unknowns + unverified assumptions become its **named risks**, and a fresh-eyes spec audit doubles as the knowframe's reflection pass. Then the slug file is deleted (see *Death trigger*).

**Advanced passes** — for a *genuinely ambiguous* item, or when asked to iterate a knowframe to convergence, read `references/advanced.md` (fork-check · loop mode) before step 5.

## Output format

Write the knowframe with these sections, in order. It is a **comprehension** document — never put execution steps in it. (A *pointer* names what must be resolved — "settle the scope boundary first"; a *step* is how you'd build it — "create the Postgres schema." Only pointers belong here.)

```markdown
# Understanding: <task / idea / decision in a line>
<!-- knowframe · comprehension layer · revise in place -->

- **Captured:** <date>  ·  **Status:** draft -> (reflected / confirmed)

## 1. What I think you're actually asking for
<one honest paragraph — the gestalt in my own words, not a feature list>

## 2. Decomposed aspects
<numbered list of the distinct sub-questions this item actually contains>

## 3. The matrix

|                            | We know it               | We don't know it            |
| -------------------------- | ------------------------ | --------------------------- |
| **We know it matters**     | <glance: known knowns>   | <glance: known unknowns>    |
| **We don't know it matters** | <glance: unknown knowns> | <glance: unknown unknowns>  |

### Known knowns — established
- <foundational commitment the understanding rests on>

### Known unknowns — open questions (conceptual first, then technical)
- <conceptual ambiguity / un-considered topic> -> ask / research / check yourself

### Unknown knowns — assumptions I'm making (flag any that are wrong)
- *Assuming* <framing / style / structure / logic-flow assumption> `[load-bearing]` → check: <self-check to run>   ·   → ask: <if only the user can settle it>

### Unknown unknowns — blind spots & directions to probe
- <smarter approach? growth direction? does an existing tool already do this?> -> probe / research

**Load-bearing assumption:** <the one belief that, if wrong, breaks the most>

## 4. What this implies (feed-forward to planning — pointers, not steps)
*Derive this list, don't hand-pick it: the load-bearing items still sitting in known-unknowns or unknown-knowns = what to resolve first.*
- <pointer to the highest-leverage gap to resolve before any plan is derived>

## Revision log
*Quadrant migrations only — a lean freshness trail, ~1 line per refresh, never a project changelog. (Item-mode only — project mode splits it: ≤3-line window in PROJECT.md, full trail in .know/LOG.md.)*
- <date> — initial draft (pre-reflection)
```

No confidence scores — what ranks the feed-forward is **load-bearing + still unresolved**. Tag only the genuinely load-bearing items `[load-bearing]`, at most ~3 — if everything looks load-bearing you haven't found the real spine yet; the single most load-bearing one also gets the callout. The glance-table is a map; the quadrant subsections carry the depth.

## Knowframe mechanics

- **Location:** write to `.know/<slug>.md` in the working directory; create `.know/` if absent.
- **Invisibility:** in a git repo, add `.know/` to `.gitignore` if not already ignored — framing files aren't committed.
- **Lifecycle:** one file per item, **overwrite in place** on correction, appending to the revision log — not versioned copies.
- **Death trigger:** an item knowframe is scaffolding, not a record — once it feeds forward (plan approved / SPEC landed / item abandoned), **delete the slug file in the same session**, folding residual unknowns into the SPEC's risks. `.know/` never accumulates stale slugs.
- **When to write a file:** non-trivial, ambiguous, or loop-driven items. Small, reversible, well-specified tasks get an inline matrix only — match depth to stakes; don't turn a quick request into a ceremony.
- **Dates:** `Captured`/`Last verified` and revision-log dates are the freshness mechanism and are exempt from any no-timestamps house rule. Nothing else in a knowframe carries dates or activity narrative.

## References & measurement

- [references/project-mode.md](references/project-mode.md) — **mandatory read for project mode** (first-run deep pass, refresh/self-heal, auto-pull, project schema).
- [references/advanced.md](references/advanced.md) — fork-check (ambiguous items) and loop mode (iterate to convergence).
- [references/examples.md](references/examples.md) — full worked knowframes; read for a concrete model of decomposition and conceptual-depth quadrants.
- [evals/README.md](evals/README.md) — blind baseline-vs-skill harness (/30 rubric, mean ± stddev). Run the project-mode track against **≥2 different repos** so the rules generalize rather than overfit.

## Activation: explicit only (by design)

Item-mode is **explicit-invocation only** — auto-triggering is deliberately *not* wired, and shouldn't be. Evals showed per-task framing is net-neutral-to-harmful when fired broadly, and the SKIP boundary (knowing when *not* to fire) is the hard part: without a tuned one the skill fires on everything and becomes noise. The single automatic trigger is **project-mode auto-pull** (the user's CLAUDE.md reads `.know/PROJECT.md` before non-trivial work) — the mode the evals validated. Don't add item-mode auto-triggering.
