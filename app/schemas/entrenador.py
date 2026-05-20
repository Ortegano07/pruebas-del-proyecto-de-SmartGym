from pydantic import BaseModel
from typing import Optional


class EntrenadorBase(BaseModel):
    usuario_id: int
    especialidad: Optional[str] = None
    activo: Optional[bool] = True


class EntrenadorCreate(EntrenadorBase):
    pass


class EntrenadorUpdate(BaseModel):
    especialidad: Optional[str] = None
    activo: Optional[bool] = None


class EntrenadorResponse(EntrenadorBase):
    id: int

    class Config:
        from_attributes = True
