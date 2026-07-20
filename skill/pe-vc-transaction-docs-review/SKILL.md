---
name: pe-vc-transaction-docs-review
description: Review, issue-spot, comment, redline, track counterparty markups, and prepare Major Issue Lists/negotiation outputs for VC/PE investment agreement packages, including VC/PE, private equity, venture capital,投融资协议,股东协议,增资协议,增资协议补充协议,认购协议,公司章程,SPA,SHA,IRA,M&A,M&AA,MAA,term sheet,红筹架构,人民币架构,境内融资,境外美元融资,VIE,offshore financing,share subscription,shareholders agreement,memorandum and articles,investment agreement,share purchase,convertible loan,down-round,redemption,anti-dilution,liquidation preference,drag-along,ROFR,co-sale,protective provisions,investor rights,founder restrictions,registered capital contribution,注册资本缴纳,出资期限,实缴,股东失权,side letter,counterparty markup,Track Changes,major issue list,主要争议清单,or related transaction documents. Do not use for private fund formation/regulation, bankruptcy restructuring investment, standalone licensing/BD, or pure AMAC questions unless directly tied to an in-scope VC/PE agreement review.
---

# PE/VC私募交易文件审阅

Use this skill to review VC/PE financing transaction documents from a company/founder-side or investor-side position. The core method is: identify structure first, map the document package, use market benchmark data as negotiation context, apply PRC law and dispute-risk checks where relevant, and deliver issue-log/comment/redline outputs that lawyers can use.

Treat `references/review-quality-gates.md` as the completion contract. A file that cannot be extracted, a later-round acceptance conclusion without a baseline, or a legal conclusion based only on an unverified/draft source is not review-complete.

The financing target is ordinarily an unlisted company. Do not route an already-listed target's valuation-adjustment, redemption or securities dispute into this skill merely because it uses similar transaction terminology. Pre-IPO special-rights treatment for an unlisted target remains in scope, as does an investment by a listed-company investor into an unlisted target.

## First Questions

Before substantive review, resolve these choices through the user's instructions and a preliminary file/package check:

1. Review scope: full agreement/package, or only Track Changes / revision marks since the prior draft.
2. Output mode: full report, clause-by-clause comments beside the relevant provisions, or both.
3. Whether to generate or update a Major Issue List for material negotiation points.
4. Output language: match the primary transaction document language unless the user instructs otherwise.
5. Client side: company/founder, investor, lead investor, follow-on investor, existing shareholder, or strategic investor.
6. Structure: RMB onshore, or offshore USD. For offshore USD, further classify as direct offshore holding of PRC entities or VIE control structure.
7. Governing law and local counsel needs: PRC, Hong Kong, Cayman, Delaware, New York, Singapore, or other.
8. Matter boundary: current matter only by default; confirm any permission to use another matter, prior deal, or external entity data.
9. Regulatory investor profile: state-owned/government-backed, insurance capital, listed company, foreign/outbound, strategic/competitor-sensitive, or ordinary financial investor.

For first-draft full-package review, do not begin substantive clause review until the mandatory intake items are either answered by the user's instructions, clear from the file/package context, or expressly authorized as assumptions by the user.

## Intake Gate

Use a two-step intake gate when the request is ambiguous:

1. Pre-intake triage: read the user's instructions and perform a non-substantive file/package check. You may inspect file names, build a document map, identify draft round, detect primary language, and form preliminary structure/law assumptions. Do not analyze clauses or draft recommendations during this step.
2. Gap questions: ask only for mandatory items that are missing, ambiguous, or inconsistent. Do not repeat questions already answered by the user's instructions or clearly answered by the files.

When asking, briefly summarize:

- Confirmed from user instructions.
- Detected from files/package context.
- Still needed before substantive review.

Mandatory for first-draft full-package review:

- Document source: files/folder to review and whether this is a first draft/full-package review.
- Client side: company/founder, investor, lead investor, follow-on investor, existing shareholder, or strategic investor.
- Output mode: full report, comments-only/comment plan, both, or redline if expressly requested.
- Major Issue List: create one, do not create one, or decide after issue severity is known.
- Structure: RMB onshore, offshore USD direct holding, or offshore USD VIE. If unclear, ask whether to infer from the documents.
- Governing law/dispute forum and whether non-PRC local counsel flags should be included.
- Output language: follow the primary transaction-document language unless the user instructs otherwise.

