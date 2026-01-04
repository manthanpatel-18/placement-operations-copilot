# 📊 Placement Operations Copilot

An **agentic, rule-based decision-support system** designed to help placement managers evaluate candidate readiness, recommend suitable roles, analyze skill gaps, and define clear pre-interview action plans.

This project was developed as part of the **Imarticus Data Science Internship - Cohort 6 Assessment**.

---

## 🎯 Project Objective

The goal of this project is to build a **local, offline decision-support system** that assists placement teams in making **explainable and structured decisions**, rather than automated or black-box predictions.

The system focuses on:
- Readiness evaluation
- Role suitability analysis
- Strengths and gaps identification
- Clear next-action recommendations

---

## 🧠 System Overview

Placement Operations Copilot is a modular analytics system that:
- Reads candidate skill scores from structured data
- Applies heuristic and rule-based reasoning
- Matches candidates against role requirements
- Explains decisions transparently
- Presents insights through an interactive **Streamlit dashboard**

The system runs **fully offline** and does not use any external APIs or cloud services.

---

## 🔁 Core Workflows

### 1️⃣ Candidate Readiness Evaluation
- Classifies candidates as **Ready**, **Almost Ready**, or **Not Ready**
- Uses score thresholds and logical rules
- Provides reasoning for each decision

### 2️⃣ Role Suitability Recommendation
- Supports multiple roles:
  - Junior Data Analyst  
  - Data Analyst  
  - Business Analyst  
  - Data Engineer  
  - Data Scientist  
  - ML Intern
- Calculates **match percentage per role**
- Recommends top **2–3 best-fit roles**
- Highlights skill gaps preventing role readiness

### 3️⃣ Feedback & Gap Analysis
- Separates **strengths** and **improvement areas**
- Ensures clarity between diagnosis and action

### 4️⃣ Next Actions Summary
- Combines readiness, role fit, and gaps
- Suggests focused preparation areas
- Recommends an interview readiness timeline

---

## 👥 Multi-Candidate Support

- Candidates are loaded from `candidate_scores.csv`
- Dropdown selector enables switching between candidates
- Each candidate receives:
  - Unique readiness status
  - Different role recommendations
  - Personalized gaps and action plans

This makes the system scalable and closer to real-world placement operations.

---

## 🖥 Dashboard Features

- Candidate profile & skill score table
- Readiness status with explanation
- Role recommendations with:
  - Match percentage
  - Progress bars
  - Color-coded confidence
- Strengths vs gaps comparison
- Action-oriented next steps
- Clean and professional Streamlit UI

---

## 🗂 Project Structure
```
placement-operations-copilot/
├── app.py
├── README.md
├── code/
│ ├── main.py
│ ├── readiness_evaluator.py
│ ├── role_recommender.py
│ ├── feedback_analyzer.py
│ └── action_summary.py
├── data/
│ ├── candidate_scores.csv
│ └── role_requirements.csv
├── outputs/
│ ├── readiness_output.json
│ ├── role_fit_output.json
│ ├── feedback_analysis.json
│ └── final_action_summary.txt
└── report/
└── Placement_Operations_Copilot_Report.pdf
```

---

## ▶️ How to Run the Project

### Step 1: Generate Outputs
```bash
cd code
python main.py
```
### Step 2: Launch Dashboard
```
cd ..
streamlit run app.py
```
The dashboard will open locally in your browser.

## 🛠 Tech Stack

Language: Python

Libraries: Pandas, Streamlit

Data Formats: CSV, JSON, TXT

Execution Mode: Fully local & offline

## 👤 Author

**Manthan Patel**
- Linkedin: [Manthan Patel](https://www.linkedin.com/in/manthan-patel18)
- Portfolio: [yourwebsite.com](https://yourwebsite.com)
