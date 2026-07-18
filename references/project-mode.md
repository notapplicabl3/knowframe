# Project mode — persisting whole-project knowframe

**Read this file whenever `/knowframe` runs bare inside a repo (project mode). Never run project mode from memory of SKILL.md alone — this file is the mode's contract.** It assumes SKILL.md's core (quadrants, workflow, output format) is already loaded.

A standing, calibrated map of the LLM's understanding of the *whole project* — what it is, what's assumed about it, where the blind spots are. It is the **calibration layer** among the project's docs: not human instructions (that's `CLAUDE.md`), not the code description (that's `architecture.md` / `architecture-logic.md`), not working state (that's `project_*` memory), but *how well the assistant actually grasps this repo, and where it's guessing.* Lives at `.know/PROJECT.md` — a single, persisting, gitignored **knowframe** (not transient, not per-slug).

**Ownership — the knowframe holds the epistemic delta only.** A fact another doc owns appears here as a pointer plus its verification status, never restated (one fact, one place). Stack, structure, commands, schema → `architecture.md` / `CLAUDE.md`; working state, decisions → `project_*` memory. The knowframe's unique cargo is the other three quadrants — unverified assumptions, open gaps, blind spots — plus the gestalt and the load-bearing assumption. Same matrix shape as a `user_understanding` memory but opposite subject: that calibrates the *user's* grasp, this calibrates the *assistant's* — never merge them.

**Graduation caps the file.** When an unknown migrates to a verified known, the *fact* moves to its owning doc and the migration line goes to the Recent-migrations window (older lines rotate into `.know/LOG.md` — see the schema). Resolved knowledge drains **out**; it never accumulates. Target **~100 lines** — the file is auto-pulled before every non-trivial task, so every line is a per-task tax.

## First run — no `.know/PROJECT.md` yet → go deep

The foundation everything else pulls from, so **invest heavily — cost is not a concern.** Confirm first (it's expensive): *"No project understanding file yet — run a deep pass to build `.know/PROJECT.md`? (y / or give me an item instead)."* Then investigate before writing:

- Read the README/docs, package manifests + lockfile, directory tree, entry points, the key files of *each* major subsystem, tests, CI/config, any CLAUDE.md, and recent git history. On a large repo, dispatch parallel `Explore` subagents per subsystem (or use `/analyze` / `understand`) as *input* — the output is the epistemic file, not their report.
- **Fork-check doesn't transfer to project mode** — there's no ambiguous request to re-interpret; the gestalt is grounded by the code, and verification beats sampling. Cheap exception: since you're already fanning out, have the passes each name *what the project is fundamentally for / its architectural spine* — if those **diverge**, the repo's purpose is underdetermined by its code, itself worth recording as a known-unknown.
- Write `.know/PROJECT.md` in the **project schema** below; known-knowns should be rich, but still populate the bottom row (assumptions + blind spots).
- The **auto-pull rule** lives in the user's global shell ("work inside the current project → read `.know/PROJECT.md` first if present, skeptically; self-heal drift"). If running without such a shell rule, tell the user the file is inert until one exists.

## Refresh — `.know/PROJECT.md` exists → incremental + self-heal

Don't re-scan the world. Read the existing file, check it against current state (use `git log` / `git diff` since the `Last verified` date as the cheap change-detector, plus the areas being touched), **self-heal** contradictions, and deepen weak or stale entries. Bare `/knowframe` on an existing file = this refresh; present changes for correction. For a **deep hardening** pass, run the refresh as **Loop mode** (`advanced.md`, sibling file) — drive each load-bearing assumption to verified-against-code until none remain unverified.

**A session-close review is the standard refresh trigger.** A session that resolves a known-unknown or invalidates an assumption logs the quadrant migration at close — append to `.know/LOG.md`, rotate the Recent-migrations window — and graduates the verified fact to its owning doc. Refresh shouldn't wait for an explicit `/knowframe`.

## Auto-pull

A rule in the user's CLAUDE.md reads `.know/PROJECT.md` before non-trivial work (`.know/LOG.md` is deliberately outside this pull). Because it's auto-injected everywhere, **a wrong entry is the deadliest known-known of all** — so read it *skeptically* and **self-heal**: if reality contradicts it, fix the file before proceeding, then bump `Last verified` + log the heal (LOG.md append + window rotate) so the freshness marker never lies. On pull, if many commits have landed since `Last verified` (or it's weeks old), treat it as stale and do a quick `git log`/`diff` refresh before trusting it.

## Project schema

The knowframe format from SKILL.md, reframed for a repo: `# Project understanding: <repo name>` + a `Last verified: <date>` line; the gestalt; decomposed aspects = subsystems/concerns/domains; the four-quadrant matrix project-flavored (known knowns = **verification status + pointers to the owning docs, never restated content** — what has been verified-against-code vs merely documented, plus only genuinely epistemic commitments; known unknowns = parts not yet understood; unknown knowns = assumed conventions treated as given but unverified; unknown unknowns = subsystems/constraints possibly missed entirely); "What this implies" (pointers, not steps); a **Recent migrations** window (below).

**The revision log is split so the context tax is structural, not disciplinary.** `PROJECT.md` carries only a `## Recent migrations` window — the **newest ≤3 migrations, one line each** — closed by a pointer line (`*Full history: .know/LOG.md.*`). The full trail lives in **`.know/LOG.md`** (newest first, same date-exemption as the knowframe): every refresh appends there, and window overflow rotates in verbatim. `LOG.md` is **never auto-pulled** — read it only when history is genuinely needed (auditing how understanding evolved, a self-heal conflict, "did we already verify this once?"). Entries there should still *lead* with the one-line migration ("live LLM path: known-unknown → known-known, verified via keyed run") so a skim stays cheap; narration below that line is tolerated — it clogs nothing.

Two discipline rules the schema enforces: **Status is one word** (draft / refreshed / hardened) — never a parenthetical of what the session built; build activity belongs to git and session logs, and a Status line narrating commits is exactly the timestamp-rule violation the date exemption doesn't cover. **Window entries are one line naming the migration**, never a session changelog — anything longer goes to `LOG.md`.

## House integration (Ben's shell — strip for standalone use)

- Subagent fan-out on first run routes per `~/BABEL/docs/delegation.md`.
- The session-close refresh trigger is the fold-back sweep (`~/BABEL/docs/conventions.md` § Fold-back sweep); the auto-pull rule lives in the shell's routing table (`~/BABEL/AGENTS.md`).
- The calibration-layer / memory-layer map is defined in `~/BABEL/docs/conventions.md`.
