"""
This module contains functions for evaluating individual queries and calculating summary statistics.
It provides the core evaluation logic used by the main evaluation script.
"""

from typing import List, Dict, Any
from llama_index.core.evaluation import FaithfulnessEvaluator, RelevancyEvaluator
from llama_index.llms.openai import OpenAI
import time

EVAL_LLM = OpenAI(model="gpt-4", temperature=0)

async def evaluate_query(query_engine, query: str) -> Dict[str, Any]:
    """
    Evaluate a single query using the provided query engine.

    Args:
        query_engine: The query engine to use for evaluation.
        query (str): The query to evaluate.

    Returns:
        Dict[str, Any]: A dictionary containing the evaluation results for the query.
    """
    start_time = time.time()
    response = await query_engine.aquery(query)
    query_runtime = time.time() - start_time

    result = {
        "query": query,
        "response": response.response,
        "source_nodes": response.source_nodes,
        "num_source_nodes": len(response.source_nodes),
        "query_runtime": query_runtime,
    }

    if hasattr(response, 'relevant_docs'):
        result['relevant_docs'] = response.relevant_docs

    contexts = [node.node.get_content() for node in response.source_nodes]
    
    faithfulness_result = await evaluate_faithfulness(query, str(response), contexts)
    relevancy_result = await evaluate_relevancy(query, str(response), contexts)

    result.update({
        "faithfulness_score": faithfulness_result.score,
        "faithfulness_passing": faithfulness_result.passing,
        "faithfulness_feedback": faithfulness_result.feedback,
        "relevancy_score": relevancy_result.score,
        "relevancy_feedback": relevancy_result.feedback,
    })

    return result

async def evaluate_faithfulness(query: str, response: str, contexts: List[str]) -> Any:
    """
    Evaluate the faithfulness of a response to a query.

    Args:
        query (str): The original query.
        response (str): The response to evaluate.
        contexts (List[str]): The source contexts used to generate the response.

    Returns:
        Any: The result of the faithfulness evaluation.
    """
    faithfulness_evaluator = FaithfulnessEvaluator(llm=EVAL_LLM)
    return await faithfulness_evaluator.aevaluate(query=query, response=response, contexts=contexts)

async def evaluate_relevancy(query: str, response: str, contexts: List[str]) -> Any:
    """
    Evaluate the relevancy of a response to a query.

    Args:
        query (str): The original query.
        response (str): The response to evaluate.
        contexts (List[str]): The source contexts used to generate the response.

    Returns:
        Any: The result of the relevancy evaluation.
    """
    relevancy_evaluator = RelevancyEvaluator(llm=EVAL_LLM)
    return await relevancy_evaluator.aevaluate(query=query, response=response, contexts=contexts)

def calculate_summary_stats(results: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    Calculate summary statistics from a list of query evaluation results.

    Args:
        results (List[Dict[str, Any]]): A list of query evaluation results.

    Returns:
        Dict[str, float]: A dictionary containing summary statistics.
    """
    return {
        "avg_faithfulness": sum(r["faithfulness_score"] for r in results) / len(results),
        "avg_relevancy": sum(r["relevancy_score"] for r in results) / len(results),
        "avg_source_nodes": sum(r["num_source_nodes"] for r in results) / len(results),
        "avg_query_runtime": sum(r["query_runtime"] for r in results) / len(results),
        "total_docs_retrieved": sum(r["num_source_nodes"] for r in results),
        "total_runtime": sum(r["query_runtime"] for r in results)
    }