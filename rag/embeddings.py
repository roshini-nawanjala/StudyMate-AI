from sentence_transformers import SentenceTransformer


class EmbeddingModel:
    """
    Generates vector embeddings
    for text chunks.
    """

    def __init__(self):
        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def encode(self, texts):
        return self.model.encode(texts)