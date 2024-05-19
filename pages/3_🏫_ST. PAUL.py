from PIL import Image
import streamlit as st

image1 = Image.open("image/C.png")
image2 = Image.open("image/E.png")

st.title("ST. PAUL UNIVERSITY SURIGAO")

with st.container():
    st.write("---")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(image1)
    with text_column:
        st.subheader("ABOUT ST. PAUL")
        st.write(
            """
            St. Paul University Surigao provides quality, Catholic Paulinian education that is customer-focused in a culture of compassionate caring through
            - involvement at all levels
            - upgrading of human resources and facilities
            - commitment to continual improvement
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
            Guided by our vision, in union with Mary, our Model and St. Paul, our patron, we endeavor to become a preferred educational community, proclaim Jesus Christ, the good news, and uplift the quality of life, in a culture of excellence, compassionate caring and collaboration through:

            - Integral Catholic formation, academic competence, research and community service;
            - Innovative and productive management systems and processes permeated with Gospel values;
            - Optimum access to Paulinian education and services with preferential option for the underprivileged.

            """
        )
with st.container():
    with text_column:
        st.subheader("VISION")
        st.write(
            """
            SPU Surigao is a Paulinian community of learners and believers impelled by the charism and spirituality of the Sisters of St. Paul of Chartres form Christ-centered, integrated, competent and responsible persons in the service of the Church and society.
            """
        )
with st.container():
    with text_column:
        st.subheader("CORE VALUES")
        st.write(
            """
            ST. PAUL UNIVERSITY SURIGAO

            The Paulinian Shares in the unique history and traditions of the Sisters of St. Paul of Charters, marked by a Christocentricpaschal spirituality, commitment to mission, service to community through one's charism, urged on by Charity for God and to men.

            1. Christ centeredness
            2. Commission
            3. Community
            4. Charism
            5. Charity
            """
        )

with st.container():
    with text_column:
        st.subheader("PROGRAM AND COURSES")
        st.write(
            """
            GRADUATE PROGRAMS
            Doctor of Philosophy
            - Major : Educational Management

            Doctor of Philosophy in Business and Management
            - Master of Business Administration (MBA)
            - Master of Public Administration (MPA)
            - Master of Science in Nursing (MSN)
            - Master of Arts in Nursing(MAN)
            - Master of Arts
            Major: Science Teaching, Mathematics Teaching, English, Filipino, Home Economics
            - Master of Arts in Cultural Education (MACulEd)
            - Master of Arts in Curriculum Development and Design (MA-CDD)
            - Master of Arts in Educational Management (MAEM)
            
            UNDERGRADUATE PROGRAMS
            
            COLLEGE OF CULTURE, EDUCATION AND ARTS
            - Bachelor of Arts
            
            Major: Political Sience, Philosophy, English Language, Sociology, Mass Communication
            - Bachelor of Library and Information Science.
            - Bachelor of Library and Information Science
            - Bachelor of Science in Mathematics
            - Bachelor of Science in Public Administration
            - Bachelor of Elementary Education
            - Bachelor of Secondary Education Major in English
            - Bachelor of Secondary Education Major in Filipino
            - Bachelor of Secondary Education Major in Mathematics
            - Bachelor of Secondary Education Major in Sciences
            - Bachelor of Secondary Education Major in Social Studies
            - Bachelor of Secondary Education Major in Values Education
            - Bachelor of Early Childhood Education
            - Bachelor of Early Physical Education
            
            COLLEGE OF BUSINESS AND TECHNOLOGY
            - Bachelor of Science in Accountancy
            - Bachelor of Science in Business Administration
            
            Major: Financial Management, Marketing Management, Human Resource Development Management
            - Bachelor of Science in Hospitality Management
            - Bachelor of Science in Office Administration
            - Bachelor of Science in Tourism Management
            - Bachelor of Science in Accounting and Information System
            - Bachelor of Science in Computer Science
            - Bachelor of Science in Information Technology
            
            COLLEGE OF ENGINEERING
            - Bachelor of Science in Civil Engineering
            - Bachelor of Science in Computer Engineering
            - Bachelor of Science in Mining Engineering
            
            COLLEGE OF HEALTH SCIENCES
            - Bachelor of Science in Nursing
            - Bachelor of Science in Psychology
            
            COLLEGE OF CRIMINAL JUSTICE EDUCATION
            - Bachelor of Science in Criminology
            - Bachelor of Science in Forensic Science
            
            COLLEGE OF TEACHER EDUCATION
            - Bachelor in Elementary Education
            - Bachelor in Secondary Education
            - Major: English
            - Filipino
            - Science
            - Mathematics
            - Biological Home Economics
            - Business Technology
            - Physical Science
            - Social Studies
            - PE., Health and Music
            - Library and Info Science
            
            BASIC EDUCATION
            
            - Senior High School (Complete K-12 Curriculum)
            - Junior High School
            - Grade School
            
            TESDA PROGRAMS
            - Computer Systems Servicing NCI
            - Food and Beverage Servicing NCII
            - Housekeeping NCII
            - Bookkeeping NCl
            """
            )
