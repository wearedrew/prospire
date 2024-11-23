from sqlalchemy import Column, String, ForeignKey, UUID
from sqlalchemy.orm import relationship, backref
from app.db import Base
from uuid import uuid4

class Component(Base):
    __tablename__ = "components"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    parent_id = Column(UUID(as_uuid=True), ForeignKey("components.id"), nullable=True)
    item_id = Column(UUID(as_uuid=True), ForeignKey("items.id"), nullable=False)

    # Relación con `Item`
    item = relationship("Item", back_populates="components")

    # Relación jerárquica (subcomponentes)
    sub_components = relationship("Component", backref=backref("parent", remote_side=[id]))