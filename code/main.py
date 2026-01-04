import json
import pandas as pd
from readiness_evaluator import evaluate_readiness
from role_recommender import recommend_roles
from feedback_analyzer import analyze_feedback
from action_summary import generate_action_summary

# Load data
scores_df = pd.read_csv("../data/candidate_scores.csv")
roles_df = pd.read_csv("../data/role_requirements.csv")
feedback = analyze_feedback("../data/mock_feedback.txt")

readiness_results = {}
role_results = {}
final_summaries = {}

for _, candidate in scores_df.iterrows():
    name = candidate["candidate_name"]

    readiness = evaluate_readiness(candidate)
    roles = recommend_roles(candidate, roles_df)

    summary = generate_action_summary(readiness, roles, feedback)

    readiness_results[name] = readiness
    role_results[name] = roles
    final_summaries[name] = summary

# Save outputs
with open("../outputs/readiness_output.json", "w") as f:
    json.dump(readiness_results, f, indent=4)

with open("../outputs/role_fit_output.json", "w") as f:
    json.dump(role_results, f, indent=4)

with open("../outputs/feedback_analysis.json", "w") as f:
    json.dump(feedback, f, indent=4)

with open("../outputs/final_action_summary.txt", "w") as f:
    json.dump(final_summaries, f, indent=4)

print("✅ Outputs generated for all candidates successfully.")
