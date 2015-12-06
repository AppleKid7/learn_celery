#!/usr/bin/env python3

"""
This code is shamelessly stolen from the rabbitmq tutorial:

https://www.rabbitmq.com/tutorials/tutorial-one-python.html
"""

import pika
credentials = pika.PlainCredentials(username='nthompson', password='changeme')
parameters = pika.ConnectionParameters(host='10.240.0.3',
                                       port=5672,
                                       virtual_host='test',
                                       credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World')
print("We have sent the message 'Hello World' to RabbitMQ")
connection.close()
