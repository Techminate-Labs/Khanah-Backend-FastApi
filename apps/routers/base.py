from fastapi import APIRouter

from apps.routers.product.product import router as items_router
from apps.routers.user.user import router as user_router

router = APIRouter(prefix="/v1")

router.include_router(items_router)
router.include_router(user_router)
