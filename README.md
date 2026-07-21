# knowframe

**Make an AI say what it doesn't know — before it acts on what it thinks it does.**

When you hand an AI a task, it starts building on a picture of what you meant. Most of that picture is fine. But some of it is *guessed* — and the AI can't tell the difference, so it won't warn you. It fills the gaps with plausible assumptions and proceeds with total confidence. By the time you notice, the wrong assumption is load-bearing and everything on top of it has to come down.

knowframe is a small routine that runs *before* the work. It asks the AI to stop and lay its own understanding out on a table, sorted into four buckets:

|  | **It knows it** | **It doesn't know it** |
|---|---|---|
| **It knows it matters** | facts it's sure of | open questions it's aware of |
| **It doesn't know it matters** | assumptions it doesn't realize it's making | blind spots it can't see at all |

The top-left is what any careful assistant already gives you. The value is the **bottom row** — the silent assumptions and the blind spots. Those are the things that sink a task, and they're exactly what a normal plan never surfaces, because a plan only lists the steps the AI can already see.

The idea is old — it's the "known knowns / known unknowns / unknown unknowns" framing (the *Rumsfeld matrix*). knowframe just points it inward: the AI maps **its own head**, not the problem. Then it does one more thing that matters — it doesn't just *list* the unknowns, it spends a minute cheaply checking the ones that count (grep the code, read the file, look it up), so what reaches you is already narrowed down. It hands you the single assumption most likely to be wrong as one plain yes/no question, and **waits** for your answer before touching anything.

That's the whole point: catch the wrong assumption while it's still cheap to fix — a one-word correction instead of a rebuild.

---

## How it works

