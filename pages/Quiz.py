import streamlit as st
from services.quiz_service import QuizService

st.set_page_config(page_title="Quiz Generator", page_icon="📝", layout="wide")

service = QuizService()

st.title("📝 AI Quiz Generator")

defaults = {
    "quiz": None,
    "current_question": 0,
    "score": 0,
    "answers": {},
    "current_quiz_review": None,
    "review_error": None,
    "quiz_submitted": False
}

for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

latest_quiz_defaults = {
    "quiz_completed": False,
    "quiz_score": None,
    "quiz_total": None,
    "quiz_correct": None,
    "quiz_wrong": None,
    "quiz_percentage": None,
    "quiz_status": None,
    "quiz_review": None,
    "quiz_overall_performance_summary": None
}

for k, v in latest_quiz_defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


def _store_latest_quiz(score_result, review=None):
    """Keep only the most recently completed quiz for Reflection."""
    st.session_state.quiz_completed = True
    st.session_state.quiz_score = score_result["score"]
    st.session_state.quiz_total = score_result["total"]
    st.session_state.quiz_correct = score_result["score"]
    st.session_state.quiz_wrong = score_result["total"] - score_result["score"]
    st.session_state.quiz_percentage = score_result["percentage"]
    st.session_state.quiz_status = score_result["status"]
    st.session_state.quiz_review = review
    st.session_state.quiz_overall_performance_summary = (
        review.get("overall_learning_report", {}).get("overall_performance")
        if review else None
    )

with st.sidebar:
    provider = "auto"
    difficulty = st.selectbox("Difficulty", ["Easy","Medium","Hard"])
    question_type = st.selectbox("Question Type", ["MCQ","True / False","Mixed"])
    num_questions = st.slider("Number of Questions",5,20,5,step=5)

    if st.button("Generate Quiz", use_container_width=True):
        result = service.generate_quiz(
            provider=provider,
            difficulty=difficulty,
            question_type=question_type,
            num_questions=num_questions
        )

        if result["success"]:
            st.session_state.quiz = result["quiz"]
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.answers = {}
            st.session_state.current_quiz_review = None
            st.session_state.review_error = None
            st.session_state.quiz_submitted = False
            st.rerun()
        else:
            st.error(result["message"])

if not st.session_state.quiz:
    st.info("Generate a quiz using the sidebar.")
    st.stop()

quiz = st.session_state.quiz
total = len(quiz)
index = st.session_state.current_question

if index >= total:
    st.header("Quiz Completed")
    st.metric("Score", f"{st.session_state.score}/{total}")
    percentage = (st.session_state.score / total) * 100 if total else 0
    st.metric("Percentage", f"{percentage:.0f}%")
    st.write(f"**Status:** {'PASS' if percentage >= 50 else 'FAIL'}")

    if st.session_state.current_quiz_review:
        review = st.session_state.current_quiz_review
        st.subheader("Quiz Review")

        for item in review["questions"]:
            is_correct = item["status"].strip().lower() == "correct"
            label = "✅ Correct" if is_correct else "❌ Incorrect"
            with st.expander(f"Question {item['question_number']} — {label}"):
                if is_correct:
                    st.success(f"Status: {label}")
                else:
                    st.error(f"Status: {label}")
                st.write(f"**Your Answer:** {item['your_answer']}")
                st.write(f"**Correct Answer:** {item['correct_answer']}")
                st.write(f"**Explanation:** {item['explanation']}")

        report = review["overall_learning_report"]
        st.subheader("Overall Learning Report")
        for title, key in [
            ("Overall Performance", "overall_performance"),
            ("Strengths", "strengths"),
            ("Weak Areas", "weak_areas"),
            ("Topics To Revise", "topics_to_revise"),
            ("Study Recommendations", "study_recommendations"),
            ("Motivational Feedback", "motivational_feedback"),
            ("Estimated Readiness Level", "estimated_readiness_level")
        ]:
            st.write(f"**{title}:** {report[key]}")

    if st.session_state.review_error:
        st.error(st.session_state.review_error)

    if not st.session_state.quiz_submitted:
        if st.button("Submit Quiz", use_container_width=True):
            score_result = service.calculate_score(quiz, st.session_state.answers)
            st.session_state.score = score_result["score"]
            result = service.review_quiz(
                quiz,
                st.session_state.answers,
                provider=provider
            )
            if result["success"]:
                st.session_state.current_quiz_review = result["review"]
                st.session_state.review_error = None
                st.session_state.quiz_submitted = True
                _store_latest_quiz(score_result, result["review"])
            else:
                st.session_state.review_error = result["message"]
                _store_latest_quiz(score_result)
            st.rerun()

    if st.button("Generate New Quiz"):
        for k, v in defaults.items():
            st.session_state[k] = v
        st.rerun()

    st.stop()

q = quiz[index]

st.progress((index+1)/total)
st.subheader(f"Question {index+1} of {total}")
st.write(q["question"])

options = [
    f"A. {q['options']['A']}",
    f"B. {q['options']['B']}",
    f"C. {q['options']['C']}",
    f"D. {q['options']['D']}",
]

# NEW - Remember previously selected answer
saved_answer = st.session_state.answers.get(index)

selected = st.radio(
    "Choose your answer",
    options,
    index=["A","B","C","D"].index(saved_answer) if saved_answer else None,
    key=f"radio_{index}"
)

# NEW - Save selected answer automatically
if selected:
    st.session_state.answers[index] = selected[0]

c1, c2 = st.columns(2)

with c1:
    if st.button("Previous", disabled=index==0):
        st.session_state.current_question -= 1
        st.rerun()

with c2:
    if index < total-1:
        if st.button("Next"):
            st.session_state.current_question += 1
            st.rerun()
    else:
        all_answered = len(st.session_state.answers) == total

        if not all_answered:
            st.caption("Answer every question before submitting the quiz.")

        if st.button("Submit Quiz", disabled=not all_answered):
            score_result = service.calculate_score(quiz, st.session_state.answers)
            st.session_state.score = score_result["score"]
            st.session_state.current_question = total
            review_result = service.review_quiz(
                quiz,
                st.session_state.answers,
                provider=provider
            )
            if review_result["success"]:
                st.session_state.current_quiz_review = review_result["review"]
                st.session_state.review_error = None
                st.session_state.quiz_submitted = True
                _store_latest_quiz(score_result, review_result["review"])
            else:
                st.session_state.current_quiz_review = None
                st.session_state.review_error = review_result["message"]
                _store_latest_quiz(score_result)
            st.rerun()
