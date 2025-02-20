from fastapi import APIRouter

v1_router = APIRouter()

from .endpoints import users, items
