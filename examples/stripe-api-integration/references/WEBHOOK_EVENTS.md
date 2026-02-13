# Stripe Webhook Events Reference

Complete reference for Stripe webhook events and handling patterns.

## Overview

Webhooks notify your application of events happening in your Stripe account. When an event occurs, Stripe creates an Event object and sends an HTTP POST request to the URL you configured.

## Setup

1. **Add endpoint in Stripe Dashboard**:
   - Go to Developers → Webhooks
   - Click "Add endpoint"
   - Enter your URL: `https://example.com/webhook`
   - Select events to listen for

2. **Get signing secret**: 
   - After creating endpoint, copy the signing secret (whsec_...)
   - Store securely in environment variables

## Event Structure

All webhook events have this structure:

```json
{
  "id": "evt_1ABC123",
  "object": "event",
  "api_version": "2023-10-16",
  "created": 1234567890,
  "type": "payment_intent.succeeded",
  "data": {
    "object": {
      // The full object (PaymentIntent, Customer, etc.)
    }
  },
  "liveness_mode": "test",
  "pending_webhooks": 1,
  "request": {
    "id": "req_ABC123",
    "idempotency_key": "key_123"
  }
}
```

## Payment Events

### payment_intent.succeeded
**When**: Payment completed successfully
**Use for**: Fulfill order, update database, send confirmation

```python
if event.type == "payment_intent.succeeded":
    payment_intent = event.data.object
    amount = payment_intent.amount  # Amount charged in cents
    customer = payment_intent.customer
    metadata = payment_intent.metadata
    
    # Your logic
    order_id = metadata.get("order_id")
    fulfill_order(order_id)
    send_confirmation_email(customer)
```

### payment_intent.payment_failed
**When**: Payment attempt failed
**Use for**: Notify customer, retry logic, update status

```python
if event.type == "payment_intent.payment_failed":
    payment_intent = event.data.object
    error = payment_intent.last_payment_error
    
    # Your logic
    notify_customer_of_failure(payment_intent.customer, error.message)
    update_order_status(metadata["order_id"], "failed")
```

### payment_intent.created
**When**: New PaymentIntent created
**Use for**: Logging, analytics

### payment_intent.canceled
**When**: PaymentIntent canceled before completion
**Use for**: Cancel order, refund if needed, update status

### payment_intent.requires_action
**When**: Payment requires customer action (3D Secure)
**Use for**: Send notification to complete authentication

## Subscription Events

### customer.subscription.created
**When**: New subscription created
**Use for**: Grant access, send welcome email, start trial

```python
if event.type == "customer.subscription.created":
    subscription = event.data.object
    customer_id = subscription.customer
    status = subscription.status  # 'active', 'trialing', etc.
    
    # Your logic
    grant_access(customer_id, subscription.id)
    if status == "trialing":
        send_trial_welcome_email(customer_id)
```

### customer.subscription.updated
**When**: Subscription modified (plan change, status change)
**Use for**: Update access level, handle upgrades/downgrades

```python
if event.type == "customer.subscription.updated":
    subscription = event.data.object
    previous_attributes = event.data.previous_attributes
    
    # Check what changed
    if "status" in previous_attributes:
        old_status = previous_attributes["status"]
        new_status = subscription.status
        print(f"Status changed: {old_status} → {new_status}")
    
    # Update user's access
    update_subscription_access(subscription.customer, subscription)
```

### customer.subscription.deleted
**When**: Subscription canceled
**Use for**: Revoke access, send cancellation confirmation

```python
if event.type == "customer.subscription.deleted":
    subscription = event.data.object
    customer_id = subscription.customer
    
    # Your logic
    revoke_access(customer_id)
    send_cancellation_email(customer_id)
    update_database_status(subscription.id, "canceled")
```

### customer.subscription.trial_will_end
**When**: 3 days before trial ends
**Use for**: Remind customer to add payment method

```python
if event.type == "customer.subscription.trial_will_end":
    subscription = event.data.object
    trial_end = subscription.trial_end
    
    send_trial_ending_reminder(subscription.customer, trial_end)
```

