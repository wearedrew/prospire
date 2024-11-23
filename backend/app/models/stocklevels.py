from sqlalchemy import Column, ForeignKey, Float, Date, UUID
from sqlalchemy.orm import relationship
from app.db import Base
from uuid import uuid4

class StockLevels(Base):
    __tablename__ = "stock_levels"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    item_id = Column(UUID(as_uuid=True), ForeignKey("items.id"), nullable=False)
    date = Column(Date, nullable=False)
    stock_quantity = Column(Float, nullable=False)

    # Relación con Items
    item = relationship("Item", back_populates="stock_history")