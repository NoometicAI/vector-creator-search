"""
Module to read and parse data from PostgreSQL database.
Provides functions to fetch TikTok and Instagram data, save to JSON, and parse conversations.

Usage:
    python -m db.pgread export_all
    python -m db.pgread export_tiktok
    python -m db.pgread export_instagram
"""
import os
import argparse
import json
import ast
from decimal import Decimal
from datetime import date, datetime
import psycopg2
from db.pgconnect import get_db_connection

def fetch_data(table_name):
    """
    Fetch all data from the specified table.
    
    Args:
        table_name (str): Name of the table to fetch data from.
    
    Returns:
        list of dict: Fetched data as a list of dictionaries, or None if an error occurs.
    """
    print(f"Attempting to connect to the database to fetch {table_name} data...")
    try:
        conn = get_db_connection()
        print("Connection established successfully.")
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

    try:
        cur = conn.cursor()
        print(f"Executing query: SELECT * FROM {table_name}")
        cur.execute(f"SELECT * FROM {table_name}")
        rows = cur.fetchall()
        
        print(f"Fetched {len(rows)} rows from the {table_name} table.")
        
        # Get column names
        column_names = [desc[0] for desc in cur.description]
        
        # Convert rows to list of dictionaries
        data = [dict(zip(column_names, row)) for row in rows]
        
        cur.close()
        conn.close()
        print("Database connection closed.")
        
        return data
    except psycopg2.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")
    
    return None

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    if isinstance(obj, Decimal):
        return float(obj)
    if isinstance(obj, bytes):
        return obj.decode('utf-8')
    raise TypeError(f"Type {type(obj)} not serializable")

def save_data_to_json(data, filename):
    """Save data to a JSON file in the index/ folder."""
    # Get the current script's directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Go up one level to the parent directory
    parent_dir = os.path.dirname(current_dir)
    
    # Create the full path for the index/ folder
    index_dir = os.path.join(parent_dir, 'index')
    
    # Ensure the index/ folder exists
    os.makedirs(index_dir, exist_ok=True)
    
    # Full path for the JSON file
    file_path = os.path.join(index_dir, filename)
    
    print(f"Saving data to {file_path}...")
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2, default=json_serial)
        print(f"Data saved successfully to {file_path}")
    except TypeError as e:
        print(f"Error while saving data: {str(e)}")
        print("Attempting to identify problematic data...")
        for i, item in enumerate(data):
            try:
                json.dumps(item, default=json_serial)
            except TypeError as e:
                print(f"Error in item {i}: {str(e)}")
                print(f"Problematic item: {item}")
                break

def fetch_conversations():
    """Fetch all conversations from the database."""
    print("Connecting to the database...")
    conn = get_db_connection()
    cur = conn.cursor()
    
    print("Executing query...")
    cur.execute("SELECT * FROM convos")
    rows = cur.fetchall()
    
    print(f"Fetched {len(rows)} rows from the database.")
    
    cur.close()
    conn.close()
    
    return rows

def parse_conversation(row):
    """Parse a single conversation row from the database."""
    id, uuid, history_dict, timestamp = row
    
    return {
        "id": id,
        "uuid": uuid,
        "history": history_dict['history'],
        "timestamp": str(timestamp)  # Convert to string for JSON serialization
    }

def parse_user_queries(conversations):
    """Extract user queries from conversations."""
    user_queries = []
    for conv in conversations:
        for message in conv['history']:
            if message['role'] == 'user':
                user_queries.append(message['content'])
    return user_queries

def safe_eval(s):
    try:
        return ast.literal_eval(s)
    except:
        return s

def parse_tool_responses(conversations):
    """Extract all unique tool responses and additional creator info from conversations."""
    tool_responses = []
    total_messages = 0
    tool_messages = 0
    parsed_responses = 0
    seen_responses = set()  # To keep track of unique responses across all conversations

    for conv in conversations:
        for message in conv['history']:
            total_messages += 1
            if message['role'] == 'tool' and message.get('name') == 'creator_search':
                tool_messages += 1
                try:
                    # The content might already be a dictionary
                    if isinstance(message['content'], dict):
                        content = message['content']
                    else:
                        # If it's a string, try to parse it
                        content = safe_eval(message['content'])
                    
                    response = content.get('response', '')
                    if response and response not in seen_responses:
                        seen_responses.add(response)  # Mark this response as seen
                        parsed_responses += 1
                        # Extract information from the first source node
                        source_nodes = content.get('source_nodes', [])
                        if source_nodes:
                            metadata = source_nodes[0].get('node', {}).get('metadata', {})
                            
                            # Correctly parse the keys
                            keys_str = metadata.get('keys', '[]')
                            keys = safe_eval(keys_str) if isinstance(keys_str, str) else keys_str
                            
                            creator_info = {
                                'response': response,
                                'keys': keys,
                                'bio': metadata.get('bio', ''),
                                'avg_engagement': float(metadata.get('avg_engagement', 0)),
                                'platform': metadata.get('platform', '')
                            }
                        else:
                            # If no source nodes, just include the response
                            creator_info = {'response': response}
                        
                        tool_responses.append(creator_info)
                except Exception as e:
                    print(f"Error processing message: {str(e)}")
                    print(f"Problematic content: {str(message['content'])[:200]}...")

    print(f"Total messages processed: {total_messages}")
    print(f"Tool messages found: {tool_messages}")
    print(f"Unique responses parsed: {parsed_responses}")
    return tool_responses

def fetch_and_parse_conversations():
    """Fetch all conversations from the database and parse them."""
    raw_conversations = fetch_conversations()
    parsed_conversations = [parse_conversation(row) for row in raw_conversations]
    return parsed_conversations

def print_raw_data(data, limit=5):
    """Print raw data exactly as it is in the database."""
    for row in data[:limit]:
        print(json.dumps(row[2]))
        print()  # Add a blank line between rows for readability

def print_parsed_data(data, limit=5):
    """Print parsed data in a readable format."""
    print(f"\nShowing first {limit} parsed conversations:")
    for conv in data[:limit]:
        print(f"ID: {conv['id']}")
        print(f"UUID: {conv['uuid']}")
        print(f"History: {json.dumps(conv['history'], indent=2)[:200]}...")  # Truncate for readability
        print(f"Timestamp: {conv['timestamp']}")
        print("-" * 50)

def main():
    parser = argparse.ArgumentParser(description="Fetch and save data from the database.")
    parser.add_argument('command', choices=['export_all', 'export_tiktok', 'export_instagram'],
                        help='Command to execute')
    args = parser.parse_args()

    if args.command == 'export_all' or args.command == 'export_tiktok':
        print("Fetching TikTok data...")
        tiktok_data = fetch_data('tiktok_final')
        if tiktok_data:
            save_data_to_json(tiktok_data, 'tiktok_store.json')
        else:
            print("Failed to fetch TikTok data.")

    if args.command == 'export_all' or args.command == 'export_instagram':
        print("Fetching Instagram data...")
        instagram_data = fetch_data('instagram_final')
        if instagram_data:
            save_data_to_json(instagram_data, 'instagram_store.json')
        else:
            print("Failed to fetch Instagram data.")

if __name__ == "__main__":
    main()