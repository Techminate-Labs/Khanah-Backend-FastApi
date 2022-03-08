from fastapi import APIRouter

from .controllers import items_controller_testing

router = APIRouter(prefix="/item")


@router.get("/")
def test_items():
    items_controller_testing()
    return {"msg": "Working"}

