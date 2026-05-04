# настройка подключения к базе данных postgresql
# используется asyncpg для асинхронной работы

import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base

# строка подключения к postgresql
# db - имя сервиса в docker-compose
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://demo_user:demo_password@db:5432/demo_db"
)

# создание асинхронного движка
engine = create_async_engine(DATABASE_URL, echo=True)

# фабрика сессий
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# базовый класс для моделей
Base = declarative_base()


async def get_session() -> AsyncSession:
    """получение сессии базы данных"""
    async with async_session() as session:
        yield session
