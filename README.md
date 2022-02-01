# Requisitos
- Python >= 3.6
- PyMySQL >= 1.0.2
- Kafka-Python >= 1.4.7

# Configuración
Para iniciar el proyecto, ejecutamos lo siguiente:
```
git clone git@182.160.28.216:rrojas/proceso-mc-kafka.git
pip install -r requirements.txt
cp .env.example .env
```

# Iniciar Kafka

Creamos los servicios de Kafka con Docker
```
docker-compose up -d
```

Para crear un topic, ejecutamos lo siguiente:
```
docker exec -it kafka /bin/sh
cd /opt/kafka_2.13-2.7.1/bin
kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic queue-notify-create-tickets-remedy
```

# Consumir Kafka
Para simular tickets en Kafka, ejecutamos:
```
python src/services/producer.py
```

Para consumir tickets en Kafka, ejecutamos:
```
python main.py
```
