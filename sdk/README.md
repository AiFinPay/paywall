# SDKs

AiFinPay SDKs provide merchant middleware, agent auto-pay clients, receipt verification, wallet binding, and protocol helpers.

## Language Matrix

| Language | Merchant SDK | Agent SDK | Package Target |
|---|---:|---:|---|
| TypeScript / Node | Yes | Yes | `@aifinpay/merchant`, `@aifinpay/agent` |
| Python | Yes | Yes | `aifinpay-merchant`, `aifinpay-agent` |
| Go | Yes | Yes | `github.com/aifinpay/aifp-go` |
| Rust | Planned | Planned | `aifinpay` |
| Java | Planned | Planned | `io.aifinpay:aifp` |
| PHP | Planned | Planned | `aifinpay/aifp` |
| .NET | Planned | Planned | `AiFinPay` |

## Pricing Helpers

SDKs should expose pricing as first-class protocol data, not as hard-coded merchant logic.

| Helper | Value |
|---|---|
| `standard` | From `$0.00001` for simple reads, single records, and lightweight API requests. |
| `complex` | From `$0.00006` for search, aggregation, multi-source queries, and higher compute. |
| `premium` | From `$0.00010` for AI inference, GPU workloads, deep analytics, and premium data. |
| `protocolFeeRate` | `0.01`, representing the AiFinPay Protocol Fee of 1%. |
| `merchantSettlementRate` | `0.99`, before any applicable network or settlement costs. |

## SDK Architecture

```mermaid
flowchart TD
    Core["Protocol Core"] --> Types["Generated Types"]
    Core --> Receipt["Receipt Verifier"]
    Core --> Errors["Error Registry"]
    Core --> Pricing["Pricing Helpers"]
    Types --> Merchant["Merchant Middleware"]
    Types --> Agent["Agent Client"]
    Types --> Wallet["Wallet Client"]
    Pricing --> Merchant
    Pricing --> Agent
    Merchant --> Frameworks["Express / Fastify / Next / Django / Rails"]
    Agent --> Fetch["fetch / requests / http clients"]
    Wallet --> Settlement["Stablecoin / fiat adapters"]
```

## Source Documents

- [AI Agent SDK Specification](../docs/aifp/03-AI-Agent-SDK-Specification.md)
- [SDK Reference](../docs/aifp/11-SDK-Reference.md)
- [OpenAPI 3.1](../docs/aifp/08-OpenAPI-3.1-Specification.yaml)
- [JSON Schemas](../docs/aifp/10-JSON-Schemas.md)
