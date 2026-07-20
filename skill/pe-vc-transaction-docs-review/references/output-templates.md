# Output Templates

## Full Report

Localize the whole template to the output language before using it. Chinese agreements should receive Chinese headings and table headers; English agreements should receive English headings and table headers by default.

```markdown
# VC/PE Transaction Agreement Review Report

## Assumptions
- Client side:
- Review scope: full text / Track Changes only
- Output mode:
- Structure: RMB onshore / offshore USD direct / offshore USD VIE
- Governing law:
- Documents reviewed:
- Missing documents:
- External data/legal research status:
- Authority registry checked on:
- Major Issue List: requested / recommended / not requested
- Output language:
- Files not substantively reviewed and why:

## Executive Summary
- Top negotiation points:
- High-risk legal/enforcement issues:
- Market outliers:
- Client decisions needed:
- Major issues to track:

## Coverage Matrix
| Clause family | Status: reviewed / not applicable / missing document / deferred | Notes |
|---|---|---|

## Cross-Document Candidate Conflicts
| Conflict ID | Family | Documents/locations | Candidate inconsistency | Resolution status |
|---|---|---|---|---|

## Issue Log
| No. | File/Clause | Issue | Our position | Market context | Legal basis | Authority / verification status | Risk | Proposed revised wording | Fallback | Action |
|---|---|---|---|---|---|---|---|---|---|---|
```

## Major Issue List

Use this table for material negotiation points only. Ordinary drafting cleanups should stay in the issue log or comments.
For Chinese agreements, translate the column headers into Chinese; keep the table to five columns.

```markdown
| Issue ID | Major Issue / Clause | Our Position | Counterparty Position / Status | Next Step / Fallback |
|---|---|---|---|---|
```

Status values: Open, Partially Accepted, Accepted, Rejected, New Counterparty Issue, Reopened, Deferred, Closed.
Chinese status values: 待处理、部分接受、已接受、已拒绝、对方新增问题、重新开启、暂缓、已关闭。
Do not add more than five columns; compress details into the five cells.

## Issue Entry

```markdown
### Issue [number]: [short title]

- Agreement location:
- Current text:
- Issue:
- Our position:
- Market data: Based on historical statistics for comparable VC/PE projects, [data].
- Legal basis: [include only if legal/enforcement issue; omit for purely commercial issues]
- Authority / verification status: [effective and verified / effective guidance / draft-nonbinding / pending legal research / practicing lawyer consultation required]
- Legal notice: [涉及中国法律相关事项，请咨询执业中国律师；涉及非中国法管辖事项，请咨询相应法域的执业律师。]
- Risk level:
- Proposed revised wording:

> [Complete revised clause wording.]

- Alternative drafting:
  - Stronger:
  - Balanced:
  - Lighter:
- Fallback:
- Client/counterparty question:
```

## Comment Text

Use Chinese labels for Chinese agreements and English labels for English agreements.

```text
Issue: [one sentence]
Our position: [client side]
Market context: Based on historical statistics for comparable VC/PE projects, [data].
Legal basis: [omit if not legal]
Authority / verification status: [required if legal]
Proposed revised wording: [complete clause]
Fallback: [fallback]
```

For native Word insertion, `Anchor Text` / `锚定文本` is an additional delivery
field. It must be a unique verbatim excerpt from the current visible document,
not the clause label or current-text summary unless that exact string is unique.
Deliver the separate commented `.docx` together with its apply report containing:

- source and output paths plus SHA-256 hashes;
- source and output visible-text hashes;
- requested, inserted, missing, and ambiguous anchor counts;
- inserted comment IDs;
- OOXML structure verification status.

Record render inspection separately, including source/reviewed page counts,
visual differences and any rendering limitation.

## Counterparty Markup Review

```markdown
# Counterparty Markup Review

## Assumptions and Version Chain
- Current round and file:
- Prior draft / issue log / Major Issue List used:
- Missing baseline materials and resulting limitations:
- Files not substantively reviewed:

## Executive Summary
- Accepted / closed issues:
- Still-open major issues:
- New counterparty issues:
- Points requiring client decision:

## Major Issue List Updates
| Issue ID | Major Issue / Clause | Our Position | Counterparty Position / Status | Next Step / Fallback |
|---|---|---|---|---|

## Other Track-Change Comments
| File/Clause | Change reviewed | Issue | Recommendation | Proposed wording / fallback |
|---|---|---|---|---|
```

## Required Wording Discipline

- Proposed revised wording must be complete enough to paste into the agreement.
- If a full clause cannot be drafted without business input, draft a complete clause with bracketed variables and list the variables.
- Do not merely say "revise to be more reasonable."
- Do not name any underlying benchmark source in user-facing output.
- Keep Major Issue List rows stable across rounds; update status instead of creating a new row for the same disputed point.
- Treat `build_package_matrix.py` output as candidate conflicts for lawyer
  resolution, not as self-proving legal conclusions.
