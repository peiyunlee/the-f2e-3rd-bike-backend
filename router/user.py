from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from router.schemas import \
    UserRequestSchema, UserResponseSchema, \
    SignInRequestSchema, UserSignInResponseSchema
from db.database import get_db
from db import db_user
from typing import List
from utils.oauth2 import get_current_user, get_current_user_with_id

router = APIRouter(
    prefix='/api/v1/users',
    tags=['users']
)


@router.post('/register')
async def register(request: UserRequestSchema, db: Session = Depends(get_db)):
    return db_user.register(request=request,db=db)


@router.post('/signin')
async def signin(request: SignInRequestSchema, db: Session = Depends(get_db)):
    return db_user.signin(request=request,db=db)


@router.get('/all', response_model=List[UserResponseSchema])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)


@router.get('/id/{user_id}', response_model=UserResponseSchema)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return db_user.get_user_by_id(user_id=user_id, db=db)


@router.get('/email/{user_email}', response_model=UserResponseSchema)
def get_user_by_email(user_email: str, db: Session = Depends(get_db)):
    return db_user.get_user_by_email(user_email=user_email, db=db)


@router.get('/name/{user_name}', response_model=UserResponseSchema)
def get_user_by_username(user_name: str, db: Session = Depends(get_db)):
    return db_user.get_user_by_username(user_name=user_name, db=db)
