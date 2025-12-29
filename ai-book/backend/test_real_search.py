"""Test search with real embedding"""
import asyncio
from qdrant_client import QdrantClient
from app.config import settings
from app.utils.embeddings import generate_embedding

async def test_search():
    client = QdrantClient(
        url=settings.qdrant_url,
        api_key=settings.qdrant_api_key,
    )

    COLLECTION_NAME = "book_embeddings"
    query = "What is humanoid robotics?"

    print(f"Query: {query}")
    print("Generating embedding...")

    # Generate real embedding
    query_vector = await generate_embedding(query)
    print(f"Embedding generated: {len(query_vector)} dimensions")

    # Search without score threshold
    print("\nSearching WITHOUT score threshold...")
    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=5,
        score_threshold=None,
    )

    print(f"Found {len(results.points)} results:")
    for i, result in enumerate(results.points, 1):
        print(f"\nResult {i}:")
        print(f"  Score: {result.score}")
        print(f"  Chapter: {result.payload.get('chapter_title', 'N/A')}")
        print(f"  Text: {result.payload.get('text', '')[:100]}...")

    # Now try with 0.7 threshold
    print("\n" + "="*50)
    print("Searching WITH score threshold 0.7...")
    results_with_threshold = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=5,
        score_threshold=0.7,
    )

    print(f"Found {len(results_with_threshold.points)} results with threshold 0.7")

if __name__ == "__main__":
    asyncio.run(test_search())
