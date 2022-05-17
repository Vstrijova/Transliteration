import streamlit as st
from transliterate import translit, get_available_language_codes

text = "Giochiamo a nascondino"
st.write(translit(text, 'ru'))
