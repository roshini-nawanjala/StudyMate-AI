import streamlit as st
from services.reflection_service import ReflectionService

st.set_page_config(
    page_title="Learning Reflection",
    page_icon="\U0001F4D8",
    layout="wide"
)

service = ReflectionService()

if "document_uploaded" not in st.session_state:
    st.session_state.document_uploaded = False

st.title(" AI Learning Reflection")
st.caption("Analyze your learning progress and receive personalized feedback.")

provider = "auto"

quiz_completed = st.session_state.get("quiz_completed", False)

if not quiz_completed:
    st.info(
        "No completed quiz was found.\n\n"
        "Please complete a quiz before generating a reflection."
    )
    st.stop()

st.subheader("Latest Quiz Results")
st.write(f"**Questions:** {st.session_state.get('quiz_total', 0)}")
st.write(f"**Correct:** {st.session_state.get('quiz_correct', 0)}")
st.write(f"**Incorrect:** {st.session_state.get('quiz_wrong', 0)}")
st.write(
    f"**Score:** {st.session_state.get('quiz_score', 0)} / "
    f"{st.session_state.get('quiz_total', 0)}"
)
st.write(f"**Percentage:** {st.session_state.get('quiz_percentage', 0):.0f}%")
st.write(f"**Status:** {st.session_state.get('quiz_status', 'FAIL')}")

generate = st.button("Generate Reflection", use_container_width=True)

if generate:
    if not st.session_state.document_uploaded:
        st.error("Please upload a PDF document before generating a reflection.")
        st.stop()

    with st.spinner("Analyzing your learning progress..."):
        result = service.generate_reflection(
            provider=provider,
            quiz_message=st.session_state.get("quiz_agent_message")
        )

    if result["success"]:
        st.success("Reflection generated successfully.")
        st.markdown(result["reflection"])
    else:
        st.error(result["message"])
