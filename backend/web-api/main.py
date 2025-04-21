from fastapi import FastAPI
from celery_app import celery

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is running!"}

@app.post("/create-user/")
def create_user(username: str, email: str, job_title: str, password: str):
    task = celery.send_task(
        "routers.user.create_user_task",
        args=[username, email, job_title, password]
    )
    return {"task_id": task.id, "status": "User creation task sent!"}