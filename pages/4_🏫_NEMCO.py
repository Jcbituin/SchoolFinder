import requests
import streamlit as st
from PIL import Image

image1 = Image.open("image/D.png")

st.title("NORTHEASTERN MINDANAO COLLEGES")

with st.container():
    st.write("---")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(image1)
    with text_column:
        st.subheader("ABOUT NEMCO")
        st.write(
            """
            Northeastern Mindanao Colleges (NEMCO) is a private non-sectarian school in Surigao City. It was established in 1947 with tertiary programs and short courses, including Civil Service Review classes. The institution opened a complete high school department the following year.
            """
        )   

# ---- MISSION SECTION ----
with st.container():
    with text_column:
        st.subheader("MISSION")
        st.write(
            """
            A transformative academic institution bridging academe with industry committed to produce competent technical graduates, socially responsible professionals and value-laden lifelong learners with a competitive advantage.
            """
        )  

# ---- VISSION SECTION ----
with st.container():
    with text_column:
        st.subheader("VISSION")
        st.write(
            """
            To produce and train dynamic, competent and creative graduates with relevant actual learning experience constantly translating knowledge, skills, and behavior using innovative methods and ideas responsive to the needs of the industry and the community.
            """
        )

# ---- OBJECTIVES SECTION ----
with st.container():
    with text_column:
        st.subheader("OBJECTIVES")
        st.write(
            """
            Northeastern Mindanao Colleges aims to:
            1. provides secondary and tertiary education for the total development of the learners in an environment responsive and relevant to the needs of the community.
            2. offer programs that are holistic and compliant with accreditation standards of excellence.
            3. produce morally upright professional leaders and globally competitive graduates.
            4. develop relevant research and other scholarly activities that generate real life learning.
            5. engage in community extension services that foster self-reliance and empowerment among the marginalized.
            6. strengthen and expand partnership with stakeholders, which are sustainable,efficient, and effective in meeting the needs of the institution and the community.
            """
        )

# ---- PROGRAMS SECTION ----
with st.container():
    st.write("---")
    with text_column:
        st.subheader("PROGRAMS OFFERED")
        st.write(
            """
            - Bachelor of Secondary Education Major in English
            - Bachelor of Elementary Education
            - Bachelor of Business Administration - Marketing Management
            - Bachelor of Business Administration - Financial Management
            - Bachelor of Information Technology Associate in Computer Technology
            - Bachelor of Criminology
            - Bachelor of Arts and Sciences
            """
        )
