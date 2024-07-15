import os
from datetime import datetime
from typing import List, Dict, Any

def write_evaluation_report(evaluation_data: Dict[str, Any], query_engine_params: Dict[str, Any], filename: str):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, "w") as f:
        write_metadata(f, evaluation_data, query_engine_params)
        write_parameters(f, query_engine_params)
        write_summary_table(f, evaluation_data["results"])
        write_detailed_summary_table(f, evaluation_data["results"])
        write_metric_definitions(f)
        write_detailed_results(f, evaluation_data["results"])

def write_metadata(f, evaluation_data: Dict[str, Any], query_engine_params: Dict[str, Any]):
    f.write("# Evaluation Report\n\n")
    f.write("## Metadata\n\n")
    f.write(f"- **Timestamp:** {datetime.now().isoformat()}\n")
    f.write(f"- **Number of Queries Run:** {len(evaluation_data['results'])}\n")
    f.write(f"- **Total Documents Retrieved:** {evaluation_data['total_docs_retrieved']}\n")
    f.write(f"- **Average Query Runtime:** {evaluation_data['avg_runtime']:.2f} seconds\n")
    f.write(f"- **Total Runtime:** {evaluation_data['total_runtime']:.2f} seconds\n\n")

def write_parameters(f, query_engine_params: Dict[str, Any]):
    f.write("## Query Engine Parameters\n\n")
    for key, value in query_engine_params.items():
        f.write(f"- **{key}:** {value}\n")
    f.write("\n")

def write_summary_table(f, results: List[Dict[str, Any]]):
    f.write("## Summary Table\n\n")
    f.write("| Metric | Value |\n")
    f.write("|--------|-------|\n")
    f.write(f"| Average Faithfulness | {sum(r['faithfulness_score'] for r in results) / len(results):.2f} |\n")
    f.write(f"| Average Relevancy | {sum(r['relevancy_score'] for r in results) / len(results):.2f} |\n")
    f.write(f"| Average Number of Source Nodes | {sum(r['num_source_nodes'] for r in results) / len(results):.2f} |\n")
    f.write(f"| Average Query Runtime (s) | {sum(r['query_runtime'] for r in results) / len(results):.2f} |\n\n")

def write_detailed_summary_table(f, results: List[Dict[str, Any]]):
    f.write("## Detailed Summary Table\n\n")
    f.write("| Query | Faithfulness | Relevancy | # Source Nodes | Runtime (s) |\n")
    f.write("|-------|--------------|-----------|----------------|-------------|\n")
    for result in results:
        f.write(f"| {result['query']} | {'✅' if result['faithfulness_passing'] else '❌'} {result['faithfulness_score']:.2f} | {result['relevancy_score']:.2f} | {result['num_source_nodes']} | {result['query_runtime']:.2f} |\n")
    f.write("\n")

def write_metric_definitions(f):
    f.write("## Metric Definitions\n\n")
    f.write("- **Faithfulness:** Measures how well the response aligns with the information provided in the source documents. A score of 1.0 indicates perfect alignment, while 0.0 suggests significant deviation.\n")
    f.write("- **Relevancy:** Assesses how relevant the response is to the given query. A score of 1.0 indicates high relevance, while 0.0 suggests the response is off-topic or unrelated.\n")
    f.write("- **Source Nodes:** The number of documents or text chunks retrieved and used to generate the response.\n")
    f.write("- **Runtime:** The time taken to process the query and generate a response, measured in seconds.\n\n")

def write_detailed_results(f, results: List[Dict[str, Any]]):
    f.write("## Detailed Query Results\n\n")
    for i, result in enumerate(results, 1):
        f.write(f"### Query {i}: {result['query']}\n\n")
        f.write(f"**Response:**\n\n{result['response']}\n\n")
        f.write("**Source Nodes:**\n\n")
        for j, node in enumerate(result['source_nodes'], 1):
            f.write(f"Node {j}:\n```\n{node}\n```\n\n")
        f.write("**Evaluation Results:**\n\n")
        f.write(f"- Faithfulness: {result['faithfulness_score']:.2f} ({'Pass' if result['faithfulness_passing'] else 'Fail'})\n")
        f.write(f"  - Explanation: {result['faithfulness_feedback']}\n")
        f.write(f"- Relevancy: {result['relevancy_score']:.2f}\n")
        f.write(f"  - Explanation: {result['relevancy_feedback']}\n")
        f.write(f"- Number of Source Nodes: {result['num_source_nodes']}\n")
        f.write(f"- Query Runtime: {result['query_runtime']:.2f} seconds\n\n")