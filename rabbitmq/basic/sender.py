#!/usr/bin/env python3

import pika

# making rabbitmq connection
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# check with the queue exists or create one
channel.queue_declare(queue="testing")

# sending message
# obs: exchange = '' is same as default exchange
channel.basic_publish(exchange="", routing_key="testing", body="lorem ipsum")

print("message sended ...")

connection.close()
