from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db import Base
import uuid

class BusinessUnit(Base):
    __tablename__ = "business_units"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    company_id = Column(UUID(as_uuid=True), ForeignKey("companies.id"), nullable=False)

    # Relaciones
    user_roles = relationship("UserBusinessUnitRole", back_populates="business_unit")
    company = relationship("Company", back_populates="business_units")

    # Relación con Items (tabla intermedia)
    items = relationship("Item", secondary="business_unit_items", back_populates="business_units")
    historical_demand = relationship("HistoricalDemand", back_populates="business_unit")