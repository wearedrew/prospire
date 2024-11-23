from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class PredictionResultsBase(BaseModel):
    prediction_date: datetime
    prediction_value: float

class PredictionResultsCreate(PredictionResultsBase):
    pass

class PredictionResultsResponse(PredictionResultsBase):
    id: UUID

    class Config:
        orm_mode = True