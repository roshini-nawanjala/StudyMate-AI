import streamlit as st

from services.chat_service import ChatService


st.set_page_config(
    page_title="Ask AI",
    page_icon="🤖",
    layout="wide"
)

service = ChatService()

st.title("🤖 Ask Your Lecture Notes")

st.write(
    "Ask questions about your uploaded lecture notes using AI."
)

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    provider = "auto"

    st.subheader("💡 Suggested Questions")

    suggestions = [

        "Summarize the uploaded notes.",

        "What are the important exam topics?",

        "Explain the main concepts.",

        "Give me revision notes.",

        "What definitions should I remember?"

    ]

    for q in suggestions:
        st.caption("• " + q)

    st.divider()

    st.metric(
        "Messages",
        len(st.session_state.messages)
    )

    if st.button(
        "🗑 Clear Chat",
        use_container_width=True
    ):

        st.session_state.messages = []
        st.rerun()

# -----------------------------
# Chat History
# -----------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if (
            message["role"] == "assistant"
            and "sources" in message
            and message["sources"]
        ):

            with st.expander("📚 Retrieved Sources"):

                for i, source in enumerate(message["sources"], start=1):

                    st.markdown(f"**Chunk {i}**")

                    st.write(source)

                    st.divider()

# -----------------------------
# User Input
# -----------------------------
prompt = st.chat_input(
    "Ask anything about your uploaded lecture notes..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("🤖 Thinking..."):

            result = service.ask_question(
                prompt,
                provider
            )

            if result["success"]:

                answer = result["answer"]

                st.markdown(answer)

                if result.get("sources"):

                    with st.expander("📚 Retrieved Sources"):

                        for i, source in enumerate(result["sources"], start=1):

                            st.markdown(f"**Chunk {i}**")

                            st.write(source)

                            st.divider()

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                        "sources": result.get("sources", [])
                    }
                )

            else:

                st.error(result["message"])

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": result["message"]
                    }
                )
