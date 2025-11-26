from dotenv import load_dotenv
import os
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider
from pydantic_ai import Agent, Tool
from tools.search_knowledge_base import search_knowledge_base
load_dotenv()

provider = GoogleProvider(api_key=os.getenv("GOOGLE_GENAI_API_KEY"))
model = GoogleModel('gemini-2.5-flash', provider=provider)

system_prompt = (
    'You are a helpful assistant. Use the tools provided to answer user queries based on the knowledge base.'
    'If you cannot find the answer in the knowledge base, respond with "I do not know."'
)

agent = Agent(model, system_prompt=system_prompt, tools=[Tool(search_knowledge_base)])

query = input("Enter your question: ")

print("\nAgent Called...\n")
res = agent.run_sync(query)

print(f"{res.output}\n")