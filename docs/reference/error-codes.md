# Error Codes

This table uses the real registry codes currently documented in the repository.
Bridge-specific codes are maintained in the related bridge implementations and are not listed
as part of this public registry page.

## Verification Scope

- Public registry codes are sourced from the AIFP documents in this repository.
- Bridge implementation codes should be verified in the corresponding bridge repositories.
- SDK wrapper errors should map back to the documented `AIFP-*` registry where possible.

## Registry

| Code | Meaning | Typical reason | What to do |
|---|---|---|---|
| `AIFP-400` | Bad request | Missing field, invalid JSON, malformed challenge | Fix the request shape and retry |
| `AIFP-401` | Unauthorized | Missing or invalid API key | Supply a valid sandbox or production key |
| `AIFP-402` | Payment required | Protected resource needs payment | Request a quote, pay, and retry with the receipt |
| `AIFP-402-ONBOARDING` | Payment required plus onboarding | Agent does not yet speak AIFP | Send the onboarding challenge and link the human to docs |
| `AIFP-403` | Forbidden | Blocklist, policy restriction, or KYC restriction | Check policy and account status |
| `AIFP-403-BUDGET-EXCEEDED` | Budget exceeded | Payment would cross a wallet or merchant budget | Raise the budget or wait for the next window |
| `AIFP-404` | Not found | Quote, receipt, merchant, or resource not found | Re-check IDs and endpoints |
| `AIFP-409` | Conflict | Receipt replay or idempotency conflict | Use a fresh quote and a new `Idempotency-Key` |
| `AIFP-410` | Gone / expired | Quote expired | Request a fresh quote |
| `AIFP-422-SIGNATURE` | Invalid receipt signature | JWKS mismatch, stale `kid`, or tampered receipt | Refresh JWKS and verify the receipt again |
| `AIFP-422-AMOUNT` | Amount below required price | Paid amount does not meet the tier price | Re-quote or pay the correct amount |
| `AIFP-425` | Settlement pending | Payment settled asynchronously | Honor `Retry-After` and poll the same receipt |
| `AIFP-429` | Rate limited | Too many requests in a window | Back off and retry later |
| `AIFP-5xx` | Server error | Merchant, bridge, or gateway failure | Retry with backoff and inspect logs |

## SDK Mapping

The SDK reference maps wrapper exceptions to the registry above. The current documented
wrappers include `BudgetExceeded`, `InvalidReceipt`, `QuoteExpired`, and `RateLimited`.
See [SDK Reference](../aifp/11-SDK-Reference.md) for the language-specific wrappers.
