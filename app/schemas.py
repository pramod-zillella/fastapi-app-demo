from pydantic import BaseModel, EmailStr, conint
# importing datetime module
from datetime import datetime
from typing import Optional

# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    created_at: datetime
    email: EmailStr

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

class UserBase(BaseModel):
    email: EmailStr
    password: str

class UserAuthenticate(BaseModel):
    email: EmailStr
    password: str   

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id : Optional[str] = None

class VoteCreate(BaseModel):
    post_id: int
    dir: conint(le=1)

