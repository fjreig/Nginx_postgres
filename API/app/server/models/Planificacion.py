from typing import Optional
from pydantic import BaseModel, Field, EmailStr, Json
from datetime import date, datetime, time, timedelta

class PlanificacionSchema(BaseModel):
    obra: int = Field(...)
    fecha: str = Field(...)
    operario: int = Field(...)
    cliente: str = Field(...)
    info: str = Field(...)
    habilitado: bool = Field(...)
    notificar: bool = Field(...)
    realizado: bool = Field(...)
    tags: object = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                'obra': 1,
                'fecha': "2024-09-10",
                'cliente': "cliente1",
                'operario': 1,
                'info': "",
                'habilitado': True,
                'notificar': True,
                'realizado': False,
                'tags': ["texto prueba"],
            }
        }

class ActualizarPlanificacion(BaseModel):
    id: str = Field(...)
    obra: int = Field(...)
    fecha: str = Field(...)
    operario: int = Field(...)
    cliente: str = Field(...)
    info: str = Field(...)
    habilitado: bool = Field(...)
    notificar: bool = Field(...)
    realizado: bool = Field(...)
    tags: object = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "id": "1231231",
                'obra': 1,
                'fecha': "2024-09-10",
                'cliente': "cliente1",
                'operario': 1,
                'info': "",
                'habilitado': True,
                'notificar': True,
                'realizado': False,
                'tags': ["texto prueba"],
            }
        }