# Microservices Choreography Saga with RabbitMQ
This project demonstrates a **Choreography-based Saga pattern** using **RabbitMQ** for asynchronous communication between services. The system includes four core services that react to events and publish new ones, forming an event-driven workflow.

## Event Flow Diagram
![GitHub Logo](choreography_saga_flow.png)
Order Service → [order.created] → RabbitMQ → Payment Service

Payment Service → [payment.completed] → RabbitMQ → Inventory Service

Inventory Service → [inventory.updated] → RabbitMQ → Notification Service

## Architecture Overview

**Services:**
- **Order Service** – Creates new orders and publishes `order.created` events.
- **Payment Service** – Listens for `order.created`, processes payment, and publishes `payment.completed`.
- **Inventory Service** – Listens for `payment.completed`, updates inventory, and publishes `inventory.updated`.
- **Notification Service** – Listens for `inventory.updated` and sends a notification.

All services communicate **only through RabbitMQ** using **direct exchanges** and **routing keys**.

## Technology used

Docker, Python, RabbitMQ, aio-pika

## Prerequisites

1. To run this project, you need to Docker and Docker Compose on your system.

## Installation

1. Clone the repository:
2. Change directory to rabbitmq-choreography-saga-with-python by running `cd rabbitmq-choreography-saga-with-python`
3. Create a .env file in the root directory of the project.
4. Set up the following environment variables:
```
RABBITMQ_USER=Testuser
RABBITMQ_PASS=Testuser@1234
RABBITMQ_HOST=rabbitmq-choreography
RABBITMQ_PORT=5672
```

## Build Docker containers:

To run this project, you just need to run the following command and the rest will do itself.

```docker compose up --build```

This command will build and start the Docker containers required for the project.

## Visit RabbitMQ dashboard:
```
http://localhost:15673
Username: Testuser
Password: Testuser@1234
```

## Create a test order:
```
curl -X POST http://localhost:4001/orders
```

## ⚠️ Note:
The order of log messages may vary slightly each time you run the system due to the asynchronous and distributed nature of microservices.