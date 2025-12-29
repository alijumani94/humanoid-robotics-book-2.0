"""Test the full API flow"""
import asyncio
from app.services.rag_service import process_question

async def test_api_flow():
    try:
        print("Testing full API flow...")
        print("Question: What is humanoid robotics?")

        # This is what the API endpoint calls
        rag_response = await process_question(
            question="What is humanoid robotics?",
            selected_text=None,
        )

        print(f"\nSuccess!")
        print(f"Answer: {rag_response.answer[:200]}...")
        print(f"Chunks used: {len(rag_response.chunks)}")
        print(f"Retrieval mode: {rag_response.retrieval_mode}")

        for i, chunk in enumerate(rag_response.chunks, 1):
            print(f"\nChunk {i}:")
            print(f"  ID: {chunk.chunk_id}")
            print(f"  Score: {chunk.score}")
            print(f"  Chapter: {chunk.chapter_title}")

    except Exception as e:
        print(f"\nERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_api_flow())
