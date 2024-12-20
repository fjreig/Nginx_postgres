import uvicorn
from fastapi import FastAPI, Body
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from app.server.routes.Logs import router as Logs

description = """
Pavener API. 🚀
"""

tags_metadata = [
    {
        "name": "Logs",
        "description": "logs de nginx",
    },
]

app = FastAPI(
    root_path="/v2",
    #docs_url=None, 
    redoc_url=None,
    title="PAPI",
    description=description,
    version="0.4",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Pavener Servicios Energeticos SLU",
        "url": "https://www.pavener.com/contacto/",
        "email": "info@pavener.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(Logs, tags=["Logs"], prefix="/Logs")