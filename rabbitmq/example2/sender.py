#!/usr/bin/env python3

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.queue_declare(queue="testing", durable=True)

message = " ".join(sys.argv[1:]) or "lorem ipsum"

channel.basic_publish(
    exchange="",
    routing_key="testing",
    body=message,
    properties=pika.BasicProperties(delivery_mode=2),  # make message persistent
)

print("message sended ...")

connection.close()
