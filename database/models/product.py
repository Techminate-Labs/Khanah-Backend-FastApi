from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import event
from sqlalchemy import Float
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String

from .base_class import Base
from apps.utils.db_helpers import get_slug


class Product(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80), nullable=False)
    slug = Column(String(80))
    cost = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    discount = Column(Float, nullable=True)
    inventory = Column(Float, nullable=False)
    available = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())

    @staticmethod
    def generate_slug(target, value, oldvalue, initiator):
        # Method to generate slug from the name passed
        if value and (not target.slug or value != oldvalue):
            target.slug = get_slug(value)
            pass

    def __repr__(self):
        return f"<Item name={self.name} price={self.price}>"


event.listen(Product.name, "set", Product.generate_slug, retval=False)
