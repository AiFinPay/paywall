# Webhook Verification Example

AIFP webhooks must be signed and timestamp-verified.

```ts
import { verifyWebhook } from "@aifinpay/merchant";

app.post("/webhooks/aifp", express.raw({ type: "application/json" }), (req, res) => {
  const event = verifyWebhook({
    payload: req.body,
    signature: req.header("AIFP-Signature"),
    timestamp: req.header("AIFP-Timestamp"),
    secret: process.env.AIFP_WEBHOOK_SECRET
  });

  if (event.type === "receipt.settled") {
    // Update internal ledger.
  }

  res.sendStatus(204);
});
```

Webhook handlers should reject missing signatures, stale timestamps, malformed payloads, and unexpected event types.
