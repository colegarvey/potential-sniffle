@echo off
echo Activating local sniff-env...
call env\Scripts\activate

echo Starting FastAPI server...
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload --reload-dir app

