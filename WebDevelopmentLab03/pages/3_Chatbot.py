import streamlit as st
import google.generativeai as genai
import os


api_key = "AIzaSyDTliIuOh7WrFN0AGfGmUfSRMTNbMWSfi4"


if os.path.exists(".streamlit/secrets.toml") or os.path.exists(os.path.expanduser("~/.streamlit/secrets.toml")):
    try:
        api_key = st.secrets["gemini"]["api_key"]
    except Exception:
        pass


genai.configure(api_key=api_key)


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("🪄 Wizarding World Chatbot")
st.write("Ask me anything about magic, spells, or characters!")


user_input = st.chat_input("What would you like to ask about the wizarding world?")


for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.write(message)


if user_input:
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.chat_history.append(("user", user_input))


    context = "You are a friendly wizarding world expert. Respond like a Hogwarts professor."
    prompt = context + "\n\n"
    for role, msg in st.session_state.chat_history:
        if role == "user":
            prompt += f"User: {msg}\n"
        else:
            prompt += f"WizardBot: {msg}\n"

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        answer = response.text

        with st.chat_message("assistant"):
            st.write(answer)
        st.session_state.chat_history.append(("assistant", answer))

    except Exception as e:
        with st.chat_message("assistant"):
            st.error("An error occurred while contacting the Gemini API.")
            st.code(str(e))
