from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class TicketBase(BaseModel):
    maquina_id: int
    descripcion_falla: str = Field(..., min_length=10)

class TicketCreate(TicketBase):
    pass

class TicketResponse(TicketBase):
    id: int
    estado: str
    fecha_reporte: datetime

    class Config:
        from_attributes = True