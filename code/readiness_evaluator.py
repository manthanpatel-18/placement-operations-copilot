def evaluate_readiness(candidate):
    scores = [
        candidate["python"],
        candidate["sql"],
        candidate["excel"],
        candidate["statistics"],
        candidate["communication"]
    ]

    avg_score = sum(scores) / len(scores)

    reasoning = []
    improvements = []

    if avg_score >= 75:
        status = "Ready"
        reasoning.append("Strong overall assessment performance")
    elif avg_score >= 60:
        status = "Almost Ready"
        reasoning.append("Good fundamentals but improvement needed in some areas")
    else:
        status = "Not Ready"
        reasoning.append("Core skill gaps identified across multiple areas")

    if candidate["statistics"] < 70:
        reasoning.append("Statistics score is below recommended level")
        improvements.append("Revise statistics fundamentals and practice problem-solving")

    if candidate["communication"] < 70:
        reasoning.append("Communication confidence can be improved")
        improvements.append("Participate in mock interviews to build confidence")

    return {
        "readiness_status": status,
        "average_score": round(avg_score, 2),
        "reasoning": reasoning,
        "improvement_suggestions": improvements
    }
