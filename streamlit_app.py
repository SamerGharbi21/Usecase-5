import streamlit as st
import base64

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("<h1 style='text-align: right; '>🤔تدور على وظيفه ؟ <h1><br>", unsafe_allow_html=True)

st.write("![Your Awsome GIF](C://Users//Public//Desktop//Usecase-5//image.gif)")

"""### gif from local file"""
file_ = open("C://Users//Public//Desktop//Usecase-5//image.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)
