from passlib.context import CryptContext
from app.models.user import User
from app.db import SessionLocal

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Función para verificar la contraseña
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Función para obtener un usuario por nombre de usuario
def get_user_by_username(username: str):
    db = SessionLocal()
    try:
        # Realizar la consulta con la sesión
        return db.query(User).filter(User.username == username).first()
    finally:
        db.close()  # Asegúrate de cerrar la sesión después de la consulta

# Función para hashear la contraseña
def hash_password(password: str):
    return pwd_context.hash(password)