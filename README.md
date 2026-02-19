# 🚀 Multi-Agent Resume Intelligence System

## 📌 Overview
The Multi-Agent Resume Intelligence System is an AI-powered application that analyzes resumes using Machine Learning, NLP, and Generative AI. The system follows an agent-based architecture to extract skills, predict job roles, generate interview questions, and provide resume improvement suggestions through an interactive Streamlit interface.

---

## 🧠 Features
- Upload Resume PDF
- Skill Extraction using NLP
- Job Role Prediction (TF-IDF + Logistic Regression)
- AI-Generated Interview Questions (Gemini API)
- Resume Feedback & Suggestions
- Interactive Streamlit Dashboard

---

## 🤖 Agent Workflow

Resume PDF → Text Extraction → Skill Extraction Agent → Role Prediction Agent (ML) → Interview Question Agent (GenAI) → Feedback Agent (GenAI) → Dashboard Output

---

## 🛠️ Tech Stack
Python • Streamlit • Scikit-learn • NLP (TF-IDF) • Google Gemini API • PDFMiner • Joblib • Git/GitHub

---

## 📂 Project Structure
multi_agent_resume_ai/
├── app.py
├── train_model.py
├── model.pkl
├── Resume.csv
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Setup

Clone repository:
```bash
git clone https://github.com/YOUR_USERNAME/multi-agent-resume-ai.git
cd multi-agent-resume-ai
Create virtual environment:

python -m venv .venv
Activate environment:

.venv\Scripts\activate
Install dependencies:

pip install -r requirements.txt
🔑 Gemini API Setup
Get API Key from:
https://aistudio.google.com/app/apikey

Add in app.py:

genai.configure(api_key="YOUR_API_KEY")
▶️ Run Application
python -m streamlit run app.py
Open in browser:

http://localhost:8501
📊 Model Training
python train_model.py
This generates model.pkl.

🎯 Highlights

Multi-Agent AI architecture
Generative AI integration
End-to-end ML pipeline
Real-world AI resume screening system

