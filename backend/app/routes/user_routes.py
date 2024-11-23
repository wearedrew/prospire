# routes/user_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.user import User, RoleEnum
from app.schemas.user import UserCreate, UserResponse
from app.utils.auth import hash_password

router = APIRouter()

@router.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Crea un nuevo usuario con la contraseña hasheada y asigna un rol.
    """
    hashed_password = hash_password(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/users/", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    """
    Lista todos los usuarios registrados en el sistema.
    """
    users = db.query(User).all()
    return users

@router.put("/users/{user_id}/role", response_model=UserResponse)
def update_user_role(user_id: int, role: RoleEnum, db: Session = Depends(get_db)):
    """
    Actualiza el rol de un usuario específico.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.role = role
    db.commit()
    db.refresh(user)
    return user

@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Elimina un usuario por su ID.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}