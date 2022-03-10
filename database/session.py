from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.settings import settings

SQLALCHEMY_DATABASE_URI = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URI)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
