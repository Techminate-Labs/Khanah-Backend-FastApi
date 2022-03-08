from fastapi import APIRouter
from .items import items_router

v1_router = APIRouter(prefix="/v1")

v1_router.include_router(items_router)
