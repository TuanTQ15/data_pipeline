from ..model.mongodb import db
from ..schema import schema as sm
from fastapi import  HTTPException, status
from ..utility.hashing import Hash
col = db['user']

def login(request: sm.User):
    user = col.find_one({"username": request.username})
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
    if user:
        if not Hash.verify(user.PASSWORD, request.password):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Incorrect Password")
            # access_token = token.create_access_token(data={"sub": user.CMND})
            return user
    return

def register(request: sm.User):
    user=col.find_one({"username": request.username})
    if not user:
        hashedPassword = Hash.bcrypt(request.password)
        col.insert_one(document={"username": request.username, "password": hashedPassword})
        check_user = col.find_one({"username": request.username},{'_id': 0})
        if check_user:
            return dict(check_user)
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User exists")

