import uuid  # Agrega esta línea al inicio del archivo

from sqlalchemy import Column, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.db import Base
from app.models.role_enum import RoleEnum

class UserBusinessUnitRole(Base):
    __tablename__ = "user_business_unit_roles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    business_unit_id = Column(UUID(as_uuid=True), ForeignKey("business_units.id"), nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)

    user = relationship("User", back_populates="business_unit_roles")
    business_unit = relationship("BusinessUnit", back_populates="user_roles")