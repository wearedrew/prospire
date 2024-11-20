from pydantic_settings import BaseSettings  # Cambia la importación

class Settings(BaseSettings):
    # Configuración general
    app_name: str = "ProSpire SaaS"
    version: str = "1.0.0"
    debug: bool = True

    # Configuración de la base de datos
    DATABASE_URL: str = "postgresql://postgres:prospire2025@localhost/prospire"

    # Configuración de seguridad
    SECRET_KEY: str = "77uWOrLryNQPrly2Tx/6h0WuzCOSosWd4kNapz1zQBk6TgrxjwEhnSbI4p6uzzdIREPKXtlAtuIMtAmbH9+SzA"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # Configuración de CORS
    allowed_origins: list[str] = ["http://localhost:3000"]

    class Config:
        # No es necesario definir env_file, ya que no estamos usando .env
        pass

settings = Settings()

# Verificar que las variables se cargan correctamente
print(f"DATABASE_URL: {settings.DATABASE_URL}")
print(f"SECRET_KEY: {settings.SECRET_KEY}")