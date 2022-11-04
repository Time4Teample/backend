from typing import Optional
from pydantic import BaseModel

class AdminBase(BaseModel):
    class Config:
        orm_mode = True


class Admin(AdminBase):
    name: str
    organization: str
    telephone: str
    email: Optional[str]
    is_active: bool

class AdminCreate(AdminBase):
    name: str
    organization: str
    telephone: str
    email: Optional[str]

 class AdminDelete(AdminBase):
     is_active: bool