from fastapi import FastAPI, Request

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

from endpoints import api_router
app.include_router(api_router, prefix="/api")