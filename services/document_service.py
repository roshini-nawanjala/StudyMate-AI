from pathlib import Path
import fitz

from utils.file_loader import PDFLoader
from rag.chunker import TextChunker
from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore

from config import (
    UPLOAD_FOLDER,
    CHROMA_DB_PATH
)


class DocumentService:
    """
    Handles the complete document processing pipeline.
    """

    def __init__(self):

        self.loader = PDFLoader()
        self.chunker = TextChunker()
        self.embedding_model = EmbeddingModel()
        self.vector_store = VectorStore()

    def save_file(self, uploaded_file):

        upload_dir = Path(UPLOAD_FOLDER)
        upload_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        file_path = upload_dir / uploaded_file.name

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        return file_path

    def get_page_count(self, file_path):

        pdf = fitz.open(file_path)

        page_count = len(pdf)

        pdf.close()

        return page_count

    def process(self, uploaded_file):

        # Save uploaded file
        file_path = self.save_file(uploaded_file)

        # Page count
        page_count = self.get_page_count(file_path)

        # Extract text
        text = self.loader.extract_text(str(file_path))

        # Split into chunks
        chunks = self.chunker.split_text(text)

        if len(chunks) == 0:

            return {
                "success": False,
                "message": "No text could be extracted from the PDF."
            }

        # Generate embeddings
        embeddings = self.embedding_model.encode(chunks)

        # IMPORTANT:
        # Remove previously uploaded document
        self.vector_store.clear_collection()

        # Generate IDs
        ids = [
            f"chunk_{i}"
            for i in range(len(chunks))
        ]

        # Store new document
        self.vector_store.add_documents(
            ids=ids,
            embeddings=embeddings.tolist(),
            documents=chunks
        )

        return {

            "success": True,

            "file_name": uploaded_file.name,

            "pages": page_count,

            "chunks": len(chunks),

            "database": CHROMA_DB_PATH

        }