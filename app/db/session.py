from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from app.db.base import Base

# Membuat engine database
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Membuat sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Membuat tabel secara otomatis
Base.metadata.create_all(bind=engine)

# Fungsi untuk mendapatkan session database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
