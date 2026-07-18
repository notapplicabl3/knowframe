---
name: knowframe
description: Metacognition-first framing — externalize and calibrate the LLM's own understanding before acting, on the 2x2 known/unknown (Rumsfeld) matrix at conceptual depth across all four quadrants. Two modes. Item mode (/knowframe with a NEW task, idea, or decision — only when no project knowframe exists yet; off if .know/PROJECT.md is present) maps a single item into a transient knowframe (its comprehension artifact). Project mode (bare /knowframe inside a repo) builds and maintains one persisting understanding of the whole project at .know/PROJECT.md, auto-pulled before non-trivial work — a deep, extensive investigation on first run, incremental self-healing refresh thereafter. The knowframe is understanding only, never a plan; it feeds forward to planning, and the user or a loop pass reflects on and corrects it. Invoke explicitly via /knowframe, or on "map the knowns and unknowns", "what do we know vs not know", "frame this before we start", "known unknowns", "what am I not seeing", "map this project".
---

## Info / Help command

**If this skill is invoked with the argument `info` (or `help` / `?`) and nothing else, do NOT run the skill's normal workflow.** Instead print a compact overview of this skill, then stop:

- **Name & one-liner** — the skill name and one sentence on what it does.
- **When to use** — 1–2 lines on the situations or triggers it's for.
- **Commands / usage** — every subcommand, flag, or invocation form this skill supports, one line each with a short description. If it has no subcommands, give the basic usage form(s).
- **Key inputs / outputs** — what it expects and what it produces, when not obvious.

Draw the details from this SKILL.md's own contents, keep it scannable (headers + tight lines), and take no other action.

# Known/Unknown Matrix

## Core principle

This skill **externalizes the LLM's own understanding** of an item (a task, idea, or decision) so it can be corrected *before* anything is built on it. It's not a plan and not a checklist — it's a **knowframe**: a picture of what you grasp, what you're guessing, and what you can't yet see.

**The bottom-row insight — why this beats just planning:** a plan lives entirely in the top row, "we know it matters." It can hold known-knowns (steps) and known-unknowns (risks it sees), but it structurally *cannot* hold the bottom row — the assumptions it doesn't notice it's making and the blind spots it doesn't know exist. Surfacing that bottom row is the whole point.

**This is metathinking, not a description.** A tool like `/understand` maps *what's here* — the code and structure that already exist. This skill's job is the opposite-facing half: *what's **not** here, and to what degree* — the unstated framing, the missing requirement, the approach you haven't considered, the part of the problem outside the repo. Forcing that question is what produces a more *functional* grasp than re-describing what's already visible.

**The map is for digging, not for closing.** Naming what you don't know is the *start* of the work, not a substitute for it. The failure mode of this skill is a tidy matrix that *feels* like understanding and quietly ends the investigation — framing standing in for digging. Guard against it: the bottom row is a worklist, not a confession. For each blind spot, gauge *how* unknown it is and run the cheapest probe to shrink it. The knowframe isn't done when the boxes are full — it's done when the load-bearing unknowns have actually been reduced, or honestly marked as residual with their degree of uncertainty named.

**It only pays off if the understanding gets challenged.** There's no score and no automatic check; the value comes entirely from you (or a loop pass) pushing back on it. Rubber-stamp it and you've produced ceremony, not safety. So map it, surface it, get it corrected — and don't start the task until there's a go-ahead.

## When to use this — gate first (vs. plan mode)

**Before running anything below, decide whether this item even needs `/knowframe`. The gate is mandatory and holds even when `/knowframe` is invoked explicitly.** Run the full item-mode framing *only* when the request genuinely **hides assumptions or has contested framing** — you could read it several ways, the real goal is unstated, or you'd otherwise build on unexamined ground. If the task is crisp, well-specified, or reversible, **do not run the matrix**: say *"this is unambiguous — going straight to plan"* and hand to plan mode (or a one-line inline note for something tiny). Borderline cases get a short inline matrix, never the full artifact. `/knowframe` feeds *into* planning; it never replaces it — **the default for a clear task is plan mode, not this skill.** (Project mode is exempt: a bare `/knowframe` in a repo isn't framing a task, so this gate doesn't apply to it.)

**First gate — a pre-existing project knowframe turns item-mode OFF.** If `.know/PROJECT.md` exists, do **not** run a per-task matrix at all, *even when `/knowframe` is invoked with a subject*. The project knowframe is your grounding: lean on it and go straight to planning (surface the one load-bearing question there if the task is genuinely ambiguous). Item-mode is for **new** items only — a task, idea, or decision with no standing project understanding to draw on (a repo with no `.know/PROJECT.md`, or anything outside a repo). Stacking a task matrix on a project knowframe was measured to *dilute* it, never improve it, so this is a hard switch, not a judgment call. The ambiguity gate above applies *only after* this one clears — i.e. to genuinely new items.

