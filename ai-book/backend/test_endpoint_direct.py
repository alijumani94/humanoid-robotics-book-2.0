"""Test the endpoint directly to see errors"""
import asyncio
import sys
from app.api.routes.chat import chat
from app.models.schemas import ChatRequest
from app.services.db_service import get_db
from fastapi import Request
from unittest.mock import Mock

async def test_endpoint():
    try:
        # Create a mock request
        mock_request = Mock(spec=Request)
        mock_request.client = Mock()
        mock_request.client.host = "127.0.0.1"

        # Create chat request
        chat_request = ChatRequest(
            question="What is humanoid robotics?",
            user_id=None,
            selected_text=None
        )

        # Get database session
        async for db in get_db():
            print("Calling chat endpoint...")
            result = await chat(
                request=mock_request,
                chat_request=chat_request,
                db=db
            )
            print(f"Success! Answer: {result.answer[:100]}...")
            break

    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_endpoint())
