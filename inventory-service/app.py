import json
import asyncio
from rabbitmq import connect_rabbit, publish_message, consume_message


async def process_inventory_callback(body: bytes):
    data = json.loads(body.decode())
    print(f"[Inventory] Received 'payment.completed' event: {data}", flush=True)

    # Simulate inventory update
    data['inventory_status'] = 'updated'
    print(f"[Inventory] Inventory updated for order: {data}", flush=True)

    # Send the message to the notification service
    exchange = "inventory_exchange"
    routing_key = "inventory.updated"

    # Publish the inventory updation data to the exchange
    await publish_message(exchange=exchange, routing_key=routing_key, message=json.dumps(data))

    print(f"[Inventory] Sent inventory updation message to the Notification. message: {data}", flush=True)


async def main():
    await connect_rabbit()
    await asyncio.gather(
        consume_message(exchange="payment_exchange", queue="inventory.payment.completed.queue", routing_key="payment.completed", handler=process_inventory_callback)
    )

if __name__ == "__main__":
    asyncio.run(main())