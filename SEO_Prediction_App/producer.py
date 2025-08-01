import pika
import json

def send_message_to_rabbitmq(queue_name, message_type, data):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    
    # Construction du message en fonction du type
    if message_type == 'keyword':
        message = json.dumps({
            'type': 'keyword',
            'data': data
        })
    elif message_type == 'url':
        message = json.dumps({
            'type': 'url',
            'data': data
        })
    else:
        raise ValueError(f"Unknown message type: {message_type}")

    # Envoi du message à RabbitMQ
    channel.basic_publish(exchange='',
                          routing_key=queue_name,
                          body=message)
    print(f" [x] Sent {message_type} message: {message}")
    connection.close()
