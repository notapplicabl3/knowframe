# concise vs current SKILL.md — item-mode A/B, 2026-07-17

**Question:** does a ~31% smaller SKILL.md (rationale prose stripped, rules kept) hold or beat the wordier version on real framing performance?

**Design:** item_mode track, all 3 cases (im_idea_vague, im_decision_vague, im_crisp) × 2 variants × n=3 independent producer agents = 18 artifacts; seeded-shuffle anonymization; 2 blind judges per case on rubric.md (/30), scores averaged — 36 judgments total. Producers ran the variant SKILL.md verbatim in a no-repo, no-interaction frame. Round 1 was discarded (harness path bug caused differential producer failures); round 2 ran 18/18 valid.

**Variants:** `current` = the 131-line / 16.1K SKILL.md. `concise` = ~11.1K rewrite: same gates, quadrants, workflow, template, and mechanics; rationale compressed to single clauses; plus two additions driven by round-1 judge notes — feed-forward must derive an **interim default + flip condition** for decision items, and unknown-unknowns aims for **≥3 distinct blind spots**.

## Result

| variant | overall /30 (n=18) | im_idea_vague | im_decision_vague | im_crisp |
|---|---|---|---|---|
| current | 25.17 ± 1.50 | 26.00 | 23.83 | 25.67 |
| **concise** | **27.50 ± 1.42** | **27.00** | **27.50** | **28.00** |

Delta +2.33 overall — above the 1–2 pt judge-noise band. Concise won every case and every criterion; largest gaps on prioritization (4.83 vs 3.89) and decision handle (4.78 vs 4.44).

## Reading

- The interim-default + flip-condition rule is the single biggest scorer — judges repeatedly called it out ("makes the plan unblockable before the answer arrives").
- The wordier variant's extra rationale did not buy depth; it cost signal-to-noise ("meta ceremony", "gate-check preamble noise"). Rules carry the behavior; rationale mostly narrates.
- Caveats: one judge-pair per case round, item-mode only (project mode untested — its text lives in references/ and was identical across variants), n=3 per cell. The concise win is directionally solid but the decision-case gap carries most of the delta.

**Action taken:** concise installed as SKILL.md.
