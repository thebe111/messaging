#!/usr/bin/env python3

import pika
import uuid


class FibonacciRPCClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
        )
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue="", exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True,
        )

    def on_response(self, channel, method, props, body):
        if self.id == props.correlation_id:
            self.response = body

    def exec(self, number):
        self.response = None
        self.id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange="",
            routing_key="rpc_method",
            properties=pika.BasicProperties(
                reply_to=self.callback_queue, correlation_id=self.id
            ),
            body=str(number),
        )

        while self.response is None:
            self.connection.process_data_events()

        return int(self.response)


client = FibonacciRPCClient()

print("client started")

number = input("type a number: ")

response = client.exec(number)

print(f"result: {response}")
