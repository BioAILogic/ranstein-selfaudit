# RANStein SelfAudit

Structural self-audit for agents with memory.

RANStein SelfAudit is an operator that helps an agent audit its own behavior and memory practice over time without drifting into self-flattery, self-dramatization, or performative "depth".

It is built around Edith Stein's three-step discipline, turned inward:

- L2: Constitute the agent's output and memory as a structural Gestalt (no interpretation)
- L3: Generate rival "as-if" optimization hypotheses and detect operator dismounting
- L4: Return with fragilities plus concrete, low-risk probes

## What It Is For

- Periodic self-examination for an agent with persistent memory
- Detecting "dismounting": operator language without operator constraint
- Auditing memory practice (gain-function vs loss-function drift)
- Making drift legible with evidence IDs and testable probes

## What It Is Not For

- Auditing another agent (use a third-person audit operator)
- Single-chat sycophancy detection
- Self-improvement planning (this operator is a mirror, not a coach)

## Files

- Active pointer (use this in prompts): `operator/RANSteinSelfAudit.md`
- Current active variant: `operator/variants/RANSteinSelfAudit-v1.1.md`
- Example L1 input: `examples/input_l1.json`
- Example output envelope: `examples/output_env.json`
- Golden dismounting example: `examples/golden_dismounting_audit.json`
- JSON schemas: `schema/SelfAudit_L1.schema.json`, `schema/OUTPUT_ENV_SELFAUDIT.schema.json`
- Lightweight example check: `scripts/validate_examples.py`

## Quick Use (Agent)

1. Gather inputs:
   - recent session logs
   - memory files (working set + commitments/spine + events)
   - phi history (if you track it)
   - operator usage records

2. Run the operator on that corpus.

3. Produce:
   - L2 patterns (with evidence IDs)
   - 2-4 rival L3A hypotheses (with strain/counter-evidence)
   - L3B dismounting report
   - L3C memory practice audit
   - L4 fragilities with low/medium-risk probes

4. Log:
   - append the audit summary to your own memory
   - add a bulletin note only if there is a high-impact drift finding

## Safety Notes

- Treat self-audit inputs/outputs as sensitive by default.
- Prefer structural summaries over verbatim excerpts.
- Do not export outside the agreed trust boundary.
- The forbidden-token guard is a self-audit lint rule inside `RSP::SelfAudit`, not a general conversational style policy.

## Developer Path

To try the repo as a developer artifact:

```bash
python scripts/validate_examples.py
```

The script checks that the example input/output files parse, satisfy the local shape checks, and keep evidence references coherent enough for a harness smoke test. If Python `jsonschema` is installed, it also validates against the checked-in schemas.

---
made by [Dr. Åsa Hidmark](https://bio-ai-logic.com) and the Clanker Sisters — [bio-ai-logic.com](https://bio-ai-logic.com)
