import streamlit as st
from services.quiz_service import QuizService

st.set_page_config(page_title="Quiz Generator", page_icon="📝", layout="wide")

service = QuizService()

st.title("📝 AI Quiz Generator")

defaults = {
    "quiz": None,
    "current_question": 0,
    "score": 0,
    "checked": False,
    "answered_questions": {},
    "answers": {}      # NEW
}

for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

with st.sidebar:
    provider = st.selectbox("AI Provider", ["auto","groq","openrouter"])
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
            st.session_state.checked = False
            st.session_state.answered_questions = {}
            st.session_state.answers = {}      # NEW
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
    st.metric("Percentage", f"{(st.session_state.score/total)*100:.0f}%")

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

# Check Answer
if st.button("Check Answer"):
    st.session_state.checked = True

if st.session_state.checked:

    if st.session_state.answers.get(index) == q["answer"]:
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Incorrect! Correct Answer: {q['answer']}")

    st.info(q["explanation"])

c1, c2 = st.columns(2)

with c1:
    if st.button("Previous", disabled=index==0):
        st.session_state.current_question -= 1
        st.session_state.checked = False
        st.rerun()

with c2:
    if index < total-1:
        if st.button("Next"):
            st.session_state.current_question += 1
            st.session_state.checked = False
            st.rerun()
    else:
        if st.button("Finish Quiz"):

            score = 0

            for i, question in enumerate(quiz):
                if st.session_state.answers.get(i) == question["answer"]:
                    score += 1

            st.session_state.score = score
            st.session_state.current_question = total
            st.rerun()