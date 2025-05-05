@echo off
echo Stop FastAPI server manually if needed...

:: No automatic FastAPI kill (you usually Ctrl+C manually), but we can bring down Docker

echo Stopping Docker containers...
docker-compose down

echo Done! Everything stopped.
pause
