from sqlalchemy.orm import Session 
from app.models.usuario import Usuario 
from app.core.security import verificar_password, crear_token_acceso
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

def autenticar_usuario(db: Session, form_data: OAuth2PasswordRequestForm):
    # 1. Buscar al usuario por email (case-insensitive)
    #usuario = db.query(Usuario).filter(Usuario.email.ilike(email)).first()
    usuario = db.query(Usuario).filter(Usuario.email.ilike(form_data.username)).first()

    # 2. Verificar si el usuario existe y la contraseña es correcta
    if not usuario or not verificar_password(form_data.password, usuario.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o contrasena invalidos",
            headers={"WWW-Authenticate": "Bearer"}   
        )   
    
    # 3. Generar el token de acceso (incluimos el rol en el payload)
    access_token = crear_token_acceso(
        data={
            "sub": usuario.email,
            "rol": usuario.rol.nombre
        }
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "usuario_id": usuario.id,
        "rol": usuario.rol.nombre
    }
    

