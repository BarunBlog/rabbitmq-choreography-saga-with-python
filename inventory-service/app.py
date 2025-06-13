import asyncio
from rabbitmq import connect_rabbit, consume_message


async def process_inventory_callback(body: bytes):
    inventory_data = eval(body.decode())
    print(f"[Inventory] Received 'order.created' event: {inventory_data}", flush=True)

    # Simulate inventory deduction
    inventory_data['inventory_status'] = 'deducted'
    print(f"[Inventory] Inventory deducted for order: {inventory_data}", flush=True)



async def main():
    await connect_rabbit()
    await asyncio.gather(
        consume_message(exchange="order_exchange", queue="inventory.order.created.queue", routing_key="order.created", handler=process_inventory_callback)
    )

if __name__ == "__main__":
    asyncio.run(main())