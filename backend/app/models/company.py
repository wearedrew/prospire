# app/models/company.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db import Base  # Asegúrate de que esto esté bien importado

class Company(Base):
    __tablename__ = "companies"  # Nombre de la tabla en la base de datos

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    # Relación con la tabla User (si corresponde)
    users = relationship("User", back_populates="company")