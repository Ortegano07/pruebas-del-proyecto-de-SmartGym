from pydantic import BaseModel
from typing import Optional

class RolCreate(BaseModel):
    """Datos para crear un nuevo rol"""
    nombre: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "Administrador"
            }
        }

class RolResponse(BaseModel):
    """Datos que retorna la API al consultar un rol"""
    id: int
    nombre: str
    
    class Config:
        from_attributes = True