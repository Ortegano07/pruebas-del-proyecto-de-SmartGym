from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.models.database import get_db
from app.schemas.categoria_maquina import CategoriaMaquinaCreate, CategoriaMaquinaResponse
from app.services import categoria_maquina_services

router = APIRouter()

@router.post("/categorias", response_model=CategoriaMaquinaResponse)
def post_categoria(data: CategoriaMaquinaCreate, db: Session = Depends(get_db)):
    return categoria_maquina_services.crear_categoria(db, data)

@router.get("/categorias", response_model=List[CategoriaMaquinaResponse])
def get_categorias(db: Session = Depends(get_db)):
    return categoria_maquina_services.obtener_categorias(db)