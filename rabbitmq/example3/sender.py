#!/usr/bin/env python3

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="logs", exchange_type="fanout")

message = " ".join(sys.argv[1:]) or "lorem ipsum"

channel.basic_publish(exchange="logs", routing_key="", body=message)

print("message sended ...")

connection.close()
