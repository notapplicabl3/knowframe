# Worked Examples

Three examples showing decomposition into aspects, mapping across quadrants, and the resolution questions that follow. Note in each how a *single* topic spreads across multiple quadrants.

---

## Example 1 — Coding task

**Request:** "Add rate limiting to our public API."

**Decompose into aspects:** which endpoints, the limit values, the storage backend, the failure behavior, who the limit is keyed on, existing infra.

```markdown
## Known/Unknown Matrix: rate-limiting the public API

|                              | We know it                                              | We don't know it                                                  |
| ---------------------------- | ------------------------------------------------------- | ----------------------------------------------------------------- |
| **We know it matters**       | **Known knowns**<br>- It's a public REST API<br>- We can add middleware | **Known unknowns**<br>- Limit values (req/min)? → ask<br>- Per-IP or per-API-key? → ask<br>- Is there a shared Redis we can use? → research the repo |
| **We don't know it matters** | **Unknown knowns**<br>- *Assuming* limits apply to all endpoints equally<br>- *Assuming* a 429 response is acceptable (vs queueing) | **Unknown unknowns**<br>- Existing limits at the load balancer / CDN layer?<br>- Distributed-counter races if there are multiple app instances |
```

**To resolve before I start:**
1. What limits, and keyed on IP or API key? — *(known unknowns — you'll know)*
2. Should auth'd endpoints get higher limits than anonymous ones? — *(assumption to confirm)*
3. I'll grep the repo for an existing Redis/cache client before picking storage. — *(known unknown — research)*
4. Worth a 2-min check of whether the CDN already rate-limits, so we don't double up. — *(unknown unknown — offer)*

---

## Example 2 — Research question

**Request:** "Is it worth migrating us from Postgres to a time-series database?"

**Decompose into aspects:** what data is actually time-series, current pain, candidate DBs, migration cost, what "worth it" means.

```markdown
## Known/Unknown Matrix: Postgres → time-series DB migration

|                              | We know it                                                    | We don't know it                                                       |
| ---------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------- |
| **We know it matters**       | **Known knowns**<br>- We run Postgres today<br>- Some tables are append-heavy metrics | **Known unknowns**<br>- Current query latency / table sizes? → ask or measure<br>- Which TSDB candidates? → research |
| **We don't know it matters** | **Unknown knowns**<br>- *Assuming* the pain is read latency (could be write volume or cost)<br>- *Assuming* "worth it" = performance, not ops simplicity | **Unknown unknowns**<br>- Postgres extensions (TimescaleDB) that solve it without leaving<br>- Downstream tools that assume SQL/Postgres wire protocol |
```

**To resolve before I start:**
1. What's actually hurting today — latency, write throughput, or storage cost? — *(assumption to confirm; this redefines the whole question)*
2. What does "worth it" mean to you — speed, cost, or operational simplicity? — *(unknown known)*
3. I'll research TSDB options *and* TimescaleDB-as-an-extension, since staying on Postgres may dominate. — *(known + unknown unknown — research)*

---

## Example 3 — Decision

**Request:** "Should I price the new plan at $49 or $99?"

**Decompose into aspects:** target segment, current pricing, willingness to pay, competitor anchors, the goal behind the change.

```markdown
## Known/Unknown Matrix: $49 vs $99 pricing

|                              | We know it                                          | We don't know it                                                 |
| ---------------------------- | --------------------------------------------------- | ---------------------------------------------------------------- |
| **We know it matters**       | **Known knowns**<br>- Two candidate price points<br>- Existing plans and their prices (ask/confirm) | **Known unknowns**<br>- Target segment for this plan? → ask<br>- Competitor price anchors? → research |
| **We don't know it matters** | **Unknown knowns**<br>- *Assuming* the goal is revenue max (could be land-grab / market share)<br>- *Assuming* it's a one-time pick, not a test | **Unknown unknowns**<br>- Willingness-to-pay data you may already have (past tests, churn-by-price)<br>- Whether $49 vs $99 crosses a buyer's budget-approval threshold |
```

**To resolve before I start:**
1. Is the goal to maximize revenue, or grab market share fast? — *(unknown known — changes the answer entirely)*
2. Who's this plan for, and what do your current plans cost? — *(known unknowns — you'll know)*
3. Have you run any pricing tests before? — *(unknown unknown — you may already hold the data)*
4. I'll pull 3–4 competitor anchors for that segment. — *(known unknown — research)*

---

## What good resolution looks like

- The **highest-leverage questions challenge the framing itself** — the goal behind the request (revenue vs share, latency vs cost). These almost always live in unknown-knowns.
- Route each gap to its **cheapest resolver**: ask the user when they hold the answer, research when it's discoverable, don't research what a one-line question settles.
- Surface assumptions as assumptions. "I'm assuming X — correct?" is worth more than silently building on X.

---

## Example 4 — A full written knowframe (the file format)

This is what gets written to `.know/<slug>.md` for a non-trivial item. Note the conceptual depth in **every** quadrant — especially the bottom row, which a plan could never produce.

