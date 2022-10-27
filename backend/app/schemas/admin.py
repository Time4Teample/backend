from typing import Optional
from pydantic import BaseModel, EmailStr

class AdminBase(BaseModel):
    class Config:
        orm_mode = True


class Admin(AdminBase):
    name: str
    organization: str
    telephone: str
    email: Optional[EmailStr]
    is_active: bool

class AdminCreate(AdminBase):
    name: str
    organization: str
    telephone: str
    email: Optional[EmailStr]

 class AdminDelete(AdminBase):
     is_active: bool