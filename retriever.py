from langchain_chroma import Chroma
from langchain_openai import AzureOpenAIEmbeddings

from config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    EMBEDDING_DEPLOYMENT,
    CHROMA_DB_DIR,
)

embeddings = AzureOpenAIEmbeddings(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_deployment=EMBEDDING_DEPLOYMENT,
)

db = Chroma(
    persist_directory=CHROMA_DB_DIR,
    embedding_function=embeddings,
)

# retriever = db.as_retriever(
#     search_type="similarity",
#     search_kwargs={"k": 4},
# )

def get_retriever():
    return db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4},
    )

if __name__ == "__main__":

    retriever = get_retriever()

    docs = retriever.invoke(
        "What is the company's leave policy?"
    )

    print(f"Retrieved {len(docs)} chunks\n")

    for i, doc in enumerate(docs, start=1):
        print("=" * 70)
        print(f"Chunk {i}")
        print("=" * 70)
        print(doc.page_content)
        print()