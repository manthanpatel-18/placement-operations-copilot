def analyze_feedback(feedback_path):
    """
    Analyzes interview feedback text to extract strengths, gaps,
    and creates a 7-day preparation plan.
    """

    with open(feedback_path, "r") as file:
        feedback = file.read().lower()

    strengths = []
    gaps = []

    if "strong" in feedback or "clear" in feedback:
        strengths.append("Strong conceptual understanding")

    if "sql" in feedback:
        strengths.append("Good SQL knowledge")

    if "hesitation" in feedback or "statistics" in feedback:
        gaps.append("Needs improvement in statistics")

    if "confidence dropped" in feedback or "communication" in feedback:
        gaps.append("Communication confidence can be improved")

    plan = {
        "Day 1-2": "Revise statistics fundamentals",
        "Day 3": "Practice SQL and Python problems",
        "Day 4": "Mock interview focusing on weak areas",
        "Day 5": "Feedback review and improvement",
        "Day 6": "Full-length mock interview",
        "Day 7": "Light revision and confidence building"
    }

    return {
        "strengths": strengths,
        "gaps": gaps,
        "7_day_preparation_plan": plan
    }
