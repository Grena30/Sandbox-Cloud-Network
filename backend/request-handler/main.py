from fastapi import FastAPI
from models.database import create_db_and_tables
from routers import user
import uvicorn


app = FastAPI()
app.include_router(user.router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

if __name__ == '__main__':
    uvicorn.run(app)