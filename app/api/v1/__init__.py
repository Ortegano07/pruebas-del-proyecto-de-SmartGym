"""
Centralizando todos los routers
"""

from fastapi import APIRouter
from app.api.v1.endpoints import (
    auth,
    usuarios,
    maquinas,
    mantenimiento,
    deportivo,
    reservas,
    acceso,
    finanzas,
    tienda,
    biometrico,
)

#Router principal para agrupar todos los modulos
api_router = APIRouter()

# Incluimos cada módulo con su prefijo
api_router.include_router(auth.router, tags=["Autenticación"])
api_router.include_router(usuarios.router, tags=["Usuarios"])
api_router.include_router(maquinas.router, tags=["Máquinas"])
api_router.include_router(mantenimiento.router, tags=["Mantenimiento"])
api_router.include_router(deportivo.router, tags=["Deportivo"])
api_router.include_router(reservas.router, tags=["Reservas"])
api_router.include_router(acceso.router, tags=["Acceso"])
api_router.include_router(finanzas.router, tags=["Finanzas"])
api_router.include_router(tienda.router, tags=["Tienda"])
api_router.include_router(biometrico.router, tags=["Biométrico"])