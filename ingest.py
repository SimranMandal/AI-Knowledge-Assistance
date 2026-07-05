from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
#from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_openai import AzureOpenAIEmbeddings
from dotenv import load_dotenv
import os
from langchain_community.vectorstores import Chroma

load_dotenv()

loader = PyPDFLoader("data/company_policy.pdf")

documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)

print(f"Number of chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
for i, chunk in enumerate(chunks):
    print(f"\n========== CHUNK {i+1} ==========\n")
    print(chunk.page_content)

# embeddings = HuggingFaceEmbeddings(
#     model_name="all-MiniLM-L6-v2"
# )

embeddings = AzureOpenAIEmbeddings(
    azure_deployment=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)

print("Embedding model loaded successfully")

db = Chroma.from_documents(
    chunks,
    embeddings,
    persist_directory="chroma_db"
)

db.persist()