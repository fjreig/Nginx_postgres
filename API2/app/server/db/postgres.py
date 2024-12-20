import pandas as pd
from datetime import datetime
from json import loads, dumps
from fastapi import HTTPException
from typing import Optional
import typing
import base64
import json
from psycopg2 import connect
from psycopg2 import OperationalError, errorcodes, errors
import pandas as pd
from app.server.core.config import settings

conn = connect(database=settings.POSTGRES_DB,
    host=settings.POSTGRES_HOST,
    user=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    port=settings.POSTGRES_PORT)

cursor = conn.cursor()

def selectSQL(sql):
    df = pd.read_sql_query(sql, conn)
    result = df.to_json(orient="records")
    parsed = loads(result)
    return(parsed)

def Informe_Mensual_Operario():
    sql = f"""select log_line from accesslog"""
    parse = selectSQL(sql)
    return(parse)