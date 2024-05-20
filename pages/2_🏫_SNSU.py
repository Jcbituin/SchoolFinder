import requests
import streamlit as st
from PIL import Image

image1 = Image.open("image/A.png")
image2 = Image.open("image/B.png")

st.title("SURIGAO DEL NORTE UNIVERSITY SCHOOL")

with st.container():
    st.write("---")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(image1)
    with text_column:
        st.subheader("ABOUT SNSU")
        st.write(
            """
            The Surigao del Norte State University is a public university in the Philippines. It is mandated to provide advanced education, higher technological, professional instruction and training in the fields of agriculture and environmental studies, fishery, engineering, forestry, industrial technology, education, law, medicine and other health-related programs, information technology, arts and sciences and other related courses.
            """
        )        

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(image2)
    with text_column:
        st.subheader("MISSION")
        st.write(
            """
            To provide quality and inclusive education: establish industry and business innovation infrastructures; develop environmental initiatives; promote peace, justice and transformative leadership: and build strong and dynamic partnership with stakeholders.
            """
            )
with st.container():
    with text_column:
        st.subheader("VISION")
        st.write(
            """
            A Leading Industry-Driven State University.
            """
        )
with st.container():
    with text_column:
        st.subheader("CORE VALUES")
        st.write(
            """
            Integrity, Respect, and Competence
            """
        )
with st.container():
    st.write("---")
    with text_column:
        st.subheader("QUALITY POLICY")
        st.write(
            """
            Surigao del Norte State University provides quality instruction, research, extention programs, and production services to satisfy its customers by responding to their needs and expectations and continually improving its quality management system.
            """
        )



