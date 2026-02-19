import streamlit as st
import joblib
import re
from pdfminer.high_level import extract_text
import google.generativeai as genai

# ----------------------------
# CONFIGURE GEMINI API
# ----------------------------
genai.configure(api_key="AIzaSyB8BYQGmm6GA1eabQdYPsqF3KMzJo5IQZo")
llm = genai.GenerativeModel("gemini-2.5-flash")

# ----------------------------
# LOAD TRAINED ML MODEL
# ----------------------------
model = joblib.load("model.pkl")

# ----------------------------
# AGENT 1: SKILL EXTRACTION
# ----------------------------
def skill_agent(text):
    skills = [
        "python", "machine learning", "data science",
        "sql", "nlp", "deep learning",
        "tensorflow", "pandas", "numpy",
        "power bi", "tableau"
    ]
    found = [s for s in skills if s in text.lower()]
    return found

# ----------------------------
# AGENT 2: ROLE PREDICTION
# ----------------------------
def role_agent(text):
    cleaned = re.sub(r'\W', ' ', text)
    role = model.predict([cleaned])[0]
    return role

# ----------------------------
# AGENT 3: INTERVIEW QUESTIONS
# ----------------------------
def interview_agent(text):
    prompt = f"""
    You are an AI interview assistant.
    Based on the following resume, generate 5 technical interview questions.

    Resume:
    {text}
    """
    try:
        response = llm.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating interview questions: {e}"

# ----------------------------
# AGENT 4: RESUME FEEDBACK
# ----------------------------
def feedback_agent(text):
    prompt = f"""
    Analyze this resume and provide:
    1. Skill gaps
    2. Improvement suggestions
    3. Formatting improvements

    Resume:
    {text}
    """
    try:
        response = llm.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating feedback: {e}"

# ----------------------------
# STREAMLIT UI
# ----------------------------
st.set_page_config(page_title="Multi-Agent Resume Intelligence", layout="wide")

st.title("🚀 Multi-Agent Resume Intelligence System")
st.write("Upload a resume PDF to analyze skills, predict job role, and generate AI-based interview questions.")

uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

if uploaded_file:
    text = extract_text(uploaded_file)

    with st.spinner("Analyzing Resume..."):

        skills = skill_agent(text)
        role = role_agent(text)
        questions = interview_agent(text)
        feedback = feedback_agent(text)

    st.success("Analysis Complete ✅")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔎 Extracted Skills")
        st.write(skills)

        st.subheader("💼 Predicted Job Role")
        st.write(role)

    with col2:
        st.subheader("🧠 Interview Questions")
        st.write(questions)

    st.subheader("📈 Resume Improvement Suggestions")
    st.write(feedback)
