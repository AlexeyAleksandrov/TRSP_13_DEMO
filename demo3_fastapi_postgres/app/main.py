# fastapi приложение с подключением к postgresql

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, text

from .database import get_session, engine, Base
from .models import Item
from .schemas import ItemCreate, ItemResponse

app = FastAPI(
    title="Demo Store API",
    description="TRSP_13_DEMO"
)


@app.on_event("startup")
async def startup():
    """создание таблиц при запуске приложения"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def root():
    """корневой эндпоинт"""
    return {"message": "Demo Store API", "docs": "/docs"}


@app.get("/health")
async def health_check(session: AsyncSession = Depends(get_session)):
    """проверка подключения к базе данных"""
    try:
        await session.execute(text("SELECT 1"))
        return {"status": "ok", "database": "connected"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/items", response_model=ItemResponse)
async def create_item(item: ItemCreate, session: AsyncSession = Depends(get_session)):
    """создание нового товара"""
    db_item = Item(name=item.name, price=item.price, description=item.description)
    session.add(db_item)
    await session.commit()
    await session.refresh(db_item)
    return db_item


@app.get("/items", response_model=list[ItemResponse])
async def get_items(session: AsyncSession = Depends(get_session)):
    """получение списка всех товаров"""
    result = await session.execute(select(Item))
    items = result.scalars().all()
    return items


@app.get("/items/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int, session: AsyncSession = Depends(get_session)):
    """получение товара по идентификатору"""
    result = await session.execute(select(Item).where(Item.id == item_id))
    item = result.scalar_one_or_none()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
