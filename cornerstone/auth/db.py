from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config.config import settings

DATABASE_URL_AIO = settings.get("DATABASE_URL_AIO")
print(f"!!! DATABASE_URL_AIO = {DATABASE_URL_AIO}")

DeclarativeBase = declarative_base()


class User(SQLAlchemyBaseUserTableUUID, DeclarativeBase):
    pass

engine = create_async_engine(DATABASE_URL_AIO)

async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(DeclarativeBase.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)