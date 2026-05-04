# модели sqlalchemy для работы с базой данных

from sqlalchemy import Column, Integer, String, Float
from .database import Base


class Item(Base):
    """модель товара в магазине"""
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(500), nullable=True)
