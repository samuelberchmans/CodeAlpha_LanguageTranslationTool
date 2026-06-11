import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

# Set up sleek web layout configuration
st.set_page_config(page_title="CodeAlpha AI Translator", page_icon="🤖", layout="centered")

st.title("🤖 AI Multilingual Translation Tool")
st.caption("Built for CodeAlpha Artificial Intelligence Internship (Task 1)")

# Language Mapping Dictionary
LANGUAGES = {
    "English": "en",
    "Tamil (தமிழ்)": "ta",
    "Japanese (日本語)": "ja",
    "Spanish (Español)": "es",
    "French (Français)": "fr",
    "German (Deutsch)": "de",
    "Hindi (हिंदी)": "hi"
}

# Core Dashboard Layout Boxes
st.subheader("1. Configure Languages")
col1, col2 = st.columns(2)

with col1:
    source_lang_name = st.selectbox("Source Language:", list(LANGUAGES.keys()), index=0)
with col2:
    target_lang_name = st.selectbox("Target Language:", list(LANGUAGES.keys()), index=1)

source_code = LANGUAGES[source_lang_name]
target_code = LANGUAGES[target_lang_name]

st.subheader("2. Input Text")
input_text = st.text_area("Enter the text you want to translate:", placeholder="Type or paste something here...", height=120)

# Translation Processing Trigger Engine
if st.button("Translate Text 🚀", use_container_width=True):
    if input_text.strip() == "":
        st.warning("⚠️ Please type some valid text first!")
    else:
        with st.spinner("AI Engine translating... Please wait..."):
            try:
                # Execute API Translation Call
                translated_res = GoogleTranslator(source=source_code, target=target_code).translate(input_text)
                
                # Display Translated Results Card cleanly
                st.success("✨ Translation Successful!")
                st.markdown(f"### **Output ({target_lang_name}):**")
                st.info(translated_res)
                
                # OPTIONAL: Text-to-Speech Engine Processing
                try:
                    tts = gTTS(text=translated_res, lang=target_code, slow=False)
                    audio_file = "translated_voice.mp3"
                    tts.save(audio_file)
                    
                    st.write("🎵 **Listen to Pronunciation:**")
                    st.audio(audio_file, format="audio/mp3")
                except Exception as audio_err:
                    st.caption("🔊 Audio preview unavailable for this script format option.")
                    
            except Exception as err:
                st.error(f"❌ Translation Processing Error: {err}")