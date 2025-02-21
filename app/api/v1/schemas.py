from pydantic import BaseModel, EmailStr

# Schema dasar untuk users
class UserBase(BaseModel):
    email: EmailStr

# Schema untuk membuat user baru
class UserCreate(UserBase):
    password: str

# Schema untuk mengembalikan detail user
class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