If any mandatory item remains missing after pre-intake triage, ask the user to confirm only those missing items and wait. If the user says to proceed with assumptions, state those assumptions before starting the substantive review.

Mandatory for second-or-later Track Changes / counterparty markup review:

- Current markup: the current draft/redline files to review and the round number if known.
- Review scope: Track Changes only, compare current clean draft against prior draft, or full re-review.
- Baseline materials: prior draft, prior issue log/comment plan, prior Major Issue List, and any counterparty response email. If unavailable, ask whether to proceed with stated limitations.
- Client side, structure, governing law, and output language: confirm they are unchanged from prior round or update them.
- Output mode: delta review memo, updated Major Issue List, clause-level comments/comment plan, or a combination.
- Major Issue List handling: update the existing list, create one if none exists, or skip it.

For later-round review, first check whether the current files and user instructions already identify the draft round, redline/Track Changes status, baseline materials, prior positions, and desired output. Ask only for missing or conflicting items.

If mandatory later-round materials remain missing after that pre-check, ask the user to provide them or expressly authorize a limited review. Do not classify counterparty changes as accepted/rejected/partially accepted unless a prior position or baseline is available.

## Core Workflow

1. Read `references/review-quality-gates.md`, `references/intake-and-routing.md`, and `references/matter-profile-and-confidentiality.md`. Complete the matter/intake gate before substantive review.
2. Build a document map for the whole package with `scripts/build_document_map.py`. Treat filename-based type, language, structure, and version results as intake hints; confirm them from operative text.
3. Extract every in-scope file with `scripts/extract_contract_text.py`. Record extraction method and readiness. If a file is empty or failed, run `scripts/ocr_pdf_macos.py` where feasible or mark that file as not substantively reviewed. Do not infer that an unread file is clean.
4. For a multi-document package, run `scripts/build_package_matrix.py`. Review its candidate definition, amount, cap-table, rights and dispute-forum conflicts; do not treat pattern-based candidates as legal conclusions. Resolve material conflicts against operative text and record missing or unread files.
5. Determine the primary document language from operative text before drafting output. Chinese agreements require Chinese output; English agreements require English output by default.
6. If Track Changes-only review is requested, use `scripts/extract_contract_text.py --scope track-changes` for `.docx`. Review `changed_paragraphs` using `before_text` and `after_text`, then drill into change metadata as needed. If revision markers exist without text-bearing changes, report that boundary and compare against a prior draft or run a full review. If high-volume Track Changes are detected, pause and ask whether to perform a full redline review, core-clause-focused review, or Major Issue List-focused review. For PDFs, inspect redline pages manually and explain limitations.
7. For second or later drafts, read `references/multi-round-review.md`. If both files are clean, isolate clause-level deltas with `scripts/compare_contract_versions.py <prior> <current>` before applying legal judgment. Manually confirm low-confidence fuzzy, split/merge, table and unnumbered-prose alignments. Compare revisions against the prior issue log and Major Issue List, then merge approved status updates with `scripts/update_major_issue_list.py` so existing Issue IDs remain stable.
8. If external legal/entity/document connectors may be used, read `references/connector-degradation-policy.md`. If target facts affect the review, read `references/entity-and-diligence-data-layer.md`. Label connected, configured-but-unverified, and unavailable states accurately.
9. Read the structure playbook:
   - RMB onshore: `references/rmb-structure-playbook.md`
   - Offshore USD direct/VIE: `references/offshore-structure-playbook.md`