## Invoice Events

### invoice.paid
**When**: Invoice payment succeeded
**Use for**: Confirm subscription payment, send receipt

```python
if event.type == "invoice.paid":
    invoice = event.data.object
    customer = invoice.customer
    subscription = invoice.subscription
    amount_paid = invoice.amount_paid
    
    send_receipt_email(customer, invoice.id, amount_paid)
```

### invoice.payment_failed
**When**: Invoice payment failed
**Use for**: Retry payment, suspend access, notify customer

```python
if event.type == "invoice.payment_failed":
    invoice = event.data.object
    customer = invoice.customer
    attempt_count = invoice.attempt_count
    
    if attempt_count >= 3:
        suspend_subscription(invoice.subscription)
    
    notify_payment_failure(customer, attempt_count)
```

### invoice.upcoming
**When**: 1 hour before invoice is charged (recurring subscription)
**Use for**: Check if payment method is valid, send reminder

### invoice.created
**When**: New invoice created
**Use for**: Logging, analytics

### invoice.finalized
**When**: Invoice finalized and ready to be paid
**Use for**: Send invoice to customer

## Customer Events

### customer.created
**When**: New customer created
**Use for**: Initialize customer record in your system

```python
if event.type == "customer.created":
    customer = event.data.object
    
    create_customer_record(
        stripe_id=customer.id,
        email=customer.email,
        name=customer.name
    )
```

### customer.updated
**When**: Customer details changed
**Use for**: Sync customer data to your database

### customer.deleted
**When**: Customer deleted
**Use for**: Clean up customer data

## Payment Method Events

### payment_method.attached
**When**: Payment method attached to customer
**Use for**: Confirm payment method added, send confirmation

### payment_method.detached
**When**: Payment method removed from customer
**Use for**: Notify if default payment method removed

### payment_method.updated
**When**: Payment method details updated
**Use for**: Sync payment method changes

## Charge Events

### charge.succeeded
**When**: Charge succeeded
**Use for**: Alternative to payment_intent.succeeded for legacy integrations

### charge.failed
**When**: Charge failed
**Use for**: Handle payment failures

### charge.refunded
**When**: Charge refunded
**Use for**: Process refund, update order status, notify customer

```python
if event.type == "charge.refunded":
    charge = event.data.object
    refund_amount = charge.amount_refunded
    
    process_refund(charge.metadata["order_id"], refund_amount)
    notify_refund(charge.customer)
```

## Dispute Events

### charge.dispute.created
**When**: Customer disputes a charge
**Use for**: Alert admin, prepare evidence

### charge.dispute.updated
**When**: Dispute status changed
**Use for**: Track dispute progress

### charge.dispute.closed
**When**: Dispute resolved
**Use for**: Process outcome, update records

## Payout Events

### payout.paid
**When**: Payout sent to bank account
**Use for**: Reconciliation, accounting

### payout.failed
**When**: Payout failed
**Use for**: Alert admin, check bank details

## Implementing Event Handlers

### Pattern 1: Switch Statement

```python
event_type = event.type

if event_type == "payment_intent.succeeded":
    handle_payment_success(event.data.object)
elif event_type == "payment_intent.payment_failed":
    handle_payment_failure(event.data.object)
elif event_type == "customer.subscription.deleted":
    handle_subscription_cancellation(event.data.object)
elif event_type == "invoice.payment_failed":
    handle_invoice_failure(event.data.object)
else:
    print(f"Unhandled event type: {event_type}")
```

### Pattern 2: Handler Registry

```python
EVENT_HANDLERS = {
    "payment_intent.succeeded": handle_payment_success,
    "payment_intent.payment_failed": handle_payment_failure,
    "customer.subscription.created": handle_new_subscription,
    "customer.subscription.deleted": handle_canceled_subscription,
    "invoice.payment_failed": handle_invoice_failure,
}

def handle_webhook(event):
    handler = EVENT_HANDLERS.get(event.type)
    if handler:
        handler(event.data.object)
    else:
        print(f"No handler for event type: {event.type}")
```

