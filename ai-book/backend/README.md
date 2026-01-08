# RAG Chatbot Backend

FastAPI backend for the RAG-powered e-book chatbot.

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment:
```bash
cp .env.example .env
# Edit .env with your API keys
```

4. Run database migrations:
```bash
python scripts/create_schema.py
```

5. Ingest book content:
```bash
python scripts/ingest_book.py
```

6. Run the server:
```bash
uvicorn app.main:app --reload
```

## API Endpoints

- `POST /api/chat` - Submit a question
- `GET /api/chat/history` - Get chat history
- `POST /api/feedback` - Submit feedback
- `GET /api/health` - Health check

## Project Structure

```
backend/
├── app/
│   ├── api/          # API routes and middleware
│   ├── services/     # Business logic
│   ├── models/       # Data models
│   └── utils/        # Utilities
├── scripts/          # Data ingestion scripts
└── tests/            # Tests
```

## Testing

```bash
pytest tests/
```

## Documentation

Interactive API docs available at: http://localhost:8000/docs

## Production Deployment

### Prerequisites
- Backend must be deployed to a hosting service (Render, Railway, etc.)
- See [DEPLOYMENT-GUIDE.md](../DEPLOYMENT-GUIDE.md) for detailed instructions

### Quick Deploy to Render
1. Push code to GitHub
2. Create Web Service on Render
3. Set Root Directory to `backend`
4. Set Build Command: `pip install -r requirements.txt`
5. Set Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
6. Add environment variables (see `.env.production.example`)
7. Deploy

### Quick Deploy to Railway
1. Push code to GitHub
2. Create project on Railway
3. Connect repository
4. Set Root Directory to `backend`
5. Add environment variables
6. Deploy

### Environment Variables for Production
```bash
OPENAI_API_KEY=your-key
QDRANT_URL=your-qdrant-url
QDRANT_API_KEY=your-qdrant-key
DATABASE_URL=your-database-url
ALLOWED_ORIGINS=https://humanoid-robotics-book.vercel.app
ENVIRONMENT=production
```

See `.env.production.example` for complete list.
