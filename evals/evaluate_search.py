"""
This module handles the evaluation of search queries using a specified query engine.
It loads test queries from a JSON file, runs them through the query engine,
and generates a detailed evaluation report.
"""

import asyncio
import json
import argparse
from typing import List, Dict, Any
from search.query_engine import get_query_engine
import logging
from datetime import datetime
from evals.report_writer import write_evaluation_report, print_query_result, print_summary_tables
from evals.evaluators import evaluate_query, calculate_summary_stats

# Configure logging
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("evaluation")
logger.setLevel(logging.INFO)

# Silence specific loggers that are too verbose
logging.getLogger("openai").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)

def load_test_queries(file_path: str) -> List[str]:
    """
    Load test queries from a JSON file.

    Args:
        file_path (str): Path to the JSON file containing test queries.

    Returns:
        List[str]: A list of test queries.
    """
    with open(file_path, 'r') as f:
        return json.load(f)

async def evaluate_queries(query_engine, queries: List[str], index_load_time: float) -> Dict[str, Any]:
    """
    Evaluate a list of queries using the provided query engine.

    Args:
        query_engine: The query engine to use for evaluation.
        queries (List[str]): A list of queries to evaluate.
        index_load_time (float): The time taken to load the index.

    Returns:
        Dict[str, Any]: A dictionary containing evaluation results and summary statistics.
    """
    results = []
    total_docs_retrieved = 0
    total_runtime = 0.0

    for i, query in enumerate(queries, 1):
        result = await evaluate_query(query_engine, query)
        result['query_number'] = i  # Add query number to the result
        results.append(result)
        total_docs_retrieved += result["num_source_nodes"]
        total_runtime += result["query_runtime"]
        print_query_result(result)
    
    avg_runtime = total_runtime / len(queries) if queries else 0.0
    summary_stats = calculate_summary_stats(results)
    
    return {
        "results": results,
        "total_docs_retrieved": total_docs_retrieved,
        "avg_runtime": avg_runtime,
        "total_runtime": total_runtime,
        "index_load_time": index_load_time,
        **summary_stats
    }

async def main():
    """
    Main function to run the evaluation process.
    """
    parser = argparse.ArgumentParser(description="Evaluate search queries")
    parser.add_argument("--queries", default="evals/test_queries.json", help="Path to the test queries JSON file")
    args = parser.parse_args()

    # persist_dir = "/Volumes/LaCie/noometic/indexes/7.15.24/_data/persist_dir_11_39_june_12_free" # lacie ssd
    persist_dir = "/Users/kenneth/Desktop/lab/noometic_dev/indexes/7.15.24/persist_dir_11_39_june_12_free" # local
    query_engine, query_engine_params = await get_query_engine(persist_dir, eval_mode=True)
    
    # Extract index_load_time from query_engine_params
    index_load_time = query_engine_params.get("index_load_time", 0.0)
    
    test_queries = load_test_queries(args.queries)
    
    evaluation_data = await evaluate_queries(query_engine, test_queries, index_load_time)
    print_summary_tables(evaluation_data)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"evals/results/results_{timestamp}.md"
    write_evaluation_report(evaluation_data, query_engine_params, filename)
    logger.info(f"Results written to {filename}")

if __name__ == "__main__":
    asyncio.run(main())