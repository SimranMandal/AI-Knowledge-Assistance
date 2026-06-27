from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

llm = OllamaLLM(
    model="llama3",
    base_url="http://host.docker.internal:11434"
)

def search_documents(question):

    docs = db.similarity_search(question, k=3)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
Answer only using the provided context.

Context:
{context}

Question:
{question}
"""

    return llm.invoke(prompt)