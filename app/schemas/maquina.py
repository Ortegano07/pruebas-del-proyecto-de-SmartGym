from pydantic import BaseModel
from typing import Optional

class MaquinaBase(BaseModel):
    nombre: str
    codigo_serial: str
    estado: Optional[str] = "disponible"
    categoria_id: int

class MaquinaCreate(MaquinaBase):
    pass

class MaquinaResponse(MaquinaBase):
    id: int

    class Config:
        from_attributes = True
