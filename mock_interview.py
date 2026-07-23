import streamlit as st
from ai.gemini import ask_gemini


st.set_page_config(
    page_title="AI Mock Interview",
    page_icon="🎤",
    layout="wide"
)


st.title("🎤 AI Mock Interview")


# -------------------------
# Select Interview Type
# -------------------------

role = st.selectbox(
    "Choose Interview Role",
    [
        "Software Developer",
        "Python Developer",
        "Data Analyst",
        "Frontend Developer",
        "Machine Learning Engineer"
    ]
)


level = st.selectbox(
    "Experience Level",
    [
        "Fresher",
        "Intermediate",
        "Advanced"
    ]
)


# -------------------------
# Session State
# -------------------------

if "question" not in st.session_state:
    st.session_state.question = None


if "feedback" not in st.session_state:
    st.session_state.feedback = None


# -------------------------
# Generate Question
# -------------------------

if st.button("🎯 Start Interview"):

    prompt = f"""
    Act as an AI interviewer.

    Ask one interview question for:

    Role: {role}
    Level: {level}

    Only return the question.
    """

    st.session_state.question = ask_gemini(prompt)

    st.session_state.feedback = None



# -------------------------
# Display Question
# -------------------------

if st.session_state.question:

    st.subheader("🤖 Interviewer")

    st.info(
        st.session_state.question
    )


    answer = st.text_area(
        "Your Answer",
        height=200
    )


    if st.button("Submit Answer"):


        feedback_prompt = f"""

        You are an expert interviewer.

        Question:
        {st.session_state.question}


        Candidate Answer:
        {answer}


        Evaluate:

        1. Communication
        2. Technical accuracy
        3. Confidence
        4. Improvement suggestions

        Give score out of 10.

        """


        st.session_state.feedback = ask_gemini(
            feedback_prompt
        )


# -------------------------
# Feedback
# -------------------------

if st.session_state.feedback:

    st.subheader("📊 AI Feedback")

    st.write(
        st.session_state.feedback
    )


    if st.button("Next Question"):

        st.session_state.question = None
        st.session_state.feedback = None

        st.rerun()