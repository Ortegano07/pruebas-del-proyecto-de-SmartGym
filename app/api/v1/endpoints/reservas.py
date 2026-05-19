from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.models.database import get_db
from app.schemas.reserva import ReservaCreate, ReservaResponse
from app.services import reserva_service

router = APIRouter(prefix="/reservas")

@router.post("/", response_model=ReservaResponse, status_code=status.HTTP_201_CREATED)
def post_reserva(data: ReservaCreate, db: Session = Depends(get_db)):
    return reserva_service.crear_reserva(db, data.cliente_id, data.sesion_id)