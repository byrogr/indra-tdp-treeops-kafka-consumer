import os

from json import loads
from dotenv import load_dotenv
from kafka import KafkaConsumer

from services.consumer import saveTicketRaw

load_dotenv()


broker_1 = "{}:{}".format(os.getenv('REMEDY_KAFKA_HOST_BROKER_1'),  os.getenv('REMEDY_KAFKA_PORT_1'))
broker_2 = "{}:{}".format(os.getenv('REMEDY_KAFKA_HOST_BROKER_2'),  os.getenv('REMEDY_KAFKA_PORT_2'))

print(f'Conectando al broker {broker_1} ...')
print(f'Conectando al broker {broker_2} ...')

consumer = KafkaConsumer(
    os.getenv('REMEDY_KAFKA_TOPIC_CREATE'),
    group_id=None,
    bootstrap_servers = [broker_1],
    auto_offset_reset='earliest',
    api_version=(0,9)
)

for message in consumer:
    data = message.value
    print(data)
    saveTicketRaw(data)
