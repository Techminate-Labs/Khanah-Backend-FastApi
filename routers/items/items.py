from typing import List

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from config.dependencies import get_db
from controllers.items import items as controllers
from schemas.items import ItemCreate
from schemas.items import ItemOut
from schemas.items import ItemUpdate

router = APIRouter(prefix="/item", tags=["Items"])


@router.get("/", status_code=200, response_model=List[ItemOut])
def get_all_items(limit: int = 20, skip: int = 0, db: Session = Depends(get_db)):
    items = controllers.get_all_items(limit=limit, skip=skip, db=db)
    return items


@router.get("/{slug}/", status_code=200, response_model=ItemOut)
def get_item_with_slug(slug: str, db: Session = Depends(get_db)):
    item = controllers.get_item_by_slug(slug=slug, db=db)
    return item


@router.post("/", status_code=201, response_model=ItemOut)
def create_item(body: ItemCreate, db: Session = Depends(get_db)):
    item = controllers.create_item(body, db)
    return item


@router.put("/{slug}/", status_code=200, response_model=ItemOut)
def update_item(slug: str, body: ItemUpdate, db: Session = Depends(get_db)):
    item = controllers.update_item_with_slug(slug=slug, body=body, db=db)
    return item


@router.delete("/{slug}/", status_code=200)
def delete_item(slug: str, db: Session = Depends(get_db)):
    message = controllers.delete_item_with_slug(db=db, slug=slug)
    return message
