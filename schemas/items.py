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
    pass


class ItemOut(ItemBase):
    id: int
    slug: str
    created_at: datetime

    class Config:
        orm_mode = True
