import socket

from fastapi import APIRouter
from kafka.consumer.fetcher import ConsumerRecord

from app.kafka_consumer import kafka_consumer


api_router = APIRouter(prefix="/api", tags=["api"])


@api_router.get("/read")
async def read():
    kafka_consumer.subscribe("test_topic")
    message: ConsumerRecord = next(kafka_consumer)
    return message
