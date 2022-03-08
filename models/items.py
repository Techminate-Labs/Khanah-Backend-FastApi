from sqlalchemy import Column, Integer, String

from .base_class import Base


class Items(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80), nullable=False)
