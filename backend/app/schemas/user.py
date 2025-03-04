from typing import Optional
from pydantic import BaseModel

class UserBase(BaseModel):
    class Config:
        orm_mode = True

class User(UserBase):
    name: str
    age: Optional[int]
    gender: Optional[str]
    address: str
    telephone: str
    email: str
    is_active: bool
    is_superuser: bool

class UserCreate(UserBase):
    name: str
    address: str
    telephone: str

class UserDelete(UserBase):
    is_active: bool


class UserUpdate(UserBase):
    ...

class UserRead(User):
    ...
