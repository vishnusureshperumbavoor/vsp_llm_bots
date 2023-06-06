import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="VSPBots",
    page_icon="🤖"
)

# Load the chatbot model
model = pipeline("text-generation")

# Create the chat bot interface
st.title("VSP Chatbot")

# Get the user's input
user_input = st.text_input("What do you want to talk about?")

# Generate a response from the chatbot model
bot_response = model(user_input)

# Display the chatbot's response
st.write(bot_response[0]["generated_text"])
