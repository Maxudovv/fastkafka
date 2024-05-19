from fastapi import APIRouter

from producer.app.kafka_producer import kafka_producer

api_router = APIRouter(prefix="/api", tags=["api"])


@api_router.get("/send")
async def send(message: str):
    kafka_producer.send(topic="test_topic", value=message)
    kafka_producer.flush()
    return "Ok"
