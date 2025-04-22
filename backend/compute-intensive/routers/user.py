from celery import shared_task
from models.database import create_db_and_tables
from sqlmodel import Session, select
from models.user import User
from models.database import engine


@shared_task
def read_root():
    return {"message": "Service is running!"}

@shared_task
def create_user_task(username: str, email: str, job_title: str, password: str):
    with Session(engine) as session:
        user = User(username=username, email=email, job_title=job_title, password=password)
        session.add(user)
        session.commit()
        session.refresh(user)
    return f"User {username} created successfully!"