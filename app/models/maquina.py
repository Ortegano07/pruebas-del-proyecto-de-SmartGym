from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base

class Maquina(Base):
    __tablename__ = "maquinas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    codigo_serial = Column(String(50), unique=True, nullable=False, index=True)
    # Estados definidos: disponible, en_mantenimiento, fuera_de_servicio
    estado = Column(String(20), default="disponible") 
    
    categoria_id = Column(Integer, ForeignKey("categorias_maquinas.id"), nullable=False)
    
    # Relación para cumplir con la integridad referencial
    categoria = relationship("CategoriaMaquina", back_populates="maquinas")
    # tickets = relationship("TicketMantenimiento", back_populates="maquina")