import chromadb

from config import (
    CHROMA_DB_PATH,
    COLLECTION_NAME
)

from rag.embeddings import EmbeddingModel


class VectorStore:
    """
    Stores and retrieves document embeddings using ChromaDB.
    """

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=CHROMA_DB_PATH
        )

        self.embedding_model = EmbeddingModel()

        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME
        )

    def clear_collection(self):
        """
        Remove all previously uploaded documents.
        """

        try:
            self.client.delete_collection(
                name=COLLECTION_NAME
            )
        except Exception:
            pass

        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME
        )

    def add_documents(
        self,
        ids,
        embeddings,
        documents
    ):

        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents
        )

    def search(
        self,
        query,
        n_results=8
    ):

        query_embedding = self.embedding_model.encode(
            [query]
        )[0].tolist()

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )

        return {

            "documents": results["documents"][0],

            "ids": results["ids"][0],

            "distances": results["distances"][0]

        }