"""Test Qdrant collection status"""
from qdrant_client import QdrantClient
from app.config import settings

# Initialize client
client = QdrantClient(
    url=settings.qdrant_url,
    api_key=settings.qdrant_api_key,
)

COLLECTION_NAME = "book_embeddings"

try:
    # Check if collection exists
    collections = client.get_collections()
    print(f"Available collections: {[c.name for c in collections.collections]}")

    # Get collection info
    collection_info = client.get_collection(COLLECTION_NAME)
    print(f"\nCollection '{COLLECTION_NAME}':")
    print(f"  Points count: {collection_info.points_count}")

    # Try a search with no score threshold
    if collection_info.points_count > 0:
        print("\nTrying search with no score threshold...")
        # Create a test vector (all zeros)
        test_vector = [0.0] * 1536

        results = client.query_points(
            collection_name=COLLECTION_NAME,
            query=test_vector,
            limit=5,
            score_threshold=None,  # No threshold
        )

        print(f"Found {len(results.points)} results")
        for i, result in enumerate(results.points, 1):
            print(f"\nResult {i}:")
            print(f"  Score: {result.score}")
            print(f"  Payload keys: {list(result.payload.keys())}")

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
