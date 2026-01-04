import json
import pandas as pd
import streamlit as st


# Page Configuration

st.set_page_config(
    page_title="Placement Operations Copilot",
    layout="wide"
)

# Load Outputs (Generated per candidate)

with open("outputs/readiness_output.json") as f:
    readiness_all = json.load(f)

with open("outputs/role_fit_output.json") as f:
    roles_all = json.load(f)

with open("outputs/feedback_analysis.json") as f:
    feedback_all = json.load(f)

with open("outputs/final_action_summary.txt") as f:
    final_summary_all = json.load(f)


# Load Candidate Scores

scores_df = pd.read_csv("data/candidate_scores.csv")


# Sidebar Controls

st.sidebar.title("⚙️ Controls")

selected_candidate_name = st.sidebar.selectbox(
    "Select Candidate",
    scores_df["candidate_name"].tolist()
)

candidate = scores_df[
    scores_df["candidate_name"] == selected_candidate_name
].iloc[0]

# Fetch candidate-specific outputs
readiness = readiness_all[selected_candidate_name]
roles = roles_all[selected_candidate_name]
final_summary = final_summary_all[selected_candidate_name]


# Header

st.title("📊 Placement Operations Copilot")
st.subheader("Decision-Support Dashboard for Placement Managers")
st.divider()


# Candidate Profile

st.markdown("## 👤 Candidate Profile")

avg_score = round(
    (
        candidate["python"]
        + candidate["sql"]
        + candidate["excel"]
        + candidate["statistics"]
        + candidate["communication"]
    ) / 5,
    2
)

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Candidate Name", candidate["candidate_name"])

with c2:
    st.metric("Average Score", avg_score)

with c3:
    st.metric("Readiness Status", readiness["readiness_status"])

st.markdown("### 📊 Skill-wise Scores")

skills_df = pd.DataFrame({
    "Skill": ["Python", "SQL", "Excel", "Statistics", "Communication"],
    "Score": [
        candidate["python"],
        candidate["sql"],
        candidate["excel"],
        candidate["statistics"],
        candidate["communication"]
    ]
})

st.dataframe(skills_df, use_container_width=True)
st.divider()


# Candidate Readiness

st.markdown("## 🧠 Candidate Readiness")

if readiness["readiness_status"] == "Ready":
    st.success("🟢 Ready for placement")
elif readiness["readiness_status"] == "Almost Ready":
    st.warning("🟡 Almost ready — minor improvements required")
else:
    st.error("🔴 Not ready for placement")

st.markdown("**Reasoning:**")
for r in readiness["reasoning"]:
    st.write(f"- {r}")

st.divider()


# Role Recommendations (with match %)

st.markdown("## 🎯 Role Recommendations")

for role in roles["role_match_scores"]:
    role_name = role["role"]
    match_pct = int(role["match_score"] * 100)

    col1, col2 = st.columns([4, 1])

    with col1:
        st.markdown(f"### {role_name}")
        st.progress(match_pct / 100)

    with col2:
        if match_pct >= 80:
            st.success(f"{match_pct}%")
        elif match_pct >= 60:
            st.warning(f"{match_pct}%")
        else:
            st.error(f"{match_pct}%")

    if role_name in roles["skill_gaps"]:
        with st.expander("View Skill Gaps"):
            for gap in roles["skill_gaps"][role_name]:
                st.write(f"- {gap}")

st.divider()


# Strengths & Gaps

st.markdown("## 📌 Strengths & Gaps")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### ✅ Strengths")
    for s in feedback_all["strengths"]:
        st.write(f"- {s}")

with col2:
    st.markdown("### ⚠️ Gaps")
    for g in feedback_all["gaps"]:
        st.write(f"- {g}")

st.divider()

# Next Actions Summary (Action-Oriented)

st.markdown("## 📋 Next Actions Summary")

c1, c2 = st.columns(2)

# Placement Decision
with c1:
    st.markdown("### 🧠 Placement Decision")

    if readiness["readiness_status"] == "Ready":
        st.success("Candidate is ready for interviews")
    elif readiness["readiness_status"] == "Almost Ready":
        st.warning("Candidate is almost ready — minor improvements required")
    else:
        st.error("Candidate is not ready for placement yet")

    st.markdown("**Recommended Roles:**")
    for r in roles["recommended_roles"]:
        st.write(f"• {r}")

# Pre-interview Preparation
with c2:
    st.markdown("### 🛠️ Pre-Interview Preparation")

    action_map = {
        "Needs improvement in statistics": "Revise core statistics concepts and solve practice questions",
        "Communication confidence can be improved": "Conduct mock interviews and practice structured explanations"
    }

    st.markdown("**Recommended Actions (Next 7 Days):**")
    for gap in feedback_all["gaps"]:
        st.write(f"- {action_map.get(gap, 'Targeted practice for identified gap')}")

    st.info("📅 Schedule interview after **7 days** of focused preparation")
