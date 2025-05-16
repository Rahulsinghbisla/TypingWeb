import streamlit as st
import random as r
from time import time

def cal_error(test, user):
    error = 0
    for i in range(min(len(test), len(user))):
        if test[i] != user[i]:
            error += 1
    error += abs(len(test) - len(user))
    return error

def calculate_wpm(start_time, end_time, typed_text):
    time_taken = end_time - start_time
    word_count = len(typed_text.split())
    wpm = word_count / (time_taken / 60) if time_taken > 0 else 0
    return round(wpm, 2)

st.title("Typing Speed Test")

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Success is not final; failure is not fatal: It is the courage to continue that counts.",
    "Artificial intelligence is transforming the world at an unprecedented pace.",
    "Persistence is the key to mastering any skill, including fast typing.",
    "Knowledge is power, but applying knowledge is true wisdom.",
    "In the world of coding, precision and logic are your best allies.",
    "A journey of a thousand miles begins with a single step.",
    "Focus on accuracy first, and speed will follow naturally.",
    "Reading and typing regularly are the best ways to improve your speed.",
    "Machine learning algorithms can be complex, but understanding them is rewarding."
]

# Initialize session state variables if not present
if "test_sentence" not in st.session_state:
    st.session_state.test_sentence = r.choice(sentences)
if "start_time" not in st.session_state:
    st.session_state.start_time = time()
if "submitted" not in st.session_state:
    st.session_state.submitted = False

st.subheader("Type the following sentence:")
st.write(st.session_state.test_sentence)

# Input box
user_input = st.text_input("Your Text:", key="user_input")

def on_submit():
    st.session_state.end_time = time()
    st.session_state.submitted = True

# Submit button
st.button("Submit", on_click=on_submit)

# Show results after submission
if st.session_state.submitted:
    errors = cal_error(st.session_state.test_sentence, st.session_state.user_input)
    wpm = calculate_wpm(st.session_state.start_time, st.session_state.end_time, st.session_state.user_input)
    st.write(f"Errors: {errors}")
    st.write(f"Typing Speed: {wpm} WPM")

    # Option to restart the test
    if st.button("Try Again"):
        st.session_state.test_sentence = r.choice(sentences)
        st.session_state.start_time = time()
        st.session_state.submitted = False
        st.session_state.user_input = ""
