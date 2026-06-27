# # def ask_question(question):
# #     return f"You asked: {question}"

# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_ollama import OllamaLLM

# embeddings = HuggingFaceEmbeddings(
#     model_name="all-MiniLM-L6-v2"
# )

# db = Chroma(
#     persist_directory="chroma_db",
#     embedding_function=embeddings
# )

# llm = OllamaLLM(model="llama3")

# def ask_question(question):

#     docs = db.similarity_search(question, k=3)

#     context = "\n".join(
#         [doc.page_content for doc in docs]
#     )

#     prompt = f"""
# Answer the question using only the provided context.

# Context:
# {context}

# Question:
# {question}
# """

#     return llm.invoke(prompt)

# #for displaying the answer is from which pdf
# def ask_question(question):

#     docs = db.similarity_search(question)

#     for doc in docs:
#         print(doc.metadata)

    
# from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_ollama import OllamaLLM

# embeddings = HuggingFaceEmbeddings(
#     model_name="all-MiniLM-L6-v2"
# )

# db = Chroma(
#     persist_directory="chroma_db",
#     embedding_function=embeddings
# )

# llm = OllamaLLM(model="llama3")

# def ask_question(question):

#     docs = db.similarity_search(question, k=3)

#     # Print metadata in terminal
#     for doc in docs:
#         print(doc.metadata)

#     context = "\n".join(
#         [doc.page_content for doc in docs]
#     )

#     prompt = f"""
# You are a company policy assistant.

# Answer ONLY using the provided context.

# If the answer is not present in the context, reply exactly:

# "I could not find information about this in the provided documents."

# Context:
# {context}

# Question:
# {question}
# """

#     response = llm.invoke(prompt)

#     return response

from rag_tool import search_documents

def ask_question(question):
    return search_documents(question)