## Two modes

`knowframe` runs in one of two modes; both externalize and calibrate understanding before acting, over different inputs.

- **Item mode — `/knowframe <task | idea | decision>`.** Frames a single **new** forward-looking item — one with no standing project knowframe to draw on (**off entirely when `.know/PROJECT.md` exists**; see the gate). Writes a transient `.know/<slug>.md` (or inline for small items). This is everything described below through *Knowframe mechanics*.
- **Project mode — `/knowframe` with no item, inside a repo.** Builds and maintains one persisting understanding of the *whole project* at `.know/PROJECT.md`, auto-pulled before non-trivial work to prime the LLM. See **Project mode** below.

## The four quadrants

The matrix is a thinking tool, not a form to fill. Each box catches a different *kind* of thing:

|                          | **We know it**                                          | **We don't know it**                                         |
| ------------------------ | ------------------------------------------------------- | ------------------------------------------------------------ |
| **We know it matters**   | **Known knowns** — the foundational commitments the understanding rests on. | **Known unknowns** — open questions and undefined framing we're aware of. |
| **We don't know it matters** | **Unknown knowns** — framing/style/structure assumptions baked in silently. | **Unknown unknowns** — blind spots, smarter approaches, growth direction. |

- **Known knowns — what the item fundamentally *is*.** The foundational commitments the understanding rests on. Honesty-check each: *genuinely established* or *assumed-but-feels-certain*? Anything you can't trace to a source is demoted to an assumption. **A wrong known-known is the deadliest error — nothing downstream questions it.**
- **Known unknowns — the open questions.** Lead with conceptual ones (undefined scope, open framing, un-considered adjacents), then technical. Route each to its cheapest resolver: ask the user when they hold the answer, research when it's discoverable — and **resolve the trivially-checkable ones yourself** (a grep, a file read) instead of punting them upward.
- **Unknown knowns — the assumptions you don't notice.** The dangerous box for an LLM. Lead with *framing* assumptions (chosen representation, "this is just how it's done," who the output is for, treating an evolving thing as static), then concrete ones. The most load-bearing are the hardest to self-surface. Give each a **falsifier** — but only a real one: a cheap *self-check you can actually run* (`→ check:` grep / read / run / lookup). If the only way to know is to ask the user, mark it `→ ask` — that's an open question, not a falsifier; don't dress it up. Hunt for a self-check before settling for an ask.
- **Unknown unknowns — the blind spots.** The highest-value box, and the one you can't fill by staring — *generate* it deliberately by probing several angles: is there a **smarter or more malleable approach** than the obvious one? Where will this **grow / what direction does it pull toward**? What **pain points haven't surfaced** yet? **Does an existing skill, tool, or product already do part of this?** What would I **regret not knowing**? Then force two prompts: a **pre-mortem** ("assume this went wrong, or was the wrong frame entirely — what did we miss?") and an **adjacent-expert** check ("what would a specialist from a neighbouring field ask first?"). Aim for several distinct, specific blind spots, not one generic caveat. For each, name *to what degree* it's actually unknown (a hunch vs. a total void) and run the cheapest probe to shrink it now — an un-probed blind spot you merely *listed* is still a blind spot.

**Why falsifiers, not confidence scores:** you can't reliably inspect your own knowledge provenance — asked *how do I know this?*, an LLM confabulates a source as readily as it recalls one. A cheap external check beats any amount of self-rated certainty.

**Depth is the whole game — show it, don't pad it.** A box listing surface particulars has failed. For "add rate limiting to our API":

> - *shallow known-known:* "It's a REST API." — trivia; true but inert.
> - *deep known-known:* "It's a **public** API with no existing limiter, so this is the first line of abuse defense, not a tuning knob — which makes failure-mode and bypass matter more than the limit value." — a commitment the rest of the understanding rests on.

If a box has no content at that level, dig until it does — or mark it honestly empty. Don't invent unknowns to fill the grid.

## Workflow

*Only once the gate above clears — a crisp task should already be in plan mode, not here.*

