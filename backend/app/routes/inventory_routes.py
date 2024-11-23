from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.inventory import InventoryItem
from app.schemas.inventory import InventoryItemCreate, InventoryItemResponse
from datetime import datetime

router = APIRouter()

@router.post("/inventory/", response_model=InventoryItemResponse)
def create_inventory_item(item: InventoryItemCreate, db: Session = Depends(get_db)):
    db_item = InventoryItem(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {
        "id": db_item.id,
        "name": db_item.name,
        "quantity": db_item.quantity,
        "minimum_stock": db_item.minimum_stock,
        "supplier": db_item.supplier,
        "last_updated": db_item.last_updated.isoformat() if db_item.last_updated else None,
    }

@router.get("/inventory/{item_id}", response_model=InventoryItemResponse)
def get_inventory_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(InventoryItem).filter(InventoryItem.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return {
        "id": db_item.id,
        "name": db_item.name,
        "quantity": db_item.quantity,
        "minimum_stock": db_item.minimum_stock,
        "supplier": db_item.supplier,
        "last_updated": db_item.last_updated.isoformat() if db_item.last_updated else None,
    }

@router.put("/inventory/{item_id}", response_model=InventoryItemResponse)
def update_inventory_item(item_id: int, item: InventoryItemCreate, db: Session = Depends(get_db)):
    db_item = db.query(InventoryItem).filter(InventoryItem.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item.dict().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return {
        "id": db_item.id,
        "name": db_item.name,
        "quantity": db_item.quantity,
        "minimum_stock": db_item.minimum_stock,
        "supplier": db_item.supplier,
        "last_updated": db_item.last_updated.isoformat() if db_item.last_updated else None,
    }

@router.delete("/inventory/{item_id}")
def delete_inventory_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(InventoryItem).filter(InventoryItem.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"message": f"Item with id {item_id} deleted successfully"}

@router.get("/inventory/items", response_model=list[InventoryItemResponse])
def get_all_inventory_items(db: Session = Depends(get_db)):
    items = db.query(InventoryItem).all()
    return [
        {
            "id": item.id,
            "name": item.name,
            "quantity": item.quantity,
            "minimum_stock": item.minimum_stock,
            "supplier": item.supplier,
            "last_updated": item.last_updated.isoformat() if item.last_updated else None,
        }
        for item in items
    ]