10. Read `references/clause-review-checklists.md`, `references/recent-practice-stress-tests-2024-2026.md`, and `references/negotiation-pattern-stress-tests.md`, then record each relevant family as reviewed, not applicable, missing-document, or deferred. Every clause analyzed in the current 2024/2025 benchmark is key under both RMB and offshore structures; RMB limited liability companies also require registered-capital contribution review. Apply the stress-test prompts only to the detected structure, investor profile, document family and facts; they are not legal authority or frequency evidence. Historical drafting movement is a neutral issue-spotting signal, not proof of party intent, optimal drafting or current market practice.
11. Look up benchmarks with `references/market-benchmarks-2023-2024.md`, bundled structured data at `references/benchmark-data.json`, or `scripts/benchmark_lookup.py`. Treat the data as market context only. Independently verify the historical figures before annual updates or high-stakes reliance; the public package intentionally omits underlying source-provenance records.
12. For every legal/enforceability issue, read `references/legal-authority-protocol.md`, the structured registry at `references/legal-authorities.json`, and `references/prc-law-risk-notes.md`, then use `scripts/legal_authority_lookup.py` and relevant material from `references/article-digest.md`. Verify authority level, status, pinpoint, and date; commentary is not primary authority. Current routed topics include redemption exercise periods, the 2025 cross-border FX reform, the 2025 state-owned asset transaction rules, the 2025 insurance-capital major-equity rule, and the outbound-investment regulation effective from 2026-07-01. Use `scripts/refresh_legal_authorities.py --check-urls` for a refresh report, treating anti-bot/TLS results as inconclusive rather than proof that an authority is invalid.
13. Apply client-specific guidance from `references/party-side-positions.md`.
14. Deliver using `references/output-templates.md` and `references/comment-only-review-mode.md`. Use the matching English or Chinese asset templates. For native comments, require exact anchor excerpts, write to a separate output with `scripts/apply_comment_plan.py apply`, and require source-file integrity, unchanged visible-text hashes, valid OOXML comment wiring and clean render inspection. Use the same script's `rollback` command to remove only comments listed in the apply report.
15. For full first-draft reviews, offer to prepare a Major Issue List for material points likely to remain in negotiation. For later rounds, update the existing list. Keep it at exactly five semantic columns and no more than five physical columns.
16. Validate issue logs with `scripts/validate_issue_log.py`, Major Issue Lists with `scripts/validate_major_issue_list.py`, and package consistency with `scripts/validate_skill_consistency.py` before final delivery or release where feasible.

When evaluating or changing this skill itself, read `references/evaluation-protocol.md`. Prepare isolated synthetic bundles with `scripts/prepare_blind_evaluation.py` and score completed submissions with `scripts/score_blind_evaluation.py`. Do not claim legal-quality passage from automatic artifact/keyword scores without the independent six-dimension lawyer scorecard.

## Output Discipline

Language rule:

- If the reviewed transaction documents are primarily Chinese, every generated output must be in Chinese, including report headings, table headers, issue summaries, comments, market context, legal analysis, Major Issue List, proposed revised wording, and fallbacks.
- If the reviewed transaction documents are primarily English, every generated output should be in English by default, including comments and proposed revised wording.
- Preserve quoted agreement text, party names, defined terms, clause numbers, and governing-law terminology in their original language unless translation is needed for explanation.
- For bilingual or mixed-language packages, use the language of the primary operative agreement or the controlling version. If unclear, infer and state the assumption or ask the user.

Each recommendation must include:

- Agreement location: file, section/article number, page if available, and quote or concise excerpt.
- Issue: what is wrong, missing, unusually broad/narrow, inconsistent, or commercially sensitive.
- Our position: company/founder-side, investor-side, lead/follow-on/strategic investor, or neutral.
- Market data: cite only as "based on historical statistics for comparable VC/PE projects" or similar; do not name the underlying law firm/report source in user-facing outputs.
- Legal basis: required for legal validity, enforceability, PRC company law, dispute resolution, or execution-risk issues. Not required for purely commercial, drafting, or business-position issues.
- Authority / verification status: for every legal issue, state effective/verified, effective guidance, draft-nonbinding, pending legal research, or local-counsel confirmation required.
- Proposed revision: provide complete and rigorous revised clause wording, not only a summary.
- Alternatives: if multiple levels are sensible, provide stronger / balanced / fallback versions.
- Fallback: commercially acceptable fallback position if the preferred revision is not accepted.

For comments-only delivery, the `Anchor Text` / `锚定文本` field must contain a unique verbatim excerpt from the current visible DOCX text. A summary that does not occur in the document is not a valid native-comment anchor.

