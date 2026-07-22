from langchain_text_splitters import RecursiveCharacterTextSplitter


class TextChunker:
    """
    Splits extracted text into smaller chunks
    for RAG.
    """

    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )

    def split_text(self, text: str):
        return self.splitter.split_text(text)