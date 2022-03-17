from apps.routers.base import router
from config.settings import settings
from fastapi import FastAPI
from starlette.responses import RedirectResponse


def include_router(app: FastAPI) -> None:
    app.include_router(router)


def start_application() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    include_router(app)

    @app.get("/")
    def redirect_to_docs():
        return RedirectResponse("/docs")

    return app


app = start_application()
