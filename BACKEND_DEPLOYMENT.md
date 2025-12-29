# Backend Deployment Guide

## Overview
The FastAPI backend needs to be deployed separately from the frontend. This guide covers deployment options.

## Prerequisites
You'll need:
- OpenAI API Key
- Qdrant Cloud account (or self-hosted Qdrant)
- PostgreSQL database (optional, for user analytics)

## Deployment Options

### Option 1: Deploy to Railway (Recommended)

1. **Create Railway Account**: Visit [railway.app](https://railway.app)

2. **Create New Project**:
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Set root directory to `ai-book/backend`

3. **Configure Environment Variables**:
   ```
   OPENAI_API_KEY=your-openai-api-key
   QDRANT_URL=your-qdrant-url
   QDRANT_API_KEY=your-qdrant-api-key
   ALLOWED_ORIGINS=https://your-vercel-app.vercel.app
   MODEL_NAME=gpt-4-turbo-preview
   MAX_RESPONSE_TOKENS=500
   TEMPERATURE=0.3
   VECTOR_DIMENSION=1536
   TOP_K_RETRIEVAL=5
   SIMILARITY_THRESHOLD=0.7
   ENVIRONMENT=production
   ```

4. **Deploy**: Railway will automatically deploy using the Dockerfile

5. **Get the URL**: Copy your Railway app URL (e.g., `https://your-app.up.railway.app`)

### Option 2: Deploy to Render

1. **Create Render Account**: Visit [render.com](https://render.com)

2. **Create New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Set root directory to `ai-book/backend`

3. **Configure**:
   - Environment: Docker
   - Add environment variables (same as Railway)

4. **Deploy**: Click "Create Web Service"

### Option 3: Deploy to Vercel (Serverless)

Note: Vercel has limitations for long-running processes. Use Railway or Render for better reliability.

## After Deploying Backend

### Update Frontend Environment Variable

1. **Go to Vercel Dashboard** → Your Project → Settings → Environment Variables

2. **Add this variable**:
   ```
   Name: DOCUSAURUS_API_URL
   Value: https://your-backend-url.railway.app (or your backend URL)
   ```

3. **Redeploy**: Vercel will automatically redeploy with the new environment variable

## Testing

After deployment, test the connection:
```bash
curl -X POST https://your-backend-url/api/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "What is Physical AI?"}'
```

You should get a JSON response with an answer.

## Troubleshooting

### CORS Errors
- Make sure `ALLOWED_ORIGINS` in backend includes your Vercel URL
- Example: `https://your-app.vercel.app`

### "Failed to fetch" Error
- Check if backend URL is correct in Vercel environment variables
- Verify backend is running (visit `https://your-backend-url/api/health`)

### Rate Limiting
- Adjust `API_RATE_LIMIT_PER_MINUTE` if needed
