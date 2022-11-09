from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

@router.get("/program")
def read_program():
    ...