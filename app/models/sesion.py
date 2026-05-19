from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.models.database import Base

class Sesion(Base):
    __tablename__ = "sesiones"

    id = Column(Integer, primary_key=True, index=True)
    disciplina_id = Column(Integer, ForeignKey("disciplinas.id"), nullable=False)
    
    # Horarios
    fecha_hora_inicio = Column(DateTime, nullable=False)
    fecha_hora_fin = Column(DateTime, nullable=False)
    
    # Capacidad
    cupo_maximo = Column(Integer, nullable=False)
    
    # Relaciones
    disciplina = relationship("Disciplina", back_populates="sesiones")
    reservas = relationship("Reserva", back_populates="sesion")