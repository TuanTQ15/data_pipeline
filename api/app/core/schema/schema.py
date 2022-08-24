from pydantic import BaseModel
class User(BaseModel):
    username: str
    password: str
    name:str
    email:str
    birthday:int
    image_url:str
class UserLogin(BaseModel):
    username: str
    password: str



