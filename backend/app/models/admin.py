from sqlalchemy import Boolean, Column, String, Integer
from sqlalchemy.dialects.mysql import INTEGER, ENUM
from app.db.session import Base

class Admin(Base):
    __tablename__ = "admin"

    id = Column(INTEGER(display_width=11, unsigned=True), primary_key=True, index=True)
    name = Column(String(100), index=True, nullable=False)
    organization = Column(String(100), nullable=False)
    telephone = Column(String(16), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)