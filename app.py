import streamlit as st
import whisper
import time
import datetime
import tempfile
import os


st.set_page_config(page_title="Whisper-GUI", layout="centered")
st.title("Whisper-GUI")


### Sidebar ###
with st.sidebar:
    # Description
    st.title("Whisper-GUI") 
    st.markdown("""This Streamlit app uses OpenAI's Whisper model to transcribe audio. Upload a file, choose a model, and get a transcription 🔥""")
    
    # Parameters
    st.header("Parameters")

    audio_file = st.file_uploader(
        "Choose an audio file :",
        type=["mp3", "mp4", "mpeg", "mpga", "m4a", "wav", "webm"]
    )

    model_name = st.selectbox(
        "Model to use :",
        ["turbo", "tiny", "base", "small", "medium", "large", "large-v1", "large-v2", "large-v3", "large-v3-turbo"],
        index=1,
        help="model: description (parameters, required VRAM, relative speed)\n\n- ⚡ turbo: fast and precise (809M, ~6GB, ~8x)\n\n- 🟢 tiny / base: ultra-fast, ideal for tests or weak CPUs (39M / 74M, ~1GB, ~10x / ~7x)\n\n- 🟡 small: good compromise between precision and resources (244M, ~2GB, ~4x)\n\n- 🔴 medium / large: better quality, but slower and greedier (769M / 1550M, ~5GB / ~10GB, ~2x / 1x)"
    )

    language = st.selectbox(
        "Choose the language :",
        ["auto", "Afrikaans", "Albanian", "Amharic", "Arabic", "Armenian", "Assamese", "Azerbaijani", "Bashkir", "Basque", "Belarusian", 
        "Bengali", "Bosnian", "Breton", "Bulgarian", "Burmese", "Cantonese", "Castilian", "Catalan", "Chinese", "Croatian", "Czech", 
        "Danish", "Dutch", "English", "Estonian", "Faroese", "Finnish", "Flemish", "French", "Galician", "Georgian", "German", "Greek", 
        "Gujarati", "Haitian", "Haitian Creole", "Hausa", "Hawaiian", "Hebrew", "Hindi", "Hungarian", "Icelandic", "Indonesian", "Italian", 
        "Japanese", "Javanese", "Kannada", "Kazakh", "Khmer", "Korean", "Lao", "Latin", "Latvian", "Letzeburgesch", "Lingala", "Lithuanian", 
        "Luxembourgish", "Macedonian", "Malagasy", "Malay", "Malayalam", "Maltese", "Mandarin", "Maori", "Marathi", "Moldavian", "Moldovan", 
        "Mongolian", "Myanmar", "Nepali", "Norwegian", "Nynorsk", "Occitan", "Panjabi", "Pashto", "Persian", "Polish", "Portuguese", "Punjabi", 
        "Pushto", "Romanian", "Russian", "Sanskrit", "Serbian", "Shona", "Sindhi", "Sinhala", "Sinhalese", "Slovak", "Slovenian", "Somali", 
        "Spanish", "Sundanese", "Swahili", "Swedish", "Tagalog", "Tajik", "Tamil", "Tatar", "Telugu", "Thai", "Tibetan", "Turkish", "Turkmen", 
        "Ukrainian", "Urdu", "Uzbek", "Valencian", "Vietnamese", "Welsh", "Yiddish", "Yoruba"],
        help="For automatic detection, leave it on auto"
    )

    translate_audio = st.checkbox("Translate audio to English", 
        value=False, 
        help="It's recommended to use a large model for better translation.\n\nNote : The turbo model will return the original language even if translate is specified."
    )

    use_cache = st.checkbox("Keep model in cache (faster)", 
        value=True, 
        help="Cache the model to speed up repeated transcriptions."
    )

    start_transcription = st.button("Transcribe", icon="📝")

    # About
    st.markdown("---")
    with st.expander("ℹ️ About"):
        st.markdown("""
        **Whisper-GUI**  
        Created by **Sarah Bouzidi**

        - GitHub: [srh-bzd](https://github.com/srh-bzd)
        - Based on [Whisper by OpenAI](https://github.com/openai/whisper)
        """)


### Functions ###
st.session_state.setdefault("last_model_name", None)

@st.cache_resource(show_spinner=False)
def _load_model_cached(model_name):
    return whisper.load_model(model_name)

def load_model(model_name, use_cache=True):
    if use_cache:
        if st.session_state.last_model_name != model_name:
            st.cache_resource.clear()
            st.session_state.last_model_name = model_name
        return _load_model_cached(model_name)
    else:
        return whisper.load_model(model_name)

def save_uploaded_file(uploaded_file):
    suffix = "." + uploaded_file.name.split(".")[-1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.read())
        return tmp.name

def transcribe_audio(model, audio_path, language=None, translate=False):
    if translate:
        return model.transcribe(audio_path, language=language, task="translate")
    else:
        return model.transcribe(audio_path, language=language)


### Main ###
if audio_file is not None:
    # Load audio
    st.audio(audio_file, format="audio/wav")

    # Transcription
    if start_transcription:
        tmp_path = None
        try:
            with st.spinner("Load model...", show_time=False):
                model = load_model(model_name, use_cache=use_cache)

            with st.spinner("Transcribe...", show_time=False):
                tmp_path = save_uploaded_file(audio_file)
                start_time = time.time()
                if language == "auto":
                    language = None
                result_transcription = transcribe_audio(model, tmp_path, language=language, translate=translate_audio)
                end_time = time.time()
                
                duration = int(end_time - start_time)
                formatted_duration = str(datetime.timedelta(seconds=duration))

            text_transcription = result_transcription["text"].strip()

            # Rendering
            with st.expander("Transcription", icon="📄", expanded=True):
                text = st.text_area("Generated text:", value=text_transcription, height=300)
                st.markdown(f"""<div style="display: flex; justify-content: space-between; color: gray;"><div>Done in {formatted_duration}</div>
                <div>{len(text)} characters, {len(text.split())} words</div></div>""", unsafe_allow_html=True)

            basename_audio_file = os.path.splitext(audio_file.name)[0]
            timestamping = datetime.datetime.now().strftime("%d%m%Y_%H%M")
            download_file_name = f"{basename_audio_file}_whisper_{timestamping}.txt"
            st.download_button("Download", icon="⬇️", data=text_transcription, file_name=download_file_name)
        
        except Exception as e:
            st.error(f"Error : {e}")
            if tmp_path and os.path.exists(tmp_path):
                os.remove(tmp_path)
            st.stop()

        finally:
            if tmp_path and os.path.exists(tmp_path):
                os.remove(tmp_path)
