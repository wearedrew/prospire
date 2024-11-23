from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.predictionresults import PredictionResultsCreate, PredictionResultsResponse
from app.models.predictionresults import PredictionResults
from app.db import get_db

router = APIRouter()

@router.get("/", response_model=list[PredictionResultsResponse])
def get_all_prediction_results(db: Session = Depends(get_db)):
    """
    Obtiene todos los resultados de predicción.
    """
    results = db.query(PredictionResults).all()
    return results

@router.post("/", response_model=PredictionResultsResponse)
def create_prediction_result(
    payload: PredictionResultsCreate, db: Session = Depends(get_db)
):
    """
    Crea un nuevo resultado de predicción.
    """
    new_result = PredictionResults(**payload.dict())
    db.add(new_result)
    db.commit()
    db.refresh(new_result)
    return new_result

@router.get("/{result_id}", response_model=PredictionResultsResponse)
def get_prediction_result_by_id(result_id: str, db: Session = Depends(get_db)):
    """
    Obtiene un resultado de predicción por su ID.
    """
    result = db.query(PredictionResults).filter(PredictionResults.id == result_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Prediction result not found")
    return result

@router.delete("/{result_id}")
def delete_prediction_result(result_id: str, db: Session = Depends(get_db)):
    """
    Elimina un resultado de predicción por su ID.
    """
    result = db.query(PredictionResults).filter(PredictionResults.id == result_id).first()
    if not result:
        raise HTTPException(status_code=404, detail="Prediction result not found")
    db.delete(result)
    db.commit()
    return {"message": "Prediction result deleted successfully"}