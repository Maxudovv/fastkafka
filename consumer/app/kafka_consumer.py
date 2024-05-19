import json

from kafka import KafkaConsumer


kafka_consumer = KafkaConsumer(
            bootstrap_servers=["localhost"],
            value_deserializer=lambda x: x.decode("utf8"),
            auto_offset_reset="latest",
        )
