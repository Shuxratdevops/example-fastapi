from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import database, schemas, models, utils, oauth2


router = APIRouter(tags=['Authentication'])


@router.post('/login')
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    # print(user_credentials.username)
    # print(db.query(models.User).filter(models.User.email))
    # print(user.__dict__)
    if not user: # user borligini tekshirish
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials1") 
    
    # user kiritgan parolni database dagisi bilan solishtirish
    if not utils.verify(user_credentials.password, user.password): # verify 2 ta malumotni tengligini solishtiradi
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")


    # creat a token
    # return token 

    access_token = oauth2.create_access_token(data={"user_id": user.id})
    
    return {"access_token" : access_token, "token_type": "bearer"}