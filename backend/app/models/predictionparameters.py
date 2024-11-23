from sqlalchemy import Column, ForeignKey, Float, Integer, UUID
from sqlalchemy.orm import relationship
from app.db import Base
from uuid import uuid4

class PredictionParameters(Base):
    __tablename__ = "prediction_parameters"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    company_id = Column(UUID(as_uuid=True), ForeignKey("companies.id"), nullable=False)
    risk_tolerance = Column(Float, nullable=False)
    forecast_horizon = Column(Integer, nullable=False)
    update_frequency = Column(Integer, nullable=False)

    # Relación con Company
    company = relationship("Company", back_populates="prediction_parameters")