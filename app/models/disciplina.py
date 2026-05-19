from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.database import Base

class Disciplina(Base):
    __tablename__ = "disciplinas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(255), nullable=True)
    
    # Relación: Una disciplina tiene muchas sesiones
    sesiones = relationship("Sesion", back_populates="disciplina")