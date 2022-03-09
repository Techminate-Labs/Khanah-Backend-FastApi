from typing import List
from typing import Union

from fastapi import HTTPException
from sqlalchemy import desc
from sqlalchemy.orm import Session

from models.items import Items
from schemas.items import ItemCreate
from schemas.items import ItemUpdate
from utils.sanitize_schemas_body import sanitize


def create(body: ItemCreate, db: Session) -> Items:
    item = Items(**body.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def get_all(db: Session, limit: int = 20, skip: int = 0) -> List[Items]:
    items = (
        db.query(Items).order_by(desc(Items.created_at)).offset(skip).limit(limit).all()
    )
    return items


def get(db: Session, _id: int) -> Items:
    item = db.query(Items).get(_id)
    if not item:
        raise HTTPException(404, f"Item with id `{_id} doesn't exist")
    return item


def get_or_none(db: Session, _id: int) -> Union[Items, None]:
    item = db.query(Items).get(_id)
    return item


def get_with_slug(db: Session, slug: str) -> Items:
    item = db.query(Items).filter(Items.slug == slug).first()
    if not item:
        raise HTTPException(404, f"Item with slug `{slug} doesn't exist")
    return item


def get_with_slug_or_none(db: Session, slug: str) -> Union[Items, None]:
    item = db.query(Items).filter(Items.slug == slug).first()
    return item


def update_with_slug(db: Session, slug: str, body: ItemUpdate) -> Items:
    item = get_with_slug(db, slug)
    filtered_body = sanitize(body)
    db.query(Items).filter(Items.slug == slug).update(filtered_body)
    db.commit()
    db.refresh(item)
    return item


def delete_with_slug(db: Session, slug: str):
    item = get_with_slug(db, slug)
    db.delete(item)
    db.commit()
    return True
