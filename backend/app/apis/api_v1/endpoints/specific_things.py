from typing import Any

from fastapi import APIRouter, Depends, Body, HTTPException
from fastapi.encoders import jsonable_encoder

from app.apis.depends import get_current_active_user, get_current_active_superuser
from app.models.user import User
from app.schemas.user import UserRead, UserUpdate
from app.apis.depends import get_db
from sqlalchemy.orm import Session
from app.crud.user import crud_user

router = APIRouter()





