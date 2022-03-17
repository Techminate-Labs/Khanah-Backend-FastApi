from sqlalchemy.orm import Session


from apps.repositories.user import create
from apps.repositories.user import get_with_id
from apps.repositories.user import get_with_email
from apps.repositories.user import update_with_id
from apps.repositories.user import get_all
from apps.schemas.user import UserCreate
from apps.schemas.user import UserUpdate


def get_all_user(*, limit: int = 20, skip: int = 0, db: Session):
    users = get_all(db=db, limit=limit, skip=skip)
    return users


def get_user_with_id(*, _id: int, db: Session):
    user = get_with_id(db=db, _id=_id)
    return user


def update_user_with_id(body: UserUpdate, _id: int, db: Session):
    user = update_with_id(db=db, body=body, _id=_id)
    return user


def create_user(body: UserCreate, db: Session):
    new_user = create(db=db, body=body)
    return new_user



