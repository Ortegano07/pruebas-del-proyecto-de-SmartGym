from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.sesion import Sesion
from app.schemas.sesion import SesionCreate

def crear_sesion(db: Session, data: SesionCreate):
    if data.fecha_hora_fin <= data.fecha_hora_inicio:
        raise HTTPException(status_code=400, detail="La hora de fin debe ser posterior a la de inicio")
        
    nueva_sesion = Sesion(**data.dict())
    db.add(nueva_sesion)
    db.commit()
    db.refresh(nueva_sesion)
    return nueva_sesion

def obtener_sesiones(db: Session):
    return db.query(Sesion).all()