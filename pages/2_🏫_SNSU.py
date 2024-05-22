import requests
import streamlit as st
from PIL import Image

image1 = Image.open("image/B.png")

st.title("SURIGAO DEL NORTE STATE UNIVERSITY")

with st.container():
    st.write("---")
    image_column, text_column = st.columns((8,1))
    with image_column:
        st.image(image1)
        


