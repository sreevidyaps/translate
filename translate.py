import streamlit as st
from googletrans import Translator

st.header("Machine Translation Demo")
input=st.text_area("Please enter the text", value="")  #can write multiple lines in text area
option=st.selectbox( #dropdown with multiple options
    "To which language you wish to translate this text to?",
    ("Malayalam", "Hindi", "Tamil"))
if st.button("Translate"): #if translate button is clicked
    translator=Translator()
    translation=translator.translate(input,dest=option) #get text from input and the language to be translated from option
    st.write(translation.text)