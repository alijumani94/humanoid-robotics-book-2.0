# Setup & Development Guide

## Quick Start

### Option 1: Start Both Frontend & Backend (RECOMMENDED)
```bash
start-dev.bat
```
This will:
- Start the backend server in a new terminal window (http://localhost:8000)
- Start the frontend in the current terminal (http://localhost:3000)

### Option 2: Start Servers Separately

**Start Backend Only:**
```bash
start-backend.bat
```

**Start Frontend Only:**
```bash
npm start
```

## Important Notes

**⚠️ MUST START BACKEND FIRST**: The chatbot will show "failed to fetch" error if the backend server is not running on port 8000.

**Why this happens**:
- When you close your laptop, all running processes stop
- When you reopen and run `npm start`, only the frontend starts
- The backend needs to be started separately (or use `start-dev.bat`)

## Environment Setup

### Backend Environment Variables
The backend uses environment variables from `backend/.env`. Make sure this file exists with:
- OpenAI API Key
- Qdrant configuration
- Database URL
- Other settings

### Frontend Environment Variables
The frontend reads the API URL from `docusaurus.config.ts` which uses:
- `DOCUSAURUS_API_URL` environment variable (for production)
- Defaults to `http://localhost:8000` (for development)

## Troubleshooting

### Chatbot shows "failed to fetch"
**Solution**: Make sure backend is running
```bash
# Check if backend is running
tasklist | findstr "python uvicorn"

# If not running, start it
start-backend.bat
```

### Backend won't start
**Solution**: Check if port 8000 is already in use
```bash
netstat -ano | findstr ":8000"
```

### Database connection issues
**Solution**: Check your `backend/.env` file and ensure DATABASE_URL is correct

## Development Workflow

1. **First Time Setup:**
   ```bash
   cd backend
   python -m venv venv
   .\\venv\\Scripts\\activate
   pip install -r requirements.txt
   ```

2. **Daily Development:**
   ```bash
   # From project root
   start-dev.bat
   ```

3. **Testing Backend API:**
   - Visit http://localhost:8000/docs for API documentation
   - Health check: http://localhost:8000/api/health

4. **Testing Frontend:**
   - Visit http://localhost:3000
   - Click the chat button in bottom-right corner
