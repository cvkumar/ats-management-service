import os

from pymongo import MongoClient

DEBUG = True

mongo_password = os.getenv("MONGO_PASSWORD")
mongo_connection = f"mongodb+srv://mya-user:{mongo_password}@cluster0-yjmri.mongodb.net/test?retryWrites=true&w=majority"
client = MongoClient(mongo_connection)
DATABASE = client.db

KAFKA_SERVERS = os.getenv("KAFKA_SERVERS", "localhost:31090")
CONFIG_PUBLISH_TOPIC = "mya-kafka-topic"
CONFIG_RESPONSE_TOPIC = "mya-kafka-response-topic"