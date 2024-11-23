from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db import Base
from uuid import uuid4

# Tabla intermedia entre BusinessUnit y Items
business_unit_items = Table(
    "business_unit_items",
    Base.metadata,
    Column("business_unit_id", UUID(as_uuid=True), ForeignKey("business_units.id"), primary_key=True),
    Column("item_id", UUID(as_uuid=True), ForeignKey("items.id"), primary_key=True),
)

class Item(Base):
    __tablename__ = "items"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    parent_id = Column(UUID(as_uuid=True), ForeignKey("items.id"), nullable=True)

    # Relación con BusinessUnits (tabla intermedia)
    business_units = relationship("BusinessUnit", secondary="business_unit_items", back_populates="items")

    # Otras relaciones
    components = relationship("Component", back_populates="item")
    demand_history = relationship("HistoricalDemand", back_populates="item")
    stock_history = relationship("StockLevels", back_populates="item")
    prediction_results = relationship("PredictionResults", back_populates="item")