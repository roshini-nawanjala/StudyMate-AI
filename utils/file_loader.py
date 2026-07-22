import fitz  # PyMuPDF
from pathlib import Path


class PDFLoader:
    """
    Responsible for loading PDF files
    and extracting plain text.
    """

    def extract_text(self, pdf_path: str) -> str:
        """
        Extract all text from a PDF file.

        Args:
            pdf_path (str): Path to the PDF

        Returns:
            str: Extracted text
        """

        path = Path(pdf_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {pdf_path}")

        document = fitz.open(pdf_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text