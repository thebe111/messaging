# MESSAGING

Concepts about message broker tools like RabbitMQ, Apache Kafka

### Status

Completed

### Content Table

- [Used Technologies](#used-technologies)
- [Methods](#methods)
- [Tools](#tools)
- [RabbitMQ](#rabbitmq)
- [Basic Working Process](#basic-working-process)
- [Exchange Types](#exchange-types)
- [Author](#author)

### Used Technologies

- RabbitMQ
- Python 3+

### Methods

- **publisher subscriber system**

works as a radio system, the publisher send any message to determined channel and any subscriber on the channel can listen this message

- **dead letter queue**

when a message exceed your TTL (time to live) or was rejected, this message was sended to DLQ (dead letter queue) 

- **request reply pattern**

has a correlation ID to work if this method, when a reply if the same correlation ID was sended the message was processed

### Tools

- rabbitmq
- apache kafka

### Rabbitmq

**How this works?**

rabbitmq make a http tcp - tube - connection and inside the "main" connection has others channels

this methods was called multiplexing connection

**obs:** for each channel was created an thread

### Basic Working Process

```
PUBLISHER => EXCHANGE => QUEUE => CONSUMER
```

### Exchange Types

- `direct`: make a bind - process of connection - with a identifier string (routing key) to know what is the correct queue to send the incoming message
- `fanout`: send the incoming message for all consumers - broadcast
- `topic`: has more advanced configuration to work with delivery process
- `headers`: work with package header 

### Author

@thebe111
