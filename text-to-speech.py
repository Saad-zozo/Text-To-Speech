import streamlit as st
from gtts import gTTS
import os

# Function to convert text to speech using gTTS
def text_to_speech(text, language='es', output_file='argentina_spanish_output.mp3'):
    try:
        # Create a gTTS object for the given text in Spanish
        tts = gTTS(text=text, lang=language, slow=False)
        
        # Save the speech to an mp3 file
        tts.save(output_file)

        # Return the file path for playback in Streamlit
        return output_file

    except Exception as e:
        st.error(f"Error occurred: {e}")
        return None

# Streamlit app
def main():
    st.subheader("Argentinian Spanish Text-to-Speech")
    
    # Input text for conversion
    text = st.text_area("Enter the text you want to convert to speech:", "Hola, ¿cómo estás? Bienvenido a Argentina.")
    
    if st.button("Convert to Speech"):
        if text.strip() != "":
            with st.spinner("Converting text to speech..."):
                output_file = text_to_speech(text)
                
                if output_file:
                    st.success("Speech generated successfully!")
                    
                    # Display a download button for the generated speech
                    audio_file = open(output_file, 'rb')
                    audio_bytes = audio_file.read()
                    st.audio(audio_bytes, format='audio/mp3')
                    
                    st.download_button(label="Download Audio", data=audio_bytes, file_name=output_file, mime='audio/mp3')
        else:
            st.warning("Please enter some text to convert.")

if __name__ == "__main__":
    main()