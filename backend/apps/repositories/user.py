from typing import List

from apps.schemas.user import UserCreate
from apps.schemas.user import UserUpdate
from sqlalchemy.orm import Session
from database.models.user import User
from fastapi import HTTPException
from apps.utils.sanitize_schemas_body import sanitize



def get_with_id(db: Session, _id: int) -> User:
    user = db.query(User).get(_id)
    if not user:
        raise HTTPException(404, f"User with id {_id} doesn't exist")
    return user


def get_with_email(db: Session, email: str) -> User:
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(404, f"User with email address {email} doesn't exist!")
    return user


def update_with_id(db: Session, _id: int, body: UserUpdate) -> User:
    user = get_with_id(db, _id)
    filtered_body = sanitize(body)
    db.query(User).filter(User.id == _id).update(filtered_body)
    db.commit()
    db.refresh(user)
    return user


def get_all(db: Session, limit: int = 20, skip: int = 0) -> List[User]:
    user = (
        db.query(User)
        .offset(skip)
        .limit(limit)
        .all()
    )
    return user


def create(body: UserCreate, db: Session) -> User: 
    body.email = body.email.lower()
    body.email = body.email.strip()
    if get_with_email(db, body.email):
        raise HTTPException(400, "User with this email already exists!")
    user = User(**body.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
