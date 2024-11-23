from pydantic import BaseModel
from uuid import UUID

class PredictionParametersBase(BaseModel):
    parameter_name: str
    parameter_value: str

class PredictionParametersCreate(PredictionParametersBase):
    pass

class PredictionParametersResponse(PredictionParametersBase):
    id: UUID

    class Config:
        orm_mode = True