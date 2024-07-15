from llama_index.core.postprocessor import SentenceTransformerRerank
from llama_index.core.node_parser import SimpleNodeParser
from llama_index.core.indices.utils import default_parse_choice_select_answer_fn
from typing import List, Tuple


def custom_parse_choice_select_answer_fn(answer: str, num_choices: int):
    print('====>>', answer)
    _answer = answer.split('Explanation')[0]
    return default_parse_choice_select_answer_fn(_answer, num_choices)

def eval_parse_choice_select_answer_fn(answer: str, num_choices: int):
    print('====>>', answer)
    _answer = answer.split('Explanation')[0]
    return default_parse_choice_select_answer_fn(_answer, num_choices)