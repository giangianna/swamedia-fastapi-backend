# My FastAPI Project

## Deskripsi
Proyek ini adalah contoh aplikasi FastAPI dengan struktur folder yang terorganisir.

## Instalasi
1. Clone repositori ini:
   ```bash
   git clone https://github.com/giangianna/swamedia-fastapi-project.git
   cd swamedia-fastapi-project

2. Buat dan aktifkan virtual environment:
python -m venv venv
source venv/bin/activate  # di Windows gunakan `venv\Scripts\activate`

3. Instal dependensi:
pip install -r requirements.txt

4. Jalankan aplikasi:
uvicorn app.main:app --reload

# Struktur Folder
my_fastapi_project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── users.py
│   │   │   │   ├── items.py
│   │   │   ├── dependencies.py
│   │   │   ├── schemas.py
│   │   │   ├── models.py
│   │   │   ├── crud.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── security.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── engine.py
│   │   ├── session.py
│   │   ├── models.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── helpers.py
│   │   ├── logger.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_main.py
│   │   ├── test_users.py
│   │   ├── test_items.py
│   ├── static/
│   │   ├── images/
│   │   ├── css/
│   │   ├── js/
│   ├── templates/
│   │   ├── index.html
│   │   ├── login.html
├── .env
├── .gitignore
├── requirements.txt
├── README.md
├── Dockerfile
├── docker-compose.yml

# Penggunaan
Menjalankan aplikasi: uvicorn app.main:app --reload
Menjalankan pengujian: pytest