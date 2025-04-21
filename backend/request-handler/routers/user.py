from fastapi import APIRouter, Depends, Query
from sqlmodel import Session, select
from models.user import User
from typing import Annotated
from models.database import get_session


SessionDep = Annotated[Session, Depends(get_session)]
router = APIRouter()

@router.get('/user')
def list_users(session: SessionDep) -> list[User]:
    users = session.exec(select(User)).all()
    return users

@router.post("/users/")
def create_user(user: User, session: SessionDep) -> User:
    session.add(user)
    session.commit()
    session.refresh(user)
    return user