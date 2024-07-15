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
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from datetime import datetime
from evals.report_writer import write_evaluation_report
from evals.evaluators import evaluate_query, calculate_summary_stats

# Configure logging
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("evaluation")
logger.setLevel(logging.INFO)

# Silence specific loggers that are too verbose
logging.getLogger("openai").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)

console = Console()

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

async def evaluate_queries(query_engine, queries: List[str]) -> Dict[str, Any]:
    """
    Evaluate a list of queries using the provided query engine.

    Args:
        query_engine: The query engine to use for evaluation.
        queries (List[str]): A list of queries to evaluate.

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
        
        console.print("─" * 80)
    
    avg_runtime = total_runtime / len(queries) if queries else 0.0
    summary_stats = calculate_summary_stats(results)
    
    return {
        "results": results,
        "total_docs_retrieved": total_docs_retrieved,
        "avg_runtime": avg_runtime,
        "total_runtime": total_runtime,
        **summary_stats
    }

def print_query_result(result: Dict[str, Any]):
    """
    Print the evaluation result for a single query.

    Args:
        result (Dict[str, Any]): The evaluation result for a query.
    """
    console.print(f"\n[bold]Query {result['query_number']}: {result['query']}[/bold]")
    
    console.print("\n[bold]Response:[/bold]")
    console.print(result['response'])
    
    console.print("\n[bold]Source Nodes:[/bold]")
    for node in result['source_nodes']:
        console.print(str(node))
    
    console.print("\n[bold]Evaluation Results:[/bold]")
    console.print(f"Faithfulness: {result['faithfulness_score']:.2f} ({'Pass' if result['faithfulness_passing'] else 'Fail'})")
    console.print(f"Relevancy: {result['relevancy_score']:.2f}")
    console.print(f"Number of Source Nodes: {result['num_source_nodes']}")
    console.print(f"Query Runtime: {result['query_runtime']:.2f} seconds")
    
    console.print("\n" + "─" * 80 + "\n")

def print_summary_tables(evaluation_data):
    console.print("\n[bold]Evaluation Summary[/bold]\n")
    summary_table = Table(show_header=True, header_style="bold")
    summary_table.add_column("Metric", style="cyan")
    summary_table.add_column("Value", justify="right")
    summary_table.add_row("Average Faithfulness", f"{sum(r['faithfulness_score'] for r in evaluation_data['results']) / len(evaluation_data['results']):.2f}")
    summary_table.add_row("Average Relevancy", f"{sum(r['relevancy_score'] for r in evaluation_data['results']) / len(evaluation_data['results']):.2f}")
    summary_table.add_row("Average Number of Source Nodes", f"{sum(r['num_source_nodes'] for r in evaluation_data['results']) / len(evaluation_data['results']):.2f}")
    summary_table.add_row("Average Query Runtime (s)", f"{evaluation_data['avg_runtime']:.2f}")
    console.print(summary_table)

    console.print("\n[bold]Detailed Summary Table[/bold]\n")
    detailed_table = Table(show_header=True, header_style="bold")
    detailed_table.add_column("Query", style="cyan")
    detailed_table.add_column("Faithfulness", justify="right")
    detailed_table.add_column("Relevancy", justify="right")
    detailed_table.add_column("# Source Nodes", justify="right")
    detailed_table.add_column("Runtime (s)", justify="right")
    for result in evaluation_data["results"]:
        detailed_table.add_row(
            result['query'],
            f"{'✅' if result['faithfulness_passing'] else '❌'} {result['faithfulness_score']:.2f}",
            f"{result['relevancy_score']:.2f}",
            str(result['num_source_nodes']),
            f"{result['query_runtime']:.2f}"
        )
    console.print(detailed_table)

async def main():
    """
    Main function to run the evaluation process.
    """
    parser = argparse.ArgumentParser(description="Evaluate search queries")
    parser.add_argument("--queries", default="evals/test_queries.json", help="Path to the test queries JSON file")
    args = parser.parse_args()

    persist_dir = "./persist_dir"  # Adjust this path as needed
    query_engine, query_engine_params = await get_query_engine(persist_dir, eval_mode=True)
    
    test_queries = load_test_queries(args.queries)
    
    evaluation_data = await evaluate_queries(query_engine, test_queries)
    print_summary_tables(evaluation_data)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"evals/results/results_{timestamp}.md"
    write_evaluation_report(evaluation_data, query_engine_params, filename)
    console.print(f"\nResults written to {filename}")

if __name__ == "__main__":
    asyncio.run(main())