"""
This module provides custom parsing functions for extracting document relevance
scores and choices from query responses.
"""

from llama_index.core.postprocessor import SentenceTransformerRerank
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.core.indices.utils import default_parse_choice_select_answer_fn
from typing import List, Tuple

def custom_parse_choice_select_answer_fn(answer: str, num_choices: int):
    """
    Custom parser for extracting choices from an answer.

    Args:
        answer (str): The answer string to parse.
        num_choices (int): The number of choices to extract.

    Returns:
        List[int]: A list of extracted choices.
    """
    print('====>>', answer)
    _answer = answer.split('Explanation')[0]
    return default_parse_choice_select_answer_fn(_answer, num_choices)

# Make eval_parse_choice_select_answer_fn the same as custom_parse_choice_select_answer_fn
def eval_parse_choice_select_answer_fn(answer: str, num_choices: int):
    """
    boiler plate for now
    """
    print('====>>', answer)
    _answer = answer.split('Explanation')[0]
    return default_parse_choice_select_answer_fn(_answer, num_choices)