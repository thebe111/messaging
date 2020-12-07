#!/usr/bin/env python3

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="test", exchange_type="topic")

routing_key = sys.argv[1] if len(sys.argv) > 1 else "empty.info"
message = " ".join(sys.argv[2:]) or "lorem ipsum"

channel.basic_publish(exchange="test", routing_key=routing_key, body=message)

print(f"message sended with [ {routing_key} ] key")

connection.close()
