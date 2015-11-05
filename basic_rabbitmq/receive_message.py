#!/usr/bin/env python3
""" 
Again, shamelessly stolen from RabbitMQ tutorial:
https://www.rabbitmq.com/tutorials/tutorial-one-python.html
"""

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

print('Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received {}".format((body,)))

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)
    
channel.start_consuming()
        
