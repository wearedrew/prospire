from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.predictionparameters import PredictionParametersCreate, PredictionParametersResponse
from app.models.predictionparameters import PredictionParameters
from app.db import get_db

router = APIRouter()

@router.get("/", response_model=list[PredictionParametersResponse])
def get_all_prediction_parameters(db: Session = Depends(get_db)):
    """
    Obtiene todos los parámetros de predicción.
    """
    parameters = db.query(PredictionParameters).all()
    return parameters

@router.post("/", response_model=PredictionParametersResponse)
def create_prediction_parameters(
    payload: PredictionParametersCreate, db: Session = Depends(get_db)
):
    """
    Crea un nuevo parámetro de predicción.
    """
    new_parameters = PredictionParameters(**payload.dict())
    db.add(new_parameters)
    db.commit()
    db.refresh(new_parameters)
    return new_parameters

@router.get("/{parameters_id}", response_model=PredictionParametersResponse)
def get_prediction_parameters_by_id(parameters_id: str, db: Session = Depends(get_db)):
    """
    Obtiene un parámetro de predicción por su ID.
    """
    parameters = db.query(PredictionParameters).filter(PredictionParameters.id == parameters_id).first()
    if not parameters:
        raise HTTPException(status_code=404, detail="Prediction parameters not found")
    return parameters

@router.delete("/{parameters_id}")
def delete_prediction_parameters(parameters_id: str, db: Session = Depends(get_db)):
    """
    Elimina un parámetro de predicción por su ID.
    """
    parameters = db.query(PredictionParameters).filter(PredictionParameters.id == parameters_id).first()
    if not parameters:
        raise HTTPException(status_code=404, detail="Prediction parameters not found")
    db.delete(parameters)
    db.commit()
    return {"message": "Prediction parameters deleted successfully"}