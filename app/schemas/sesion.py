from pydantic import BaseModel, Field
from datetime import datetime

class SesionBase(BaseModel):
    disciplina_id: int
    fecha_hora_inicio: datetime
    fecha_hora_fin: datetime
    cupo_maximo: int = Field(..., gt=0) # Debe ser mayor a 0

class SesionCreate(SesionBase):
    pass

class SesionResponse(SesionBase):
    id: int

    class Config:
        from_attributes = True