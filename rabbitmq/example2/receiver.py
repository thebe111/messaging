#!/usr/bin/env python3

import pika
import sys
import os
import time


def exec():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="testing", durable=True)

    def reader(channel, method, properties, body):
        print(f"message: {body.decode()}", end="\n")

        time.sleep(body.count(b"."))

        print("done")

        # if any worker chash the message was
        # delivered to another functional worker
        channel.basic_ack(delivery_tag=method.delivery_tag)

    # send message to worker was free
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="testing", on_message_callback=reader)

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
