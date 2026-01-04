def recommend_roles(candidate, roles_df, top_n=3):
    skills = ["python", "sql", "excel", "statistics", "communication"]

    role_scores = []
    skill_gaps = {}

    for _, role in roles_df.iterrows():
        match_count = 0
        gaps = []

        for skill in skills:
            if candidate[skill] >= role[skill]:
                match_count += 1
            else:
                gaps.append(skill)

        match_pct = match_count / len(skills)

        role_scores.append({
            "role": role["role"],
            "match_score": match_pct
        })

        if gaps:
            skill_gaps[role["role"]] = gaps

    role_scores = sorted(role_scores, key=lambda x: x["match_score"], reverse=True)

    recommended_roles = [
        r["role"] for r in role_scores if r["match_score"] >= 0.6
    ][:top_n]

    return {
        "recommended_roles": recommended_roles,
        "role_match_scores": role_scores,
        "skill_gaps": skill_gaps
    }
