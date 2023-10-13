

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
import databases
from config.config import settings
from fastapi import FastAPI


DATABASE_URL = settings.get("DATABASE_URL")
print(f"!!! notes sqlachemy call DATABASE_URL = {DATABASE_URL}")

Base = declarative_base()
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

database = databases.Database(DATABASE_URL)


def create_all_tables(app: FastAPI):
    Base.metadata.create_all(engine)  # Create tables

    app.state.db = database
    print("-- call create all over ----")



