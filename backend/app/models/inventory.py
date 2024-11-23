from sqlalchemy import Column, Integer, String, Float, DateTime, func
from app.db import Base

class InventoryItem(Base):
    __tablename__ = "inventory_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    quantity = Column(Integer, nullable=False)
    minimum_stock = Column(Integer, default=0)
    supplier = Column(String, nullable=True)
    last_updated = Column(DateTime, server_default=func.now(), onupdate=func.now())