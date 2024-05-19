from kafka import KafkaProducer

topic = "test_topic"

kafka_producer = KafkaProducer(
    bootstrap_servers=["localhost"],
    value_serializer=lambda v: v.encode("utf-8"),
)
