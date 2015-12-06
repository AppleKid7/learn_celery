#!/usr/bin/env python3
""" 
Again, shamelessly stolen from RabbitMQ tutorial:
https://www.rabbitmq.com/tutorials/tutorial-one-python.html
"""

import pika

credentials = pika.PlainCredentials(username='nthompson',
                                    password='changeme')
parameters = pika.ConnectionParameters(host='localhost',
                                       port=5672,
                                       virtual_host='test',
                                       credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='hello')

print('Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received {}".format((body,)))

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)
    
channel.start_consuming()
        
