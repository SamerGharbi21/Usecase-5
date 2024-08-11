import streamlit as st
import base64

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)
# Load the GIF and encode it to base64
gif_path = "./image.gif"

with open(gif_path, "rb") as gif_file:
    gif_bytes = gif_file.read()
    encoded_gif = base64.b64encode(gif_bytes).decode("utf-8")

# Embed the GIF in the app and align it to the center
gif_html = f'''
<div style="text-align: center;">
    <img src="data:image/gif;base64,{encoded_gif}" alt="Your Awesome GIF">
</div>
'''
st.write("<h1 style='text-align: right;'>🤔تدور على وظيفه ؟<h1>", unsafe_allow_html=True)
st.write(gif_html, unsafe_allow_html=True)
