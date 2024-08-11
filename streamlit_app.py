import os
import streamlit as st
import base64

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("<h1 style='text-align: right;'>🤔تدور على وظيفه ؟<h1><br>", unsafe_allow_html=True)

gif_path = "C:\\Users\\Public\\Desktop\\Usecase-5\\image.gif"

# Check if the file exists
if os.path.exists(gif_path):
    with open(gif_path, "rb") as gif_file:
        gif_bytes = gif_file.read()
        encoded_gif = base64.b64encode(gif_bytes).decode("utf-8")

    gif_html = f'<img src="data:image/gif;base64,{encoded_gif}" alt="Your Awesome GIF">'
    st.write(gif_html, unsafe_allow_html=True)
else:
    st.error("GIF file not found. Please check the file path.")