1. **Decompose into aspects.** A task is rarely one quadrant — break it into distinct sub-questions, since different aspects land in different boxes (scope = known known, data source = known unknown, the real goal = unknown known, an edge case = unknown unknown). This is the most important step; skipping it collapses a rich picture into one misleading label. Decompose along **more than one lens** (stakeholder, lifecycle, abstraction layer, failure mode) — aspects that surface only under a second lens are often where the blind spots live.
2. **Map each aspect onto the matrix.** One aspect may span two boxes — note the split rather than forcing it. An assumption goes in unknown-knowns, not known-knowns.
3. **Interrogate the map before you trust it:**
   - For each known-known, ask *"how do I actually know this?"* If the answer is "it just seems true," demote it to an assumption.
   - For any thin box, ask *"am I dodging work here?"* — especially the bottom row.
   - **Reduce, don't just list.** Before you present, run the cheapest probe (a grep, a file read, a doc check) on the load-bearing unknowns. Handing over a tidy matrix you haven't tried to dent is the core failure of this skill — the framing must drive investigation, not replace it.
   - Name the single **load-bearing** belief: the one that, if wrong, collapses the most. It anchors what to resolve first.
4. **Render** — a file for consequential/ambiguous/loop items (per *Output format* + *Knowframe mechanics*), an inline matrix for small ones.
5. **Present, then revise in place.** **Lead the hand-off with exactly ONE question** — the single load-bearing assumption, as a direct yes/no ("I'm assuming X — right?"). *One*, not two: if several feel essential, ask only the one that, if wrong, breaks the most, and hold the rest in the matrix. Never bundle two with "and" — that destroys the focus this is for. The full matrix sits below as backup, but the wall of quadrants is not the hand-off; the one question is. Apply corrections directly, logging any **quadrant migration** (e.g. unknown-known → known-known, verified via X). **Do not start the task until there's a go-ahead.**
6. **Feed forward.** Derive the plan from the corrected understanding — the whole point of going first (see *Output format*). For a non-trivial build the plan persists as `plans/SPEC-<topic>.md` (`~/BABEL/docs/building.md` § Spec convention): "What this implies" seeds the SPEC, residual known-unknowns + unverified assumptions become its **named risks**, and the fresh-session spec audit doubles as the knowframe's reflection pass. Then the slug file is deleted (see *Death trigger*).

**Fork-check (optional — genuinely ambiguous items only).** A single pass can silently collapse an ambiguous request to one reading *without ever feeling uncertain* — a failure invisible to introspection, so re-reading your own framing won't surface it. Instead, re-derive **only** the interpretation ("what are they actually asking for?") once in a **fresh subagent that can't see your first reading**, then compare on substance, not wording. *Converge* → the reading is stable; proceed. *Diverge* → you've found a fork a single pass would have hidden; make it the **lead hand-off question** in step 5, not a guessed one. One extra pass, interpretation only — skip it on crisp tasks. It can't catch two passes collapsing to the *same* wrong reading (only the user can), so it sharpens the lead question; it doesn't replace the falsifiers or the ask.

**Loop mode (optional — investigation-driven refinement).** Iterate a knowframe to convergence instead of producing it in one pass — but **each pass must drive an unknown to resolution, not rewrite the matrix.** Re-phrasing the boxes without new investigation is the closure trap and does *not* count as a pass. One pass:

1. Take the single highest **load-bearing, still-unresolved** item — an open known-unknown, or an unverified unknown-known assumption.
2. **Drive it:** run the cheapest probe that could settle it (grep / read / verify; or surface it as the one question if only the user can).
3. **Apply the result:** resolve or downgrade it, log the **quadrant migration** (e.g. *assumption → known-known, verified via X*), and add any new unknown the probe exposed.

