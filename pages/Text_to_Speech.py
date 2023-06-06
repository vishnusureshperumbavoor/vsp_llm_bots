import streamlit as st
from gtts import gTTS
import tempfile

# Set the title of the app
st.title("Text-to-Speech App")

# Get the text input from the user
text = st.text_input("Enter the text to convert to speech:")

# If the user enters text, generate and play the speech
if text:
    # Generate the speech
    speech = gTTS(text)

    # Create a temporary file to save the speech
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        file_path = tmp_file.name
        speech.save(file_path)

    # Play the speech using the temporary audio file
    st.audio(file_path, format='audio/mp3')
