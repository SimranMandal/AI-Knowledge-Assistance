from openai import AzureOpenAI
from prompts.prompt_template import PROMPT_TEMPLATE
from services.retriever import get_retriever
from utils.logger import logger
import time

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

logger.info("Azure OpenAI client initialized.")

retriever = get_retriever()

logger.info("Retriever initialized successfully.")


def ask_question(question: str):

    overall_start = time.perf_counter()

    try:

        logger.info("========== New User Request ==========")
        logger.info(f"Question: {question}")

        retrieval_start = time.perf_counter()

        logger.info("Performing semantic search.")

        docs = retriever.invoke(question)

        retrieval_time = time.perf_counter() - retrieval_start

        logger.info(
            f"Retrieved {len(docs)} document chunk(s) "
            f"in {retrieval_time:.2f} seconds."
        )

        logger.info("Building context.")

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        logger.info(
            f"Context successfully created "
            f"({len(context)} characters)."
        )

        prompt = PROMPT_TEMPLATE.format(
            context=context,
            question=question
        )

        logger.info("Prompt generated successfully.")

        llm_start = time.perf_counter()

        logger.info(
            f"Calling Azure OpenAI deployment: {CHAT_DEPLOYMENT}"
        )

        response = client.chat.completions.create(
            model=CHAT_DEPLOYMENT,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ]
        )

        llm_time = time.perf_counter() - llm_start

        logger.info(
            f"Azure OpenAI responded in "
            f"{llm_time:.2f} seconds."
        )

        answer = response.choices[0].message.content

        logger.info(
            f"Generated answer "
            f"({len(answer)} characters)."
        )

        total_time = time.perf_counter() - overall_start

        logger.info(
            f"Total request completed "
            f"in {total_time:.2f} seconds."
        )

        return {
            "answer": answer,
            "sources": docs
        }

    except Exception:

        logger.exception(
            "Error occurred while processing the question."
        )

        raise