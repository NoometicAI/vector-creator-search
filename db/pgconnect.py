"""
Module to establish and test PostgreSQL database connections.

Usage:
    python -m db.pgconnect
"""
import os
import dotenv
import psycopg2

dotenv.load_dotenv()

def get_db_connection():
    """
    Establish and return a database connection.
    
    Returns:
        psycopg2.connection: A database connection object.
    
    Raises:
        Exception: If connection fails.
    """
    print("Attempting to connect to the database...")
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("PG_DATABASE"),
            user=os.getenv("PG_USER"),
            password=os.getenv("PG_PASSWORD"),
            host=os.getenv("PG_HOST"),
            port=os.getenv("PG_PORT")
        )
        print("Database connection established successfully.")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        raise

def test_connection():
    """
    Test the database connection.
    
    Returns:
        bool: True if connection is successful, False otherwise.
    """
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
                result = cur.fetchone()
        print("Database connection test successful.")
        return result[0] == 1
    except Exception as e:
        print(f"Connection test failed: {e}")
        return False

if __name__ == "__main__":
    if test_connection():
        print("Database connection successful!")
    else:
        print("Database connection failed.")