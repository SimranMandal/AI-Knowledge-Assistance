# import streamlit as st
# from query import ask_question

# st.title("AI Knowledge Assistant")

# question = st.text_input("Ask a Question")

# if question:
#     answer = ask_question(question)
#     st.write(answer)

import streamlit as st
from query import ask_question

st.title("AI Knowledge Assistant")

# Create chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

question = st.text_input("Ask a Question")

if question:
    answer = ask_question(question)

    st.session_state.chat_history.append({
        "question": question,
        "answer": answer
    })

    st.write(answer)

st.subheader("Chat History")

for chat in st.session_state.chat_history:
    st.write(f"Q: {chat['question']}")
    st.write(f"A: {chat['answer']}")

