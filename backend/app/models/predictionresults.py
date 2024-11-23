from sqlalchemy import Column, ForeignKey, Float, Date, UUID
from sqlalchemy.orm import relationship
from app.db import Base
from uuid import uuid4

class PredictionResults(Base):
    __tablename__ = "prediction_results"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    item_id = Column(UUID(as_uuid=True), ForeignKey("items.id"), nullable=False)
    prediction_date = Column(Date, nullable=False)
    predicted_demand = Column(Float, nullable=True)
    predicted_stock = Column(Float, nullable=True)

    # Relación con Items
    item = relationship("Item", back_populates="prediction_results")