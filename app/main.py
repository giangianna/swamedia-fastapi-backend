from fastapi import FastAPI
from app.api.v1 import v1_router
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

app.include_router(v1_router, prefix="/api/v1", tags=["v1"])
