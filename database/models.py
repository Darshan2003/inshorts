from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    email = Column(String)
    username = Column(String)
    password = Column(String)

class Shorts(Base):
    __tablename__ = 'shorts'
    short_id = Column(Integer, primary_key=True)
    category = Column(String)
    title = Column(String)
    author = Column(String)
    publish_date = Column(String)
    content = Column(String)
    actual_content_link = Column(String)
    image = Column(String)
    upvote = Column(Integer)
    downvote = Column(Integer)

