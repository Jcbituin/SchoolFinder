import requests
import streamlit as st
from PIL import Image



st.title("SURIGAO DEL NORTE STATE UNIVERSITY")

import streamlit as st

image1 = Image.open("image/B.png")

with st.container():
    st.write("---")
    image_column, text_column = st.columns((5,2))
    with image_column:
        st.image(image1)

with st.container():
    with text_column:
        st.subheader("ABOUT SNSU")
        st.write(
            """
            The Surigao del Norte State University is a public university in the Philippines. It is mandated to provide advanced education, higher technological, professional instruction and training in the fields of agriculture and environmental studies, fishery, engineering, forestry, industrial technology, education, law, medicine and other health-related programs, information technology, arts and sciences and other related courses.
            """
        )        

with st.container():
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
    with text_column:
        st.subheader("QUALITY POLICY")
        st.write(
            """
            Surigao del Norte State University provides quality instruction, research, extention programs, and production services to satisfy its customers by responding to their needs and expectations and continually improving its quality management system.
            """
        )
with st.container():
    with text_column:
        st.subheader("PROGRAM AND COURSES OFFERED")
        st.write(
            """
            UNDERGRADUATE PROGRAMS:
            - BACHELOR OF SCIENCE IN CIVIL ENGINEERING (BSCE)
            - BACHELOR OF SCIENCE IN ELECTRONICS ENGINEERING (BSECE) 
            - BACHELOR OF SCIENCE IN ELECTRICAL ENGINEERING (BSEE)
            - BACHELOR OF SOCIENCE IN COMPUTER ENGINEERING (BSCpE)
            - Bachelor of Science in Information System (BSIS)
            - Bachelor of Science in Information Technology (BSinfoTech)
            - Bachelor of Science in Computer Science (BSCS)
            
            - BACHELOR IN AUTOMOTIVE ENGINEERING TECHNOLOGY (BAET)
            - BACHELOR IN ELECTRICAL ENGINEERING TECHNOL0GY (BEET)
            - BACHELOR IN ELECTRONICS ENGINEERING TECHNOLOGY (BEXET)
            - BACHELOR IN MECHANICAL ENGINEERING TECHNOLOGY (BMET)
            CONCENTRATION IN: 
            - MECHANICAL TECHNOLOGY (BMET- MT)
            - REFRIGERATION AND AIR-CONDITIONING TECHNOLoGY (BMET-RAC)
            
            Bachelor of Science in Industrial Technology (BSIT) Major in:
            - Architectural Drafting Technology (BSIT-ADT)
            - Automotive Technology (BSIT-AT)
            - Electricol Technology (BSIT-ELT)
            - Electronics Technology (BSIT-ELX)
            - Mechanical Technology (BSIT-MT)
            - Welding and Fabricotion Technology (BSIT-WAFT)
            - Heating, Ventilation, Air-conditioning and Refrigeration (BSIT-HVACR)
            
            - Bachelor of science in Hospitality Manogement (BSHM)
            - Bachelor of science in Tourism Management (BSTM)
            
            BACHELOR OF TECHNICAL- VOCATIONAL TEACHER EDUCATION (BTVTED) MAJOR:
            - FOOD AND SERVICEs MANAGEMENT
            
            BACHELOR OF SECONDARY EDUCATION (BSED) MAJOR IN:
            - ENGLISH
            - FILIPINO
            - MATHEMATICS
            - SCIENCES
            
            - BACHELOR OF ELEMENTARY EDUCATION (BEED)
            - Bachelor of Physical Education (BPED)
            
            - BACHELOR OF SCIENCE IN ENVIRONMENTAL SCIENCE (BSES)
            - BACHELOR OF SCIENCE IN MATHEMATICS (BSMATH)
            - BACHELOR OF ARTS IN ENGLISH LANGUAGE (AB-EL)
            """
        )



