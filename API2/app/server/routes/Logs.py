from fastapi import APIRouter

from app.server.db.postgres import(
    consulta1,
)

router = APIRouter()

@router.get('/Consulta', summary="Consultar Logs")
async def get_redis_user():
    Registro = consulta1()
    if Registro:
        return Registro
    return []