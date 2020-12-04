#!/usr/bin/env python3

import pika
import sys
import os


def exec():
    # making rabbitmq connection
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    # check if the queue exists or create one
    channel.queue_declare(queue="testing")

    # rammitmq work with a callback to read the message
    def reader(channel, method, properties, body):
        print(f"message: {body}")

    # setup reader callback to proccess the message
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
