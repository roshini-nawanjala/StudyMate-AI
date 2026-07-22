from rag.embeddings import EmbeddingModel

model = EmbeddingModel()

texts = [
    "Artificial Intelligence",
    "Machine Learning",
    "Deep Learning"
]

embeddings = model.encode(texts)

print("Number of Embeddings:", len(embeddings))
print("Embedding Dimension:", len(embeddings[0]))