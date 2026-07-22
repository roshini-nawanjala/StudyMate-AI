import streamlit as st

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- Sidebar ----------
with st.sidebar:
    st.title("📚 StudyMate AI")

    st.markdown("### 🌐 Language")

    language = st.selectbox(
        "Response Language",
        [
            "English",
            "Sinhala",
            "Mixed"
        ]
    )

    st.divider()

    st.markdown("### 📄 Session")

    st.info("No document uploaded")

    st.button("🗑 Clear Session", use_container_width=True)

# ---------- Main ----------
st.title("📚 StudyMate AI")

st.caption("An Agentic Learning Assistant")

st.divider()

col1, col2 = st.columns([1,1])

with col1:
    st.info("📄 Upload your lecture notes from the sidebar.")

with col2:
    st.success("🤖 AI Agents are ready.")

st.markdown("---")

st.subheader("🚀 Available Features")

c1, c2, c3 = st.columns(3)

with c1:
    st.container(border=True)
    st.markdown("### 📚 Summary")
    st.write("Generate concise notes.")

with c2:
    st.container(border=True)
    st.markdown("### ❓ Ask AI")
    st.write("Ask questions using RAG.")

with c3:
    st.container(border=True)
    st.markdown("### 📝 Quiz")
    st.write("Generate quizzes automatically.")

st.markdown("---")

st.caption("Version 1.0 | Built with Streamlit + LangGraph + Groq")