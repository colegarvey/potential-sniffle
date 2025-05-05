from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Request
import os


client = None
db = None

async def init_db():
    global client, db
    
    # Load environment variables from the .env file
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

    # Now fetch them
    MONGO_USER = os.getenv("MONGO_USER")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
    MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
    MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
    MONGO_DB = os.getenv("MONGO_DB")

    # Build the MongoDB URI
    MONGO_URI = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"

    # Set up the client
    client = AsyncIOMotorClient(MONGO_URI)
    db = client[MONGO_DB]

