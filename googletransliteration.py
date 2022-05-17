from google.transliteration import transliterate_text
import streamlit as st
result = transliterate_text(["Altalena"], "it", "ru")
st.write(result)
