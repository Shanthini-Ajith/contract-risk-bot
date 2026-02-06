from nlp.obligation_classifier import classify_obligation

clauses = [
    {"text": "The vendor shall deliver the goods within 10 days."},
    {"text": "Either party may terminate the agreement with notice."},
    {"text": "The employee shall not disclose confidential information."}
]

for c in clauses:
    print(classify_obligation(c))
