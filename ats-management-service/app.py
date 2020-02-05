import connexion

from services.event_processors import process_response_event
from services.kafka_client import KafkaClient
from settings import CONFIG_PUBLISH_TOPIC, KAFKA_SERVERS

app = connexion.FlaskApp(
    __name__, specification_dir="./swagger/", options={"swagger_ui": False}
)
app.add_api("swagger.yaml")
# app.app.config.from_object(settings)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    kafka = KafkaClient(kafka_servers=KAFKA_SERVERS)
    kafka.consume(CONFIG_PUBLISH_TOPIC, process_response_event)


@app.route("/test", methods=["GET", "POST", "OPTIONS"])
def home_test():
    return {}
