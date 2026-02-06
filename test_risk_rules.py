from nlp.risk_rules import assess_risk

sample_clause = {
    "clause_id": "5",
    "title": "Termination",
    "text": "Either party may terminate this agreement without notice."
}

result = assess_risk(sample_clause)
print(result)
