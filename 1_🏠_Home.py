from PIL import Image
import streamlit as st

# Stack class definition
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

# School class definition
class School:
    def __init__(self, name, image, description, programs):
        self.name = name
        self.image = image
        self.description = description
        self.programs = programs
        self.additional_info = Stack()  # Stack for additional information

# School list
schools = {
    "surigao del norte state university": School(
        "Surigao del Norte State University",
        "image/A.png",
        """
        The Surigao del Norte State University is a public university in the Philippines. It is mandated to provide advanced education, higher technological, professional instruction and training in the fields of agriculture and environmental studies, fishery, engineering, forestry, industrial technology, education, law, medicine and other health-related programs, information technology, arts and sciences and other related courses.
        """,
        """
        UNDERGRADUATE PROGRAMS:
        - BACHELOR OF SCIENCE IN CIVIL ENGINEERING (BSCE)
        - BACHELOR OF SCIENCE IN ELECTRONICS ENGINEERING (BSECE)
        - BACHELOR OF SCIENCE IN ELECTRICAL ENGINEERING (BSEE)
        - BACHELOR OF SCIENCE IN COMPUTER ENGINEERING (BSCpE)
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
        ...
        """
    ),
    "st. paul university surigao": School(
        "St. Paul University Surigao",
        "image/C.png",
        """
        St. Paul University Surigao provides quality, Catholic Paulinian education that is customer-focused in a culture of compassionate caring through
        - involvement at all levels
        - upgrading of human resources and facilities
        - commitment to continual improvement
        """,
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
        ...
        """
    ),
    "northeastern mindanao colleges": School(
        "Northeastern Mindanao Colleges",
        "image/D.png",
        """
        Northeastern Mindanao Colleges (NEMCO) is a private non-sectarian school in Surigao City. It was established in 1947 with tertiary programs and short courses, including Civil Service Review classes. The institution opened a complete high school department the following year.
        """,
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
}

# Display search results
def display_search_results(school):
    with st.container():
        st.write("---")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(school.image)
        with text_column:
            st.subheader(school.name)
            st.write(school.description)
            st.subheader("Programs and Courses Offered")
            st.write(school.programs)
        st.subheader("Additional Information for " + school.name)
        if not school.additional_info.is_empty():
            while not school.additional_info.is_empty():
                st.write(school.additional_info.pop())
        else:
            st.write("No additional information available for this school")

search_query = st.text_input("Search for a school", "")
search_query = search_query.lower()

# Display search results
if search_query:
    if search_query in schools:
        school = schools[search_query]
        display_search_results(school)
    else:
        st.write("School not found. Please try another search term.")
