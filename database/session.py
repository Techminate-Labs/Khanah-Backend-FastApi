from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.settings import settings

SQLALCHEMY_DATABASE_URI = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# if you don't want to install postgres or any database,
# use sqlite, a file system based database,
# uncomment below lines if you would like to use sqlite and comment above
# 2 lines of SQLALCHEMY_DATABASE_URL AND engine

# SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite3"
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