**Converged when** no load-bearing item remains un-probed — each is either resolved or marked residual with its degree named (a probe was tried and it genuinely needs the user, or is irreducibly uncertain). Also stop on a pass that produces no migration and no new probe (converged, or *stuck* — if stuck, surface what's blocking), or at a hard cap of ~5 passes. **Progress is measured by migrations, never by text edits** — that's what keeps the loop honest. Composes with `/orchestrate` iterate mode; most valuable for **project-mode hardening** (drive every load-bearing assumption in `.know/PROJECT.md` to verified-against-code), and usable on a genuinely ambiguous new item.

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
*Derive this list, don't hand-pick it: the load-bearing items still sitting in known-unknowns or unknown-knowns (open questions + unverified assumptions) = what to resolve first.*
- <pointer to the highest-leverage gap to resolve before any plan is derived>

## Revision log
*Record quadrant migrations as understanding firms up — e.g. "data source: known-unknown → known-known (verified via X)". Keep this a **lean freshness trail — ~1 line per refresh, epistemic migrations only** — not a project changelog: build/activity history belongs in the repo's own log or git, and resolved items already show inline in the quadrants (strikethrough), so don't re-narrate them here. (This inline log is item-mode only — the file is transient. Project mode splits it: a ≤3-line window in `PROJECT.md`, full trail in `.know/LOG.md`; see Project schema.)*
- <date> — initial draft (pre-reflection)
```

No confidence scores — self-rated certainty is unreliable and adds false precision. What ranks the feed-forward instead is simply **load-bearing + still unresolved**: a belief that, if wrong, breaks the most and hasn't yet been verified or answered. Tag only the genuinely load-bearing items `[load-bearing]` — keep it to a few (≤3); if everything looks load-bearing you haven't found the real spine yet. The single most load-bearing one also gets the **Load-bearing assumption** callout. The glance-table is a map; the quadrant subsections carry the depth.

## Knowframe mechanics

- **Location:** write to `.know/<slug>.md` in the working directory; create the `.know/` directory if absent.
- **Invisibility:** if the working directory is a git repo and `.know/` isn't already ignored, add `.know/` to `.gitignore` so framing files aren't committed.
- **Lifecycle:** one file per item, **overwrite in place** on correction, appending to the revision log — not versioned copies.
- **Death trigger:** an item knowframe is scaffolding, not a record — once it feeds forward (plan approved / SPEC landed / item abandoned), **delete the slug file in the same session**, folding any residual unknowns into the SPEC's risks. `.know/` never accumulates stale slugs; the fold-back sweep catches strays.
- **When to write a file:** non-trivial, ambiguous, or loop-driven items. Small, reversible, well-specified tasks get an inline matrix only.
- **Dates:** `Captured`/`Last verified` and revision-log dates are the freshness mechanism and are exempt from the no-timestamps rule (`docs/conventions.md` names the exemption). Nothing else in a knowframe carries dates or activity narrative.

## Project mode (`/knowframe` with no item)

**Heavy mode — skip this section if you're framing a single task.**

A standing, calibrated map of the LLM's understanding of the *whole project* — what it is, what's assumed about it, where the blind spots are. It is the **calibration layer** in the memory layer map (`docs/conventions.md`): not human instructions (that's the Map, `CLAUDE.md`), not the code description (that's `architecture.md` / `architecture-logic.md`), not working state (that's `project_*` memory), but *how well the assistant actually grasps this repo, and where it's guessing.* Lives at `.know/PROJECT.md` — a single, persisting, gitignored **knowframe** (not transient, not per-slug).

**Ownership — the knowframe holds the epistemic delta only.** A fact another doc owns appears here as a pointer plus its verification status, never restated (one fact, one place). Stack, structure, commands, schema → `architecture.md` / the Map; working state, decisions → `project_*` memory. The knowframe's unique cargo is the other three quadrants — unverified assumptions, open gaps, blind spots — plus the gestalt and the load-bearing assumption. Same matrix shape as the `user_understanding` memory but opposite subject: that file calibrates *Ben's* grasp, this one calibrates *Claude's* — never merge them.

**Graduation caps the file.** When an unknown migrates to a verified known, the *fact* moves to its owning doc (`architecture.md` / Map / `project_*` memory) and the migration line goes to the Recent-migrations window (older lines rotate into `.know/LOG.md` — see the schema). Resolved knowledge drains **out**; it never accumulates. Target **~100 lines** — the file is auto-pulled before every non-trivial task, so every line is a per-task tax.

### First run — no `.know/PROJECT.md` yet → go deep
The foundation everything else pulls from, so **invest heavily — cost is not a concern.** Confirm first (it's expensive): *"No project understanding file yet — run a deep pass to build `.know/PROJECT.md`? (y / or give me an item instead)."* Then investigate before writing:
- Read the README/docs, package manifests + lockfile, directory tree, entry points, the key files of *each* major subsystem, tests, CI/config, any CLAUDE.md, and recent git history. On a large repo, dispatch parallel `Explore` subagents per subsystem (or use `/analyze` / `understand`) as *input* — the output is the epistemic file, not their report. Route the fan-out per `~/BABEL/docs/delegation.md`.
- **Fork-check doesn't transfer to project mode** — there's no ambiguous request to re-interpret; the gestalt is grounded by the code, and verification beats sampling (exactly what trace-to-source known-knowns and the refresh self-heal already do). Cheap exception: since you're already fanning out, have the passes each name *what the project is fundamentally for / its architectural spine* — if those **diverge**, the repo's purpose is underdetermined by its code, itself worth recording as a known-unknown.
- Write `.know/PROJECT.md` in the **project schema** below; known-knowns should be rich, but still populate the bottom row (assumptions + blind spots).
- The **auto-pull rule** lives in the global shell's routing table ("work inside the current project → read `.know/PROJECT.md` first if present, skeptically; self-heal drift"). If running without that shell, tell the user the file is inert until such a rule exists.

### Refresh — `.know/PROJECT.md` exists → incremental + self-heal
Don't re-scan the world. Read the existing file, check it against current state (use `git log` / `git diff` since the `Last verified` date as the cheap change-detector, plus the areas being touched), **self-heal** contradictions, and deepen weak or stale entries. Bare `/knowframe` on an existing file = this refresh; present changes for correction. For a **deep hardening** pass, run the refresh as **Loop mode** (above) — drive each load-bearing assumption to verified-against-code until none remain unverified.

**The fold-back sweep is the standard refresh trigger.** A session that resolves a known-unknown or invalidates an assumption logs the quadrant migration at close (`docs/conventions.md` § Fold-back sweep) — append to `.know/LOG.md`, rotate the Recent-migrations window — and graduates the verified fact to its owning doc. Refresh shouldn't wait for an explicit `/knowframe`.

### Auto-pull
A rule in the user's CLAUDE.md reads `.know/PROJECT.md` before non-trivial work (`.know/LOG.md` is deliberately outside this pull). Because it's auto-injected everywhere, **a wrong entry is the deadliest known-known of all** — so read it *skeptically* and **self-heal**: if reality contradicts it, fix the file before proceeding, then bump `Last verified` + log the heal (LOG.md append + window rotate) so the freshness marker never lies. On pull, if many commits have landed since `Last verified` (or it's weeks old), treat it as stale and do a quick `git log`/`diff` refresh before trusting it.

### Project schema
The knowframe format above, reframed for a repo: `# Project understanding: <repo name>` + a `Last verified: <date>` line; the gestalt; decomposed aspects = subsystems/concerns/domains; the four-quadrant matrix project-flavored (known knowns = **verification status + pointers to the owning docs, never restated content** — what has been verified-against-code vs merely documented, plus only genuinely epistemic commitments; known unknowns = parts not yet understood; unknown knowns = assumed conventions treated as given but unverified; unknown unknowns = subsystems/constraints possibly missed entirely); "What this implies" (pointers, not steps); a **Recent migrations** window (below).

**The revision log is split so the context tax is structural, not disciplinary.** `PROJECT.md` carries only a `## Recent migrations` window — the **newest ≤3 migrations, one line each** — closed by a pointer line (`*Full history: `.know/LOG.md`.*`). The full trail lives in **`.know/LOG.md`** (newest first, same date-exemption as the knowframe): every refresh/fold-back appends there, and window overflow rotates in verbatim. `LOG.md` is **never auto-pulled** — read it only when history is genuinely needed (auditing how understanding evolved, a self-heal conflict, "did we already verify this once?"). Entries there should still *lead* with the one-line migration ("live LLM path: known-unknown → known-known, verified via keyed run") so a skim stays cheap, but narration below that line is tolerated — it clogs nothing.

Two discipline rules the schema enforces: **Status is one word** (draft / refreshed / hardened) — never a parenthetical of what the session built; build activity belongs to git and `summary_reading/`, and a Status line narrating commits is exactly the timestamp-rule violation the exemption doesn't cover. **Window entries are one line naming the migration**, never a session changelog — anything longer goes to `LOG.md`.

## Notes on calibration

- **Match depth to stakes.** Keep the machinery minimal (a markdown file, no tooling); put the depth in the *reasoning*, scaled to the item. A small, reversible task gets a short inline matrix, not a file or an interrogation; a consequential or ambiguous one warrants full decomposition and a written knowframe. Don't turn a quick request into a ceremony.
- **Assumptions default to unknown-knowns, not known-knowns.** If you can't point to where a "fact" came from, it's an assumption — treat it as such.
- See [references/examples.md](references/examples.md) for full worked knowframes — read it for a concrete model of decomposition and conceptual-depth quadrants.
- To measure whether this skill earns its keep, see [evals/README.md](evals/README.md) — a blind baseline-vs-skill harness (/30 rubric, mean ± stddev). Run the project-mode track against **≥2 different repos** to check the rules generalize rather than overfit the repo they were tuned on.

## Activation: explicit only (by design)

Item-mode is **explicit-invocation only** — auto-triggering is deliberately *not* wired, and shouldn't be. Evals showed per-task framing is net-neutral-to-harmful when fired broadly, and the SKIP boundary (knowing when *not* to fire) is the hard part: without a tuned one the skill fires on everything and becomes noise. The single automatic trigger is **project-mode auto-pull** (CLAUDE.md reads `.know/PROJECT.md` before non-trivial work) — the mode the evals validated. Don't add item-mode auto-triggering.
