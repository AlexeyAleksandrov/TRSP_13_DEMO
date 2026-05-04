# pydantic схемы для валидации данных

from pydantic import BaseModel
from typing import Optional


class ItemCreate(BaseModel):
    """схема для создания товара"""
    name: str
    price: float
    description: Optional[str] = None


class ItemResponse(BaseModel):
    """схема ответа с данными товара"""
    id: int
    name: str
    price: float
    description: Optional[str] = None

    class Config:
        from_attributes = True
