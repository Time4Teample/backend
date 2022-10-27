from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative
class Base:
    __name__: str

    id: Any
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()