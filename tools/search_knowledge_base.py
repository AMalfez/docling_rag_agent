from embedding import get_db
from dotenv import load_dotenv
load_dotenv()

def search_knowledge_base(query, db_name="test_db", n_results=3):
    """
    Search the knowledge base using semantic similarity.

    Args:
        query: The search query to find relevant information
        db_name: name of vector database collection (default is "test_db")
        n_results: number of top results to return (default is 3)

    Returns:
        Relevant results from the knowledge base
    """

    try:
        print("\Searching relevant info...\n")

        db = get_db(db_name)

        results = db.query(
            query_texts=[query],
            n_results=n_results
        )

        # Format results for response
        if not results:
            return "No relevant information found in the knowledge base for your query."

        return results
    
    except Exception as e:
        return f"An error occurred while searching the knowledge base: {str(e)}"