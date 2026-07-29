"""Small, explicit message contracts shared by StudyMate agents."""

import re
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class QuizResultMessage:
    """Structured protocol message sent from Quiz Agent to Reflection Agent."""

    score: float
    correct_answers: int
    wrong_answers: int
    weak_topics: list[str]
    strong_topics: list[str]
    recommendation: str
    total_questions: int
    status: str
    message_type: str = "quiz_result"
    version: int = 1

    def to_dict(self):
        """Return the JSON-compatible representation used in the LLM prompt."""
        return asdict(self)


def _topics(value):
    """Turn the quiz report's human-readable topic field into a list."""
    if not value:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]

    topics = []
    for item in re.split(r"\n|•|;|,(?=\s*[A-Z])", str(value)):
        item = re.sub(r"^\s*[-*]\s*", "", item).strip()
        if item:
            topics.append(item)
    return topics


def build_quiz_result_message(score_result, review=None):
    """Create the structured Quiz Agent -> Reflection Agent message."""
    review = review or {}
    report = review.get("overall_learning_report", {})
    correct = score_result.get("score", 0)
    total = score_result.get("total", 0)
    percentage = score_result.get("percentage", 0)

    return QuizResultMessage(
        score=round(percentage, 2),
        correct_answers=correct,
        wrong_answers=max(total - correct, 0),
        total_questions=total,
        status=score_result.get("status"),
        weak_topics=_topics(
            report.get("topics_to_revise") or report.get("weak_areas")
        ),
        strong_topics=_topics(report.get("strengths")),
        recommendation=report.get(
            "study_recommendations",
            "Review the weak topics and retry a practice quiz."
        ),
    )
