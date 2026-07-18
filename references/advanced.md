# Advanced passes — fork-check and loop mode

**Read this file only when a trigger below fires; neither pass is part of the default workflow.**

- **Fork-check** — load when an item is *genuinely ambiguous*: the request could be read several ways and the reading chosen would steer everything downstream.
- **Loop mode** — load when the user asks to iterate/harden a knowframe to convergence, or a project-mode deep-hardening pass is requested.

## Fork-check (ambiguous items only)

A single pass can silently collapse an ambiguous request to one reading *without ever feeling uncertain* — a failure invisible to introspection, so re-reading your own framing won't surface it. Instead, re-derive **only** the interpretation ("what are they actually asking for?") once in a **fresh subagent that can't see your first reading**, then compare on substance, not wording.

- *Converge* → the reading is stable; proceed.
- *Diverge* → you've found a fork a single pass would have hidden; make it the **lead hand-off question** (workflow step 5), not a guessed one.

One extra pass, interpretation only — skip it on crisp tasks. It can't catch two passes collapsing to the *same* wrong reading (only the user can), so it sharpens the lead question; it doesn't replace the falsifiers or the ask. It does **not** transfer to project mode (see `project-mode.md`, sibling file).

## Loop mode (investigation-driven refinement)

Iterate a knowframe to convergence instead of producing it in one pass — but **each pass must drive an unknown to resolution, not rewrite the matrix.** Re-phrasing the boxes without new investigation is the closure trap and does *not* count as a pass. One pass:

1. Take the single highest **load-bearing, still-unresolved** item — an open known-unknown, or an unverified unknown-known assumption.
2. **Drive it:** run the cheapest probe that could settle it (grep / read / verify; or surface it as the one question if only the user can).
3. **Apply the result:** resolve or downgrade it, log the **quadrant migration** (e.g. *assumption → known-known, verified via X*), and add any new unknown the probe exposed.

**Converged when** no load-bearing item remains un-probed — each is either resolved or marked residual with its degree named (a probe was tried and it genuinely needs the user, or is irreducibly uncertain). Also stop on a pass that produces no migration and no new probe (converged, or *stuck* — if stuck, surface what's blocking), or at a hard cap of ~5 passes. **Progress is measured by migrations, never by text edits** — that's what keeps the loop honest.

Composes with `/orchestrate` iterate mode. Most valuable for **project-mode hardening** (drive every load-bearing assumption in `.know/PROJECT.md` to verified-against-code); also usable on a genuinely ambiguous new item.
