from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings  # Asegúrate de que aquí esté la cadena de conexión correcta

DATABASE_URL = settings.DATABASE_URL

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Crear una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarar la base para las clases de los modelos
Base = declarative_base()

# Función para inicializar la base de datos, creando las tablas
def init_db():
    # Importa todos los modelos para registrar sus metadatos en SQLAlchemy
    from app.models import user, company, business_unit, item, component
    Base.metadata.create_all(bind=engine, checkfirst=True)

# Función para obtener una sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()