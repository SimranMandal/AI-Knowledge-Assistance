import streamlit as st
from services.chat_service import ask_question
import utils.azure_monitor
from utils.logger import logger

logger.info("========== Enterprise Knowledge Assistant Started ==========")

st.set_page_config(
    page_title="Enterprise Knowledge Assistant",
    page_icon="📚",
    layout="wide",
)

logger.info("Streamlit page configuration completed.")

st.title("📚 Enterprise Knowledge Assistant")
st.write("Ask questions about your company documents.")

logger.info("User interface loaded successfully.")

if "messages" not in st.session_state:
    st.session_state.messages = []
    logger.info("Initialized chat session state.")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask a question...")

if question:

    logger.info(f"Received user question: {question}")

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    try:

        logger.info("Sending question to chat service.")

        with st.spinner("Searching documents..."):
            result = ask_question(question)

        logger.info("Response successfully received from chat service.")

        answer = result["answer"]

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer,
            }
        )

        with st.chat_message("assistant"):
            st.markdown(answer)

        logger.info("Answer displayed successfully.")

        with st.expander("📄 View Retrieved Sources"):

            logger.info(
                f"Displaying {len(result['sources'])} retrieved source(s)."
            )

            for i, doc in enumerate(result["sources"], start=1):
                st.markdown(f"### Source {i}")
                st.write(doc.page_content)
                st.caption(doc.metadata)

    except Exception:

        logger.exception("Error while processing user question.")

        st.error("Something went wrong while processing your request.")

with st.sidebar:

    st.header("Options")

    if st.button("🗑️ Clear Chat"):

        logger.info("User cleared chat history.")

        st.session_state.messages = []

        st.rerun()