from pydantic import BaseModel, EmailStr, ConfigDict

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

    model_config = ConfigDict(from_attributes=True)
