from fastapi import APIRouter

from .items.items import router as items_router

router = APIRouter(prefix="/v1")

router.include_router(items_router)
