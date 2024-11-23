from sqlalchemy import Column, String, Enum, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship
from app.db import Base
import enum
from uuid import uuid4


class RoleEnum(enum.Enum):
    ADMIN = "ADMIN"
    EDITOR = "EDITOR"
    VIEWER = "VIEWER"
    BILLING = "BILLING"
    DEMAND_MANAGER = "DEMAND_MANAGER"
    SUPERADMIN = "SUPERADMIN"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), nullable=False, default=RoleEnum.VIEWER)
    # Relación con roles en unidades de negocio
    business_unit_roles = relationship("UserBusinessUnitRole", back_populates="user")


class UserBusinessUnitRole(Base):
    __tablename__ = "user_business_unit_roles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    business_unit_id = Column(Integer, ForeignKey("business_units.id"), nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)
    user = relationship("User", back_populates="business_unit_roles")
    business_unit = relationship("BusinessUnit", back_populates="user_roles")