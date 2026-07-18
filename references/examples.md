# Worked Examples

Examples of decomposition, quadrant mapping, and resolution questions. One topic can span multiple quadrants.

---

## Example 1 — Coding task

**Request:** "Add rate limiting to our public API."

**Decompose into aspects:** endpoints, limits, storage, failure behavior, keying, infra.

```markdown
## Known/Unknown Matrix: rate-limiting the public API

|                              | We know it | We don't know it |
| ---------------------------- | ---------- | ---------------- |
| **We know it matters**       | **Known knowns**<br>- Public REST API<br>- Middleware possible | **Known unknowns**<br>- Limit values? → ask<br>- IP or API-key? → ask<br>- Shared Redis/cache? → research |
| **We don't know it matters** | **Unknown knowns**<br>- *Assuming* all endpoints share limits<br>- *Assuming* 429 is acceptable | **Unknown unknowns**<br>- LB/CDN limits?<br>- Multi-instance counter races |
```

**To resolve before I start:**
1. Limits and key? *(known unknowns)*
2. Higher limits for auth'd endpoints? *(assumption)*
3. Grep for Redis/cache. *(research)*
4. Check LB/CDN limits. *(unknown unknown)*

---

## Example 2 — Decision

**Request:** "Should I price the new plan at $49 or $99?"

**Decompose into aspects:** segment, current pricing, willingness to pay, competitor anchors, goal.

```markdown
## Known/Unknown Matrix: $49 vs $99 pricing

|                              | We know it | We don't know it |
| ---------------------------- | ---------- | ---------------- |
| **We know it matters**       | **Known knowns**<br>- Two candidate prices<br>- Current plan prices need confirming | **Known unknowns**<br>- Target segment? → ask<br>- Competitor anchors? → research |
| **We don't know it matters** | **Unknown knowns**<br>- *Assuming* revenue max, not market share<br>- *Assuming* one-time pick, not a test | **Unknown unknowns**<br>- Prior tests / churn-by-price data?<br>- Buyer approval threshold at $99? |
```

**To resolve before I start:**
1. Revenue max or fast market share? *(unknown known — changes answer)*
2. Who's this for, and current plan prices? *(known unknowns)*
3. Any prior pricing tests? *(unknown unknown)*
4. Pull 3–4 competitor anchors. *(research)*

---

## What good resolution looks like

- The **highest-leverage questions challenge the framing itself** — goal behind request (revenue vs share, latency vs cost), usually unknown-knowns.
- Route each gap to its **cheapest resolver**: ask when the user holds it, research when discoverable, don't research what one question settles.
- Surface assumptions as assumptions. "I'm assuming X — correct?" beats silently building on X.

---

## Example 3 — A full written knowframe (the file format)

This is what gets written to `.know/<slug>.md` for a non-trivial item. Note depth in **every** quadrant, especially the bottom row.

