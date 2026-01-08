@echo off
echo ====================================
echo Starting Backend Server Only
echo ====================================
cd backend
call .\\venv\\Scripts\\activate
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