```markdown
# Understanding: SaaS to help first-time business owners figure out logistics + who to contact
<!-- knowframe · comprehension layer · revise in place -->

- **Captured:** 2026-06-25  ·  **Status:** draft -> (reflected / confirmed)

## 1. What I think you're actually asking for
A guided tool that takes a would-be owner from "I have an idea" to a concrete, ordered,
personalized checklist of logistical steps (entity, licenses, tax, banking, insurance)
AND the specific people/agencies to contact for each. The implied core value is reducing
overwhelm and unknown-unknowns for someone who doesn't know what they don't know — a
sequencer + router, not a directory.

## 2. Decomposed aspects
1. Who exactly is the user? (solo founder, trade, restaurant, location)
2. What "logistics" means — its true scope and boundaries
3. Personalization logic (what makes one owner's path differ)
4. The "who to contact" data — source and freshness
5. Regulatory exposure (is this legal/tax advice?)
6. Business model (why this vs. free .gov resources)
7. Build surface (the actual software)

## 3. The matrix

|                            | We know it                       | We don't know it                     |
| -------------------------- | -------------------------------- | ------------------------------------ |
| **We know it matters**     | sequencer+router, blind-spot value | scope boundary, true differentiator |
| **We don't know it matters** | assuming US / web app / advice-safe | regulated-advice risk, existing players |

### Known knowns — established
- It's a *sequencer + contact-router*, not a static directory. `[load-bearing]`
- Value hinges on handling the user's blind spots, not just listing steps.

### Known unknowns — open questions (conceptual first, then technical)
- What does "all the logistics" bound to? Without a hard scope this is infinite. `[load-bearing]`
- Is the differentiator the *sequencing intelligence* or the *contact data*? Different products. `[load-bearing]`
- (technical) Where does jurisdiction-specific contact data come from, and who keeps it current? -> research

### Unknown knowns — assumptions I'm making (flag any that are wrong)
- *Assuming* US-based owners — laws/agencies are jurisdiction-specific; this reshapes the whole data model. `[load-bearing]`
- *Assuming* a web app, not a human-assisted/concierge service.
- *Assuming* it stays on the "information, not legal/tax advice" side of the line. `[load-bearing]`
- *Assuming* "first-time owner" = small/solo, not a funded startup founder.

### Unknown unknowns — blind spots & directions to probe
- Does this already exist well? Stripe Atlas, LegalZoom, ZenBusiness, SBA/SBDC cover slices — what's the gap? -> research
- Regulated-advice territory? Routing "who to contact" may edge into UPL / tax-advice exposure. -> probe
- Growth direction: stays a checklist, or pulls toward becoming the filing-agent that *does* the steps? Big fork.
- Data-decay may be the real moat-or-killer — the hard part is maintenance, not the app.

## 4. What this implies (feed-forward to planning — pointers, not steps)
- The scope boundary and the US-jurisdiction assumption are load-bearing; resolve both before any data-model or build planning.
- Settle "sequencing vs. contact-data differentiator" first — it decides what the product even is.

## Revision log
- 2026-06-25 — initial draft (pre-reflection)
```

---

## Example 5 — Project mode (`.know/PROJECT.md`, the persisting file)

Built by a **deep** first pass (cost is fine), then auto-pulled before non-trivial work and self-healed when it goes stale. Note the project-flavored quadrants and the `Last verified` line.

```markdown
# Project understanding: acme-billing-api
<!-- knowframe · comprehension layer · persisting · read skeptically + self-heal -->

- **Last verified:** 2026-06-25

## What I think this project is
A FastAPI service that issues and reconciles subscription invoices against Stripe,
with a Postgres ledger as source of truth. Webhooks drive state; a nightly job
closes billing periods. The hard part is idempotency across retried webhooks.

## Decomposed aspects
1. HTTP/API layer  2. Stripe webhook ingestion  3. Ledger/Postgres  4. Period-close job  5. Auth  6. Tests/CI

## The matrix

|                            | We know it                          | We don't know it                       |
| -------------------------- | ----------------------------------- | -------------------------------------- |
| **We know it matters**     | FastAPI + Postgres + Stripe (verified) | how period-close handles partial failures |
| **We don't know it matters** | assuming webhooks are idempotent by design | a second consumer of the ledger?      |

### Known knowns — established
- FastAPI app, Postgres via SQLAlchemy, Stripe SDK — confirmed in `pyproject.toml` + `app/`.
- Webhooks are the primary state driver; `app/webhooks/` handlers map events → ledger writes. `[load-bearing]`

### Known unknowns — open questions
- How does the nightly period-close (`jobs/close.py`) behave on partial failure / mid-run crash? `[load-bearing]` -> read + ask
- Is there a staging Stripe account, or do tests hit a mock? -> check CI

### Unknown knowns — assumptions I'm making (flag if wrong)
- *Assuming* webhook handlers are idempotent (retries are safe) — not yet verified. `[load-bearing]`
- *Assuming* Postgres is the single source of truth and nothing else writes the ledger. `[load-bearing]`
- *Assuming* the API is internal-only (no public consumers shaping back-compat).

### Unknown unknowns — blind spots
- Any downstream/analytics consumer reading the ledger tables directly? -> grep + ask
- Money/rounding conventions and multi-currency handling — haven't looked. -> probe

## What this implies (before working in this repo)
- Verify webhook idempotency before touching ingestion — it's an unverified load-bearing assumption.
- Confirm period-close failure behavior before changing the nightly job.

## Revision log
- 2026-06-25 — initial deep pass
```
