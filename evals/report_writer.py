"""
This module handles the generation of evaluation reports, both for console output and file writing.
It provides functions to format and present evaluation results in a clear and structured manner.
"""

import os
from datetime import datetime
from typing import List, Dict, Any
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def write_evaluation_report(evaluation_data: Dict[str, Any], query_engine_params: Dict[str, Any], filename: str):
    """
    Write the complete evaluation report to a Markdown file.

    Args:
        evaluation_data (Dict[str, Any]): A dictionary containing evaluation results and summary statistics.
        query_engine_params (Dict[str, Any]): A dictionary containing query engine parameters.
        filename (str): The name of the file to write the report to.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, "w") as f:
        write_metadata(f, evaluation_data, query_engine_params)
        write_parameters(f, query_engine_params)
        write_summary_table(f, evaluation_data["results"])
        write_detailed_summary_table(f, evaluation_data["results"])
        write_metric_definitions(f)
        write_detailed_results(f, evaluation_data["results"])

def write_metadata(f, evaluation_data: Dict[str, Any], query_engine_params: Dict[str, Any]):
    """Write metadata section of the report."""
    f.write("# Evaluation Report\n\n")
    f.write("## Metadata\n\n")
    f.write(f"- **Timestamp:** {datetime.now().isoformat()}\n")
    f.write(f"- **Number of Queries Run:** {len(evaluation_data['results'])}\n")
    f.write(f"- **Total Documents Retrieved:** {evaluation_data['total_docs_retrieved']}\n")
    f.write(f"- **Average Query Runtime:** {evaluation_data['avg_runtime']:.2f} seconds\n")
    f.write(f"- **Total Runtime:** {evaluation_data['total_runtime']:.2f} seconds\n")
    f.write(f"- **Index Load Time:** {evaluation_data['index_load_time']:.2f} seconds\n\n")

def write_parameters(f, query_engine_params: Dict[str, Any]):
    """Write query engine parameters section of the report."""
    f.write("## Query Engine Parameters\n\n")
    for key, value in query_engine_params.items():
        f.write(f"- **{key}:** {value}\n")
    f.write("\n")

def write_summary_table(f, results: List[Dict[str, Any]]):
    """Write summary table section of the report."""
    f.write("## Summary Table\n\n")
    f.write("| Metric | Value |\n")
    f.write("|--------|-------|\n")
    f.write(f"| Average Faithfulness | {sum(r['faithfulness_score'] for r in results) / len(results):.2f} |\n")
    f.write(f"| Average Relevancy | {sum(r['relevancy_score'] for r in results) / len(results):.2f} |\n")
    f.write(f"| Average Number of Source Nodes | {sum(r['num_source_nodes'] for r in results) / len(results):.2f} |\n")
    f.write(f"| Average Query Runtime (s) | {sum(r['query_runtime'] for r in results) / len(results):.2f} |\n\n")

def write_detailed_summary_table(f, results: List[Dict[str, Any]]):
    """Write detailed summary table section of the report."""
    f.write("## Detailed Summary Table\n\n")
    f.write("| Query | Faithfulness | Relevancy | # Source Nodes | Runtime (s) |\n")
    f.write("|-------|--------------|-----------|----------------|-------------|\n")
    for result in results:
        f.write(f"| {result['query']} | {'✅' if result['faithfulness_passing'] else '❌'} {result['faithfulness_score']:.2f} | {result['relevancy_score']:.2f} | {result['num_source_nodes']} | {result['query_runtime']:.2f} |\n")
    f.write("\n")

def write_metric_definitions(f):
    """Write metric definitions section of the report."""
    f.write("## Metric Definitions\n\n")
    f.write("- **Faithfulness:** Measures how well the response aligns with the information provided in the source documents. A score of 1.0 indicates perfect alignment, while 0.0 suggests significant deviation.\n")
    f.write("- **Relevancy:** Assesses how relevant the response is to the given query. A score of 1.0 indicates high relevance, while 0.0 suggests the response is off-topic or unrelated.\n")
    f.write("- **Source Nodes:** The number of documents or text chunks retrieved and used to generate the response.\n")
    f.write("- **Runtime:** The time taken to process the query and generate a response, measured in seconds.\n\n")

def write_detailed_results(f, results: List[Dict[str, Any]]):
    """Write detailed query results section of the report."""
    f.write("## Detailed Query Results\n\n")
    for i, result in enumerate(results, 1):
        f.write(f"### Query {i}: {result['query']}\n\n")
        f.write(f"**Response:**\n\n{result['response']}\n\n")
        
        f.write("**Source Nodes:**\n\n")
        for j, node in enumerate(result['source_nodes'], 1):
            f.write(f"Node {j}:\n")
            f.write("```\n")
            f.write(f"Node ID: {node.node.id_}\n")
            f.write(f"Text: {node.node.text[:500]}...(truncated)\n")  # Truncate long texts
            f.write("Metadata:\n")
            for key, value in node.node.metadata.items():
                if isinstance(value, str) and len(value) > 100:
                    value = value[:100] + "...(truncated)"
                f.write(f"  {key}: {value}\n")
            f.write(f"Score: {node.score:.3f}\n")
            f.write("```\n\n")
        
        f.write("**Evaluation Results:**\n\n")
        f.write(f"- Faithfulness: {result['faithfulness_score']:.2f} ({'Pass' if result['faithfulness_passing'] else 'Fail'})\n")
        f.write(f"  - Explanation: {result['faithfulness_feedback']}\n")
        f.write(f"- Relevancy: {result['relevancy_score']:.2f}\n")
        f.write(f"  - Explanation: {result['relevancy_feedback']}\n")
        f.write(f"- Number of Source Nodes: {result['num_source_nodes']}\n")
        f.write(f"- Query Runtime: {result['query_runtime']:.2f} seconds\n\n")

def print_query_result(result: Dict[str, Any]):
    """
    Print the evaluation result for a single query to the console.

    Args:
        result (Dict[str, Any]): The evaluation result for a query.
    """
    console.print("\n" + "─" * 80 + "\n")
    
    console.print(f"[bold]Query {result['query_number']}: {result['query']}[/bold]\n")
    
    console.print("[bold]Response:[/bold]")
    console.print(result['response'])
    console.print()
    
    console.print("[bold]Source Nodes:[/bold]")
    for i, node in enumerate(result['source_nodes'], 1):
        console.print(Panel(
            f"Node ID: {node.node.id_}\n"
            f"Text: {node.node.text[:200]}...(truncated)\n"
            f"Score: {node.score:.3f}",
            title=f"Node {i}",
            expand=False
        ))
    console.print()
    
    console.print("[bold]Evaluation Results:[/bold]")
    console.print(f"Faithfulness: {result['faithfulness_score']:.2f} ({'Pass' if result['faithfulness_passing'] else 'Fail'})")
    console.print(f"Relevancy: {result['relevancy_score']:.2f}")
    console.print(f"Number of Source Nodes: {result['num_source_nodes']}")
    console.print(f"Query Runtime: {result['query_runtime']:.2f} seconds")
    
    console.print("\n" + "─" * 80)

def print_summary_tables(evaluation_data: Dict[str, Any]):
    """
    Print summary tables of the evaluation results to the console.

    Args:
        evaluation_data (Dict[str, Any]): A dictionary containing evaluation results and summary statistics.
    """
    console.print("\n[bold]Evaluation Summary[/bold]\n")
    summary_table = Table(show_header=True, header_style="bold")
    summary_table.add_column("Metric", style="cyan")
    summary_table.add_column("Value", justify="right")
    summary_table.add_row("Average Faithfulness", f"{sum(r['faithfulness_score'] for r in evaluation_data['results']) / len(evaluation_data['results']):.2f}")
    summary_table.add_row("Average Relevancy", f"{sum(r['relevancy_score'] for r in evaluation_data['results']) / len(evaluation_data['results']):.2f}")
    summary_table.add_row("Average Number of Source Nodes", f"{sum(r['num_source_nodes'] for r in evaluation_data['results']) / len(evaluation_data['results']):.2f}")
    summary_table.add_row("Average Query Runtime (s)", f"{evaluation_data['avg_runtime']:.2f}")
    summary_table.add_row("Index Load Time (s)", f"{evaluation_data['index_load_time']:.2f}")
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