Never state that a benchmark is a legal requirement. Treat benchmarks as market/negotiation context only.

Never state a consultation draft or secondary article as effective law. Re-check bundled legal authorities when the registry is stale or the matter points to a later rule.

Benchmark method:

- Use the 2025 current-year statistic as the primary anchor.
- Where exact comparable 2024 and 2025 figures are available in the benchmark reference, use the 2024/2025 two-year average.
- Where 2024 is unavailable, not comparable, or the 2025 report provides only a trend statement, use 2025 only and mark that internally.

## Delivery Modes

- Full report: issue log plus executive summary and negotiation priorities.
- Comments-only: comment plan or verified native Word comments anchored to specific provisions; do not alter visible original text and never overwrite the source file.
- Both: full report plus comment plan/comments.
- Major Issue List: table of material negotiation points for first draft and every subsequent counterparty markup round.
- Redline: only when the user expressly asks for redline/tracked changes. For first-pass review, prefer comments-only plus issue log.

## Validation Utilities

- Use `scripts/smoke_test_transactions.py <folder> --strict --format md` to regression-test extraction/routing and return non-zero on critical failures. Add `--anonymize` before sharing any report outside the private matter workspace.
- Use `scripts/validate_issue_log.py <issue-log.csv>` before delivering an issue log where feasible.
- Use `scripts/make_comment_plan.py <issue-log.csv> --language auto` to convert report issues into clause-level comment plans.
- Use `scripts/make_major_issue_list.py <issue-log.csv> --language auto` to seed a Major Issue List from material issues in a first-draft review.
- Use `scripts/update_major_issue_list.py <existing.csv> <updates.csv>` to merge later-round changes while preserving Issue IDs.
- Use `scripts/compare_contract_versions.py <prior> <current>` when later-round files are clean and native Track Changes are unavailable; review clause identity, renumbering, movement, split/merge and fallback confidence, and treat alignment as a textual delta rather than acceptance/rejection proof.
- Use `scripts/build_package_matrix.py <files-or-folder> --strict` for candidate cross-document definition, rights, numeric, cap-table and dispute-mechanism conflicts.
- Use `scripts/apply_comment_plan.py apply <source.docx> <comment-plan.csv> --output <commented.docx> --report <report.json>` for native comments; use its `rollback` subcommand with that report for a reversible clean copy.
- Use `scripts/validate_major_issue_list.py <major-issue-list.csv>` before delivering or updating a Major Issue List where feasible.
- Use `scripts/benchmark_lookup.py <terms>` for market context and `scripts/legal_authority_lookup.py <terms> --check-freshness` for legal research routing.
- Use `scripts/refresh_legal_authorities.py --check-urls` to produce a schema, temporal-status and official-URL health report; manually verify blocked/inconclusive sources before changing `last_verified`.
- Use `scripts/validate_skill_consistency.py` after changing skill references, schemas, templates, or scripts.
- Use `scripts/prepare_blind_evaluation.py` and `scripts/score_blind_evaluation.py` only for isolated skill evaluation under `references/evaluation-protocol.md`.
- Use `scripts/ocr_pdf_macos.py <file.pdf>` when PDF text extraction is empty and the machine can use macOS Vision OCR.

## Safety Boundaries

- Do not review private fund formation, AMAC filing, asset management regulation, training/news, or fund compliance articles unless they are directly tied to a VC/PE transaction agreement.
- Do not silently expand into bankruptcy restructuring investment agreements or standalone biotech licensing/BD agreements. Treat those as separate document families requiring express scope confirmation and dedicated checklists.
- Do not give final opinions on Cayman, Hong Kong, Delaware, New York, Singapore, or other non-PRC law. Flag local-counsel confirmation points.
- Do not treat a draft judicial interpretation, consultation paper, meeting minute, law-firm article, or unverified database result as effective legislation or a binding judicial interpretation.
- Do not assume missing documents are clean. Mark missing disclosure letters, articles/章程, side letters, ESOP plans, VIE documents, board/shareholder approvals, or closing documents.
- Do not treat enterprise-data search results as confirmed disclosure by the parties.
- Do not read across client matters unless the user expressly asks for cross-matter comparison.
