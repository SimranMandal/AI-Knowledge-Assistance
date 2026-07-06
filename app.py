# # import streamlit as st
# # from query import ask_question

# # st.title("AI Knowledge Assistant")

# # question = st.text_input("Ask a Question")

# # if question:
# #     answer = ask_question(question)
# #     st.write(answer)

# import streamlit as st
# from query import ask_question

# st.title("AI Knowledge Assistant")

# # Create chat history
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# question = st.text_input("Ask a Question")

# if question:
#     answer = ask_question(question)

#     st.session_state.chat_history.append({
#         "question": question,
#         "answer": answer
#     })

#     st.write(answer)

# st.subheader("Chat History")

# for chat in st.session_state.chat_history:
#     st.write(f"Q: {chat['question']}")
#     st.write(f"A: {chat['answer']}")

import streamlit as st
from chat import ask_question

st.set_page_config(
    page_title="Enterprise Knowledge Assistant",
    page_icon="📚",
    layout="wide",
)

st.title("📚 Enterprise Knowledge Assistant")
st.write("Ask questions about your company documents.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask a question...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.spinner("Searching documents..."):
        result = ask_question(question)

    answer = result["answer"]

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)

    with st.expander("📄 View Retrieved Sources"):
        for i, doc in enumerate(result["sources"], start=1):
            st.markdown(f"### Source {i}")
            st.write(doc.page_content)
            st.caption(doc.metadata)

with st.sidebar:
    st.header("Options")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()