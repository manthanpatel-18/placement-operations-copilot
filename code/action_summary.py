def generate_action_summary(readiness, roles, feedback):
    """
    Combines all workflow outputs into a single actionable summary.
    """

    summary = []
    summary.append(f"Candidate Readiness Status: {readiness['readiness_status']}")

    if roles["recommended_roles"]:
        summary.append(f"Recommended Role(s): {', '.join(roles['recommended_roles'])}")
    else:
        summary.append("No roles recommended currently")

    if feedback["gaps"]:
        summary.append("Focus Areas Before Interview:")
        for gap in feedback["gaps"]:
            summary.append(f"- {gap}")

    summary.append("Suggested interview scheduling: After 7 days of preparation")

    return "\n".join(summary)
