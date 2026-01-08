# Production Deployment Guide

## Overview

Your application has two parts that need to be deployed separately:

1. **Frontend (Docusaurus)** - Already deployed on Vercel ✅
2. **Backend (FastAPI)** - Needs to be deployed separately ❌

## The Problem

Currently, your Vercel deployment shows "failed to fetch" because:
- The frontend is trying to call `http://localhost:8000/api/chat`
- But there's no backend server running in production
- The backend only runs on your local machine

## Solution: Deploy Backend + Connect to Frontend

---

## Step 1: Deploy Backend to Render (RECOMMENDED - FREE)

### Option A: Deploy via Render Dashboard

1. **Create Render Account**
   - Go to https://render.com
   - Sign up/Login with GitHub

2. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the repository: `humanoid-robotics-book`
   - Configure settings:
     - **Name**: `humanoid-robotics-backend`
     - **Region**: Oregon (US West)
     - **Branch**: `main`
     - **Root Directory**: `backend`
     - **Runtime**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
     - **Plan**: Free

3. **Add Environment Variables**
   Click "Environment" and add these variables (copy from your local `backend/.env`):

   ```
   OPENAI_API_KEY=sk-proj-...
   MODEL_NAME=gpt-4-turbo-preview
   MAX_RESPONSE_TOKENS=500
   TEMPERATURE=0.3

   QDRANT_URL=https://9b8eb544-...
   QDRANT_API_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
   VECTOR_DIMENSION=1536
   TOP_K_RETRIEVAL=5
   SIMILARITY_THRESHOLD=0.25

   DATABASE_URL=postgresql+asyncpg://neondb_owner:...

   ENVIRONMENT=production
   API_RATE_LIMIT_PER_MINUTE=20
   API_RATE_LIMIT_PER_USER=10
   ALLOWED_ORIGINS=https://humanoid-robotics-book.vercel.app

   CHUNK_SIZE=600
   CHUNK_OVERLAP=100
   ```

4. **Deploy**
   - Click "Create Web Service"
   - Wait 5-10 minutes for deployment
   - You'll get a URL like: `https://humanoid-robotics-backend.onrender.com`

### Option B: Deploy via render.yaml (Blueprint)

1. Push `backend/render.yaml` to your GitHub repo
2. In Render dashboard, click "New +" → "Blueprint"
3. Connect your repository
4. Render will automatically detect `render.yaml` and configure everything
5. Add environment variables as shown above

---

## Step 2: Configure Vercel Frontend

Once your backend is deployed, you need to tell your frontend where to find it:

1. **Go to Vercel Dashboard**
   - Visit https://vercel.com/dashboard
   - Select your project: `humanoid-robotics-book`

2. **Add Environment Variable**
   - Go to "Settings" → "Environment Variables"
   - Add new variable:
     - **Key**: `DOCUSAURUS_API_URL`
     - **Value**: `https://your-backend-url.onrender.com` (your Render backend URL)
     - **Environments**: Select "Production", "Preview", and "Development"
   - Click "Save"

3. **Redeploy Frontend**
   - Go to "Deployments" tab
   - Click the three dots on the latest deployment
   - Click "Redeploy"
   - **OR** just push a new commit to trigger redeployment

---

## Step 3: Verify Everything Works

### Test Backend
```bash
curl https://your-backend-url.onrender.com/api/health
```

Should return:
```json
{
  "status": "healthy",
  "services": {...},
  "timestamp": "..."
}
```

### Test Chat Endpoint
```bash
curl -X POST https://your-backend-url.onrender.com/api/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "What is Physical AI?"}'
```

Should return an answer with sources.

### Test Production Website
1. Visit https://humanoid-robotics-book.vercel.app
2. Click the chat button (💬)
3. Ask a question
4. Should receive an answer (no "failed to fetch" error!)

---

## Alternative: Deploy Backend to Railway

Railway is another excellent free option:

1. **Sign up at https://railway.app**
2. **Create New Project** → "Deploy from GitHub repo"
3. **Select your repository**
4. **Configure Service:**
   - Root Directory: `backend`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. **Add Environment Variables** (same as Render)
6. **Generate Domain** - Railway will give you a URL
7. **Update Vercel** with the Railway URL in `DOCUSAURUS_API_URL`

---

## Alternative: Deploy Backend to Vercel Serverless

**Note**: This requires restructuring the backend as serverless functions. Not recommended for now as it requires significant changes.

---

## Troubleshooting

### Backend deployment fails
- Check build logs in Render/Railway dashboard
- Verify all environment variables are set correctly
- Ensure `requirements.txt` is in the `backend` directory

### CORS errors in browser console
- Check that `ALLOWED_ORIGINS` includes your Vercel URL
- Verify both URLs (with and without trailing slash)
- Update `backend/app/config.py` if needed and redeploy

### Chatbot still shows "failed to fetch"
- Verify `DOCUSAURUS_API_URL` is set in Vercel
- Check that backend is actually running (visit the health endpoint)
- Open browser DevTools → Network tab to see the actual request URL
- Make sure you redeployed Vercel after setting the environment variable

### Backend takes long to respond (30+ seconds)
- This is normal for Render free tier on first request (cold start)
- Backend goes to sleep after 15 minutes of inactivity
- Consider upgrading to paid tier or using Railway (faster cold starts)

---

## Cost Summary

| Service | Plan | Cost | Notes |
|---------|------|------|-------|
| Vercel (Frontend) | Free | $0/month | Already deployed ✅ |
| Render (Backend) | Free | $0/month | Sleeps after 15 min inactivity |
| Railway (Backend) | Free | $0/month | $5 free credit/month |
| Qdrant Cloud | Free | $0/month | Already configured ✅ |
| Neon Postgres | Free | $0/month | Already configured ✅ |

**Total Monthly Cost**: $0 (for free tiers)

---

## Recommended Deployment Flow

1. **Deploy Backend to Render** (most reliable free tier)
2. **Get Backend URL** (e.g., `https://humanoid-robotics-backend.onrender.com`)
3. **Set Vercel Environment Variable** (`DOCUSAURUS_API_URL`)
4. **Redeploy Vercel**
5. **Test Production Site**

---

## Maintenance

### Updating Backend
1. Push changes to GitHub
2. Render/Railway will automatically detect and redeploy
3. Check deployment logs to ensure success

### Updating Frontend
1. Push changes to GitHub
2. Vercel will automatically detect and redeploy

### Monitoring
- **Backend Health**: Visit `https://your-backend-url.onrender.com/api/health`
- **Backend Logs**: Check Render/Railway dashboard
- **Frontend Logs**: Check Vercel dashboard

---

## Security Notes

- ✅ CORS is configured to only allow requests from your Vercel domain
- ✅ API keys are stored as environment variables (not in code)
- ✅ Rate limiting is enabled (20 requests/minute)
- ⚠️ Consider adding authentication for production use
- ⚠️ Monitor OpenAI API usage to avoid unexpected costs

---

## Next Steps

After deployment:
1. Test all chatbot functionality
2. Monitor backend logs for errors
3. Set up monitoring/alerting (optional)
4. Consider adding analytics
5. Add authentication if needed
