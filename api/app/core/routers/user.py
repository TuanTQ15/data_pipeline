from fastapi import APIRouter
from ..repository import user

from ..schema import  schema as sm
router = APIRouter(prefix="/api/user", tags=['User'])
@router.post('/login',response_description="Login")
def login(request: sm.UserLogin):
    return user.login(request=request)

@router.post('/register',response_description="Register")
def register(request: sm.User):
    return user.register(request=request)

@router.post('/check')
def check_new_user(request: sm.User):
    return user.check_new_user(request=request)

@router.get('/check_user_exists')
def check_user_exists(username):
    return user.checkuser_exists(username)