from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.user import User
from app.schemas import UserRegister  # Asegúrate de que esta importación es correcta
from app.utils.jwt import create_access_token
from app.utils.auth import verify_password, get_user_by_username

router = APIRouter()

@router.post("/register")
def register_user(credentials: UserRegister, db: Session = Depends(get_db)):
    existing_user = get_user_by_username(credentials.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    new_user = User(username=credentials.username, hashed_password=verify_password(credentials.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    access_token = create_access_token(data={"sub": new_user.username})
    return {"access_token": access_token, "token_type": "bearer"}