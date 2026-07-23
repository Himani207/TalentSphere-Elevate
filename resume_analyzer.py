import streamlit as st
from ai.resume_ai import analyze_resume
from utils.pdf_report import create_report

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")

st.write("Upload your Resume (PDF)")

uploaded_file = st.file_uploader(
    "Choose Resume",
    type=["pdf"]
)

if uploaded_file:

    st.success("Resume Uploaded Successfully")

    if st.button("Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            result = analyze_resume(uploaded_file)

            st.success("Analysis Completed ✅")

            st.markdown(result)

            # Generate PDF Report
            pdf_file = create_report(result)

            # Download Button
            with open(pdf_file, "rb") as f:

                st.download_button(
                    label="📄 Download PDF Report",
                    data=f,
                    file_name="AI_Report.pdf",
                    mime="application/pdf"
                )