# Vector Creator Search

This project provides a FastAPI server for querying creator data using a custom query engine.

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/vector_creator_search.git
   cd vector_creator_search
   ```

2. Create a virtual environment:
   ```
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```
   - On Windows:
     ```
     venv\Scripts\activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```


5. Set up environment variables:
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Running the Server

1. Start the FastAPI server:
   ```
   python main.py
   ```
   The server will start running on `http://0.0.0.0:9090`.

## Making a Query

You can test the API using curl. Here's an example:
    ```
    curl -X POST "http://localhost:9090/query" \
    -H "Content-Type: application/json" \
    -d '{"query": "Find gaming influencers"}'
    ```


## Running Evals

Evals will run the search and evaluate the results. A report will print to the console. You can update the queries to evaluation queries in the `evals/evaluate_search.py` file.
   ```
   python -m evals.evaluate_search
   ```