"""Test Qdrant connection and query_points method"""
import asyncio
from app.services.retrieval_service import search_similar_chunks

async def test_qdrant():
    try:
        print("Testing Qdrant search...")
        results = await search_similar_chunks("What is humanoid robotics?", top_k=3)
        print(f"Success! Found {len(results)} chunks:")
        for i, chunk in enumerate(results, 1):
            print(f"\nChunk {i}:")
            print(f"  Score: {chunk.score}")
            print(f"  Chapter: {chunk.chapter_title}")
            print(f"  Text preview: {chunk.text[:100]}...")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_qdrant())
