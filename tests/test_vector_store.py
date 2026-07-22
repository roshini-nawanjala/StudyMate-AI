from utils.file_loader import PDFLoader
from rag.chunker import TextChunker
from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore

# Load PDF
loader = PDFLoader()
text = loader.extract_text("data/uploads/lecture1.pdf")

# Split into chunks
chunker = TextChunker()
chunks = chunker.split_text(text)

# Create embeddings
embedding_model = EmbeddingModel()
embeddings = embedding_model.encode(chunks)

# Store in ChromaDB
store = VectorStore()

ids = [f"chunk_{i}" for i in range(len(chunks))]

store.add_documents(
    ids=ids,
    embeddings=embeddings.tolist(),
    documents=chunks
)

print("✅ Documents stored successfully!")