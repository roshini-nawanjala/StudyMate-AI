import streamlit as st
from components.styles import load_css

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚",
    layout="wide"
)

load_css()

st.title("📚 StudyMate AI")
st.subheader("Your AI-Powered Learning Assistant")

st.write(
    """
Welcome to **StudyMate AI**.

StudyMate AI helps students learn smarter by analyzing lecture notes,
answering questions, generating summaries, creating quizzes, and providing
personalized learning reflections.
"""
)

st.divider()

col1, col2 = st.columns(2)

with col1:

    with st.container(border=True):

        st.subheader("📤 Upload Document")

        st.write(
            "Upload lecture notes in PDF format to begin your learning session."
        )

    with st.container(border=True):

        st.subheader("📝 AI Summary")

        st.write(
            "Generate concise summaries and key points from your uploaded document."
        )

    with st.container(border=True):

        st.subheader("💬 Ask AI")

        st.write(
            "Ask questions about your lecture notes and receive AI-powered answers."
        )

with col2:

    with st.container(border=True):

        st.subheader("🧠 Quiz Generator")

        st.write(
            "Generate multiple-choice quizzes to test your understanding."
        )

    with st.container(border=True):

        st.subheader("📘 Learning Reflection")

        st.write(
            "Receive personalized feedback, strengths, weak areas, and study recommendations."
        )

    with st.container(border=True):

        st.subheader("🚀 Quick Start")

        st.markdown("""
1. Upload a PDF document.
2. Generate a summary.
3. Ask questions.
4. Take a quiz.
5. View your learning reflection.
""")

st.divider()

st.info(
    "💡 Tip: Begin by uploading a lecture note from the **Upload** page."
)

st.caption("StudyMate AI • Powered by Groq • OpenRouter • ChromaDB • Streamlit")