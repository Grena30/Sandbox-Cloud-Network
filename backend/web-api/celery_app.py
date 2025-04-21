from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv()

celery = Celery(
    "compute-tasks",
    broker=os.getenv("RABBITMQ_URL")
)

celery.autodiscover_tasks(["routers.user"])