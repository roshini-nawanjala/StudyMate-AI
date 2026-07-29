import json

from rag.vector_store import VectorStore
from agents.ai_provider import AIProvider
from agents.messages import QuizResultMessage


class ReflectionService:

    def __init__(self):
        self.vector_store = VectorStore()
        self.ai_provider = AIProvider()

    def generate_reflection(
        self,
        provider="auto",
        quiz_message=None
    ):

        try:

            if not isinstance(quiz_message, QuizResultMessage):
                return {
                    "success": False,
                    "message": "No QuizResultMessage was provided by the Quiz Agent."
                }

            results = self.vector_store.collection.get()

            documents = results.get("documents", [])

            if len(documents) == 0:

                return {
                    "success": False,
                    "message": "No lecture notes found. Please upload a document first."
                }

            text = "\n\n".join(documents)

            llm = self.ai_provider.get_llm(provider=provider, task="reflection")

            prompt = f"""
You are an intelligent AI Study Coach.

The Quiz Agent has sent the following structured message. Use it directly;
do not recalculate the score or rebuild the quiz analysis:

{json.dumps(quiz_message.to_dict(), ensure_ascii=False)}

Analyze the following lecture notes in light of that message.

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
