import json

from rag.vector_store import VectorStore
from agents.ai_provider import AIProvider


class QuizService:

    def __init__(self):

        self.vector_store = VectorStore()
        self.ai_provider = AIProvider()

    def generate_quiz(
        self,
        provider="auto",
        difficulty="Medium",
        question_type="Mixed",
        num_questions=5
    ):

        try:

            # Get entire uploaded lecture
            collection = self.vector_store.collection.get()

            documents = collection.get("documents", [])

            if not documents:

                return {
                    "success": False,
                    "message": "No lecture notes found. Please upload a document first."
                }

            context = "\n\n".join(documents)

            prompt = f"""
You are StudyMate AI.

Generate a quiz ONLY from the lecture notes provided.

IMPORTANT RULES

- Use ONLY the lecture notes.
- Never invent information.
- Generate exactly {num_questions} questions.
- Difficulty: {difficulty}
- Question Type: {question_type}
- Every question MUST have exactly 4 options.
- Only ONE correct answer.
- Provide a short explanation.
- Return ONLY valid JSON.
- Do NOT use Markdown.
- Do NOT wrap the JSON inside ```json.
- Do NOT write any text before or after the JSON.

JSON FORMAT

[
  {{
    "question": "Question text",
    "options": {{
      "A": "Option A",
      "B": "Option B",
      "C": "Option C",
      "D": "Option D"
    }},
    "answer": "A",
    "explanation": "Short explanation."
  }}
]

LECTURE NOTES

{context}
"""

            llm = self.ai_provider.get_llm(provider)

            response = llm.invoke(prompt)

            content = response.content.strip()

            # Remove markdown if model accidentally adds it
            if content.startswith("```json"):
                content = content.replace("```json", "", 1)

            if content.startswith("```"):
                content = content.replace("```", "", 1)

            if content.endswith("```"):
                content = content[:-3]

            content = content.strip()

            quiz = json.loads(content)

            # Basic validation
            if not isinstance(quiz, list):
                raise Exception("Quiz is not a valid list.")

            for item in quiz:

                if "question" not in item:
                    raise Exception("Missing question.")

                if "options" not in item:
                    raise Exception("Missing options.")

                if "answer" not in item:
                    raise Exception("Missing answer.")

                if "explanation" not in item:
                    raise Exception("Missing explanation.")

                options = item["options"]

                for key in ["A", "B", "C", "D"]:

                    if key not in options:
                        raise Exception(f"Missing option {key}")

            return {
                "success": True,
                "quiz": quiz
            }

        except json.JSONDecodeError:

            return {
                "success": False,
                "message": "The AI returned an invalid quiz format. Please try again."
            }

        except Exception as e:

            return {
                "success": False,
                "message": str(e)
            }