import os
from dotenv import load_dotenv

# ==========================================================
# Load Environment Variables
# ==========================================================
load_dotenv()

# ==========================================================
# Application
# ==========================================================
APP_NAME = "StudyMate AI"
APP_VERSION = "1.0.0"

# ==========================================================
# AI Providers
# ==========================================================
DEFAULT_PROVIDER = "auto"

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# ==========================================================
# Models
# ==========================================================
GROQ_MODEL = "llama-3.3-70b-versatile"

OPENROUTER_MODEL = os.getenv(
    "OPENROUTER_MODEL",
    "meta-llama/llama-3.3-70b-instruct"
)

# ==========================================================
# ChromaDB
# ==========================================================
CHROMA_DB_PATH = "data/chroma_db"
COLLECTION_NAME = "studymate"

# ==========================================================
# Embeddings
# ==========================================================
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ==========================================================
# Upload Settings
# ==========================================================
UPLOAD_FOLDER = "data/uploads"

SUPPORTED_FILE_TYPES = [
    "pdf"
]

MAX_UPLOAD_SIZE_MB = 200

# ==========================================================
# Text Chunking
# ==========================================================
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# ==========================================================
# Retrieval Settings
# ==========================================================
RETRIEVAL_TOP_K = 8

MAX_CONTEXT_CHUNKS = 8

# ==========================================================
# UI Settings
# ==========================================================
SIDEBAR_STATE = "expanded"

LAYOUT = "wide"

# ==========================================================
# Theme Colors
# ==========================================================
PRIMARY_COLOR = "#2563EB"

SUCCESS_COLOR = "#16A34A"

WARNING_COLOR = "#F59E0B"

ERROR_COLOR = "#DC2626"

BACKGROUND_COLOR = "#FFFFFF"

SIDEBAR_COLOR = "#F8FAFC"

BORDER_COLOR = "#E5E7EB"

TEXT_COLOR = "#111827"

# ==========================================================
# Session Keys
# ==========================================================
SESSION_DOCUMENT = "current_document"

SESSION_PAGE_COUNT = "page_count"

SESSION_CHUNK_COUNT = "chunk_count"

SESSION_MESSAGES = "messages"

SESSION_QUIZ = "quiz"