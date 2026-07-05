from dotenv import load_dotenv
from langchain_openai import AzureOpenAIEmbeddings
import os

load_dotenv()

embeddings = AzureOpenAIEmbeddings(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_deployment=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)

result = embeddings.embed_query("Hello World")

print("Success!")
print("Embedding length:", len(result))
print(result[:10])