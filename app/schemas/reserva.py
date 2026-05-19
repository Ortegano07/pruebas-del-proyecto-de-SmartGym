from pydantic import BaseModel

class ReservaBase(BaseModel):
    cliente_id: int
    sesion_id: int

class ReservaCreate(ReservaBase):
    pass

class ReservaResponse(ReservaBase):
    id: int

    class Config:
        from_attributes = True