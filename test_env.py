from dotenv import load_dotenv
import os

load_dotenv()

print("Endpoint:", os.getenv("AZURE_OPENAI_ENDPOINT"))
print("Embedding:", os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"))
print("Chat:", os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT"))
print("API Version:", os.getenv("AZURE_OPENAI_API_VERSION"))