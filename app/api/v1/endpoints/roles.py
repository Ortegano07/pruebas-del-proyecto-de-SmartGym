from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models.database import get_db
from app.models.rol import Rol
from app.schemas.rol import RolCreate, RolResponse

router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)

@router.post("/", response_model=RolResponse, status_code=201)
def crear_rol(rol: RolCreate, db: Session = Depends(get_db)):
    """Crear un nuevo rol (Admin, Finanzas, Entrenador, Cliente)"""
    # Verificar si ya existe
    existe = db.query(Rol).filter(Rol.nombre == rol.nombre).first()
    if existe:
        raise HTTPException(status_code=409, detail=f"El rol '{rol.nombre}' ya existe")
    
    nuevo_rol = Rol(nombre=rol.nombre)
    db.add(nuevo_rol)
    db.commit()
    db.refresh(nuevo_rol)
    return nuevo_rol

@router.get("/", response_model=List[RolResponse])
def listar_roles(db: Session = Depends(get_db)):
    """Listar todos los roles disponibles"""
    return db.query(Rol).all()

@router.get("/{rol_id}", response_model=RolResponse)
def obtener_rol(rol_id: int, db: Session = Depends(get_db)):
    """Obtener un rol por su ID"""
    rol = db.query(Rol).filter(Rol.id == rol_id).first()
    if not rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return rol