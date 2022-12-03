from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"



# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Vatsal Sinha"
PAGE_ICON = ":wave:"
NAME = "Vatsal Sinha"
DESCRIPTION = """
Tech Enthusiast.
"""
EMAIL = "vatsalsinha75@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/vatsal-sinha-76b7411a6/",
    "GitHub": "https://github.com/Vatsal162",
   
}
PROJECTS = {
    "🏆 Cricket Scorer - Scoring for an entire cricket match": "https://github.com/Vatsal162/projects/blob/main/scorer.java",
    "🏆 Twitter Crawler- Crawl Data from Twitter with the help of GUI": "https://youtu.be/3egaMfE9388",
    "🏆 Calories Burnt Prediction - Calculate no of calories burnt per workout": "https://youtu.be/LzCfNanQ_9c",
    "🏆 Sentiment Analysis - Separate negative and positive sentiments": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()



# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")


with col1:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming:Java, Python,C++,MatLab
- 📊 Data Visulization: MS Excel, R
- 📚 Modeling: Logistic regression, linear regression, decision trees
- 🗄️ Databases: MySQL, Firebase
-    Cloud: Microsoft Azure
- FrameWorks: React,flask

"""
)

st.write('\n')
st.subheader("Education")
st.write("---")

# --- JOB 1
st.write( "📚","**Birla Institute of Technology, Mesra **")
st.write("08/2021 - Present |   Masters in Computer Applications")
st.write(
    """
- ► Sgpa: 8.79
"""
)

st.write( "📚","**Birla Institute of Technology, Mesra , Lalpur Extension**")
st.write("07/2018 - 05/2021  |   Bachelors in Computer Applications")
st.write(
    """
- ► Sgpa: 8.45
"""
)

st.write( "📚","**S.T. Xavier's Hazaribagh **")
st.write("03/2017 - 03/2018  |   All India Senior School Certificate Examination")
st.write(
    """
- ► Percentage 74.8%
"""
)
st.write( "📚","**S.T. Xavier's Hazaribagh **")
st.write("03/2015 - 03/2016  |   Secondary School Examination Certificate")
st.write(
    """
- ► CGPA: 9.8
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Software Web Developer | Betiyan Nidhi Private Limited**")
st.write("05/2022 - Present")
st.write(
    """
- ► Created the entire Structural representation of the projects
- ► Led a team of similar minds throughout the first phase
- ► Worked methodically on both backend and frontend
"""
)

st.write('\n')
st.subheader("Roles and Responsibility")
st.write(
    """
- ✔️ House Captain and prefect at my school
- ✔️ Vice President at Research and Developement Wing
"""
)





# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
