import streamlit as st
from services.reflection_service import ReflectionService

st.set_page_config(
    page_title="Learning Reflection",
    page_icon="📘",
    layout="wide"
)

service = ReflectionService()

# -------------------------------
# NEW
# Initialize session variable
# -------------------------------
if "document_uploaded" not in st.session_state:
    st.session_state.document_uploaded = False

st.title("📘 AI Learning Reflection")
st.caption("Analyze your learning progress and receive personalized feedback.")

with st.sidebar:

    st.header("Settings")

    provider = st.selectbox(
        "AI Provider",
        ["auto", "groq", "openrouter"]
    )

    st.divider()

    quiz_score = st.number_input(
        "Quiz Score",
        min_value=0,
        value=0,
        step=1
    )

    total_questions = st.number_input(
        "Total Questions",
        min_value=1,
        value=5,
        step=1
    )

    generate = st.button(
        "Generate Reflection",
        use_container_width=True
    )

if generate:

    # -------------------------------
    # NEW
    # Check whether a document has
    # been uploaded in this session.
    # -------------------------------
    if not st.session_state.document_uploaded:
        st.error("Please upload a PDF document before generating a reflection.")
        st.stop()

    with st.spinner("Analyzing your learning progress..."):

        result = service.generate_reflection(
            provider=provider,
            quiz_score=quiz_score,
            total_questions=total_questions
        )

    if result["success"]:

        st.success("Reflection generated successfully.")

        st.markdown(result["reflection"])

    else:

        st.error(result["message"])

else:

    st.info(
        """
Upload lecture notes first.

Then enter your quiz score and click **Generate Reflection** to receive:

- Overall Performance
- Strengths
- Weak Areas
- Topics to Revise
- Study Recommendations
- Motivation
"""
    )