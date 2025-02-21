from fastapi import APIRouter

v1_router = APIRouter()

from .endpoints import users, items

# Include the routers from the endpoints
v1_router.include_router(users.router, tags=["users"])
# v1_router.include_router(items.router, prefix="/items", tags=["items"])

# Export the v1_router
__all__ = ["v1_router"]

