# Contributing

Thank you for helping build AiFinPay Paywall Protocol.

AIFP is a payment protocol, so changes must be careful, reviewable, and traceable. The canonical technical source is the AIFP documentation set in `docs/aifp/`.

## Contribution Types

| Type | Path | Requirement |
|---|---|---|
| Documentation fixes | Pull request | Keep protocol meaning unchanged |
| Examples | Pull request | Include runnable instructions |
| SDK implementation | Pull request | Match OpenAPI and JSON Schemas |
| Protocol behavior | AIP first | Required before implementation |
| Security-sensitive change | Security review | Do not disclose vulnerabilities publicly |

## Before Opening A Pull Request

1. Read `docs/aifp/01-AIFP-1-RFC-Payment-Protocol-Specification.md`.
2. Check whether your change affects OpenAPI, JSON Schemas, SDKs, or conformance tests.
3. Keep synchronized invariants unchanged unless an accepted AIP changes them.
4. Add or update examples when changing developer behavior.
5. Run documentation, link, schema, and Markdown validation when available.

## Protocol Changes

Protocol changes require an AIP:

1. Open an RFC Proposal issue.
2. Explain motivation, compatibility impact, security impact, and migration path.
3. Reference affected docs and schemas.
4. Wait for maintainer review before changing normative behavior.

## Pull Request Expectations

Every pull request should include:

- What changed and why.
- Which documents or APIs are affected.
- Compatibility impact: PATCH, MINOR, or MAJOR.
- Validation performed.
- Screenshots or rendered Markdown previews when presentation changes.

## Style

- Use clear, precise language.
- Prefer examples over abstract descriptions.
- Keep documents cross-linked.
- Keep headings stable when other documents link to them.
- Preserve canonical protocol wording unless intentionally changing it through governance.
