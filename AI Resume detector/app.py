import streamlit as st
import pdfplumber
import pandas as pd

# Page Configuration
st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and get skill analysis, resume score, and improvement suggestions.")

# Skills Database
skills_db = [
    "python",
    "java",
    "c++",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "sql",
    "html",
    "css",
    "javascript",
    "react",
    "streamlit",
    "data analysis",
    "data science",
    "power bi",
    "excel",
    "tensorflow",
    "pandas",
    "numpy",
    "scikit-learn",
    "github",
    "aws"
]

# Upload PDF
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file is not None:

    # Extract Text
    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    st.subheader("📋 Resume Text Preview")
    st.text_area("", text[:3000], height=250)

    text_lower = text.lower()

    # Skill Detection
    found_skills = []

    for skill in skills_db:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    missing_skills = list(set(skills_db) - set(found_skills))

    # Resume Score
    score = int((len(found_skills) / len(skills_db)) * 100)

    st.subheader("📊 Resume Score")

    if score >= 80:
        st.success(f"Excellent Resume Score: {score}/100")
    elif score >= 60:
        st.warning(f"Good Resume Score: {score}/100")
    else:
        st.error(f"Needs Improvement: {score}/100")

    # Found Skills
    st.subheader("✅ Skills Found")

    if found_skills:
        st.write(found_skills)
    else:
        st.warning("No matching skills detected.")

    # Missing Skills
    st.subheader("❌ Recommended Skills")

    st.write(missing_skills[:10])

    # Skill Summary Table
    st.subheader("📈 Skill Analysis")

    analysis_df = pd.DataFrame({
        "Detected Skills": pd.Series(found_skills),
    })

    st.dataframe(analysis_df)

    # Suggestions
    st.subheader("💡 Suggestions")

    if "github" not in found_skills:
        st.info("Add GitHub projects to strengthen your profile.")

    if "machine learning" not in found_skills:
        st.info("Include Machine Learning projects if you are applying for AI/ML roles.")

    if "python" not in found_skills:
        st.info("Python is highly recommended for AI/ML internships.")

    if "streamlit" not in found_skills:
        st.info("Mention Streamlit projects if you have built web applications.")

    st.success("Analysis Completed Successfully ✅")