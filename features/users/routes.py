from fastapi import APIRouter
from .sql_alchemy_engine.service import User_service

router =  APIRouter(prefix="/users")

@router.get("")
def get_users():
    return User_service.service_get_users()