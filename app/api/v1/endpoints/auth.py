from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session 
from app.models.database import get_db
from app.services.auth_service import autenticar_usuario

router = APIRouter(prefix="/login")

@router.post("/", status_code=200)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Pasamos el objeto form_data completo al servicio
    return autenticar_usuario(db, form_data)