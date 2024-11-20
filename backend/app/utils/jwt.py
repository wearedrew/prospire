from app.config import settings
from datetime import datetime, timedelta
from jose import JWTError, jwt

# Asegurémonos de que la SECRET_KEY esté correctamente asignada
SECRET_KEY = settings.SECRET_KEY  # Debería ser settings.secret_key, ya que cargamos las variables de .env
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

# Función para crear el token
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt