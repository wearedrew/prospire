from pydantic import BaseModel
from uuid import UUID
from datetime import date

class HistoricalDemandBase(BaseModel):
    item_id: UUID
    business_unit_id: UUID
    demand_date: date
    demand: int

class HistoricalDemandCreate(HistoricalDemandBase):
    pass

class HistoricalDemandUpdate(HistoricalDemandBase):
    pass

class HistoricalDemandResponse(HistoricalDemandBase):
    id: UUID
    item_id: UUID


    class Config:
        form_attributes = True