```markdown
# Understanding: SaaS to help first-time business owners figure out logistics + who to contact
<!-- knowframe · comprehension layer · revise in place -->

- **Captured:** 2026-06-25  ·  **Status:** draft -> (reflected / confirmed)

## 1. What I think you're actually asking for
A guided tool that turns "I have an idea" into an ordered checklist + contact route for entity, licenses, tax, banking, insurance, and agencies/people to call. Core value: reduce overwhelm and unknown-unknowns; a sequencer + router, not a directory.

## 2. Decomposed aspects
1. User type  2. Logistics scope  3. Personalization logic  4. Contact-data freshness  5. Legal/tax exposure  6. Business model  7. Build surface

## 3. The matrix

|                            | We know it | We don't know it |
| -------------------------- | ---------- | ---------------- |
| **We know it matters**     | sequencer+router, blind-spot value | scope boundary, true differentiator |
| **We don't know it matters** | assuming US / web app / advice-safe | regulated-advice risk, existing players |

### Known knowns — established
- It's a *sequencer + contact-router*, not a static directory. `[load-bearing]`
- Value hinges on handling blind spots, not just listing steps.

### Known unknowns — open questions (conceptual first, then technical)
- What does "all the logistics" bound to? Without a hard scope this is infinite. `[load-bearing]`
- Is the differentiator *sequencing intelligence* or *contact data*? Different products. `[load-bearing]`
- (technical) Where does jurisdiction-specific contact data come from, and who keeps it current? -> research

### Unknown knowns — assumptions I'm making (flag any that are wrong)
- *Assuming* US-based owners — laws/agencies are jurisdiction-specific; this reshapes the data model. `[load-bearing]`
- *Assuming* a web app, not a human-assisted/concierge service.
- *Assuming* it stays on the "information, not legal/tax advice" side. `[load-bearing]`
- *Assuming* "first-time owner" = small/solo, not a funded startup founder.

### Unknown unknowns — blind spots & directions to probe
- Does this already exist well? Stripe Atlas, LegalZoom, ZenBusiness, SBA/SBDC cover slices — what's the gap? -> research
- Regulated-advice territory? Routing "who to contact" may edge into UPL / tax-advice exposure. -> probe
- Growth fork: checklist, or filing-agent that *does* the steps?
- Data-decay may be the moat-or-killer — maintenance, not the app.

## 4. What this implies (feed-forward to planning — pointers, not steps)
- Resolve scope boundary and US-jurisdiction assumption before data-model/build planning.
- Settle "sequencing vs. contact-data differentiator" first — it decides what the product is.

## Revision log
- 2026-06-25 — initial draft (pre-reflection)
```

---

## Example 4 — Project mode (`.know/PROJECT.md`, the persisting file)

Built by a **deep** first pass, then auto-pulled before non-trivial work and self-healed when stale. Note project quadrants and `Last verified`.

```markdown
# Project understanding: acme-billing-api
<!-- knowframe · comprehension layer · persisting · read skeptically + self-heal -->

- **Last verified:** 2026-06-25

## What I think this project is
A FastAPI service issuing/reconciling Stripe invoices with a Postgres ledger as source of truth. Webhooks drive state; a nightly job closes periods. Hard part: idempotency across retried webhooks.

## Decomposed aspects
1. HTTP/API layer  2. Stripe webhook ingestion  3. Ledger/Postgres  4. Period-close job  5. Auth  6. Tests/CI

## The matrix

|                            | We know it | We don't know it |
| -------------------------- | ---------- | ---------------- |
| **We know it matters**     | FastAPI + Postgres + Stripe (verified) | how period-close handles partial failures |
| **We don't know it matters** | assuming webhooks are idempotent by design | a second consumer of the ledger? |

### Known knowns — established
- FastAPI app, Postgres via SQLAlchemy, Stripe SDK — confirmed in `pyproject.toml` + `app/`.
- Webhooks are the primary state driver; `app/webhooks/` handlers map events → ledger writes. `[load-bearing]`

### Known unknowns — open questions
- How does nightly period-close (`jobs/close.py`) behave on partial failure / mid-run crash? `[load-bearing]` -> read + ask
- Is there a staging Stripe account, or do tests hit a mock? -> check CI

### Unknown knowns — assumptions I'm making (flag if wrong)
- *Assuming* webhook handlers are idempotent (retries are safe) — not yet verified. `[load-bearing]`
- *Assuming* Postgres is the single source of truth and nothing else writes the ledger. `[load-bearing]`
- *Assuming* the API is internal-only (no public consumers shaping back-compat).

### Unknown unknowns — blind spots
- Any downstream/analytics consumer reading ledger tables directly? -> grep + ask
- Money/rounding conventions and multi-currency handling — haven't looked. -> probe

## What this implies (before working in this repo)
- Verify webhook idempotency before touching ingestion — it's an unverified load-bearing assumption.
- Confirm period-close failure behavior before changing the nightly job.

## Revision log
- 2026-06-25 — initial deep pass
```
