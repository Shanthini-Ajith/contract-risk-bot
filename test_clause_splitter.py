from nlp.clause_splitter import extract_clauses

sample_text = """
4. Payment Terms
Payment shall be made within 15 days.

5. Termination
Either party may terminate this agreement with 30 days notice.

6. Governing Law
This agreement shall be governed by Indian law.
"""

clauses = extract_clauses(sample_text)

print("Number of clauses:", len(clauses))
for clause in clauses:
    print(clause)
