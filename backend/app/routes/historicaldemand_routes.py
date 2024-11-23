from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.historicaldemand import HistoricalDemandCreate, HistoricalDemandResponse
from app.models.historicaldemand import HistoricalDemand
from app.db import get_db

router = APIRouter()

@router.get("/", response_model=list[HistoricalDemandResponse])
def get_all_historical_demands(db: Session = Depends(get_db)):
    """
    Obtiene todos los registros de demanda histórica.
    """
    demands = db.query(HistoricalDemand).all()
    return demands

@router.post("/", response_model=HistoricalDemandResponse)
def create_historical_demand(payload: HistoricalDemandCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo registro de demanda histórica.
    """
    new_demand = HistoricalDemand(**payload.dict())
    db.add(new_demand)
    db.commit()
    db.refresh(new_demand)
    return new_demand

@router.get("/{demand_id}", response_model=HistoricalDemandResponse)
def get_historical_demand_by_id(demand_id: str, db: Session = Depends(get_db)):
    """
    Obtiene un registro de demanda histórica por su ID.
    """
    demand = db.query(HistoricalDemand).filter(HistoricalDemand.id == demand_id).first()
    if not demand:
        raise HTTPException(status_code=404, detail="Historical demand not found")
    return demand

@router.delete("/{demand_id}")
def delete_historical_demand(demand_id: str, db: Session = Depends(get_db)):
    """
    Elimina un registro de demanda histórica por su ID.
    """
    demand = db.query(HistoricalDemand).filter(HistoricalDemand.id == demand_id).first()
    if not demand:
        raise HTTPException(status_code=404, detail="Historical demand not found")
    db.delete(demand)
    db.commit()
    return {"message": "Historical demand deleted successfully"}