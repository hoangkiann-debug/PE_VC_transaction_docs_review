# PE/VC私募交易文件审阅

`PE/VC私募交易文件审阅` is an open Skill for reviewing transaction
documents involving investments in unlisted companies. It supports RMB and
offshore financing structures, company/founder-side and investor-side reviews,
first drafts and later-round markups, issue logs, clause comments, Major Issue
Lists, document-package checks, and reversible native Word comments.

The machine-compatible Skill ID is `pe-vc-transaction-docs-review`. The GitHub
repository and release package use `PE_VC_transaction_docs_review` because `/`
cannot be used in those names.

## Install

### Codex

Copy or link `skill/pe-vc-transaction-docs-review` into your Codex skills
directory, then invoke `$pe-vc-transaction-docs-review`.

### WorkBuddy

Upload the ZIP file in `dist/` through WorkBuddy's local Skill import function.
The ZIP contains one top-level folder named `pe-vc-transaction-docs-review`.

## Important limits

- This Skill assists professional review; it is not a substitute for matter-
  specific legal advice or review by qualified counsel.
- Market figures are historical negotiation context, not legal requirements.
- Non-PRC governing-law conclusions require appropriate local counsel.
- The public package contains no client files, client names, private article
  corpus, or underlying source-provenance registry.
- Before public release, run the repository tests and inspect the generated
  release manifest and privacy report.

See `DISCLAIMER.md`, `PRIVACY.md`, and `SECURITY.md`.
