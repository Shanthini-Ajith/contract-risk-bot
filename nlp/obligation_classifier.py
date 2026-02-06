def classify_obligation(clause):
    text = clause["text"].lower()

    # PROHIBITION (check first)
    if "shall not" in text or "must not" in text or "is prohibited" in text:
        return {
            "clause_type": "Prohibition",
            "explanation": "This clause restricts certain actions."
        }

    # OBLIGATION
    if "shall" in text or "must" in text or "is required to" in text:
        return {
            "clause_type": "Obligation",
            "explanation": "This clause imposes a mandatory responsibility."
        }

    # RIGHT
    if "may" in text or "entitled to" in text:
        return {
            "clause_type": "Right",
            "explanation": "This clause grants a discretionary right."
        }

    # DEFAULT
    return {
        "clause_type": "Neutral",
        "explanation": "This clause does not clearly impose rights or obligations."
    }
