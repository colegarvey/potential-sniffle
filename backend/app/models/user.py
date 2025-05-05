from pydantic import BaseModel, EmailStr
from typing import Optional
# from bson import ObjectId

# class User(BaseModel):
#     id: Optional[str]
#     email: EmailStr
#     username: str
#     hashed_password: str

#     class Config:
#         arbitrary_types_allowed = True


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str  # plaintext password at first, you'll hash it later

    
class UserInDB(UserCreate):
    id: Optional[str]