from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.models.database import get_db
from app.schemas.maquina import MaquinaCreate, MaquinaResponse
from app.services import maquina_services

router = APIRouter(prefix="/maquinas")

@router.post("/", response_model=MaquinaResponse, status_code=status.HTTP_201_CREATED)
def crear_maquina(data: MaquinaCreate, db: Session = Depends(get_db)):
    return maquina_services.crear_maquina(db, data)

@router.get("/", response_model=List[MaquinaResponse])
def listar_maquinas(db: Session = Depends(get_db)):
    return maquina_services.obtener_maquinas(db)