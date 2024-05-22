from PIL import Image
import streamlit as st

# ---- LOAD ASSETS ----
image1 = Image.open("image/H.png")

st.title("SCHOOL FINDER HUB")

# ---- SEARCH BAR ----
search_query = st.text_input("Search for a school:")

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

# ---- OBJECTIVES SECTION ----
with st.container():
    st.subheader("OBJECTIVES")
    st.write(
        """
        The primary objectives of School Finder Hub are to:
        1. Provide an accessible and user-friendly platform for researching educational institutions in Surigao City.
        2. Offer detailed information on each school, including programs, courses, extracurricular activities, teacher qualifications, facilities, and curriculum.
        3. Facilitate informed decision-making for parents, students, and educators.
        """
    )

# ---- MISSION SECTION ----
with st.container():
    st.subheader("MISSION")
    st.write(
        """
        The mission of School Finder Hub is to bridge the gap between educational aspirations and opportunities in Surigao City by offering a centralized, informative platform that aids in the selection of the best educational paths for students.
        """
    )

# ---- CORE VALUES SECTION ----
with st.container():
    st.write("---")
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

# ---- SEARCH FUNCTIONALITY (Example) ----
# Assume we have a list of schools
schools = [
    "Surigao City National High School",
    "Northeastern Mindanao Colleges",
    "St. Paul University Surigao",
    "Surigao Education Center",
    "Surigao State College of Technology",
]

# Filter the list of schools based on the search query
if search_query:
    filtered_schools = [school for school in schools if search_query.lower() in school.lower()]
else:
    filtered_schools = schools

# Display the search results
st.subheader("Search Results")
for school in filtered_schools:
    st.write(school)