knowframe is an **agent skill** — a packaged set of instructions, not a program you run. You drop it into an AI coding assistant that supports skills (it's built for [Claude Code](https://docs.claude.com/en/docs/claude-code), whose `SKILL.md` format it uses), and invoke it with `/knowframe`. The assistant reads the instructions and follows the routine in its own context.

It has two modes, chosen automatically by where and how you invoke it.

### Item mode — frame one new thing

```
/knowframe <a task, an idea, or a decision>
```

Maps a single new item you're about to start — a feature request, a product idea, a "$49 or $99?" call. The AI decomposes the item along a couple of different lenses, sorts the pieces into the four quadrants, cheaply probes the unknowns that are worth probing, and comes back with:

- a one-line read of *what it thinks you're actually asking for*,
- the four-quadrant matrix, with the bottom row (assumptions + blind spots) populated,
- **one** load-bearing yes/no question to answer first,
- and *what this implies* for planning — pointers, never steps.

For a small item this is just a few lines inline. For a consequential or ambiguous one it's written to a throwaway file (`.know/<slug>.md`) so you can correct it in place. Once your answer feeds into a plan or spec, the file is deleted — its leftover unknowns become the plan's named risks.

**It deliberately does nothing for a crisp, well-specified request.** A gate up front checks whether the task actually hides any assumptions; if it doesn't, knowframe says so and hands straight to planning. Framing everything is noise — the skill's whole job is knowing when *not* to run.

### Project mode — a persisting understanding of a whole repo

```
/knowframe          # run bare, inside a repo
```

Builds one durable file, `.know/PROJECT.md`, holding the AI's calibrated grasp of the *entire project* — what it's for, what's verified against the code, what's still assumed, what might have been missed. The first run goes deep (reads the docs, manifests, entry points, each subsystem, tests, CI, recent history). After that it's incremental: each run detects what changed since it was last verified, self-heals anything the code now contradicts, and deepens the weak spots.

The payoff comes from one host rule: **your assistant reads `.know/PROJECT.md` before any non-trivial work in that repo.** With that rule in place, every task in the project starts from a calibrated, skeptically-maintained understanding instead of a cold read. (See [Host integration](#host-integration) — without the rule, the file is inert.)

Project mode owns only the **epistemic delta** — assumptions, gaps, blind spots. Hard facts (stack, commands, schema) stay in their own docs and appear here only as a pointer plus a verification status. Resolved unknowns graduate *out* to the doc that owns them, so the file stays small (~100 lines) because it's read so often. Full history rotates into `.know/LOG.md`, which is never auto-read.

---

## Design principles

A few rules do most of the work. They're what separate a useful knowframe from a tidy-looking grid that quietly ends the investigation.

- **Understanding only, never a plan.** knowframe produces *comprehension* — pointers like "settle the scope boundary first," not execution steps. It feeds planning; it doesn't replace it.
- **The map is a worklist, not a deliverable.** Every unknown that matters gets the cheapest possible probe *before* you ever see the matrix. A neat grid that stopped the investigation is the core failure mode.
- **Blind spots are generated, not recalled.** The bottom-right quadrant is forced open with a pre-mortem ("assume this was the wrong frame — what did we miss?") and an adjacent-expert check, aiming for several specific blind spots, each with the probe that would reveal it. "Performance might be a concern" is a hedge wearing a quadrant label, not a blind spot.
- **Lead with exactly one question.** The single assumption that, if wrong, breaks the most — asked as one yes/no. Never two, never bundled with "and," because you'd answer the easy one and the load-bearing one would die unexamined.
- **No confidence scores.** An LLM confabulates how it knows what it knows; a cheap external check beats any number it rates itself. Boxes are backed by a source or a probe, or marked honestly empty — never padded to fill the grid.
- **No go-ahead, no start.** The knowframe's value is in being challenged. It waits.

---

## Repository layout

```
knowframe/
├── SKILL.md                      # the skill — core routine, the matrix, item-mode workflow, output format
├── references/
│   ├── project-mode.md           # project-mode contract (read before running project mode)
│   ├── advanced.md               # fork-check (ambiguous items) · loop mode (drive to convergence)
│   └── examples.md               # worked knowframes — coding task, decision, full file, project file
├── evals/                        # blind-judge harness measuring whether the skill actually helps
└── LICENSE
```

`SKILL.md` is the entry point and is loaded whenever the skill runs. The `references/` files are pulled in on demand — project mode reads `project-mode.md`, ambiguous or iterative work reads `advanced.md`, and `examples.md` is there when you want to see what "deep enough" looks like in each quadrant.

## Installation

Place the `knowframe/` folder where your assistant looks for skills. For Claude Code:

```bash
# personal (available in every project)
git clone https://github.com/notapplicabl3/knowframe.git ~/.claude/skills/knowframe

# or per-project
git clone https://github.com/notapplicabl3/knowframe.git .claude/skills/knowframe
```

Then invoke it with `/knowframe` (item mode with an argument, project mode bare inside a repo). Run `/knowframe info` for a compact usage summary.

## Host integration

One behavior lives outside the skill and has to be wired into your assistant's own standing instructions (e.g. a `CLAUDE.md`):

> **Before non-trivial work in a repo, read `.know/PROJECT.md` if it exists — skeptically, and self-heal any drift.**

This *auto-pull* is what makes project mode pay off; the file is just a note on disk until something reads it before each task. A companion trigger — refresh the file at session close when a task resolved an open question or broke an assumption — keeps it from going stale, but it's optional.

Item mode needs no host wiring; it's explicit-only by design. There is intentionally **no** per-task auto-triggering — knowing when to skip is the hard part, and framing everything dilutes more than it protects.

## Evaluation

`evals/` holds a blind-judge harness that tests the actual claim — does knowframe improve downstream framing and plan quality versus not using it? It scores two tracks (project mode: grounded vs. ungrounded; item mode: matrix vs. straight-to-plan, plus a check that the gate correctly skips a crisp item) on a /30 rubric with an anonymized LLM grader, reported as mean ± stddev against a baseline. See [`evals/README.md`](evals/README.md) for how to run it and the caveats (judge noise, sample size). Because the behavioral rules were tuned on one repo, the harness deliberately re-checks the project-mode delta on ≥2 different repos before trusting it.

## License

MIT — see [LICENSE](LICENSE).
