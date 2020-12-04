#!/usr/bin/env python3

import pika
import sys
import os
import time


def exec():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="testing")

    def reader(channel, method, properties, body):
        print(f"message: {body.decode()}", end="\n")

        time.sleep(body.count(b"."))

        print("done")

    channel.basic_consume(
        queue="testing", auto_ack="true", on_message_callback=reader
    )

    print("waiting for messages ...")

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
