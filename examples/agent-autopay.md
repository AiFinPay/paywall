# Agent Autopay Example

This example shows an agent consuming a paid resource without human checkout.

```ts
import { AIFPAgent } from "@aifinpay/agent";

const agent = new AIFPAgent({
  apiKey: process.env.AIFP_AGENT_KEY,
  walletId: "wlt_3a1b",
  budget: {
    dailyUsd: 5,
    maxPerRequestUsd: 0.10
  }
});

const response = await agent.fetch("https://merchant.example.com/api/data", {
  headers: { "Accept-Payment": "aifp/1.0" }
});

console.log(await response.json());
```

The SDK should:

1. Detect `402 Payment Required`.
2. Parse the payment challenge.
3. Check budget policy.
4. Request a quote.
5. Pay using an idempotency key.
6. Retry the original request with `Payment-Receipt`.
