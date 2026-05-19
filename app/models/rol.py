"""
Modelo ORM (Objets relationship Mapping) para la tabla 'roles'
Se definen perfiles de usuario: Administrador, Finanzas, Entrenador, Cliente 
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import  relationship
from app.models.database import Base
 
class Rol(Base):
    """
    Roles predefinidos:
    - Administrador: Acceso total al sistema
    - Finanzas:      Gestion de pagos, membresías y tienda
    - Entrenador:    Gestion de sesiones y evaluacion biometrica
    - Cliente:       Reservas, acceso al gemnasio, compras
    """
    
    # Nombre de la tabla en la base de datos
    __tablename__ = "roles"
      
    # --- Columnas ---
    id = Column(
        Integer,
        primary_key = True,      # Clave primaria
        index = True,            # Crea un índice para búsquedas por ID
        autoincrement = True     # El ID se genera automáticamente: 1, 2, 3...
    )
   
    nombre = Column(
        String(50),
        unique = True,           # No puede haber dos roles con el mismo nombre
        nullable = False,        # Campo OBLIGATORIO (NOT NULL)
        index = True             # Índice para busqueda por nombre
    )
   
    # --- Relaciones con otras tablas ---
    # Un rol tiene MUCHOS usuarios
    # back_populates = "rol" se conecta con el atributo 'rol' en la clase Usuario
    usuarios = relationship(
        "Usuario",              # Nombre de la clase relacionada
        back_populates = "rol", # Atributo en Usuario que apunta de vuelta a Rol
        lazy = "select"         # Carga los usuarios cuando se acceda a este atributo
    )
   
    # --- Métodos especiales ---
    def __repr__(self):
        """Representación legible del objeto para debugging"""
        return f"<Rol(id={self.id}, nombre='{self.nombre}')>"

