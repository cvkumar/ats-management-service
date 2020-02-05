from typing import Dict, Optional
from services.ats_storage_service import insert_ats_config, retrieve_ats_config
from services.kafka_client import KafkaClient
from settings import CONFIG_PUBLISH_TOPIC, CONFIG_RESPONSE_TOPIC, KAFKA_SERVERS


def process_add_configuration_event(tenant: str, configuration: Dict, source: Optional[str], meta: Optional[str]):
    service = KafkaClient(kafka_servers=KAFKA_SERVERS)
    body = service.prepare_message(
        type="ADD",
        message_dict={"tenant": tenant, "configuration": configuration},
        source=source
    )
    service.produce(CONFIG_PUBLISH_TOPIC, body)


def process_get_configuration_event(tenant: str, source: Optional[str], meta: Optional[str]):
    service = KafkaClient(kafka_servers=KAFKA_SERVERS)
    body = service.prepare_message(
        type="GET",
        message_dict={"tenant": tenant},
        source=source,
        meta=meta
    )
    service.produce(CONFIG_PUBLISH_TOPIC, body)

def process_response_event(response_dict: Dict):
    service = KafkaClient(kafka_servers=KAFKA_SERVERS)
    tenant = response_dict.get("message", {}).get("tenant")
    source = response_dict.get("message", {}).get("source")
    meta = response_dict.get("message", {}).get("meta")
    if response_dict["type"] == "ADD":
        config = response_dict.get("message", {}).get("configuration")
        if tenant and config:
            result = insert_ats_config(tenant, config)
            body = service.prepare_message(
                type="RESPONSE",
                message_dict=result,
                source=source,
                meta=meta
            )
            service.produce(CONFIG_RESPONSE_TOPIC, body)
    elif response_dict["type"] == "GET":
        if tenant:
            result = retrieve_ats_config(tenant=tenant)
            if result:
                body = service.prepare_message(
                    type="RESPONSE",
                    message_dict=result,
                    source=source,
                    meta=meta
                )
                service.produce(CONFIG_RESPONSE_TOPIC, body)
            else:
                print(f"Failed to find config for tenant: [{tenant}]")
        else:
            print(f"Event received is missing tenant [{response_dict}]")
    else:
        print(f"received an unknown event [{response_dict}]")

