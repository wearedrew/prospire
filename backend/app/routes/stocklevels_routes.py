from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.stocklevels import StockLevelsCreate, StockLevelsResponse
from app.models.stocklevels import StockLevels
from app.db import get_db

router = APIRouter()

@router.get("/", response_model=list[StockLevelsResponse])
def get_all_stock_levels(db: Session = Depends(get_db)):
    """
    Obtiene todos los niveles de stock.
    """
    stock_levels = db.query(StockLevels).all()
    return stock_levels

@router.post("/", response_model=StockLevelsResponse)
def create_stock_level(payload: StockLevelsCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo nivel de stock.
    """
    new_stock = StockLevels(**payload.dict())
    db.add(new_stock)
    db.commit()
    db.refresh(new_stock)
    return new_stock

@router.get("/{stock_id}", response_model=StockLevelsResponse)
def get_stock_level_by_id(stock_id: str, db: Session = Depends(get_db)):
    """
    Obtiene un nivel de stock por su ID.
    """
    stock = db.query(StockLevels).filter(StockLevels.id == stock_id).first()
    if not stock:
        raise HTTPException(status_code=404, detail="Stock level not found")
    return stock

@router.delete("/{stock_id}")
def delete_stock_level(stock_id: str, db: Session = Depends(get_db)):
    """
    Elimina un nivel de stock por su ID.
    """
    stock = db.query(StockLevels).filter(StockLevels.id == stock_id).first()
    if not stock:
        raise HTTPException(status_code=404, detail="Stock level not found")
    db.delete(stock)
    db.commit()
    return {"message": "Stock level deleted successfully"}