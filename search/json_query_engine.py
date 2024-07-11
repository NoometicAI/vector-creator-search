import logging
import sys
import json
from pathlib import Path
from jsonpath_ng import parse

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

import os
import openai
import dotenv; dotenv.load_dotenv()

# openai key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# load in first 10 records of data from index/tiktok_store.json
def load_sample_json(file_path: str, num_records: int = 10):
    data = []
    try:
        with open(file_path, "r") as f:
            json_data = json.load(f)
            if isinstance(json_data, list):
                data = json_data[:num_records]
            elif isinstance(json_data, dict):
                data = [json_data]
            else:
                raise ValueError("Unexpected JSON structure")
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON: {e}")
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    
    return data

# Load the sample data
json_data = load_sample_json("index/tiktok_store.json", 100)

print('------\n\nprinting sample:\n\n------')
print(json_data)
print('------\n\n------')

def load_json_schema(file_path: str) -> dict:
    print(f"Attempting to load schema from: {file_path}")  # Add this line
    try:
        with open(file_path, 'r') as schema_file:
            return json.load(schema_file)
    except FileNotFoundError:
        logging.error(f"JSON schema file not found: {file_path}")
        return {}
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON schema file: {file_path}")
        return {}
    except Exception as e:
        logging.error(f"Error loading JSON schema: {e}")
        return {}

# Get the directory of the current script
current_dir = Path(__file__).parent.resolve()
print(f"Current directory: {current_dir}")  # Add this line

# Construct the path to the JSON schema file
schema_path = current_dir / "tiktok_user_schema.json"
print(f"Full schema path: {schema_path}")  # Add this line

# Load the JSON schema
json_schema = load_json_schema(str(schema_path))

if not json_schema:
    logging.warning("JSON schema not loaded. Using an empty schema.")
    json_schema = {}  # Provide a default empty schema


from llama_index.llms.openai import OpenAI
from llama_index.core.indices.struct_store import JSONQueryEngine

llm = OpenAI(model="gpt-4")

nl_query_engine = JSONQueryEngine(
    json_value=json_data,
    json_schema=json_schema,
    llm=llm,
)
raw_query_engine = JSONQueryEngine(
    json_value=json_data,
    json_schema=json_schema,
    llm=llm,
    synthesize_response=False,
)


query = "Which creators have the most followers?"

nl_response = nl_query_engine.query(
    query,
)
raw_response = raw_query_engine.query(
    query,
)

print(f'NL Response: {nl_response}')
print(f'RAW Response: {raw_response}')

# Add this section to manually process the data
print("\nManual processing of data:")
sorted_creators = sorted(json_data, key=lambda x: x.get('followers', 0), reverse=True)
top_5_creators = sorted_creators[:5]
for creator in top_5_creators:
    print(f"Name: {creator['name']}, Followers: {creator['followers']}")

# Using jsonpath-ng
print("\nUsing jsonpath-ng:")
jsonpath_expr = parse('$[*]')
sorted_creators = sorted(jsonpath_expr.find(json_data), key=lambda match: match.value.get('followers', 0), reverse=True)
top_5_creators = sorted_creators[:5]
for match in top_5_creators:
    creator = match.value
    print(f"Name: {creator['name']}, Followers: {creator['followers']}")