#!/usr/bin/env python3

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="logs", exchange_type="direct")

severity = sys.argv[1] if len(sys.argv) > 1 else "info"
message = " ".join(sys.argv[2:]) or "lorem ipsum"

channel.basic_publish(exchange="logs", routing_key=severity, body=message)

print(f"message sended with [ {severity} ] status")

connection.close()
