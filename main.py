import os
from datetime import timedelta

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from auth import Auth
from db import JsonDb
from dto import Features, Token
from ml_models import AnimalClassificationModel

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", "1"))

app = FastAPI()
db = JsonDb().get_db()
auth = Auth(db=db)


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = auth.authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect user name or password",
            headers={"WWW-Authentificate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/make_inference")
async def make_inference(
    features: Features, current_user=Depends(auth.get_current_user)
):
    result = AnimalClassificationModel.make_inference(
        paws_count=features.paws_count, has_fur=features.has_fur, mammal=features.mammal
    )
    return {"result": result, "user": current_user}
