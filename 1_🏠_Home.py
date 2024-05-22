from PIL import Image
import streamlit as st

# ---- LOAD ASSETS ----
image1 = Image.open("image/H.png")

st.title("SCHOOL FINDER HUB")

# ---- HEADER SECTION ----
with st.container():
    st.write("---")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(image1)
    with text_column:
        st.subheader("Summary of School Finder Hub")
        st.write(
            """
            School Finder Hub is a comprehensive online resource tailored for those seeking detailed information about educational institutions in Surigao City, from elementary schools to universities. Utilizing Python programming, the website ensures a seamless user experience, allowing users to effortlessly explore and evaluate various schools based on their specific needs and preferences.
            """
        )
with st.container():
    with text_column:
        st.subheader("OBJECTIVES")
        st.write(
            """
            The primary objectives of School Finder Hub are to:
            1. Provide an accessible and user-friendly platform for researching educational institutions in Surigao City.
            2. Offer detailed information on each school, including programs, courses, extracurricular activities, teacher qualifications, facilities, and curriculum.
            3. Facilitate informed decision-making for parents, students, and educators.
            """
        )
with st.container():
    with text_column:
        st.subheader("MISSION")
        st.write(
            """
            The mission of School Finder Hub is to bridge the gap between educational aspirations and opportunities in Surigao City by offering a centralized, informative platform that aids in the selection of the best educational paths for students.
            """
        )
with st.container():
    st.write("---")
    with text_column:
        st.subheader("CORE VALUES")
        st.write(
            """
            1. Comprehensiveness: Delivering detailed and wide-ranging information about educational institutions.
            2. User-Centricity: Ensuring a smooth, intuitive user experience through thoughtful design and functionality.
            3. Transparency: Providing clear, accurate, and up-to-date information about each school.
            4. Empowerment: Enabling users to make well-informed decisions about their educational journeys.
            5. Innovation: Continuously improving the platform using the latest technologies to enhance user experience and information accuracy.
            """
        )

# Search bar implementation
search_query = st.text_input("Search for a school", "")
search_query = search_query.lower()

# School list
schools = {
    "surigao del norte state university": {
        "image": "image/A.png",
        "description": """
        The Surigao del Norte State University is a public university in the Philippines. It is mandated to provide advanced education, higher technological, professional instruction and training in the fields of agriculture and environmental studies, fishery, engineering, forestry, industrial technology, education, law, medicine and other health-related programs, information technology, arts and sciences and other related courses.
        """,
        "programs": """
        UNDERGRADUATE PROGRAMS:
        - BACHELOR OF SCIENCE IN CIVIL ENGINEERING (BSCE)
        - BACHELOR OF SCIENCE IN ELECTRONICS ENGINEERING (BSECE)
        - BACHELOR OF SCIENCE IN ELECTRICAL ENGINEERING (BSEE)
        - BACHELOR OF SCIENCE IN COMPUTER ENGINEERING (BSCpE)
        - Bachelor of Science in Information System (BSIS)
        - Bachelor of Science in Information Technology (BSinfoTech)
        - Bachelor of Science in Computer Science (BSCS)
        ...
        """
    },
    "st. paul university surigao": {
        "image": "image/C.png",
        "description": """
        St. Paul University Surigao provides quality, Catholic Paulinian education that is customer-focused in a culture of compassionate caring through
        - involvement at all levels
        - upgrading of human resources and facilities
        - commitment to continual improvement
        """,
        "programs": """
        GRADUATE PROGRAMS
        Doctor of Philosophy
        - Major : Educational Management
        Doctor of Philosophy in Business and Management
        - Master of Business Administration (MBA)
        - Master of Public Administration (MPA)
        - Master of Science in Nursing (MSN)
        - Master of Arts in Nursing(MAN)
        ...
        """
    },
    "northeastern mindanao colleges": {
        "image": "image/D.png",
        "description": """
        Northeastern Mindanao Colleges (NEMCO) is a private non-sectarian school in Surigao City. It was established in 1947 with tertiary programs and short courses, including Civil Service Review classes. The institution opened a complete high school department the following year.
        """,
        "programs": """
        - Bachelor of Secondary Education Major in English
        - Bachelor of Elementary Education
        - Bachelor of Business Administration - Marketing Management
        - Bachelor of Business Administration - Financial Management
        - Bachelor of Information Technology Associate in Computer Technology
        - Bachelor of Criminology
        - Bachelor of Arts and Sciences
        """
    }
}

# Display search results
if search_query:
    if search_query in schools:
        school = schools[search_query]
        with st.container():
            st.write("---")
            image_column, text_column = st.columns((1, 2))
            with image_column:
                st.image(school["image"])
            with text_column:
                st.subheader(search_query.title())
                st.write(school["description"])
                st.subheader("Programs and Courses Offered")
                st.write(school["programs"])
    else:
        st.write("School not found. Please try another search term.")
