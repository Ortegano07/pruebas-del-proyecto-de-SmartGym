from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UsuarioCreate(BaseModel):
    """Datos para crear un nuevo usuario"""
    email: EmailStr
    password: str
    nombre: str
    apellido: str
    rol_id: int
    
    class Config:
        json_schema_extra = {
            "example": {
                "email": "admin@smartgym.com",
                "password": "Admin123!",
                "nombre": "Luis",
                "apellido": "Moreno",
                "rol_id": 1
            }
        }

class UsuarioResponse(BaseModel):
    """Datos que retorna la API al consultar un usuario"""
    id: int
    email: str
    nombre: str
    apellido: str
    activo: bool
    rol_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True