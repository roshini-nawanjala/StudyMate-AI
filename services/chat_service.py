from rag.vector_store import VectorStore
from agents.ai_provider import AIProvider


class ChatService:

    def __init__(self):

        self.vector_store = VectorStore()
        self.ai_provider = AIProvider()

    def ask_question(
        self,
        question,
        provider="auto"
    ):

        try:

            results = self.vector_store.search(
                query=question,
                n_results=6
            )

            documents = results.get("documents", [])

            if len(documents) == 0:

                return {
                    "success": False,
                    "message": "No uploaded lecture notes were found. Please upload a document first."
                }

            context = "\n\n-----------------------------\n\n".join(
                documents
            )

            prompt = f"""
You are StudyMate AI.

You are helping a university student prepare for exams.

Use ONLY the uploaded lecture notes below.

Rules:

1. Answer ONLY using the uploaded notes.

2. If the answer is only partially available,
say:

"According to the uploaded lecture notes..."

3. Never invent information.

4. Never use outside knowledge.

5. If the answer is genuinely unavailable, reply:

"I couldn't find this information in the uploaded lecture notes."

6. Explain in simple English.

7. Use headings where appropriate.

8. Use bullet points whenever possible.

9. Highlight important exam points.

10. Keep the answer clear and easy to understand.

====================================

LECTURE NOTES

{context}

====================================

STUDENT QUESTION

{question}

====================================

Generate the best possible answer.
"""

            llm = self.ai_provider.get_llm(
                provider=provider,
                task="question_answering"
            )

            response = llm.invoke(prompt)

            answer = response.content.strip()

            return {

                "success": True,

                "answer": answer,

                "sources": documents

            }

        except Exception as e:

            return {

                "success": False,

                "message": str(e)

            }
