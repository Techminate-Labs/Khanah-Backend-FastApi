from sqlalchemy.orm import Session

from repositories.items import create
from repositories.items import delete_with_slug
from repositories.items import get_all
from repositories.items import get_with_slug
from repositories.items import update_with_slug
from schemas.items import ItemCreate
from schemas.items import ItemUpdate


def get_all_items(*, limit: int = 20, skip: int = 0, db: Session):
    items = get_all(db=db, limit=limit, skip=skip)
    return items


def get_item_by_slug(*, slug: str, db: Session):
    item = get_with_slug(slug=slug, db=db)
    return item


def create_item(body: ItemCreate, db: Session):
    item = create(body, db)
    return item


def update_item_with_slug(body: ItemUpdate, slug: str, db: Session):
    item = update_with_slug(db=db, body=body, slug=slug)
    return item


def delete_item_with_slug(db: Session, slug: str):
    delete_with_slug(db=db, slug=slug)
    return {"msg": "deleted."}
