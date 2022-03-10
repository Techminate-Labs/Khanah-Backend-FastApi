from fastapi import APIRouter

from apps.routers.product.product import router as items_router

router = APIRouter(prefix="/v1")

router.include_router(items_router)
