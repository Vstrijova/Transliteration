from google.transliteration import transliterate_text
import streamlit as st
google.load("language", "1");
result = google.language.transliterate(["Namaste"], "en", "hi")
st.write(result)
#result = transliterate_text('Giochiamo a nascondino',  "ru")
#st.write(result)
