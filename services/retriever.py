from langchain_chroma import Chroma
from langchain_openai import AzureOpenAIEmbeddings
from utils.logger import logger

from config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    EMBEDDING_DEPLOYMENT,
    CHROMA_DB_DIR,
)

logger.info("Initializing Azure OpenAI embedding model.")

embeddings = AzureOpenAIEmbeddings(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_deployment=EMBEDDING_DEPLOYMENT,
)

logger.info("Embedding model initialized successfully.")

logger.info(
    f"Loading Chroma vector database from: {CHROMA_DB_DIR}"
)

db = Chroma(
    persist_directory=CHROMA_DB_DIR,
    embedding_function=embeddings,
)

logger.info("Vector database loaded successfully.")


def get_retriever():

    logger.info("Creating retriever instance.")

    retriever = db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4},
    )

    logger.info("Retriever created successfully.")

    return retriever


if __name__ == "__main__":

    logger.info("Running retriever standalone test.")

    retriever = get_retriever()

    docs = retriever.invoke(
        "What is the company's leave policy?"
    )

    logger.info(
        f"Standalone retrieval returned {len(docs)} chunks."
    )

    print(f"Retrieved {len(docs)} chunks\n")

    for i, doc in enumerate(docs, start=1):
        print("=" * 70)
        print(f"Chunk {i}")
        print("=" * 70)
        print(doc.page_content)
        print()

    logger.info("Standalone retriever test completed successfully.")