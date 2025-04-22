from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select
from models.user import User
from typing import Annotated
from models.database import get_session


SessionDep = Annotated[Session, Depends(get_session)]
router = APIRouter()

@router.get("/status")
def read_root():
    return {"message": "Service is running!"}

@router.get('/user')
def list_users(session: SessionDep) -> list[User]:
    users = session.exec(select(User)).all()
    return users

@router.get('/user/{user_id}')
def get_user(user_id: int, session: SessionDep) -> User | None:
    user = session.exec(select(User).where(User.id == user_id)).first()
    return user