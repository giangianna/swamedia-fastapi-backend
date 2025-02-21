from pydantic_settings import BaseSettings

# Kelas konfigurasi yang menggunakan Pydantic untuk validasi dan pengaturan lingkungan
class Settings(BaseSettings):
    PROJECT_NAME: str = "Swamedia FastAPI Project"
    PROJECT_VERSION: str = "1.0.0"
    DATABASE_URL: str = "sqlite:///./test.db"
    SECRET_KEY: str = "your_secret_key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        # Menggunakan file .env untuk variabel lingkungan
        env_file = ".env"

# Membuat instance konfigurasi
settings = Settings()
