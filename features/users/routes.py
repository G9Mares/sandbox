from fastapi import APIRouter
from .service import service_get_users

router =  APIRouter(prefix="/users")

@router.get("")
def get_users():
    return service_get_users()