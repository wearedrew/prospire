from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class StockLevelsBase(BaseModel):
    item_id: UUID
    stock_quantity: int
    last_updated: datetime

class StockLevelsCreate(StockLevelsBase):
    pass

class StockLevelsResponse(StockLevelsBase):
    id: UUID

    class Config:
        orm_mode = True