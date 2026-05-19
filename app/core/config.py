"""
Configuración centralizada
Lee variables de entorno con valores por defecto
"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    """Configuración de la aplicación SmartGym"""
   
    # --- Base de datos ---
    @property
    def DATABASE_URL(self) -> str:  # Esta función devolverá un string
        """
        Construye la URL de conexión a PostgreSQL.
        El formato es: postgresql://usuario:contraseña@host:puerto/nombre_db
        """
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


    DATABASE_URL: str = "postgresql://smartgym_user:smartgym_pass@localhost:5432/smartgym_db"
    
    # --- Seguridad JWT ---
    SECRET_KEY: str = "smartgym-clave-secreta-desarrollo-2026"   ####CAMBIAR :)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
   
    # --- Nombre de la aplicación ---
    APP_NAME: str = "SmartGym API"
    APP_VERSION: str = "1.0.0"
   
    


@lru_cache()
def get_settings() -> Settings: # Esta función devolverá un objeto que es una instancia de la clase Settings
    """
    Retorna la configuración cacheada.
    lru_cache evita leer el archivo .env cada vez que se necesita la config.
    """
    return Settings()


# Instancia global para importar el objeto setting en cualquier módulo
settings = get_settings()