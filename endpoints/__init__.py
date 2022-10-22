from fastapi import APIRouter

api_router = APIRouter()

from . import home
api_router.include_router(home.router, tags=["Home"])