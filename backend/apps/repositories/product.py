from typing import List
from typing import Union

from apps.schemas.product import ProductCreate
from apps.schemas.product import ProductUpdate
from apps.utils.sanitize_schemas_body import sanitize
from database.models.product import Product
from fastapi import HTTPException
from sqlalchemy import desc
from sqlalchemy.orm import Session


def create(body: ProductCreate, db: Session) -> Product:
    item = Product(**body.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def get_all(db: Session, limit: int = 20, skip: int = 0) -> List[Product]:
    items = (
        db.query(Product)
        .order_by(desc(Product.created_at))
        .offset(skip)
        .limit(limit)
        .all()
    )
    return items


def get(db: Session, _id: int) -> Product:
    item = db.query(Product).get(_id)
    if not item:
        raise HTTPException(404, f"Item with id `{_id} doesn't exist")
    return item


def get_or_none(db: Session, _id: int) -> Union[Product, None]:
    item = db.query(Product).get(_id)
    return item


def get_with_slug(db: Session, slug: str) -> Product:
    item = db.query(Product).filter(Product.slug == slug).first()
    if not item:
        raise HTTPException(404, f"Item with slug `{slug} doesn't exist")
    return item


def get_with_slug_or_none(db: Session, slug: str) -> Union[Product, None]:
    item = db.query(Product).filter(Product.slug == slug).first()
    return item


def update_with_slug(db: Session, slug: str, body: ProductUpdate) -> Product:
    item = get_with_slug(db, slug)
    filtered_body = sanitize(body)
    db.query(Product).filter(Product.slug == slug).update(filtered_body)
    db.commit()
    db.refresh(item)
    return item


def delete_with_slug(db: Session, slug: str):
    item = get_with_slug(db, slug)
    db.delete(item)
    db.commit()
    return True
