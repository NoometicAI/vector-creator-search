import time
import asyncio
from search.query_pipeline import get_query_pipeline

async def test_get_query_pipeline(query):
    start_time = time.time()
    pipeline = await get_query_pipeline()
    init_time = time.time()
    print(f"Time to initialize pipeline: {init_time - start_time}")
    response = await pipeline.arun(input=query)
    query_time = time.time()
    print(f"Time to query: {query_time - init_time}")
    assert response is not None
    end_time = time.time()
    print(f"Time to run pipeline: {end_time - query_time}\n")
    print("Response:", response)
    return response


if __name__ == "__main__":
    asyncio.run(test_get_query_pipeline("find gaming creators"))
