import os

from json import loads
from dotenv import load_dotenv
from kafka import KafkaConsumer


load_dotenv()

consumer = KafkaConsumer(
    os.getenv('REMEDY_KAFKA_TOPIC_CREATE'),
    bootstrap_servers = [os.getenv('REMEDY_KAFKA_HOST_BROKER_1'), os.getenv('REMEDY_KAFKA_HOST_BROKER_2'),],
    auto_offset_reset = 'earliest',
    enable_auto_commit = True,
    #value_deserializer = lambda x: loads(x.decode('utf-8'))
)

for message in consumer:
    data = message.value
    print(f'Data {data}')
