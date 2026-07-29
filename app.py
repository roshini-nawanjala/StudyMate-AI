import streamlit as st


st.set_page_config(
    page_title="StudyMate AI",
    page_icon="\U0001F4DA",
    layout="wide",
    initial_sidebar_state="expanded"
)


def app_page():
    # ---------- Sidebar ----------
    with st.sidebar:
        st.title("StudyMate AI")

        st.markdown("### Language")

        language = st.selectbox(
            "Response Language",
            [
                "English",
                "Sinhala",
                "Mixed"
            ]
        )

        st.divider()

        st.markdown("### Session")

        st.info("No document uploaded")

        st.button("Clear Session", use_container_width=True)

    # ---------- Main ----------
    st.title("StudyMate AI")

    st.caption("An Agentic Learning Assistant")

    st.divider()

    col1, col2 = st.columns([1, 1])

    with col1:
        st.info("Upload your lecture notes from the Upload page.")

    with col2:
        st.success("AI agents are ready.")

    st.markdown("---")

    st.subheader("Available Features")

    c1, c2, c3 = st.columns(3)

    with c1:
        with st.container(border=True):
            st.subheader("Summary")
            st.write("Generate concise notes from uploaded lecture materials.")

    with c2:
        with st.container(border=True):
            st.subheader("Ask AI")
            st.write("Ask questions and receive context-aware answers using RAG.")

    with c3:
        with st.container(border=True):
            st.subheader("Quiz")
            st.write("Generate quizzes to assess your understanding.")

    st.markdown("---")

    st.caption("Version 1.0 | Powered by Streamlit, LangGraph, Groq and ChromaDB")


pages = [
    st.Page(app_page, title="app", default=True),
    st.Page("pages/Upload.py", title="Upload"),
    st.Page("pages/Summary.py", title="Summary"),
    st.Page("pages/Ask_AI.py", title="Ask AI"),
    st.Page("pages/Quiz.py", title="Quiz"),
    st.Page("pages/Reflection.py", title="Reflection"),
]

navigation = st.navigation(pages)
navigation.run()
