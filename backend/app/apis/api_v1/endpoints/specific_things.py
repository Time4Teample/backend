from typing import Any
from pydantic import BaseModel
from pydantic import Field

from fastapi import APIRouter, Depends, Body, HTTPException,FastAPI,status
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder

from app.apis.depends import get_current_active_user, get_current_active_superuser
from app.models.user import User
from app.schemas.user import UserRead, UserUpdate
from app.apis.depends import get_db
from sqlalchemy.orm import Session
from app.crud.user import crud_user
from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, List
import motor.motor_asyncio


client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])

db = client.college

router = APIRouter()

app = FastAPI()


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class CreateLectureModel(BaseModel):

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(...)
    place : str = Field(...) #What exactly placed value?
    duration : str = Field(...)
    call_number : str = Field(...)
    start_duration : str = Field(...)
    time : str = Field(...)
    cost : str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example1": {
                "name": "1st lecture",
                "place": "25.12321 , 12.43321",
                "duration": "2022.05.15 , 2022.08.15",
                "call_number": "010-0101-1010",
                "start_duration": "2022.05.15",
                "time" : "13:00 - 17:05",
                "cost" : "1370000",
            }
        }

@app.post("/", response_description="Add new lecture", response_model=CreateLectureModel)
async def create_lecture(lecture: User = Body(...)):
    lecture = jsonable_encoder(lecture)
    new_lecture = await db["lectures"].insert_one(lecture)
    created_lecture = await db["lectures"].find_one({"_id": new_lecture.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_lecture)



