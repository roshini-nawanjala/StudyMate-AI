import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        /* ======================================
           GLOBAL
        ====================================== */

        html,
        body {

            font-family: "Segoe UI", sans-serif;

        }

        .stApp {

         font-family: "Segoe UI", sans-serif;
  
        }

        .block-container{
            padding-top:2rem;
            padding-bottom:2rem;
            padding-left:3rem;
            padding-right:3rem;
            max-width:1400px;
        }

        /* ======================================
           HEADINGS
        ====================================== */

        h1{
            font-size:2.3rem;
            font-weight:700;
            color:#111827;
            margin-bottom:0.4rem;
        }

        h2{
            font-size:1.8rem;
            font-weight:600;
            color:#111827;
        }

        h3{
            font-size:1.3rem;
            font-weight:600;
            color:#1F2937;
        }

        p{
            color:#4B5563;
            line-height:1.7;
        }

        hr{
            margin-top:1rem;
            margin-bottom:1rem;
        }

        /* ======================================
           SIDEBAR
        ====================================== */

    section[data-testid="stSidebar"]{

        background:#FFFFFF;

        border-right:1px solid #E5E7EB;

    }

        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3{

            color:#111827;

        }

        /* ======================================
           BUTTONS
        ====================================== */

        .stButton>button{

            width:100%;
            height:46px;

            border-radius:10px;

            border:1px solid #2563EB;

            background:#2563EB;

            color:white;

            font-weight:600;

            transition:all .25s ease;

            cursor:pointer;

        }

        .stButton>button:hover{

            background:#1D4ED8;

            border-color:#1D4ED8;

            transform:translateY(-2px);

            box-shadow:0 8px 18px rgba(37,99,235,.25);

        }

        /* ======================================
           INPUTS
        ====================================== */

        .stTextInput input,
        .stTextArea textarea{

            border-radius:10px;

            border:1px solid #D1D5DB;

        }

        .stTextInput input:focus,
        .stTextArea textarea:focus{

            border-color:#2563EB;

            box-shadow:0 0 0 3px rgba(37,99,235,.15);

        }

        .stSelectbox div{

            border-radius:10px;

        }

        /* ======================================
           FILE UPLOADER
        ====================================== */

        div[data-testid="stFileUploader"]{

            border:2px dashed #CBD5E1;

            border-radius:14px;

            background:#F8FAFC;

            padding:18px;

        }

        /* ======================================
           CARDS
        ====================================== */

        .card{

            background:#FFFFFF;

            border:1px solid #E5E7EB;

            border-radius:14px;

            padding:22px;

            margin-bottom:20px;

            box-shadow:0 2px 10px rgba(0,0,0,.04);

            transition:all .25s ease;

        }

        .card:hover{

            transform:translateY(-4px);

            box-shadow:0 10px 22px rgba(0,0,0,.08);

        }

        .card-title{

            font-size:18px;

            font-weight:600;

            color:#111827;

            margin-bottom:10px;

        }

        .card-text{

            color:#4B5563;

            font-size:15px;

            line-height:1.6;

        }

        /* ======================================
           METRIC CARDS
        ====================================== */

        div[data-testid="metric-container"]{

            border:1px solid #E5E7EB;

            border-radius:12px;

            padding:12px;

            background:white;

            box-shadow:0 2px 8px rgba(0,0,0,.04);

        }

                /* ======================================
           SUCCESS / WARNING / ERROR
        ====================================== */

        div[data-testid="stSuccess"],
        div[data-testid="stWarning"],
        div[data-testid="stError"]{

            border-radius:12px;

            border:none;

            box-shadow:0 2px 8px rgba(0,0,0,.05);

        }

        /* ======================================
           CHAT
        ====================================== */

        div[data-testid="stChatMessage"]{

            border-radius:14px;

            padding:12px;

            border:1px solid #E5E7EB;

            background:#FFFFFF;

            margin-bottom:10px;

        }

        /* ======================================
           TABS
        ====================================== */

        .stTabs [role="tab"]{

            border-radius:10px;

            padding:10px 18px;

            font-weight:600;

            transition:0.2s;

        }

        .stTabs [aria-selected="true"]{

            background:#2563EB;

            color:white;

        }

        /* ======================================
           EXPANDERS
        ====================================== */

        .streamlit-expanderHeader{

            font-weight:600;

            color:#111827;

        }

        /* ======================================
           TABLES
        ====================================== */

        table{

            width:100%;

            border-collapse:collapse;

            border-radius:10px;

            overflow:hidden;

        }

        thead{

            background:#F3F4F6;

        }

        th{

            color:#111827;

            font-weight:600;

        }

        th, td{

            padding:12px;

        }

        /* ======================================
           SPINNER
        ====================================== */

        div[data-testid="stSpinner"]{

            color:#2563EB;

        }

        /* ======================================
           SCROLLBAR
        ====================================== */

        ::-webkit-scrollbar{

            width:8px;

            height:8px;

        }

        ::-webkit-scrollbar-track{

            background:#F3F4F6;

        }

        ::-webkit-scrollbar-thumb{

            background:#CBD5E1;

            border-radius:10px;

        }

        ::-webkit-scrollbar-thumb:hover{

            background:#94A3B8;

        }

        /* ======================================
           RESPONSIVE
        ====================================== */

        @media (max-width:768px){

            .block-container{

                padding-left:1rem;

                padding-right:1rem;

            }

        }

        </style>
        """,
        unsafe_allow_html=True
    )