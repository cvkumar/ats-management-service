
from services.event_processors import process_response_event
from services.kafka_client import KafkaClient
from settings import CONFIG_PUBLISH_TOPIC, KAFKA_SERVERS

# import logging
# logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    kafka = KafkaClient(kafka_servers=KAFKA_SERVERS)
    kafka.consume(
        topic=CONFIG_PUBLISH_TOPIC,
        f=process_response_event
    )
