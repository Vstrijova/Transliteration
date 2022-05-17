from google.transliteration import transliterate_text
import streamlit as st
result = transliterate_text(['Altalena'], 'it', lang_code='ru')
st.write(result)
