# consume.py
import pika,time, os

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('BROKER_URL')
params = pika.URLParameters(url)
print("URL = " + str(url))
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue="test-delayed")

def callback(ch, method, properties, body):
  print(" [x] Received " + str(body))
  print(" Properties: " + str(properties.headers))
  ch.basic_ack(delivery_tag = method.delivery_tag)

time.sleep(1)
channel.basic_consume('test-delayed',
                      callback,
                      auto_ack=False)

print(' [*] Waiting for messages:')
channel.start_consuming()
connection.close()
