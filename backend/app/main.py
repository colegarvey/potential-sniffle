from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from app.routes import users, workouts
# from app.db import init_db

app = FastAPI()
# app.include_router(users.router)
# app.include_router(workouts.router)

# @app.on_event("startup")
# async def startup_db():
#     await init_db()
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