### Pattern 3: Class-Based Handlers

```python
class WebhookHandler:
    def handle(self, event):
        method_name = f"handle_{event.type.replace('.', '_')}"
        method = getattr(self, method_name, None)
        
        if method:
            method(event.data.object)
        else:
            self.handle_unhandled(event.type)
    
    def handle_payment_intent_succeeded(self, payment_intent):
        # Handle payment success
        pass
    
    def handle_customer_subscription_deleted(self, subscription):
        # Handle cancellation
        pass
    
    def handle_unhandled(self, event_type):
        print(f"Unhandled: {event_type}")

# Usage
handler = WebhookHandler()
handler.handle(event)
```

## Idempotency

Webhooks may be sent multiple times. Implement idempotency:

```python
def handle_webhook(event):
    # Check if already processed
    if Event.objects.filter(stripe_id=event.id).exists():
        return {"status": "already_processed"}
    
    # Store event
    Event.objects.create(stripe_id=event.id, type=event.type)
    
    # Process event
    process_event(event)
    
    return {"status": "success"}
```

## Error Handling

Always return 200 OK to acknowledge receipt:

```python
@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        event = stripe.Webhook.construct_event(
            request.data,
            request.headers["Stripe-Signature"],
            endpoint_secret
        )
        
        handle_event(event)
        
        return {"status": "success"}, 200
    except Exception as e:
        # Log error but still return 200
        logger.error(f"Webhook error: {e}")
        return {"status": "error", "message": str(e)}, 200
```

**Important**: If you return non-200, Stripe will retry the webhook, potentially causing duplicate processing.

## Testing Webhooks

### Using Stripe CLI

```bash
# Forward to local server
stripe listen --forward-to localhost:5000/webhook

# Trigger specific events
stripe trigger payment_intent.succeeded
stripe trigger customer.subscription.deleted
stripe trigger invoice.payment_failed
```

### Manual Testing

Send test webhook from Dashboard:
1. Go to Developers → Webhooks
2. Click on your endpoint
3. Click "Send test webhook"
4. Select event type
5. Click "Send test webhook"

## Security

Always verify webhook signatures:

```python
import stripe

try:
    event = stripe.Webhook.construct_event(
        payload,
        sig_header,
        endpoint_secret
    )
except stripe.error.SignatureVerificationError:
    # Invalid signature - don't process
    return "Invalid signature", 400
```

**Never skip signature verification in production!**

## Complete Event List

### Payment
- `payment_intent.created`
- `payment_intent.succeeded`
- `payment_intent.payment_failed`
- `payment_intent.canceled`
- `payment_intent.requires_action`

### Subscription
- `customer.subscription.created`
- `customer.subscription.updated`
- `customer.subscription.deleted`
- `customer.subscription.trial_will_end`

### Invoice
- `invoice.created`
- `invoice.finalized`
- `invoice.paid`
- `invoice.payment_failed`
- `invoice.upcoming`

### Customer
- `customer.created`
- `customer.updated`
- `customer.deleted`

### Payment Method
- `payment_method.attached`
- `payment_method.detached`
- `payment_method.updated`

### Charge
- `charge.succeeded`
- `charge.failed`
- `charge.refunded`
- `charge.dispute.created`
- `charge.dispute.updated`
- `charge.dispute.closed`

### Payout
- `payout.paid`
- `payout.failed`

For complete event catalog, see: https://stripe.com/docs/api/events/types

## Best Practices

1. **Return 200 quickly** - Don't do heavy processing in webhook handler
2. **Use a queue** - Queue events for async processing
3. **Implement idempotency** - Check for duplicate events
4. **Verify signatures** - Always verify webhook signatures
5. **Log everything** - Log all webhook events for debugging
6. **Handle failures gracefully** - Don't crash on unexpected events
7. **Monitor webhook health** - Check for failed deliveries in dashboard
8. **Test thoroughly** - Use Stripe CLI to test all event types
