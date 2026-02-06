from nlp.ner import extract_entities

sample_text = """
This agreement is between ABC Pvt Ltd and John Doe.
Payment of ₹5,00,000 shall be made within 30 days.
The agreement shall be governed by the laws of India.
"""

entities = extract_entities(sample_text)

for e in entities:
    print(e)
