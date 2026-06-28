# Security Policy

AiFinPay Paywall Protocol handles payments, receipts, agent identity, merchant access control, and settlement metadata. Please report security issues privately.

## Reporting A Vulnerability

Do not open a public GitHub issue for vulnerabilities.

Email: security@aifinpay.io

Include:

- Affected component or document.
- Reproduction steps.
- Expected and actual behavior.
- Exploitability assessment.
- Suggested remediation if known.

## Scope

In scope:

- Receipt forgery or verification bypass.
- Replay protection failures.
- Idempotency and double-charge issues.
- JWKS, `kid`, or key rotation weaknesses.
- Webhook signature verification issues.
- Agent Passport identity or delegation flaws.
- OpenAPI or JSON Schema inconsistencies that cause unsafe implementation.

Out of scope:

- Social engineering.
- Denial-of-service without a protocol-specific vulnerability.
- Vulnerabilities in third-party systems not controlled by AiFinPay.

## Cryptographic Baseline

AIFP-1 requires:

- EdDSA / Ed25519 receipt signatures.
- TLS 1.3 for control-plane traffic.
- HMAC-SHA256 signed webhooks.
- Audience, resource, amount, expiry, and nonce validation.
- Short-lived receipts with default TTL of 600 seconds.
- Idempotency keys with a 24 hour dedupe window.

## Disclosure Process

1. We acknowledge receipt.
2. We investigate and reproduce.
3. We coordinate remediation.
4. We publish an advisory when appropriate.
5. We credit reporters unless anonymity is requested.
