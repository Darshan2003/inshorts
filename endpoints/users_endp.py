from fastapi import APIRouter
from database.users_db import (
    create_user,
    check_user
)

router = APIRouter(
    prefix="/api",
    tags=["User"]
)

@router.post("/signup")
def user_signup(username, password, email):
    if username=="" or password=="" or email=="":
        return {"status": "Username/Password/Email cannot be empty"}
    user_id = create_user(username, password, email)
    return {"status": "Account Successfully created", "status_code":200, "user_id":user_id}

@router.post("/login")
def user_login(username, password):
    if username=="" or password=="":
        return {"status":"Incorrect username/password provided. Please retry", "status_code":401}

    uid = check_user(username, password)
    if uid==-1:
        return {"status":"Incorrect username/password provided. Please retry", "status_code":401}
    return {"status":"Login Successful", "status_code":"200", "user_id": uid}

