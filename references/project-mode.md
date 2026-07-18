# Project mode — persisting whole-project knowframe

**Read this file whenever `/knowframe` runs bare inside a repo (project mode). Never run project mode from memory of SKILL.md alone — this file is the mode's contract.** It assumes SKILL.md's core (quadrants, workflow, output format) is already loaded.

Project mode = `.know/PROJECT.md`: one persisting, gitignored **knowframe** for the LLM's calibrated grasp of the *whole project* — purpose, assumptions, guesses (not transient, not per-slug). It is the **calibration layer**: not human instructions (`CLAUDE.md`), not code description (`architecture.md` / `architecture-logic.md`), not working state (`project_*` memory), but assistant self-calibration.

**Ownership — the knowframe holds the epistemic delta only.** Another doc's fact appears only as pointer + verification status, never restated (one fact, one place). Stack/structure/commands/schema -> `architecture.md` / `CLAUDE.md`; working state/decisions -> `project_*` memory. This file owns assumptions, gaps, blind spots, gestalt, load-bearing assumption. Same shape as `user_understanding`, opposite subject — never merge.

**Graduation caps the file.** Unknown -> verified: *fact* to owning doc; migration to Recent migrations; overflow to `.know/LOG.md`. Resolved knowledge drains **out**; it never accumulates. Target **~100 lines** because auto-pulled before every non-trivial task.

## First run — no `.know/PROJECT.md` yet → go deep

No file => foundation pass; **invest heavily — cost is not a concern.** Confirm first: *"No project understanding file yet — run a deep pass to build `.know/PROJECT.md`? (y / or give me an item instead)."* Then investigate:

- Read README/docs; package manifests + lockfile; directory tree; entry points; key files of *each* major subsystem; tests; CI/config; any CLAUDE.md; recent git history.
- Large repo: parallel `Explore` subagents per subsystem (or `/analyze` / `understand`) as *input*; output is `.know/PROJECT.md`, not their report.
- **Fork-check doesn't transfer to project mode** — no ambiguous request is being re-interpreted; verification beats sampling. Cheap exception: each pass names *what the project is fundamentally for / its architectural spine*; if those **diverge**, record underdetermined purpose as a known-unknown.
- Write `.know/PROJECT.md` in the **project schema** below; known-knowns rich, bottom row populated (assumptions + blind spots).
- The **auto-pull rule** lives in the user's global shell ("work inside the current project → read `.know/PROJECT.md` first if present, skeptically; self-heal drift"). If running without such a shell rule, tell the user the file is inert until one exists.

## Refresh — `.know/PROJECT.md` exists → incremental + self-heal

Existing file = incremental; don't re-scan the world. Read it; cheap change-detector = `git log` / `git diff` since `Last verified` + touched areas; **self-heal** contradictions; deepen weak/stale entries. Bare `/knowframe` on an existing file = this refresh; present changes for correction. **Deep hardening** = refresh as **Loop mode** (`advanced.md`, sibling file): drive each load-bearing assumption to verified-against-code until none remain unverified.

**A session-close review is the standard refresh trigger.** If a session resolves a known-unknown or invalidates an assumption, append the quadrant migration to `.know/LOG.md`, rotate Recent migrations, and graduate the verified fact to its owning doc. Refresh shouldn't wait for explicit `/knowframe`.

## Auto-pull

The user's CLAUDE.md reads `.know/PROJECT.md` before non-trivial work; `.know/LOG.md` is deliberately outside this pull. Because it is auto-injected everywhere, **a wrong entry is the deadliest known-known of all**: read it *skeptically* and **self-heal**. If reality contradicts it, fix the file before proceeding, then bump `Last verified` + log the heal (LOG.md append + window rotate) so the freshness marker never lies. If many commits landed since `Last verified` (or it is weeks old), treat it as stale and do a quick `git log`/`diff` refresh before trusting it.

## Project schema

Use SKILL.md's repo-flavored knowframe:

- Header: `# Project understanding: <repo name>` + `Last verified: <date>`.
- Gestalt; decomposed aspects = subsystems/concerns/domains; four-quadrant matrix.
- Known knowns = **verification status + pointers to owning docs, never restated content**: verified-against-code vs documented, plus genuinely epistemic commitments.
- Known unknowns = not-yet-understood parts; unknown knowns = assumed conventions treated as given but unverified; unknown unknowns = subsystems/constraints possibly missed entirely.
- "What this implies" = pointers, not steps.
- `## Recent migrations`: **newest ≤3 migrations, one line each**, closed by `*Full history: .know/LOG.md.*`.

**The revision log is split so the context tax is structural, not disciplinary.** Full trail: **`.know/LOG.md`** (newest first, same date-exemption as the knowframe); every refresh appends there; window overflow rotates in verbatim. `LOG.md` is **never auto-pulled** — read it only when history is genuinely needed (audit evolution, self-heal conflict, "did we already verify this once?"). Entries still *lead* with the one-line migration ("live LLM path: known-unknown → known-known, verified via keyed run"); narration below is tolerated.

Discipline: **Status is one word** (draft / refreshed / hardened) — never parenthetical; build activity belongs to git/session logs, and commit narration in Status violates the timestamp rule. **Window entries are one line naming the migration**, never a session changelog; longer goes to `LOG.md`.

## House integration (Ben's shell — strip for standalone use)

- Subagent fan-out on first run routes per `~/BABEL/docs/delegation.md`.
- The session-close refresh trigger is the fold-back sweep (`~/BABEL/docs/conventions.md` § Fold-back sweep); the auto-pull rule lives in the shell's routing table (`~/BABEL/AGENTS.md`).
- The calibration-layer / memory-layer map is defined in `~/BABEL/docs/conventions.md`.
