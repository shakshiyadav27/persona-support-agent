import streamlit as st
import requests

st.title("Persona Adaptive Support Agent")

user_input = st.text_input("Enter your issue")

if st.button("Submit"):
    response = requests.get(
        "http://127.0.0.1:8000/chat/",
        params={"user_input": user_input}
    )

    data = response.json()

    st.write("Detected Persona:", data["persona"])
    st.write("Response:", data["response"])