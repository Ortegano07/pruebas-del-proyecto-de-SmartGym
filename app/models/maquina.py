from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Date, DateTime
from app.models.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum


class EstadoMaquina(enum.Enum):
    activa = "Activa"
    mantenimiento = "Mantenimiento"
    fuera_servicio = "Fuera de servicio"

class Maquina(Base):
    __tablename__ = "maquinas"
    
    id = Column(Integer, primary_key=True, index=True)
    categoria_id = Column(Integer, ForeignKey("categorias_maquinas.id"), nullable=False)
    nombre = Column(String, nullable=False)
    descripcion_tecnica = Column(String, nullable=False)
    estado_operativo = Column(Enum(EstadoMaquina), nullable=False)
    fecha_adquisicion = Column(Date, nullable=False)
    ultima_revision = Column(Date, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    categoria = relationship("Categoria", back_populates="maquinas")
    
    def __repr__(self):
        return f"<Maquina {self.nombre}>"