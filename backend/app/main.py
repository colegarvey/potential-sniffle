from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.database import init_db
from app.models.user import UserCreate
from app.crud import user as user_crud

# from app.routes import users, workouts
# from app.db import init_db

app = FastAPI()
# app.include_router(users.router)
# app.include_router(workouts.router)

@app.on_event("startup")
async def start_db():
    await init_db()


# Allow requests from frontend's origin
origins = [
    "http://localhost:3000",  # React development server (default port)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (be more specific for security)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


@app.get("/")
def root():
    return {"message": "Api is running"}

@app.get("/workouts")
async def get_workouts():
    return [
        {"id": 1, "name": "Push Ups", "duration_minutes": 10},
        {"id": 2, "name": "Running", "duration_minutes": 30},
        {"id": 3, "name": "Plank", "duration_minutes": 5},
        ]


@app.post("/users/")
async def create_user(user: UserCreate):
    user_id = await user_crud.create_user(user)
    return {"message": "User created successfully", "user_id": user_id}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    user = await user_crud.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user