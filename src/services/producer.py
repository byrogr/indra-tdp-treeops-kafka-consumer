import time
import json
import random

from datetime import datetime
from utils.generator import generate_message
from kafka import KafkaProducer


def serializer(message):
    return json.dumps(message).encode("utf-8")

# Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=serializer
)

# Solo pruebas
if __name__ == '__main__':
    while True:
        dummy_message = generate_message()
        print(f'Produciendo mensaje @ {datetime.now()} | Mensaje = {str(dummy_message)}')
        producer.send('queue-notify-create-tickets-remedy', dummy_message)
        time_to_sleep = random.randint(1, 11)
        time.sleep(time_to_sleep)