from fastapi import Depends
from fastapi import APIRouter
from typing import List

from apps.controllers.user import user as controllers

from config.dependencies import get_db
from sqlalchemy.orm import Session

from apps.schemas.user import UserCreate
from apps.schemas.user import UserOut
from apps.schemas.user import UserUpdate


router = APIRouter(prefix="/user", tags=["User"])


@router.put('/{_id}/', status_code=200, response_model=UserOut)
def update_user(_id: int, body: UserUpdate, db: Session = Depends(get_db)):
    user = controllers.update_user_with_id(body=body, _id=_id, db=db)
    return user


@router.get('/{_id}/', status_code=200, response_model=UserOut)
def get_user_by_their_id(_id: int, db: Session = Depends(get_db)):
    user = controllers.get_user_with_id(_id=_id, db=db)
    return user


@router.post('/', status_code=201, response_model = UserOut)
def create_a_user(body: UserCreate, db: Session = Depends(get_db)):
    user = controllers.create_user(body=body, db=db)
    return user


@router.get('/', status_code=200, response_model=List[UserOut])
def get_all_users(limit: int = 20, skip: int = 0, db: Session =  Depends(get_db)):
    users = controllers.get_all_user(limit=limit, skip=skip, db=db)
    return users

