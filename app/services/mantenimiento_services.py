from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.ticket_mantenimiento import TicketMantenimiento
from app.models.maquina import Maquina
from app.schemas.ticket_mantenimiento import TicketCreate

def crear_ticket(db: Session, ticket_data: TicketCreate):
    # 1. Buscar la máquina
    maquina = db.query(Maquina).filter(Maquina.id == ticket_data.maquina_id).first()
    if not maquina:
        raise HTTPException(status_code=404, detail="Máquina no encontrada")
    
    # 2. Crear el ticket
    nuevo_ticket = TicketMantenimiento(**ticket_data.dict())
    
    # 3. RF10: Actualizar estado de la máquina
    maquina.estado = "en_mantenimiento"
    
    db.add(nuevo_ticket)
    db.commit()
    db.refresh(nuevo_ticket)
    return nuevo_ticket

def obtener_tickets_por_maquina(db: Session, maquina_id: int):
    # Verificamos que la máquina exista
    maquina = db.query(Maquina).filter(Maquina.id == maquina_id).first()
    if not maquina:
        raise HTTPException(status_code=404, detail="Máquina no encontrada")
    
    # Obtenemos todos los tickets de esa máquina
    tickets = db.query(TicketMantenimiento).filter(TicketMantenimiento.maquina_id == maquina_id).all()
    return tickets

def cerrar_ticket(db: Session, ticket_id: int):
    # 1. Buscar el ticket
    ticket = db.query(TicketMantenimiento).filter(TicketMantenimiento.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket no encontrado")
    
    if ticket.estado == "resuelto":
        raise HTTPException(status_code=400, detail="Este ticket ya está cerrado")

    # 2. Buscar la máquina asociada
    maquina = db.query(Maquina).filter(Maquina.id == ticket.maquina_id).first()
    
    # 3. Cerrar el ticket y liberar la máquina
    ticket.estado = "resuelto"
    if maquina:
        maquina.estado = "disponible"
    
    db.commit()
    db.refresh(ticket)
    return ticket