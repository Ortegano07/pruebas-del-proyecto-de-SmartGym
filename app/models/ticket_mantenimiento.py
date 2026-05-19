from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models.database import Base

class TicketMantenimiento(Base):
    __tablename__ = "tickets_mantenimiento"

    id = Column(Integer, primary_key=True, index=True)
    maquina_id = Column(Integer, ForeignKey("maquinas.id"), nullable=False)
    descripcion_falla = Column(String(255), nullable=False)
    estado = Column(String(20), default="abierto") # abierto, en_reparacion, resuelto
    fecha_reporte = Column(DateTime, default=datetime.utcnow)
    maquina = relationship("Maquina", back_populates="tickets")