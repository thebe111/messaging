#!/usr/bin/env python3

import pika
import sys
import os


def exec():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.exchange_declare(exchange="test", exchange_type="topic")

    result = channel.queue_declare(queue="", exclusive=True)
    queue_name = result.method.queue

    keys = sys.argv[1:] or "info"

    for key in keys:
        channel.queue_bind(exchange="test", queue=queue_name, routing_key=key)

    def reader(channel, method, properties, body):
        print(f"message: {body}", end="\n")

    channel.basic_consume(
        queue=queue_name, on_message_callback=reader, auto_ack=True
    )

    print(f"waiting for messages with {keys} keys")

    channel.start_consuming()


if __name__ == "__main__":
    try:
        exec()
    except KeyboardInterrupt:
        print("canceling ...")

        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
