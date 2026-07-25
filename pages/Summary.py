import streamlit as st

from services.summary_service import SummaryService
from components.styles import load_css

from config import (
    DEFAULT_PROVIDER,
    SESSION_DOCUMENT,
    SESSION_PAGE_COUNT,
    SESSION_CHUNK_COUNT
)

st.set_page_config(
    page_title="Document Summary",
    layout="wide"
)

load_css()

service = SummaryService()

st.title("Document Summary")

st.caption(
    "Generate an AI-powered summary from the uploaded document."
)

# ---------------------------------------------------
# Current Document
# ---------------------------------------------------

if SESSION_DOCUMENT in st.session_state:

    with st.container(border=True):

        st.subheader("Current Document")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.write("**Document**")
            st.write(
                st.session_state[SESSION_DOCUMENT]
            )

        with col2:

            st.write("**Pages**")
            st.write(
                st.session_state.get(
                    SESSION_PAGE_COUNT,
                    "-"
                )
            )

        with col3:

            st.write("**Chunks**")
            st.write(
                st.session_state.get(
                    SESSION_CHUNK_COUNT,
                    "-"
                )
            )

else:

    st.info(
        "Upload a document before generating a summary."
    )
    st.stop()

st.divider()

provider = DEFAULT_PROVIDER

button_col1, button_col2, button_col3 = st.columns([1, 0.5, 1])

with button_col2:
    generate_summary = st.button(
        "Generate Summary",
        use_container_width=True
    )

if generate_summary:

    with st.spinner("Generating summary..."):

        result = service.get_document_summary(
            provider=provider
        )

    if result is None:

        st.warning(
            "No uploaded lecture notes found."
        )

    elif not result["success"]:

        st.error(
            result["message"]
        )

    else:

        st.success(
            "Summary generated successfully."
        )

        col1, col2 = st.columns(2)

        with col1:

            st.write("**Chunks Used**")
            st.write(result["chunks"])

        with col2:

            st.write("**Characters**")
            st.write(result["characters"])

        st.divider()

        st.subheader("Summary")

        with st.container(border=True):

            st.write(
                result["summary"]
            )

        st.download_button(
            label="Download Summary",
            data=result["summary"],
            file_name="StudyMate_Summary.txt",
            mime="text/plain",
            use_container_width=True
        )
