from fastapi import FastAPI
from app.api.v1 import v1_router
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, 
              version=settings.PROJECT_VERSION,
              description="API untuk manajemen pengguna.",
              openapi_tags=[
                {
                    "name": "users",
                    "description": "Operasi CRUD untuk pengguna.",
                },
            ],
        )

app.include_router(v1_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to Swamedia Framework FastAPI!"}
