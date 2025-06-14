import json
import asyncio
from rabbitmq import connect_rabbit, publish_message, consume_message

async def process_notification_callback(body: bytes):
    data = json.loads(body.decode())
    print(f"[Notification] Received 'inventory.updated' event: {data}", flush=True)


async def main():
    await connect_rabbit()
    await asyncio.gather(
        consume_message(exchange="inventory_exchange", queue="notification.inventory.updated.queue", routing_key="inventory.updated", handler=process_notification_callback)
    )

if __name__ == "__main__":
    asyncio.run(main())