from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str
    password: str


class UserCreate(UserBase):
    class Config:
        schema_extra = {
            "example": {
                "name": "Sheyzi Silver",
                "email": "gistkiosk@gmail.com",
                "password": "password",
            }
        }


class UserUpdate(UserBase):
    class Config:
        schema_extra = {
            "example": {
                "name": "Sheyzi Silver",
                "email": "gistkiosk@gmail.com",
                "password": "password",
            }
        }


class UserOut(UserBase):
    id: int
    is_active: bool
    email_verified: bool
    created_at: datetime

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Sheyzi Silver",
                "email": "gistkiosk@gmail.com",
                "password": "password",
                "is_active": True,
                "email_verified": True,
                "created_at": "2022-03-09T14:27:04.800Z",
            }
        }
