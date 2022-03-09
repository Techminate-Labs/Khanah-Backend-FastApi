from decouple import config
from pydantic import BaseModel


class Settings(BaseModel):
    PROJECT_TITLE: str = "Khanah Backend"
    PROJECT_VERSION: str = "1.0.0"

    DATABASE_USER: str = config("POSTGRES_USER")
    DATABASE_PASSWORD: str = config("POSTGRES_PASSWORD")
    DATABASE_SERVER: str = config("POSTGRES_SERVER")
    DATABASE_PORT: str = config("POSTGRES_PORT")
    DATABASE_NAME: str = config("POSTGRES_NAME")
    DATABASE_URL: str = f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_SERVER}:{DATABASE_PORT}/{DATABASE_NAME}"


settings = Settings()
