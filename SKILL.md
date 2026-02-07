# SKILL: RANSteinSelfAudit

This repository packages one operator as a skill-like artifact: **RANStein SelfAudit**.

## Intended User

- Humans who collaborate with agents and want a disciplined self-audit routine
- Agents (Codex/OpenClaw/Claude Code/etc.) with persistent memory across sessions

## How To Use (Minimal)

1. Load the operator text:
   - `operator/RANSteinSelfAudit.md` (active pointer)

2. Provide the operator with a corpus of the agent's own artifacts:
   - session logs
   - memory files
   - phi history (optional)
   - operator usage records (optional)

3. Ask for the operator's output envelope:
   - L2 patterns
   - L3A hypotheses (2-4 rivals, "as-if")
   - L3B dismounting detections
   - L3C memory practice findings
   - L4 fragilities and probes

## How To Use (OpenClaw Agents)

- Prefer loading the unversioned pointer so prompts stay stable:
  - `C:\Users\asahi\Killroy_Vault\60_Operators\RANStein\variants\RANSteinSelfAudit.md`

## What To Store

- Store the audit summary in the agent's own memory.
- If you share with sister agents, share only:
  - the high-level findings
  - the probes
  - minimal evidence IDs

Avoid sharing verbatim excerpts.

## Versioning

- The unversioned pointer file is the canonical entrypoint.
- Versioned variants live under `operator/variants/`.

---
made by Asa Hidmark and the Clanker Sisters asa.hidmark@bio-ai-logic.com