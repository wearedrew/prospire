import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db import Base

class Company(Base):
    __tablename__ = "companies"

    # Definición de columnas
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, index=True, nullable=False)

    # Relaciones
    business_units = relationship("BusinessUnit", back_populates="company", cascade="all, delete-orphan")
    prediction_parameters = relationship("PredictionParameters", back_populates="company")