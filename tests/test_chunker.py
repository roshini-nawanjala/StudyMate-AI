from utils.file_loader import PDFLoader
from rag.chunker import TextChunker

# Load PDF
loader = PDFLoader()
text = loader.extract_text("data/uploads/lecture1.pdf")

# Chunk text
chunker = TextChunker()
chunks = chunker.split_text(text)

# Print results
print(f"Total Chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0])