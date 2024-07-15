import asyncio
from typing import List, Dict, Any
from search.query_engine import get_query_engine
from llama_index.core.evaluation import FaithfulnessEvaluator, RelevancyEvaluator
from llama_index.llms.openai import OpenAI
from base import BaseConfig
import logging
from rich.console import Console
from rich.table import Table

config = BaseConfig("evaluation", log_level=logging.DEBUG)
logger = logging.getLogger("evaluation")
console = Console()

async def evaluate_queries(query_engine, queries: List[str]) -> List[Dict[str, Any]]:
    results = []
    faithfulness_evaluator = FaithfulnessEvaluator(llm=OpenAI(model="gpt-4", temperature=0))
    relevancy_evaluator = RelevancyEvaluator(llm=OpenAI(model="gpt-4", temperature=0))

    for i, query in enumerate(queries, 1):
        logger.debug(f"Processing query {i}: {query}")
        
        response = await query_engine.aquery(query)
        logger.debug(f"Raw response: {response}")
        
        contexts = [node.node.get_content() for node in response.source_nodes]
        
        # Evaluate faithfulness
        faithfulness_result = await faithfulness_evaluator.aevaluate(
            query=query,
            response=str(response),
            contexts=contexts
        )
        
        # Evaluate relevancy
        relevancy_result = await relevancy_evaluator.aevaluate(
            query=query,
            response=str(response),
            contexts=contexts
        )
        
        results.append({
            "query": query,
            "response": str(response),
            "faithfulness_score": faithfulness_result.score,
            "faithfulness_passing": faithfulness_result.passing,
            "relevancy_score": relevancy_result.score,
            "num_source_nodes": len(response.source_nodes),
        })
        
        logger.debug(f"Evaluation results for query {i}:")
        logger.debug(f"Faithfulness: {faithfulness_result.score:.2f} ({'Pass' if faithfulness_result.passing else 'Fail'})")
        logger.debug(f"Relevancy: {relevancy_result.score:.2f}")
        logger.debug(f"Number of source nodes: {len(response.source_nodes)}")
        
    return results

def print_summary(results: List[Dict[str, Any]]):
    table = Table(title="Evaluation Summary")
    
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
    logging.basicConfig(level=logging.DEBUG)
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