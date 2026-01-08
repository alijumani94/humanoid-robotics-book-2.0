@echo off
echo ====================================
echo Starting Humanoid Robotics Book
echo ====================================
echo.

REM Start backend in a new terminal
echo [1/2] Starting Backend Server...
start "Backend Server" cmd /k "cd backend && .\\venv\\Scripts\\activate && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload"

REM Wait a few seconds for backend to start
timeout /t 3 /nobreak > nul

REM Start frontend
echo [2/2] Starting Frontend Server...
echo.
echo ====================================
echo Both servers are starting!
echo Backend: http://localhost:8000
echo Frontend: http://localhost:3000
echo ====================================
echo.
npm start
