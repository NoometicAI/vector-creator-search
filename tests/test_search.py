from search.query_engine import get_test_query_engine

def test_search(query:str):
    query_engine = get_test_query_engine()
    result = query_engine.query(query)

    # Check if the result is a string
    # assert isinstance(result, str), "The search result should be a string"

    return result

if __name__ == "__main__":
    query = "find gaming infleuncers"
    result = test_search(query)
    print(result)