from rag.vector_store import VectorStore
from agents.ai_provider import AIProvider


class ReflectionService:

    def __init__(self):
        self.vector_store = VectorStore()
        self.ai_provider = AIProvider()

    def generate_reflection(self, provider="auto", quiz_score=None, total_questions=None):

        try:

            results = self.vector_store.collection.get()

            documents = results.get("documents", [])

            if len(documents) == 0:

                return {
                    "success": False,
                    "message": "No lecture notes found. Please upload a document first."
                }

            text = "\n\n".join(documents)

            llm = self.ai_provider.get_llm(provider)

            if quiz_score is not None and total_questions is not None:
                performance = f"""
Quiz Performance:
- Score: {quiz_score}/{total_questions}
- Percentage: {(quiz_score / total_questions) * 100:.0f}%
"""
            else:
                performance = "Quiz Performance: Not Available"

            prompt = f"""
You are an intelligent AI Study Coach.

Analyze the following lecture notes and the student's quiz performance.

{performance}

Generate a personalized learning reflection using the following format.

# Learning Reflection

## Overall Performance
Write a short paragraph evaluating the student's understanding.

## Strengths
- Point 1
- Point 2
- Point 3

## Weak Areas
- Point 1
- Point 2
- Point 3

## Topics to Revise
- Topic 1
- Topic 2
- Topic 3

## Study Recommendations
Provide practical study tips to improve understanding.

## Motivation
Write a short motivational message.

Lecture Notes:

{text[:15000]}
"""

            response = llm.invoke(prompt)

            return {
                "success": True,
                "reflection": response.content
            }

        except Exception as e:

            return {
                "success": False,
                "message": str(e)
            }