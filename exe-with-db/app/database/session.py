from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlmodel import SQLModel, Session
from sqlalchemy.orm import sessionmaker
from app.database.config import settings

engine = create_async_engine(
    # url="sqlite:///sqlite.db",
    url=f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@localhost:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}",
    echo=True
)

async def create_db_tables():
    async with engine.begin() as connection:
        from .models import Shipment
        await connection.run_sync(SQLModel.metadata.create_all)

async def get_session():
    async_session = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with async_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_session)]