import json

from rag.vector_store import VectorStore
from agents.ai_provider import AIProvider
from agents.messages import build_quiz_result_message


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

            llm = self.ai_provider.get_llm(provider=provider, task="quiz")

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

    @staticmethod
    def calculate_score(quiz, answers):
        """Calculate the final score from the stored answer choices."""
        score = sum(
            1
            for index, question in enumerate(quiz)
            if answers.get(index) == question.get("answer")
        )

        total = len(quiz)
        percentage = (score / total) * 100 if total else 0

        return {
            "score": score,
            "total": total,
            "percentage": percentage,
            "status": "PASS" if percentage >= 50 else "FAIL"
        }

    @staticmethod
    def create_reflection_message(score_result, review=None):
        """Publish the Quiz Agent's result in the inter-agent protocol."""
        return build_quiz_result_message(score_result, review)

    def review_quiz(self, quiz, answers, provider="auto"):
        """Generate one complete, structured review for the submitted quiz."""
        try:
            review_input = []

            for index, question in enumerate(quiz):
                user_answer = answers.get(index)
                review_input.append({
                    "question_number": index + 1,
                    "question": question["question"],
                    "options": question["options"],
                    "your_answer": user_answer or "Not answered",
                    "your_answer_text": (
                        question["options"].get(user_answer, "Not answered")
                        if user_answer else "Not answered"
                    ),
                    "correct_answer": question["answer"],
                    "correct_answer_text": question["options"].get(
                        question["answer"], question["answer"]
                    )
                })

            prompt = f"""
You are StudyMate AI, an educational quiz review assistant.

Review the entire quiz in ONE response. Use the supplied questions, user answers,
and correct answers. Do not invent facts that are unrelated to the quiz.
Explain every answer in simple educational language. For incorrect answers,
explain why the user's answer is incorrect and clearly teach the correct concept.
Use the supplied answer text in `your_answer` and `correct_answer` (not only the
option letters). Keep the question order unchanged and return exactly one item
for every question.

Return ONLY valid JSON. Do not use Markdown or add text outside the JSON.

JSON FORMAT
{{
  "questions": [
    {{
      "question_number": 1,
      "status": "Correct",
      "your_answer": "Answer text",
      "correct_answer": "Correct answer text",
      "explanation": "Simple educational explanation."
    }}
  ],
  "overall_learning_report": {{
    "overall_performance": "...",
    "strengths": "...",
    "weak_areas": "...",
    "topics_to_revise": "...",
    "study_recommendations": "...",
    "motivational_feedback": "...",
    "estimated_readiness_level": "..."
  }}
}}

QUIZ REVIEW DATA
{json.dumps(review_input, ensure_ascii=False)}
"""

            llm = self.ai_provider.get_llm(provider=provider, task="quiz")
            response = llm.invoke(prompt)
            content = response.content.strip()

            if content.startswith("```json"):
                content = content.replace("```json", "", 1)
            if content.startswith("```"):
                content = content.replace("```", "", 1)
            if content.endswith("```"):
                content = content[:-3]

            review = json.loads(content.strip())
            self._validate_review(review, len(quiz))

            return {"success": True, "review": review}

        except json.JSONDecodeError:
            return {
                "success": False,
                "message": "The AI returned an invalid quiz review format. Please try again."
            }
        except Exception as e:
            return {"success": False, "message": str(e)}

    @staticmethod
    def _validate_review(review, question_count):
        """Validate the minimum structure required by the review UI."""
        if not isinstance(review, dict):
            raise ValueError("Quiz review is not a valid object.")

        questions = review.get("questions")
        report = review.get("overall_learning_report")

        if not isinstance(questions, list) or len(questions) != question_count:
            raise ValueError("Quiz review does not contain every question.")
        if not isinstance(report, dict):
            raise ValueError("Quiz review is missing the overall learning report.")

        question_fields = {
            "question_number", "status", "your_answer",
            "correct_answer", "explanation"
        }
        report_fields = {
            "overall_performance", "strengths", "weak_areas",
            "topics_to_revise", "study_recommendations",
            "motivational_feedback", "estimated_readiness_level"
        }

        for item in questions:
            if not question_fields.issubset(item):
                raise ValueError("Quiz review is missing question details.")
        if not report_fields.issubset(report):
            raise ValueError("Quiz review is missing report details.")
