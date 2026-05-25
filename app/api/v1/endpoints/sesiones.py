from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date

from app.models.database import get_db
from app.models.sesion import Sesion
from app.models.disciplina import Disciplina
from app.models.entrenador import Entrenador
from app.schemas.sesion import SesionCreate, SesionUpdate, SesionResponse

router = APIRouter(prefix="/sesiones", tags=["Deportivo"])


@router.post("/", response_model=SesionResponse, status_code=201)
def crear_sesion(datos: SesionCreate, db: Session = Depends(get_db)):
    # Validar disciplina
    if not db.query(Disciplina).filter(Disciplina.id == datos.disciplina_id).first():
        raise HTTPException(404, "Disciplina no encontrada")
   
    # Validar entrenador
    if not db.query(Entrenador).filter(Entrenador.id == datos.entrenador_id).first():
        raise HTTPException(404, "Entrenador no encontrado")
   
    # Validar horario
    if datos.hora_inicio >= datos.hora_fin:
        raise HTTPException(409, "La hora de inicio debe ser menor a la hora de fin")
   
    # Validar solapamiento de entrenador
    conflicto = db.query(Sesion).filter(
        Sesion.entrenador_id == datos.entrenador_id,
        Sesion.fecha == datos.fecha,
        Sesion.hora_inicio < datos.hora_fin,
        Sesion.hora_fin > datos.hora_inicio
    ).first()
    if conflicto:
        raise HTTPException(409, "El entrenador ya tiene una sesión en ese horario")
   
    sesion = Sesion(**datos.model_dump())
    db.add(sesion)
    db.commit()
    db.refresh(sesion)
    return sesion


@router.get("/", response_model=List[SesionResponse])
def listar_sesiones(
    skip: int = 0,
    limit: int = 10,
    fecha: Optional[date] = Query(None),
    disciplina_id: Optional[int] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Sesion)
    if fecha:
        query = query.filter(Sesion.fecha == fecha)
    if disciplina_id:
        query = query.filter(Sesion.disciplina_id == disciplina_id)
    return query.offset(skip).limit(limit).all()


@router.get("/{sesion_id}", response_model=SesionResponse)
def obtener_sesion(sesion_id: int, db: Session = Depends(get_db)):
    sesion = db.query(Sesion).filter(Sesion.id == sesion_id).first()
    if not sesion:
        raise HTTPException(404, "Sesión no encontrada")
    return sesion


@router.patch("/{sesion_id}", response_model=SesionResponse)
def actualizar_sesion(sesion_id: int, datos: SesionUpdate, db: Session = Depends(get_db)):
    sesion = db.query(Sesion).filter(Sesion.id == sesion_id).first()
    if not sesion:
        raise HTTPException(404, "Sesión no encontrada")
    for campo, valor in datos.model_dump(exclude_unset=True).items():
        setattr(sesion, campo, valor)
    db.commit()
    db.refresh(sesion)
    return sesion