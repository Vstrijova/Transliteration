from google.transliteration import transliterate_text
import streamlit as st
result = transliterate_text('altalena',  "ru")
st.write(result)
