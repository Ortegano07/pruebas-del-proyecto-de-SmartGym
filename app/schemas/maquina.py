from pydantic import BaseModel
from datetime import date
from app.models.maquina import EstadoMaquina

class MaquinaBase(BaseModel):
    categoria_id: int
    nombre: str
    descripcion_tecnica: str
    fecha_adquisicion: date
    ultima_revision: date

class MaquinaCreate(MaquinaBase):
    pass

class MaquinaOut(MaquinaBase):
    id: int
    estado_operativo: EstadoMaquina

    class Config:
        from_attributes = True
