from fastapi import APIRouter

v1_router = APIRouter()

from .endpoints import users

# Include the routers from the endpoints
v1_router.include_router(users.router, tags=["users"])

# Export the v1_router
__all__ = ["v1_router"]

