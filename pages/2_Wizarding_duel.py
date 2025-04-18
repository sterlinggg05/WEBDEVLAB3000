import streamlit as st
import google.generativeai as genai
import os

dev_api_key = "AIzaSyDTliIuOh7WrFN0AGfGmUfSRMTNbMWSfi4"

if os.path.exists(".streamlit/secrets.toml") or os.path.exists(os.path.expanduser("~/.streamlit/secrets.toml")):
    try:
        api_key = st.secrets["gemini"]["api_key"]
    except Exception:
        api_key = dev_api_key
else:
    api_key = dev_api_key

genai.configure(api_key=api_key)

st.title("⚡ Wizard Duel Analyzer")
st.write("Compare two wizarding characters using AI magic!")

characters = [
    "Fred Weasley", "Fleur Delacour", "Harry Potter", "Hermione Granger", "Draco Malfoy", "Tom Riddle",
    "Nicolas Flamel", "George Weasley", "Lavender Brown", "Erica Stainwright"
]

col1, col2 = st.columns(2)
with col1:
    char1 = st.selectbox("Choose first wizard:", characters)
with col2:
    char2 = st.selectbox("Choose second wizard:", [c for c in characters if c != char1])

duel_style = st.radio(
    "Choose a duel style:",
    ["Serious (tactical duel)", "Funny (chaotic duel)", "Dramatic (like a movie scene)"]
)

do_duel = st.button("Analyze the Duel")

if do_duel:
    prompt = f"""
    Compare the following two wizarding characters in a {duel_style.lower()}:

    1. {char1}
    2. {char2}

    Write a Hogwarts-style personality profile for each, then guess who would win in a magical duel and why.
    Be creative and magical in tone, like you're a professor at Hogwarts.
    """

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        st.subheader("🪄 Gemini's Analysis")
        st.write(response.text)
    except Exception as e:
        st.error("An error occurred while contacting the Gemini API. Please try again.")
        st.code(str(e))
