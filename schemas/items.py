from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    cost: float
    price: float
    discount: Optional[float]
    inventory: int
    available: Optional[bool] = True


class ItemCreate(ItemBase):
    class Config:
        schema_extra = {
            "example": {
                "name": "Pizza",
                "cost": 5,
                "price": 15,
                "discount": 10,
                "inventory": 100,
                "available": True,
            }
        }


class ItemUpdate(ItemBase):
    class Config:
        schema_extra = {
            "example": {
                "name": "Pizza",
                "cost": 5,
                "price": 15,
                "discount": 10,
                "inventory": 100,
                "available": True,
            }
        }


class ItemOut(ItemBase):
    id: int
    slug: str
    created_at: datetime

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "pizza",
                "slug": "pizza-53627",
                "cost": 5,
                "price": 15,
                "discount": 10,
                "inventory": 100,
                "available": True,
                "created_at": "2022-03-09T14:27:04.800Z",
            }
        }
        orm_mode = True
