from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from router.schemas import StoreRequestSchema, StoreResponseSchema, UserRequestSchema
from db.database import get_db
from db import db_store
from typing import List
from utils.oauth2 import get_current_user

router = APIRouter(
    prefix='/api/v1/store',
    tags=['store']
)


@router.post('')
def create(request: StoreRequestSchema, db: Session = Depends(get_db), current_user: UserRequestSchema = Depends(get_current_user)):
    return db_store.create(db, request)


@router.get('/all', response_model=List[StoreResponseSchema])
def get_all_store(db: Session = Depends(get_db)):
    return db_store.get_all_store(db)


@router.get('/user/{user_id}', response_model=StoreResponseSchema)
def get_store_by_user_id(user_id: int, db: Session = Depends(get_db)):
    return db_store.get_store_by_user_id(user_id=user_id, db=db)
