import argparse
import sys

import pika


def parse_arguments():
    parser = argparse.ArgumentParser(description='MQTT Publish -> AMQP Consume w/ Python and RabbitMQ')
    parser.add_argument('--rabbit-host', required=False, type=str, default='localhost', help='Host for RabbitMQ Broker')
    parser.add_argument('--rabbit-port', required=False, type=int, default=5672, help='Port for RabbitMQ Broker')
    parser.add_argument('--rabbit-user', required=True, type=str, help='Username for RabbitMQ')
    parser.add_argument('--rabbit-pass', required=True, type=str, help='Password for RabbitMQ')
    parser.add_argument('--rabbit-topic', required=True, help='Pattern that matches the MQTT topic')

    return parser.parse_args()


def consumer_callback(channel, method, property, body):
    print(f'Received Data From MQTT: {body}')


def main():

    args = parse_arguments()
    broker_credentials = pika.PlainCredentials(args.rabbit_user, args.rabbit_pass)


    print("Setting Up Connection with RabbitMQ Broker")

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
           host=args.rabbit_host,
           port=args.rabbit_port,
           credentials=broker_credentials
        )
    )

    # Create Channel
    print("Creating Channel")

    channel = connection.channel()

    # Declare the Exchange

    print("Declaring the exchange to read incoming MQTT Messages")
    # Exchange to read mqtt via RabbitMQ is always `amq.topic`
    # Type of exchange is `topic` based
    channel.exchange_declare(exchange='amq.topic', exchange_type='topic', durable=True)

    # the Queue Name for MQTT Messages is the MQTT-TOPIC name where `/` is replaced by `.`
    # Let RabbitMQ create the name for us
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    # Bind the Queue with some specific topic where you wish to get the data from

    channel.queue_bind(exchange='amq.topic', queue=queue_name, routing_key=args.rabbit_topic)

    # Start Consuming from Queue

    channel.basic_consume(queue=queue_name, on_message_callback=consumer_callback, auto_ack=True)

    print("Waiting for MQTT Payload")

    channel.start_consuming()




if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        print("CTRL+C Pressed")
        sys.exit(0)