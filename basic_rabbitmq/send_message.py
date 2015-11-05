#!/usr/bin/env python3

"""
This code is shamelessly stolen from the rabbitmq tutorial:

https://www.rabbitmq.com/tutorials/tutorial-one-python.html
"""


import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World')
print("We have send the message 'Hello World' to RabbitMQ")
connection.close()
