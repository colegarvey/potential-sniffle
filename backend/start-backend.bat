@echo off
echo Activating local sniff-env...
call env\Scripts\activate

echo Checking if Docker is running...
docker info >nul 2>&1
if errorlevel 1 (
    echo.
    echo ERROR: Docker Desktop is not running. Please start Docker and try again.
    pause
    exit /b
)

echo Starting Docker containers...
docker-compose up -d

echo Starting FastAPI server...
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload --reload-dir app

