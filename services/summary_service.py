from rag.vector_store import VectorStore
from agents.ai_provider import AIProvider


class SummaryService:

    def __init__(self):
        self.vector_store = VectorStore()
        self.ai_provider = AIProvider()

    def get_document_summary(self, provider="auto"):

        try:

            results = self.vector_store.collection.get()

            documents = results.get("documents", [])

            if len(documents) == 0:

                return None

            text = "\n\n".join(documents)

            llm = self.ai_provider.get_llm(provider)

            prompt = f"""
You are an expert study assistant.

Your task is to summarize the following lecture notes.

Create the response using the following format.

# Summary
Write a concise summary.

# Key Points
- Bullet Point 1
- Bullet Point 2
- Bullet Point 3

# Important Concepts
Mention the important concepts discussed.

# Exam Tips
Give useful exam preparation tips based on these notes.

Lecture Notes:

{text[:15000]}
"""

            response = llm.invoke(prompt)

            return {
                "success": True,
                "summary": response.content,
                "chunks": len(documents),
                "characters": len(text)
            }

        except Exception as e:

            return {
                "success": False,
                "message": str(e)
            }