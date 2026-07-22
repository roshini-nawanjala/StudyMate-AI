import streamlit as st

from services.document_service import DocumentService
from components.styles import load_css

from config import (
    SESSION_DOCUMENT,
    SESSION_PAGE_COUNT,
    SESSION_CHUNK_COUNT
)

st.set_page_config(
    page_title="Upload Document",
    layout="wide"
)

load_css()

st.title("Upload Document")

st.caption(
    "Upload a PDF document to begin summarizing, asking questions, and generating quizzes."
)

# ----------------------------------------
# Current Document
# ----------------------------------------

if SESSION_DOCUMENT in st.session_state:

    with st.container(border=True):

        st.subheader("Current Document")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Document",
                st.session_state[SESSION_DOCUMENT]
            )

        with col2:
            st.metric(
                "Pages",
                st.session_state.get(
                    SESSION_PAGE_COUNT,
                    "-"
                )
            )

        with col3:
            st.metric(
                "Chunks",
                st.session_state.get(
                    SESSION_CHUNK_COUNT,
                    "-"
                )
            )

uploaded_file = st.file_uploader(
    "Select PDF",
    type=["pdf"]
)

if uploaded_file:

    service = DocumentService()

    with st.spinner("Processing document..."):

        result = service.process(uploaded_file)

    if result["success"]:

        st.session_state[SESSION_DOCUMENT] = result["file_name"]

        st.session_state[SESSION_PAGE_COUNT] = result.get(
            "pages",
            "-"
        )

        st.session_state[SESSION_CHUNK_COUNT] = result["chunks"]

        # ----------------------------------------
        # NEW
        # Mark document as uploaded for this session
        # ----------------------------------------
        st.session_state.document_uploaded = True

        st.success("Document processed successfully.")

        st.divider()

        with st.container(border=True):

            st.subheader("Document Information")

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Document",
                    result["file_name"]
                )

            with col2:

                st.metric(
                    "Pages",
                    result.get("pages", "-")
                )

            with col3:

                st.metric(
                    "Chunks",
                    result["chunks"]
                )

    else:

        st.error(result["message"])