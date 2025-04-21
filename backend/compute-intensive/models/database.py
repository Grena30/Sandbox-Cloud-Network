from sqlmodel import Session, SQLModel, create_engine
from dotenv import load_dotenv
import os


load_dotenv()

sqlite_url = os.getenv("POSTGRES_URL")
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session