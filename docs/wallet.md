# Wallet Guide

Wallets fund agents, enforce spending controls, and settle value with merchants.

## Supported Settlement Modes

| Mode | Description |
|---|---|
| Stablecoin | USDC, USDT, PYUSD settlement on supported networks |
| Fiat hybrid | Fiat on/off-ramp with stablecoin settlement via BVNK |
| Custodial | Platform-managed wallet for agents |
| Non-custodial | Agent or user-controlled wallet |
| MPC | Managed signing with distributed key custody |

## Settlement Flow

```mermaid
flowchart LR
    Quote["Quote"] --> Budget["Budget policy"]
    Budget --> Wallet["Wallet authorization"]
    Wallet --> Settlement["Stablecoin / fiat settlement"]
    Settlement --> Receipt["Receipt issued"]
    Receipt --> Webhook["Merchant webhook"]
```

## Canonical References

- [Security & Cryptography Specification](aifp/04-Security-and-Cryptography-Specification.md)
- [AIFP-1 RFC](aifp/01-AIFP-1-RFC-Payment-Protocol-Specification.md)
- [OpenAPI 3.1](aifp/08-OpenAPI-3.1-Specification.yaml)
