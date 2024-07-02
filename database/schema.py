from pydantic import BaseModel

class Users(BaseModel):
    user_id: int
    username: str
    password: str
    email: str

    class Config:
        orm_mode = True

class VoteModel(BaseModel):
    upvote: int
    downvote: int

class CreateShorts(BaseModel):
    category: str
    title: str
    author: str
    publish_date: str
    content: str
    actual_content_link: str
    image: str
    vote: VoteModel

class Shorts(BaseModel):
    category: str
    title: str
    author: str
    publish_date: str
    content: str
    actual_content_link: str
    image: str
    upvote: int
    downvote: int

    class Config:
        orm_mode = True
