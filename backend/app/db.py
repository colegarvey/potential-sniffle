from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Request
import os

client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
db = client["fitness"]

async def init_db():
    # any DB init logic here (indexes, etc.)
    pass
