def assess_risk(clause):
    """
    Assess legal risk of a clause using rule-based logic.
    """

    text = clause["text"].lower()

    # HIGH RISK
    if "without notice" in text:
        return {
            "risk_level": "High",
            "risk_reason": "Termination without notice can cause sudden business disruption."
        }

    if "penalty" in text or "liquidated damages" in text:
        return {
            "risk_level": "High",
            "risk_reason": "Penalty clauses may lead to heavy financial loss."
        }

    if "unilateral" in text or "sole discretion" in text:
        return {
            "risk_level": "High",
            "risk_reason": "Unilateral rights unfairly favor one party."
        }

    # MEDIUM RISK
    if "auto-renew" in text or "automatically renew" in text:
        return {
            "risk_level": "Medium",
            "risk_reason": "Auto-renewal clauses may lock the business into unwanted commitments."
        }

    if "arbitration" in text or "jurisdiction" in text:
        return {
            "risk_level": "Medium",
            "risk_reason": "Arbitration or jurisdiction clauses may increase dispute costs."
        }

    # LOW RISK (DEFAULT)
    return {
        "risk_level": "Low",
        "risk_reason": "No major legal risk detected in this clause."
    }
