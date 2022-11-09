from typing import Optional

from pydantic import BaseModel, Field

class ProgramBase(BaseModel):
    class Config:
        schema_extra = {
            "example": {
                "url"
            }
        }