from pydantic import BaseModel
from typing import Optional

class InventoryItemBase(BaseModel):
    name: str
    quantity: int
    minimum_stock: int
    supplier: Optional[str]

class InventoryItemCreate(InventoryItemBase):
    pass

class InventoryItemResponse(InventoryItemBase):
    id: int
    last_updated: Optional[str]  # Cambiado a str para serialización

    class Config:
        form_attributes = True