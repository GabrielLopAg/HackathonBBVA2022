from fastapi import FastAPI, Request
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware


description = """
API para la solución PyME

- Scrapping de paginas web
- Obtiene modelos de credito para PyMEs
"""

app = FastAPI(
    title="PyMEs",
    openapi_url="/openapi.json",
    description=description,
    version="0.1.0",
)

@app.get(
    path="/",
    status_code=200,
    tags=["default"],
    summary="Root",
    )
def hello_world():
    """
    # Hola mundo de la aplicación
    Este endpoint muestra un mensaje de bienvenida.

    Regresa un JSON con el mensaje de bienvenida.
    """
    return {"message": "Hello World"}

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from endpoints import api_router
app.include_router(api_router, prefix="/api/v1")
handler = Mangum(app)

