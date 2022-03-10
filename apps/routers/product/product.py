from typing import List

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from apps.controllers.product import product as controllers
from apps.schemas.product import ProductCreate
from apps.schemas.product import ProductOut
from apps.schemas.product import ProductUpdate
from config.dependencies import get_db

router = APIRouter(prefix="/product", tags=["Product"])


@router.get("/", status_code=200, response_model=List[ProductOut])
def get_all_items(limit: int = 20, skip: int = 0, db: Session = Depends(get_db)):
    items = controllers.get_all_products(limit=limit, skip=skip, db=db)
    return items


@router.get("/{slug}/", status_code=200, response_model=ProductOut)
def get_item_with_slug(slug: str, db: Session = Depends(get_db)):
    item = controllers.get_products_by_slug(slug=slug, db=db)
    return item


@router.post("/", status_code=201, response_model=ProductOut)
def create_item(body: ProductCreate, db: Session = Depends(get_db)):
    item = controllers.create_product(body, db)
    return item


@router.put("/{slug}/", status_code=200, response_model=ProductOut)
def update_item(slug: str, body: ProductUpdate, db: Session = Depends(get_db)):
    item = controllers.update_product_with_slug(body=body, slug=slug, db=db)
    return item


@router.delete("/{slug}/", status_code=200)
def delete_item(slug: str, db: Session = Depends(get_db)):
    message = controllers.delete_product_with_slug(db=db, slug=slug)
    return message
