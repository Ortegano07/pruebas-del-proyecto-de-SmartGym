from sqlalchemy.orm import Session
from app.models.maquina import Maquina, EstadoMaquina
from fastapi import HTTPException, status
from datetime import date

from app.schemas.maquina import MaquinaCreate

def registrar_maquina(db: Session, maquina_in: MaquinaCreate):
    nueva_maquina = Maquina(
        nombre=maquina_in.nombre,
        descripcion_tecnica=maquina_in.descripcion_tecnica,
        categoria_id=maquina_in.categoria_id,
        estado_operativo=EstadoMaquina.activa,
        fecha_adquisicion=maquina_in.fecha_adquisicion,
        ultima_revision=maquina_in.ultima_revision
    )
    db.add(nueva_maquina)
    db.commit()
    db.refresh(nueva_maquina)
    return nueva_maquina

def listar_maquinas(db: Session, estado: str = None):
    query = db.query(Maquina)
    if estado:
        query = query.filter(Maquina.estado_operativo == estado)
    return query.all()