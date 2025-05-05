from app.database import db
from app.models.user import UserCreate, UserInDB
from bson import ObjectId


def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "email": user["email"],
        "username": user["username"],
        # don't return password by default!
    }


async def create_user(user_data: UserCreate) -> str:
    user = user_data.dict()
    result = await db["users"].insert_one(user)
    return str(result.inserted_id)


async def get_user_by_id(user_id: str) -> dict:
    user = await db["users"].find_one({"_id": ObjectId(user_id)})
    if user:
        return user_helper(user)
    return None


async def get_user_by_email(email: str) -> User:
    user = await db["users"].find_one({"email": email})
    if user:
        return user_helper(user)
    return None
