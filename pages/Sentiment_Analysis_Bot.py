import streamlit as st
from transformers import pipeline

# Load the sentiment analysis model
model = pipeline("sentiment-analysis")

# Create the sentiment analysis interface
st.title("VSP Sentiment Analysis Bot")

# Get the user's input
user_input = st.text_input("Enter your text:")

# Analyze the sentiment of the user's input
sentiment = model(user_input)

# Display the sentiment analysis results
st.write("The sentiment of your input is:", sentiment[0]["label"])
