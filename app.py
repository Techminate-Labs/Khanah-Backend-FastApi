from fastapi import FastAPI

from apps.routers.base import router
from config.settings import settings
from database.models.base import Base
from database.session import engine


def include_router(app: FastAPI) -> None:
    app.include_router(router)


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    include_router(app)
    create_tables()
    return app


app = start_application()
