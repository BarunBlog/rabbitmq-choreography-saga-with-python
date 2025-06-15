import json
import asyncio
from rabbitmq import connect_rabbit, publish_message, consume_message

async def process_payment_callback(body: bytes):
    data = json.loads(body.decode())
    print(f"[PAYMENT] Received 'order.created' event: {data}", flush=True)

    # Simulate payment processing...
    data['payment_status'] = 'paid'
    print(f"[PAYMENT] Payment processed: {data}", flush=True)

    # Send the message to the Inventory service
    exchange = "payment_exchange"
    routing_key = "payment.completed"

    # Publish payment completion data to the exchange
    await publish_message(exchange=exchange, routing_key=routing_key, message=json.dumps(data))

    print(f"[Payment] Sent payment completion message to Inventory. message: {data}", flush=True)


async def main():
    await connect_rabbit()
    await asyncio.gather(
        consume_message(exchange="order_exchange", queue="payment.order.created.queue", routing_key="order.created", handler=process_payment_callback)
    )

if __name__ == "__main__":
    asyncio.run(main())