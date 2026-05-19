from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.schemas.sesion import SesionCreate, SesionResponse
from app.services import sesion_service
from typing import List
from app.models.database import get_db
from app.schemas.disciplina import DisciplinaCreate, DisciplinaResponse
from app.services import disciplina_services

router = APIRouter(prefix="/disciplinas")

@router.post("/", response_model=DisciplinaResponse, status_code=status.HTTP_201_CREATED)
def post_disciplina(data: DisciplinaCreate, db: Session = Depends(get_db)):
    return disciplina_services.crear_disciplina(db, data)

@router.get("/", response_model=List[DisciplinaResponse])
def get_disciplinas(db: Session = Depends(get_db)):
    return disciplina_services.obtener_disciplinas(db)

@router.post("/sesiones", response_model=SesionResponse)
def post_sesion(data: SesionCreate, db: Session = Depends(get_db)):
    return sesion_service.crear_sesion(db, data)

@router.get("/sesiones", response_model=List[SesionResponse])
def get_sesiones(db: Session = Depends(get_db)):
    return sesion_service.obtener_sesiones(db)