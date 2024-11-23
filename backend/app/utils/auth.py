from passlib.context import CryptContext
from app.models.user import User
from app.db import get_db
from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

# Configuración para el hashing de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Claves para los JWT
SECRET_KEY = "ProSpireUltraSecureSecretKey2024!"  # Usaremos esta clave fija para el proyecto
ALGORITHM = "HS256"

# Función para hashear contraseñas
def hash_password(password: str) -> str:
    """
    Genera un hash seguro para la contraseña proporcionada.
    """
    return pwd_context.hash(password)

# Función para verificar contraseñas
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica si la contraseña en texto plano coincide con su hash.
    """
    return pwd_context.verify(plain_password, hashed_password)

# Función para obtener un usuario por nombre de usuario
def get_user_by_username(username: str, db: Session) -> User:
    """
    Busca un usuario por nombre de usuario en la base de datos.
    """
    return db.query(User).filter(User.username == username).first()

# Función para crear un token JWT
def create_access_token(data: dict) -> str:
    """
    Crea un token JWT con los datos proporcionados.
    """
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

# Middleware para obtener el usuario actual a partir del token
def get_current_user(token: str, db: Session = Depends(get_db)) -> User:
    """
    Decodifica un token JWT y obtiene el usuario correspondiente.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if not username:
            raise HTTPException(status_code=401, detail="Invalid token: missing subject")
        user = get_user_by_username(username, db)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Middleware para verificar el rol del usuario
def verify_role(required_role: str):
    """
    Middleware para verificar que el usuario tiene el rol requerido.
    """
    def role_checker(current_user: User = Depends(get_current_user)) -> User:
        if current_user.role != required_role:
            raise HTTPException(status_code=403, detail="Not enough permissions")
        return current_user
    return role_checker