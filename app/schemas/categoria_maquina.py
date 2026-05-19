from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class CategoriaMaquinaBase(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=100)
    descripcion: Optional[str] = None

class CategoriaMaquinaCreate(CategoriaMaquinaBase):
    pass

class CategoriaMaquinaResponse(CategoriaMaquinaBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True