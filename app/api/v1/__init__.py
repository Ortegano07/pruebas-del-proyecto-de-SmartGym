"""
Centralizando todos los routers
"""

from fastapi import APIRouter
<<<<<<< HEAD

from app.api.v1.endpoints import roles, usuarios, auth, maquinas, categorias_maquinas

=======
<<<<<<< HEAD
from app.api.v1.endpoints import roles, usuarios #33(
    #auth,
=======
from app.api.v1.endpoints import roles, usuarios, auth, maquinas
>>>>>>> adrian/main
>>>>>>> 72b2b31e65c4e9ed1a165be28bd25948483dc50c
    #usuarios,
    #maquinas,
    #mantenimiento,
    #deportivo,
    #reservas,
    #acceso,
    #finanzas,
    #tienda,
    #biometrico,
    #roles
#)

#Router principal para agrupar todos los modulos
api_router = APIRouter()

# Incluimos cada módulo con su prefijo
api_router.include_router(roles.router,tags=["Roles"])
api_router.include_router(usuarios.router, tags=["Usuarios"])
<<<<<<< HEAD

api_router.include_router(auth.router, tags=["Autenticación"])
api_router.include_router(maquinas.router, tags=["Máquinas"])
api_router.include_router(categorias_maquinas.router, tags=["Categorías de Máquinas"])

=======
<<<<<<< HEAD
#api_router.include_router(auth.router, tags=["Autenticación"])
#api_router.include_router(maquinas.router, tags=["Máquinas"])
=======
api_router.include_router(auth.router, tags=["Autenticación"])
api_router.include_router(maquinas.router, tags=["Máquinas"])
#api_router.include_router(categorias_maquinas.router, tags=["Categorías de Máquinas"])
>>>>>>> adrian/main
>>>>>>> 72b2b31e65c4e9ed1a165be28bd25948483dc50c
#api_router.include_router(mantenimiento.router, tags=["Mantenimiento"])
#api_router.include_router(deportivo.router, tags=["Deportivo"])
#api_router.include_router(reservas.router, tags=["Reservas"])
#api_router.include_router(acceso.router, tags=["Acceso"])
#api_router.include_router(finanzas.router, tags=["Finanzas"])
#api_router.include_router(tienda.router, tags=["Tienda"])
#pi_router.include_router(biometrico.router, tags=["Biométrico"])