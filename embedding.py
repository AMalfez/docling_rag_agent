# import
import chromadb.utils.embedding_functions as embedding_functions
import chromadb
import os
from dotenv import load_dotenv
load_dotenv()

chroma_client = chromadb.PersistentClient(path="./chroma_db")

def create_chroma_db(name):
  try:
    google_ef  = embedding_functions.GoogleGenerativeAiEmbeddingFunction(api_key=os.getenv("GOOGLE_GENAI_API_KEY"), model_name="gemini-embedding-001")
    db = chroma_client.create_collection(
        name=name,
        embedding_function=google_ef
    )
    return db
  
  except Exception as e:
    print(f"An error occurred while creating the database: {str(e)}")
    return None

def get_db(name):
  try:
    db = chroma_client.get_collection(name=name)
    return db
  except Exception as e:
    print(f"An error occurred while accessing the database: {str(e)}")
    return None
