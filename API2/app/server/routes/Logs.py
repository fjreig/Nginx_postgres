from fastapi import APIRouter

from app.server.db.postgres import(
    Informe_Mensual_Operario,
)

router = APIRouter()

@router.get('/Consulta', summary="Consultar Logs")
async def get_redis_user():
    Registro = Informe_Mensual_Operario()
    if Registro:
        return Registro
    return []