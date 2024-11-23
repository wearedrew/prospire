from pydantic import BaseModel, EmailStr
from enum import Enum

# Definición de roles como un enumerado
class RoleEnum(str, Enum):
    ADMIN = "ADMIN"
    EDITOR = "EDITOR"
    VIEWER = "VIEWER"
    BILLING = "BILLING"
    DEMAND_MANAGER = "DEMAND_MANAGER"

# Esquema para registrar un usuario
class UserRegister(BaseModel):
    username: str
    password: str
    email: EmailStr
    role: RoleEnum = RoleEnum.VIEWER  # Rol por defecto

# Alias para UserCreate (mismo esquema que UserRegister)
UserCreate = UserRegister

# Esquema para login de usuario
class UserLogin(BaseModel):
    username: str
    password: str

# Esquema para respuesta de usuario
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: RoleEnum

    class Config:
        from_attributes = True