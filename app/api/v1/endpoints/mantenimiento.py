from app.services import mantenimiento_services
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.models.database import get_db
from app.schemas.ticket_mantenimiento import TicketCreate, TicketResponse
from app.services import mantenimiento_services
from typing import List
from sqlalchemy.orm import relationship

router = APIRouter(prefix="/mantenimiento")

@router.post("/", response_model=TicketResponse, status_code=status.HTTP_201_CREATED)
def reportar_falla(ticket: TicketCreate, db: Session = Depends(get_db)):
    return mantenimiento_services.crear_ticket(db, ticket)

@router.get("/{maquina_id}", response_model=List[TicketResponse])
def leer_tickets_por_maquina(maquina_id: int, db: Session = Depends(get_db)):
    return mantenimiento_services.obtener_tickets_por_maquina(db, maquina_id)

@router.patch("/{ticket_id}/cerrar", response_model=TicketResponse)
def cerrar_ticket_mantenimiento(ticket_id: int, db: Session = Depends(get_db)):
    return mantenimiento_services.cerrar_ticket(db, ticket_id)
