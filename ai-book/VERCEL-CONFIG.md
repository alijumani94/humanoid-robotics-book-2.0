# Vercel Configuration - Quick Reference

## Problem: Chatbot Shows "Failed to Fetch" on Production

Your Vercel frontend is trying to call `http://localhost:8000` which doesn't exist in production.

## Solution: Set Environment Variable

### Step 1: Deploy Your Backend First
Deploy your backend to Render, Railway, or another hosting service.
See [DEPLOYMENT-GUIDE.md](./DEPLOYMENT-GUIDE.md) for detailed instructions.

### Step 2: Configure Vercel

1. Go to https://vercel.com/dashboard
2. Select your project: **humanoid-robotics-book**
3. Click **Settings** tab
4. Click **Environment Variables** in the left sidebar
5. Add new variable:
   - **Name**: `DOCUSAURUS_API_URL`
   - **Value**: Your backend URL (e.g., `https://humanoid-robotics-backend.onrender.com`)
   - Check all three environments: Production, Preview, Development
6. Click **Save**

### Step 3: Redeploy

**Option A: Force Redeploy**
1. Go to **Deployments** tab
2. Click the three dots (...) on the latest deployment
3. Click **Redeploy**
4. Confirm

**Option B: Trigger via Git Push**
```bash
git commit --allow-empty -m "Trigger redeploy"
git push
```

### Step 4: Verify

Visit your site: https://humanoid-robotics-book.vercel.app
- Click the chat button (💬)
- Ask: "What is Physical AI?"
- Should work without errors!

---

## Environment Variables Reference

| Variable | Value | Purpose |
|----------|-------|---------|
| `DOCUSAURUS_API_URL` | Your backend URL | Tells frontend where the API is |

Example:
```
DOCUSAURUS_API_URL=https://humanoid-robotics-backend.onrender.com
```

**Important**: No trailing slash in the URL!

---

## How It Works

1. **Development** (local):
   - Frontend uses `http://localhost:8000` (default)
   - Backend runs locally

2. **Production** (Vercel):
   - Frontend uses `DOCUSAURUS_API_URL` from environment variable
   - Backend runs on Render/Railway/etc.

The code in `docusaurus.config.ts`:
```typescript
customFields: {
  apiUrl: process.env.DOCUSAURUS_API_URL || 'http://localhost:8000',
}
```

---

## Troubleshooting

### Still getting "failed to fetch"
- Did you redeploy after setting the environment variable?
- Is the backend URL correct? (test it: `curl https://your-backend.onrender.com/api/health`)
- Check browser DevTools → Network tab to see the actual URL being called

### CORS errors
- Make sure backend's `ALLOWED_ORIGINS` includes your Vercel URL
- Redeploy the backend after changing CORS settings

### Environment variable not working
- Make sure you checked all three environments (Production, Preview, Development)
- Environment variables take effect on next deployment, not immediately
