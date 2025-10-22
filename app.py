import streamlit as st
from grammarchecker import grammer_ui
from PIL import Image
##from grammarchecker import grammar_ui

st.set_page_config(page_title="Language Coaching Chatbot",page_icon="💬")

st.sidebar.title("Language Coaching Chatbot")
page=st.sidebar.radio("Navigation",["Home","Grammar Checker"])
##Historical data
if page=="Home":
        
    img=Image.open("chatbot.png")
    st.image(img)

    st.markdown(
        """
    # Language Coaching Chatbot
    Your personal AI-powered language coach — here to help you practice, learn, and improve anytime, anywhere.
    Whether you’re mastering pronunciation, building vocabulary, or preparing for real-world conversations, our chatbot adapts to your level and goals.
    - Practice natural dialogue
    - Get instant feedback and corrections
    - Get guided feedback and step-by-step milestones toward fluency

        """
    )
if page=="Grammar Checker":

    grammer_ui()


