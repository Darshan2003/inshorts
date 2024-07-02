from fastapi_sqlalchemy import db

from database.models import Users as UserModel

def create_user(username, password, email)->int:
    user = UserModel(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()
    return user.user_id

def check_user(username, password)->int:
    user = db.session.query(UserModel).filter(UserModel.username==username).all()
    if len(user)==0:
        return -1
    user = user[0]
    if password==user.password:
        return user.user_id
    return -1