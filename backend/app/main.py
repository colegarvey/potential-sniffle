from fastapi import FastAPI
# from app.routes import users, workouts
# from app.db import init_db

app = FastAPI()
# app.include_router(users.router)
# app.include_router(workouts.router)

# @app.on_event("startup")
# async def startup_db():
#     await init_db()


@app.get("/")
def root():
    return {"message": "Api is running"}