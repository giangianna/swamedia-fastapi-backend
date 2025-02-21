from fastapi import FastAPI
from app.api.v1 import v1_router
from app.core.config import settings

# Inisialisasi aplikasi FastAPI dengan judul dan versi dari konfigurasi
app = FastAPI(title=settings.PROJECT_NAME, 
              version=settings.PROJECT_VERSION,
              description="Swamedia API untuk Aplikasi XYZ.",
              openapi_tags=[
                {
                    "name": "users",
                    "description": "Operasi CRUD untuk pengguna.",
                },
            ],
        )

# Menyisipkan router v1 ke aplikasi FastAPI
app.include_router(v1_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to Swamedia Framework FastAPI!"}
