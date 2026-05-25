from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.sesion import Sesion
from app.schemas.sesion import SesionCreate


def crear_sesion(db: Session, data: SesionCreate):
    # Validar horario
    if data.hora_fin <= data.hora_inicio:
        raise HTTPException(400, "La hora de fin debe ser posterior a la de inicio")
   
    # Validar solapamiento de entrenador
    horario_ocupado = db.query(Sesion).filter(
        Sesion.entrenador_id == data.entrenador_id,
        Sesion.fecha == data.fecha,
        Sesion.hora_inicio < data.hora_fin,
        Sesion.hora_fin > data.hora_inicio
    ).first()
   
    if horario_ocupado:
        raise HTTPException(409, "El entrenador ya tiene una sesión en ese horario")
   
    nueva_sesion = Sesion(**data.model_dump())
    db.add(nueva_sesion)
    db.commit()
    db.refresh(nueva_sesion)
    return nueva_sesion


def obtener_sesiones(db: Session):
    return db.query(Sesion).all()