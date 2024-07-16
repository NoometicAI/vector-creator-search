from search.query_engine import get_test_query_engine, get_kg_retriever_query_engine

def test_search(query:str):
    query_engine = get_test_query_engine()
    result = query_engine.query(query)

    # Check if the result is a string
    # assert isinstance(result, str), "The search result should be a string"

    return result


def test_kg_retriever_query_engine(query:str):
    query_engine = get_kg_retriever_query_engine()
    result = query_engine.query(query)
    print(result)

if __name__ == "__main__":
    query = "find gaming infleuncers"
    
    print('test_search:')
    result = test_search(query)
    print(result)
    print('-'*10)
    print('test_kg_retriever_query_engine:')
    result = test_kg_retriever_query_engine(query)
    print(result)