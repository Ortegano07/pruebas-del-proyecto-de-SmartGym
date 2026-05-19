from pydantic import BaseModel, Field
from typing import Optional

class DisciplinaBase(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=50)
    descripcion: Optional[str] = None

class DisciplinaCreate(DisciplinaBase):
    pass

class DisciplinaResponse(DisciplinaBase):
    id: int

    class Config:
        from_attributes = True