from langchain_ollama import OllamaLLM
from langchain_core.tools import tool
from rag_tool import search_documents

# llm = OllamaLLM(model="llama3")

llm = OllamaLLM(
    model="llama3",
    base_url="http://host.docker.internal:11434"
)

# @tool
# def calculator(expression: str):
#     """Perform mathematical calculations"""
#     return str(eval(expression))

# @tool
# def knowledge_base_search(query: str):
#     return search_documents(query)

# @tool
# def web_search(query: str):
#     """Search internet"""
#     return "Searching internet..."

@tool
def calculator(expression: str):
    """Perform mathematical calculations."""
    return str(eval(expression))


@tool
def knowledge_base_search(query: str):
    """Search company policy documents using the RAG knowledge base."""
    return search_documents(query)

tools = [
    calculator,
    knowledge_base_search,
]

# question = input("Ask: ")

# if any(op in question for op in ["+", "-", "*", "/"]):
#     expression = question.lower().replace("calculate", "").strip()
#     print(calculator.invoke(expression))

# elif "policy" in question.lower():
#     print(knowledge_base_search.invoke(question))

# else:
#     print(web_search.invoke(question))

question = input("Ask: ")

if any(op in question for op in ["+", "-", "*", "/"]):

    try:
        print(eval(question))
    except:
        print("Invalid expression")

else:
    print(knowledge_base_search.invoke(question))





