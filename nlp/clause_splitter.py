import re

def extract_clauses(text):
    """
    Extracts clauses with clause_id, title, and text
    """
    pattern = r'(\d+)\.\s*([A-Za-z &]+)\n(.*?)(?=\n\d+\.|\Z)'
    matches = re.findall(pattern, text, re.S)

    clauses = []

    for clause_id, title, clause_text in matches:
        clauses.append({
            "clause_id": clause_id.strip(),
            "title": title.strip(),
            "text": clause_text.strip()
        })

    return clauses
