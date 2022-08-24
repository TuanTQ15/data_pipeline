from ..model.mongodb import db
from ..schema import schema as sm
from fastapi import  HTTPException, status
from ..utility.hashing import Hash
from ..utility.upload_image import uploadFile
import os
import math
import random
import smtplib



col = db['user']

def login(request: sm.UserLogin):
    user = col.find_one({"username": request.username},{'_id': 0})
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
    if user:
        if not Hash.verify(user['password'], request.password):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Incorrect Password")
            # access_token = token.create_access_token(data={"sub": user.CMND})
        else:
            return user
    return

def check_new_user(request: sm.User):
    user = col.find_one({"username": request.username})
    user_mail = col.find_one({"email": request.email})
    if not user:
        if not user_mail:
            return
        else:
            raise HTTPException(status_code=status.HTTP_417_EXPECTATION_FAILED, detail="Email exist")
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User exists")

def register(request: sm.User):
    user=col.find_one({"username": request.username})
    user_mail = col.find_one({"email": request.email})
    if not user :
        if not user_mail:
            hashedPassword = Hash.bcrypt(request.password)
            image_url=uploadFile(request.image_url)
            col.insert_one(document={"username": request.username, "password": hashedPassword,
                                     "name":request.name,"email":request.email,"birth_day":request.birthday,"image_url":image_url} )
            check_user = col.find_one({"username": request.username},{'_id': 0})
            if check_user:
                return dict(check_user)
            else:
                raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insert fail")
        else:
            raise HTTPException(status_code=status.HTTP_417_EXPECTATION_FAILED, detail="Email exist")
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User exists")

def checkuser_exists(username):
    user = col.find_one({"username": username},{'_id': 0})
    if user:
        return user['email']
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User non-exists")