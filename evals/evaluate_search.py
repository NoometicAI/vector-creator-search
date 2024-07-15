import asyncio
from typing import List, Dict, Any
from search.query_engine import get_query_engine
from llama_index.core.evaluation import FaithfulnessEvaluator, RelevancyEvaluator
from llama_index.llms.ollama import Ollama
from llama_index.llms.openai import OpenAI
from base import BaseConfig
import logging
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# Configure logging
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("evaluation")
logger.setLevel(logging.INFO)

# Silence specific loggers that are too verbose
logging.getLogger("openai").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)

console = Console()

# EVAL_LLM = Ollama(model="llama3", request_timeout=360.0, temperature=0)
EVAL_LLM = OpenAI(model="gpt-4", temperature=0)

async def evaluate_queries(query_engine, queries: List[str]) -> List[Dict[str, Any]]:
    results = []
    faithfulness_evaluator = FaithfulnessEvaluator(llm=EVAL_LLM)
    relevancy_evaluator = RelevancyEvaluator(llm=EVAL_LLM)

    for i, query in enumerate(queries, 1):
        console.print(f"\n[bold cyan]Query {i}:[/bold cyan] {query}")
        
        response = await query_engine.aquery(query)
        console.print(Panel(str(response), title="Response", expand=False))
        
        contexts = [node.node.get_content() for node in response.source_nodes]
        
        console.print("[bold magenta]Source Nodes:[/bold magenta]")
        for j, context in enumerate(contexts, 1):
            console.print(f"[bold]Node {j}:[/bold]\n{context}\n")
        
        faithfulness_result = await faithfulness_evaluator.aevaluate(
            query=query,
            response=str(response),
            contexts=contexts
        )
        
        relevancy_result = await relevancy_evaluator.aevaluate(
            query=query,
            response=str(response),
            contexts=contexts
        )
        
        console.print(Panel(f"[bold green]Faithfulness:[/bold green] {faithfulness_result.score:.2f} ({'Pass' if faithfulness_result.passing else 'Fail'})\n"
                            f"[bold]Explanation:[/bold] {faithfulness_result.feedback}\n\n"
                            f"[bold green]Relevancy:[/bold green] {relevancy_result.score:.2f}\n"
                            f"[bold]Explanation:[/bold] {relevancy_result.feedback}",
                            title="Evaluation Results", expand=False))
        
        results.append({
            "query": query,
            "response": str(response),
            "faithfulness_score": faithfulness_result.score,
            "faithfulness_passing": faithfulness_result.passing,
            "faithfulness_feedback": faithfulness_result.feedback,
            "relevancy_score": relevancy_result.score,
            "relevancy_feedback": relevancy_result.feedback,
            "num_source_nodes": len(response.source_nodes),
        })
        
        console.print("─" * 80)
        
    return results

def print_summary(results: List[Dict[str, Any]]):
    console.print("\n[bold underline]Evaluation Summary[/bold underline]\n")
    
    table = Table(title="Query Results")
    
    table.add_column("Query", style="cyan")
    table.add_column("Faithfulness", style="magenta")
    table.add_column("Relevancy", style="green")
    table.add_column("# Source Nodes", style="yellow")
    
    for result in results:
        table.add_row(
            result["query"][:50] + "..." if len(result["query"]) > 50 else result["query"],
            f"{'✅' if result['faithfulness_passing'] else '❌'} {result['faithfulness_score']:.2f}",
            f"{result['relevancy_score']:.2f}",
            str(result['num_source_nodes'])
        )
    
    console.print(table)
    
    avg_faithfulness = sum(r["faithfulness_score"] for r in results) / len(results)
    avg_relevancy = sum(r["relevancy_score"] for r in results) / len(results)
    avg_source_nodes = sum(r["num_source_nodes"] for r in results) / len(results)
    
    console.print(f"\n[bold]Average Faithfulness Score:[/bold] {avg_faithfulness:.2f}")
    console.print(f"[bold]Average Relevancy Score:[/bold] {avg_relevancy:.2f}")
    console.print(f"[bold]Average Number of Source Nodes:[/bold] {avg_source_nodes:.2f}")

async def main():
    persist_dir = "./persist_dir"  # Adjust this path as needed
    query_engine = await get_query_engine(persist_dir, eval_mode=True)
    
    test_queries = [
        "find gaming creators",
        "who are the top beauty influencers?",
        "list some popular tech reviewers",
        "what are the trending fashion channels?",
        "recommend some cooking YouTubers"
    ]
    
    results = await evaluate_queries(query_engine, test_queries)
    print_summary(results)

if __name__ == "__main__":
    asyncio.run(main())