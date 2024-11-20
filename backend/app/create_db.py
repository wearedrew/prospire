from app.db import engine, Base  # Se importa el engine y la Base de db.py
from app.models import company, user  # Aquí importas los modelos que hayas creado

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine, checkfirst=True)
print("Tablas creadas exitosamente.")

