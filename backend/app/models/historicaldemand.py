from sqlalchemy import Column, ForeignKey, Float, Date, UUID
from sqlalchemy.orm import relationship
from app.db import Base
from uuid import uuid4

class HistoricalDemand(Base):
    __tablename__ = "historical_demand"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    item_id = Column(UUID(as_uuid=True), ForeignKey("items.id", ondelete="CASCADE"), nullable=False)
    business_unit_id = Column(UUID(as_uuid=True), ForeignKey("business_units.id", ondelete="CASCADE"), nullable=True)
    date = Column(Date, nullable=False)
    quantity = Column(Float, nullable=False)
    created_at = Column(Date, nullable=False, default="now")
    updated_at = Column(Date, nullable=False, default="now")

    # Relationships
    item = relationship("Item", back_populates="demand_history")
    business_unit = relationship("BusinessUnit", back_populates="historical_demands")