from fastapi import APIRouter
from ..repository import user

from ..schema import  schema as sm
router = APIRouter(prefix="/api/user", tags=['News'])
@router.post('/login',response_description="Login")
def login(request: sm.User):
    return user.login(request=request)

@router.post('/register',response_description="Register")
def register(request: sm.User):
    return user.register(request=request)