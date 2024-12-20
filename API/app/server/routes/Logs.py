from fastapi import APIRouter, Body, Depends, Path
from fastapi.encoders import jsonable_encoder
from fastapi.responses import StreamingResponse
from pathlib import Path
from fastapi import Query
from io import BytesIO
import pandas as pd

from app.server.db.postgres import(
    Informe_Mensual_Operario,
)

router = APIRouter()

@router.get('/Ultima_Consulta', summary="Consultar Logs")
async def get_redis_user():
    Registro = Informe_Mensual_Operario()
    if Registro:
        return Registro
    return []