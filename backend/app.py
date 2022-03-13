from fastapi import FastAPI

from backend.apps.routers.base import router
from backend.config.settings import settings
from backend.database import engine
from backend.database.models.base import Base


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
