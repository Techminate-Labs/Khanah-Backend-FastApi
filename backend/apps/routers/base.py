from apps.routers.product.product import router as items_router
from fastapi import APIRouter

router = APIRouter(prefix="/v1")

router.include_router(items_router)
