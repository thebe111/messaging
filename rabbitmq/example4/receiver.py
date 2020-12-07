#!/usr/bin/env python3

import pika
import sys
import os


def exec():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.exchange_declare(exchange="logs", exchange_type="direct")

    result = channel.queue_declare(queue="", exclusive=True)
    queue_name = result.method.queue

    severities = sys.argv[1:] or "info"

    for severity in severities:
        channel.queue_bind(
            exchange="logs", queue=queue_name, routing_key=severity
        )

    def reader(channel, method, properties, body):
        print(f"message: {body}", end="\n")

    channel.basic_consume(
        queue=queue_name, on_message_callback=reader, auto_ack=True
    )

    print(f"waiting for messages with {severities} status")

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
