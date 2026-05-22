from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.reserva import Reserva
from app.models.sesion import Sesion
from datetime import datetime

def crear_reserva(db: Session, cliente_id: int, sesion_id: int):
    # 1. Obtener la sesión que se desea reservar
    nueva_sesion = db.query(Sesion).filter(Sesion.id == sesion_id).first()
    if not nueva_sesion:
        raise HTTPException(status_code=404, detail="Sesión no encontrada")

    # 2. VALIDACIÓN: Sobreventa de cupos (RNF6.2)
    total_reservas = db.query(Reserva).filter(Reserva.sesion_id == sesion_id).count()
    if total_reservas >= nueva_sesion.cupo_maximo:
        raise HTTPException(status_code=409, detail="Sesión llena: No hay cupos disponibles")

    # 3. VALIDACIÓN: Solapamiento de horarios (RNF6.1)
    # Buscamos todas las reservas del cliente
    reservas_cliente = db.query(Reserva).filter(Reserva.cliente_id == cliente_id).all()
    
    for reserva in reservas_cliente:
        sesion_existente = reserva.sesion
        # Comparamos si los horarios se cruzan
        if (nueva_sesion.fecha_hora_inicio < sesion_existente.fecha_hora_fin and 
            nueva_sesion.fecha_hora_fin > sesion_existente.fecha_hora_inicio):
            raise HTTPException(status_code=409, detail="Solapamiento detectado: Ya tienes una reserva en este horario")

    # Si pasa todas las validaciones, creamos la reserva
    nueva_reserva = Reserva(cliente_id=cliente_id, sesion_id=sesion_id)
    db.add(nueva_reserva)
    db.commit()
    return nueva_reserva