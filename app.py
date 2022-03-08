from fastapi import FastAPI

from core.settings import settings
from core.database import engine
from versions.v1 import v1_router
from models.base import Base


def include_router(app: FastAPI) -> None:
    app.include_router(v1_router)


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    include_router(app)
    create_tables()
    return app


app = start_application()
