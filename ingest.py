from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import AzureOpenAIEmbeddings
import os

import utils.azure_monitor
from utils.logger import logger

from config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    EMBEDDING_DEPLOYMENT,
    CHROMA_DB_DIR,
    DATA_DIR
)

try:

    logger.info("========== Document Ingestion Started ==========")

    pdf_path = os.path.join(DATA_DIR, "company_policy.pdf")

    logger.info(f"Loading PDF from: {pdf_path}")

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    logger.info(f"Successfully loaded {len(documents)} page(s).")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    logger.info(
        "Splitting document into chunks "
        "(chunk_size=1000, overlap=200)."
    )

    chunks = splitter.split_documents(documents)

    logger.info(f"Created {len(chunks)} document chunks.")

    logger.info(
        f"Initializing Azure OpenAI Embedding deployment: "
        f"{EMBEDDING_DEPLOYMENT}"
    )

    embeddings = AzureOpenAIEmbeddings(
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_API_KEY,
        api_version=AZURE_OPENAI_API_VERSION,
        azure_deployment=EMBEDDING_DEPLOYMENT,
    )

    logger.info("Embedding model initialized successfully.")

    logger.info("Creating Chroma vector database...")

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DB_DIR
    )

    logger.info(
        f"Vector database successfully stored at: {CHROMA_DB_DIR}"
    )

    logger.info("========== Document Ingestion Completed ==========")

except Exception:

    logger.exception("Document ingestion failed.")

    raise