import streamlit as st

st.set_page_config(
    page_title="TalentSphere Elevate",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# Hide Default Streamlit UI
# -----------------------------
st.markdown("""
<style>

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

[data-testid="stSidebarNav"]{
display:none;
}

.block-container{
padding-top:0rem;
padding-bottom:0rem;
max-width:100%;
}

</style>
""",unsafe_allow_html=True)
# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>

.hero{
padding:70px 40px;
text-align:center;
background:linear-gradient(135deg,#2563eb,#7c3aed);
border-radius:25px;
color:white;
}

.hero h1{
font-size:58px;
font-weight:800;
margin-bottom:10px;
}

.hero p{
font-size:22px;
opacity:.95;
}

.stat-card{

background:white;
padding:25px;
border-radius:18px;
box-shadow:0 8px 25px rgba(0,0,0,.08);
text-align:center;
margin-top:15px;

}

.stat-card h2{

font-size:38px;
color:#2563eb;

}

.feature{

background:white;
padding:25px;
border-radius:18px;
box-shadow:0 8px 25px rgba(0,0,0,.08);
text-align:center;
height:220px;

}

.feature h1{

font-size:45px;

}

.feature h3{

color:#1f2937;

}

.feature p{

color:#6b7280;

}

</style>
""",unsafe_allow_html=True)
# -----------------------------
# Top Right Admin
# -----------------------------
c1, c2 = st.columns([9,1])

with c1:
    st.write("")

with c2:
    if st.button("⚙️ Admin"):
        st.switch_page("pages/admin_login.py")
# -----------------------------
# Hero
# -----------------------------
st.markdown("""
<div class="hero-section">
<div class="brand">
<div class="brand-logo">
🎓
</div>
<div class="brand-text">
<h1>Talent<span>Sphere</span> Elevate</h1>
<h3>AI-Powered Career Development Platform</h3>
</div>
</div>
<p class="hero-description">
Empowering students, professionals, teachers, and parents with
AI-driven career guidance, ATS resume analysis, coding practice,
mock interviews, and personalized learning roadmaps.
</p>

</div>
""", unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")

st.markdown(
"""
<h2 style="text-align:center;">
Get Started
</h2>

<p style="text-align:center;color:gray;">
Login or create your account to begin your AI-powered career journey.
</p>
""",
unsafe_allow_html=True
)
#LOGIN/REGISTER
c1, c2, c3 = st.columns(3)
with c1:
    if st.button(
        "🔐 Login",
        use_container_width=True
    ):
        st.switch_page("pages/login.py")

with c2:
    if st.button(
        "🎓 Student Register",
        use_container_width=True
    ):
        st.switch_page("pages/register.py")

with c3:
    if st.button(
        "👨‍🏫 Parent / Teacher Register",
        use_container_width=True
    ):
        st.switch_page("pages/parent_teacher_register.py")

st.divider()

# -----------------------------
# Platform Stats
# -----------------------------
st.subheader("📊 Platform Impact")

a,b,c,d=st.columns(4)

stats=[
("10K+","Students"),
("500+","Companies"),
("95%","Placement Success"),
("24/7","AI Support")
]

for col,item in zip([a,b,c,d],stats):

    with col:

        st.markdown(f"""

        <div class="stat-card">

        <h2>{item[0]}</h2>

        <p>{item[1]}</p>

        </div>

        """,unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

st.subheader("✨ Platform Features")
f1, f2, f3 = st.columns(3)
with f1:
    st.success("📄 ATS Resume Analyzer")
    st.success("💻 Coding Practice")
    st.success("🎤 Mock Interview")

with f2:
    st.info("🧠 Skill Gap Analysis")
    st.info("🗺 Personalized Learning Roadmap")
    st.info("🤖 AI Career Coach")

with f3:
    st.warning("🎯 Career Recommendation")
    st.warning("📊 Progress Dashboard")
    st.warning("🏆 Placement Preparation")
pages = {
    "High School": "pages/login.py",
    "College": "pages/login.py",
    "Professional": "pages/login.py",
    "Teacher": "pages/login.py",
    "Parent": "pages/login.py",
}

# -----------------------------
# Journey
# -----------------------------
# -----------------------------
# Journey
# -----------------------------

st.subheader("🎯 Choose Your Journey")

c1, c2, c3, c4, c5 = st.columns(5)

journeys = [
    ("🎓", "High School"),
    ("🏫", "College"),
    ("💼", "Professional"),
    ("👨‍🏫", "Teacher"),
    ("👨‍👩‍👧", "Parent")
]

cols = [c1, c2, c3, c4, c5]

for col, (icon, title) in zip(cols, journeys):

    with col:

        st.markdown(
            f"""
            <div class="journey-icon">
                {icon}
            </div>

            <div class="journey-title">
                {title}
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            f"Continue as {title}",
            key=title,
            use_container_width=True
        ):
            st.session_state.selected_role = title
            st.switch_page(pages[title])


# Show this before clicking
st.markdown("""
<h2 style="text-align:center;">
🚀 Start Your AI-Powered Career Journey Today
</h2>
""", unsafe_allow_html=True)
st.caption(
"© 2026 TalentSphere Elevate | AI Powered Career Development Platform"
)

st.caption("© 2026 TalentSphere Elevate | AI Powered Career Development Platform")