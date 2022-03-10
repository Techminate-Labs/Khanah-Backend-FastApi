from sqlalchemy.orm import Session

from apps.repositories.product import create
from apps.repositories.product import delete_with_slug
from apps.repositories.product import get_all
from apps.repositories.product import get_with_slug
from apps.repositories.product import update_with_slug
from apps.schemas.product import ProductCreate
from apps.schemas.product import ProductUpdate


def get_all_products(*, limit: int = 20, skip: int = 0, db: Session):
    items = get_all(db=db, limit=limit, skip=skip)
    return items


def get_products_by_slug(*, slug: str, db: Session):
    item = get_with_slug(slug=slug, db=db)
    return item


def create_product(body: ProductCreate, db: Session):
    item = create(body, db)
    return item


def update_product_with_slug(body: ProductUpdate, slug: str, db: Session):
    item = update_with_slug(db=db, body=body, slug=slug)
    return item


def delete_product_with_slug(db: Session, slug: str):
    delete_with_slug(db=db, slug=slug)
    return {"msg": "deleted."}
