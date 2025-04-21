from celery import Celery
from models.database import create_db_and_tables
from routers import user
from dotenv import load_dotenv
import os


load_dotenv()
rabbitmq_url = os.getenv("RABBITMQ_URL")

app = Celery("compute-intensive", broker=rabbitmq_url)
create_db_and_tables()
app.autodiscover_tasks(['routers.user'])