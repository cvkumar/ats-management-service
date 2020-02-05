from json import dumps, loads
from kafka import KafkaConsumer, KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
from typing import Callable, Dict, Optional


class KafkaClient(object):
    def __init__(
        self,
        kafka_servers,
        batch_size=None,
        ):
        self.kafka_servers = kafka_servers
        if isinstance(kafka_servers, str):
            self.kafka_servers = [kafka_servers]
        self.batch_size = batch_size or 16384

    def produce(self, topic: str, message: Dict):
        try:
            producer = KafkaProducer(
                bootstrap_servers=self.kafka_servers,
                value_serializer=lambda x: dumps(x).encode('utf-8'),
                batch_size=self.batch_size
            )
            meta = producer.send(topic, message)
            producer.flush()
            return meta
        except Exception as e:
            print(f"producer: exception: {e}")

    def consume(self, topic: str, f: Callable, group: str = "mya", auto_offset_reset: str = "latest", enable_auto_commit: bool = True):
        try:
            consumer = KafkaConsumer(
                bootstrap_servers=self.kafka_servers,
                auto_offset_reset=auto_offset_reset,
                enable_auto_commit=enable_auto_commit,
                group_id=group,
                value_deserializer=lambda x: loads(x.decode('utf-8'))
            )
            consumer.subscribe([topic])

            for message in consumer:
                f(message.value)
        except Exception as e:
            print(f"consumer: exception: {e}")

    def create_topic(self, topic_name: str, partitions: int = 1, replications: int = 1, validate: bool = False):
        try:
            admin_client = KafkaAdminClient(bootstrap_servers=self.kafka_servers, client_id="mya_client")
            new_topic = NewTopic(name=topic_name, num_partitions=partitions, replication_factor=replications)
            admin_client.create_topics(new_topics=[new_topic], validate_only=validate)
        except Exception as e:
            print(f"create_topic: exception: {e}")

    def prepare_message(self, type: str, message_dict: Dict, source: Optional[str] = None, meta: Optional[str] = None):
        return {
            "type": type,
            "message": message_dict,
            "meta": meta,
            "source": source
        }
