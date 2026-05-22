from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verificar_password(password_plano: str, password_hash: str) -> bool:
    """Compara una contraseña en texto plano con su hash"""
    return pwd_context.verify(password_plano, password_hash)

def hashear_password(password: str) -> str:
    """Genera el hash de una contraseña"""
    return pwd_context.hash(password)

def crear_token_acceso(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Genera un token JWT con los datos proporcionados"""
    to_encode = data.copy()
    expire = datetime.now() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def decodificar_token(token: str) -> Optional[dict]:
    """Decodifica y valida un token JWT"""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None