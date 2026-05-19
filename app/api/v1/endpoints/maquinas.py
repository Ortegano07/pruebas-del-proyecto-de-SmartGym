from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.models.database import get_db
from app.services import maquina_services
from app.schemas.maquina import MaquinaCreate, MaquinaOut
#from app.core.dependencies import require_role

router = APIRouter(prefix="/maquinas")

@router.get("/", response_model=List[MaquinaOut])
def obtener_maquinas(estado: str = None, db: Session = Depends(get_db)):
    """Lista todas las máquinas. Accesible por cualquier usuario autenticado."""
    return maquina_services.listar_maquinas(db, estado)

@router.post("/", response_model=MaquinaOut, status_code=status.HTTP_201_CREATED)#, dependencies=[Depends(require_role("Administración"))"])
def crear_maquina(maquina_in: MaquinaCreate, db: Session = Depends(get_db)):
    """Registra una nueva máquina. Solo accesible por Administración."""
    return maquina_services.registrar_maquina(db, maquina_in)