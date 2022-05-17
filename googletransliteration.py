from google.transliteration import transliterate_text
import streamlit as st

result = transliterate_text('Giochiamo a nascondino',  "ru")
st.write(result)
