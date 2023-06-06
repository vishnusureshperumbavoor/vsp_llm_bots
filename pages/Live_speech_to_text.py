import streamlit as st
import speech_recognition as sr
import pyaudio
import wave

# Set the title of the app
st.title("Live Speech-to-Text App")

# Create a SpeechRecognizer instance
recognizer = sr.Recognizer()

# Define the function to convert speech to text
def convert_speech_to_text(audio):
    # Convert speech to text
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Unable to recognize speech"

# Get audio input from the microphone
audio_input = st.checkbox("Use Microphone")

if audio_input:
    # Create a microphone instance
    microphone = sr.Microphone()

    # Start capturing audio from the microphone
    with microphone as source:
        # Adjust the microphone for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        # Create a new wave file
        with wave.open("audio.wav", "wb") as audio_file:
            # Set the audio file parameters
            audio_file.setnchannels(1)
            audio_file.setsampwidth(2)
            audio_file.setframerate(16000)

            # Continuously read audio from the microphone and save to the file
            while audio_input:
                audio_data = recognizer.record(source, duration=5)
                audio_file.writeframes(audio_data.get_raw_data())

                # Convert speech to text
                text = convert_speech_to_text(audio_data)
                st.text_area("Live Transcription", value=text)
else:
    st.info("Click the checkbox to enable live speech-to-text translation using the microphone.")
