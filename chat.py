from openai import AzureOpenAI

from retriever import get_retriever

from config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_API_VERSION,
    CHAT_DEPLOYMENT,
)

client = AzureOpenAI(
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
)

retriever = get_retriever()


def ask_question(question: str):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
You are an Enterprise Knowledge Assistant.

Your job is to answer ONLY from the provided context.

If the answer is not available in the context, reply:

"I couldn't find this information in the uploaded company documents."

Do not make up answers.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model=CHAT_DEPLOYMENT,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ]
    )
    
    return {
        "answer": response.choices[0].message.content,
        "sources": docs
    }


