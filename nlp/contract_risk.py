def calculate_contract_risk(clauses):
    """
    Calculate overall contract risk from clause-level risks.
    """

    risk_score_map = {
        "Low": 1,
        "Medium": 2,
        "High": 3
    }

    total_score = 0
    clause_count = 0

    for clause in clauses:
        risk_level = clause.get("risk_level", "Low")
        total_score += risk_score_map.get(risk_level, 1)
        clause_count += 1

    if clause_count == 0:
        return {
            "contract_risk": "Low",
            "average_score": 1.0
        }

    average_score = total_score / clause_count

    if average_score <= 1.5:
        contract_risk = "Low"
    elif average_score <= 2.3:
        contract_risk = "Medium"
    else:
        contract_risk = "High"

    return {
        "contract_risk": contract_risk,
        "average_score": round(average_score, 2)
    }
