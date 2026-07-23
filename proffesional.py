import streamlit as st
from utils.session import logout

# -------------------------------
# Check Login
# -------------------------------

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please login first.")
    st.switch_page("pages/login.py")

# -------------------------------
# Page Settings
# -------------------------------

st.set_page_config(
    page_title="Professional Dashboard",
    page_icon="💼",
    layout="wide"
)

# -------------------------------
# Header
# -------------------------------

st.title("💼 Working Professional Dashboard")

st.write(f"### Welcome {st.session_state.name}")

st.write("Email :", st.session_state.email)

st.markdown("---")

# -------------------------------
# Profile
# -------------------------------

st.subheader("👤 Professional Profile")

col1, col2 = st.columns(2)

with col1:
    st.info(f"Name : {st.session_state.name}")

with col2:
    st.info(f"Category : {st.session_state.category}")

st.markdown("---")

# -------------------------------
# Dashboard Metrics
# -------------------------------

st.subheader("📊 Career Dashboard")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Skill Score", "88%", "+5%")

with c2:
    st.metric("Career Growth", "85%", "+3%")

with c3:
    st.metric("Promotion Readiness", "80%", "+4%")

st.markdown("---")

# -------------------------------
# Skill Assessment
# -------------------------------

st.subheader("📝 Skill Assessment")

python = st.slider("Python", 0, 10, 8)

sql = st.slider("SQL", 0, 10, 6)

docker = st.slider("Docker", 0, 10, 4)

aws = st.slider("AWS", 0, 10, 3)

communication = st.slider("Communication", 0, 10, 7)

if st.button("Analyze Skills"):

    st.success("Assessment Completed")

    if docker < 5:
        st.warning("Learn Docker")

    if aws < 5:
        st.warning("Learn AWS")

    if sql < 7:
        st.warning("Improve SQL")

    if communication < 7:
        st.warning("Improve Communication Skills")

st.markdown("---")

# -------------------------------
# AI Career Coach
# -------------------------------

st.subheader("🤖 AI Career Coach")

career_goal = st.selectbox(
    "Select Your Goal",
    [
        "Promotion",
        "Switch Company",
        "Become Team Lead",
        "Become AI Engineer",
        "Become Cloud Engineer"
    ]
)

if st.button("Get Career Advice"):

    if career_goal == "Promotion":
        st.success("Improve leadership, communication, and project management skills.")

    elif career_goal == "Switch Company":
        st.success("Update Resume, LinkedIn Profile, and Practice Coding Interviews.")

    elif career_goal == "Become Team Lead":
        st.success("Develop leadership, mentoring, and system design skills.")

    elif career_goal == "Become AI Engineer":
        st.success("Learn Python, Machine Learning, Deep Learning, and Generative AI.")

    elif career_goal == "Become Cloud Engineer":
        st.success("Learn AWS, Docker, Kubernetes, Linux, and Terraform.")

st.markdown("---")

# -------------------------------
# Industry Trends
# -------------------------------

st.subheader("📈 Industry Trends")

st.info("🔥 Artificial Intelligence")

st.info("☁ Cloud Computing")

st.info("🔐 Cyber Security")

st.info("📊 Data Science")

st.info("⚙ DevOps")

st.info("📱 Mobile Development")

st.markdown("---")

# -------------------------------
# Certification Suggestions
# -------------------------------

st.subheader("🏅 Certification Suggestions")

career = st.selectbox(
    "Choose Career Path",
    [
        "Software Developer",
        "Cloud Engineer",
        "AI Engineer",
        "Cyber Security",
        "Data Analyst"
    ]
)

if st.button("Show Certifications"):

    if career == "Software Developer":

        st.write("✔ Oracle Java Certification")

        st.write("✔ Python Professional")

    elif career == "Cloud Engineer":

        st.write("✔ AWS Cloud Practitioner")

        st.write("✔ AWS Solutions Architect")

    elif career == "AI Engineer":

        st.write("✔ Google AI Certification")

        st.write("✔ TensorFlow Developer")

    elif career == "Cyber Security":

        st.write("✔ CEH")

        st.write("✔ CompTIA Security+")

    elif career == "Data Analyst":

        st.write("✔ Google Data Analytics")

        st.write("✔ Microsoft Power BI")

st.markdown("---")

# -------------------------------
# Promotion Readiness
# -------------------------------

st.subheader("🚀 Promotion Readiness Score")

promotion = 80

st.progress(promotion)

st.write(f"Promotion Readiness : {promotion}%")

st.success("Continue learning leadership and cloud technologies.")

st.markdown("---")

# -------------------------------
# Career Switching Guide
# -------------------------------

st.subheader("🔄 Career Switching Guide")

current = st.selectbox(
    "Current Role",
    [
        "Python Developer",
        "Java Developer",
        "Manual Tester",
        "Support Engineer"
    ]
)

target = st.selectbox(
    "Target Role",
    [
        "AI Engineer",
        "Cloud Engineer",
        "Data Scientist",
        "DevOps Engineer"
    ]
)

if st.button("Generate Roadmap"):

    st.success(f"Roadmap : {current} ➜ {target}")

    st.write("Step 1 : Learn Python")

    st.write("Step 2 : Learn SQL")

    st.write("Step 3 : Learn Git")

    st.write("Step 4 : Build Projects")

    st.write("Step 5 : Earn Certifications")

    st.write("Step 6 : Update Resume")

    st.write("Step 7 : Apply for Jobs")

st.markdown("---")

# -------------------------------
# Weekly Goals
# -------------------------------

st.subheader("🎯 Weekly Goals")

st.checkbox("Complete AWS Course")

st.checkbox("Complete Docker Course")

st.checkbox("Update Resume")

st.checkbox("Practice Coding")

st.checkbox("Attend Webinar")

st.markdown("---")
st.subheader("🤖 AI Tools")

if st.button("Open AI Career Chatbot"):
    st.switch_page("pages/chatbot.py")
st.subheader("AI Resume")
if st.button("Open Resume Analyzer"):
    st.switch_page("pages/resume_analyzer.py")
st.markdown("---")
# -------------------------------
# Logout
# -------------------------------

if st.button("🚪 Logout"):

    logout()

    st.switch_page("app.py")