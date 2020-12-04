#!/usr/bin/env python3

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

channel.queue_declare(queue="testing")

message = " ".join(sys.argv[1:]) or "lorem ipsum"

channel.basic_publish(exchange="", routing_key="testing", body=message)

print("message sended ...")

connection.close()
