import streamlit as st

import google.generativeai as genai

 

st.title("Hey There")
st.image("./image.png")

genai.configure(api_key="")

text = st.text_input("Ask any thing you want")

model = genai.GenerativeModel('gemini-pro')

chat = model.start_chat(history=[])
 

if st.button("Generate"):
    

    response = chat.send_message(text)

    st.write(response.text)




