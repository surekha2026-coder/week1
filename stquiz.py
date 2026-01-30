import streamlit as st

st.set_page_config(page_title="Quiz App", layout="centered")

st.title("📝 Simple Quiz App")
st.write("Answer the following questions:")

# Questions and answers
questions = [
    {
        "question": "What is the output of print(2 + 3 * 2)?",
        "options": ["10", "8", "7", "12"],
        "answer": "8"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "def", "fun", "define"],
        "answer": "def"
    },
    {
        "question": "Which data type is mutable?",
        "options": ["tuple", "string", "list", "int"],
        "answer": "list"
    }
]

score = 0

# Display questions
for i, q in enumerate(questions):
    st.subheader(f"Q{i+1}. {q['question']}")
    user_answer = st.radio(
        "Choose one:",
        q["options"],
        key=i
    )

    if user_answer == q["answer"]:
        score += 1

# Submit button
if st.button("Submit Quiz"):
    st.divider()
    st.subheader("📊 Result")

    st.success(f"Your Score: {score} / {len(questions)}")

    if score == len(questions):
        st.balloons()
    elif score >= 2:
        st.info("Good job 👍")
    else:
        st.warning("Keep practicing 💪")
