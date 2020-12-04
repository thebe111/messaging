# messaging

### methods

- publisher subscriber system

work as a radio system, the publisher send any message to determinated channel and any subscriber on the channel can listen this message

- dead letter queue

when a message exceed your TTL (time to live) or was rejected, this message was sended to DLQ (dead letter queue) 

- request reply pattern

has a correlation ID to work if this method, when a reply if the same correlation ID was sended the message was processed

### tools

- rabbitmq
- apache kafka

### rabbitmq

**how this work?**

rabbitmq make a http tcp (tube) connection and inside the "main" connection has others channels

this methods was called multiplexing connection

obs: for each channel was created an thread

### basic working proccess

PUBLISHER => EXCHANGE => QUEUE => CONSUMER

### exchange types

- direct: make a bind (proccess of connection) with a identifier string (routing key) to know what is the correct queue to send the incoming message
- fanout: send the incoming message for all consumers (broadcast)
- topic: has more advanced configuration to work with delivery proccess
- headers: work with package header 

