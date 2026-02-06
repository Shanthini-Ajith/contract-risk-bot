import os

# Example using OpenAI-style API (logic only)
# Replace this with Claude if needed

def explain_clause_with_llm(clause):
    """
    Uses LLM to explain a contract clause in simple language.
    """

    clause_text = clause["text"]
    clause_title = clause["title"]

    prompt = f"""
You are a legal assistant for small business owners.

Explain the following contract clause in simple, non-legal language.
Then explain why it could be risky.
Then suggest a safer alternative clause.

Clause Title: {clause_title}
Clause Text:
\"\"\"
{clause_text}
\"\"\"

Respond in the following format:
Plain Explanation:
Risk Summary:
Suggested Alternative:
"""

    # ⚠️ MOCK RESPONSE for now (safe for demo & development)
    # Replace with real LLM call when needed
    return {
        "plain_explanation": "This clause explains the rules related to termination of the contract.",
        "risk_summary": "Depending on the terms, this clause could create uncertainty for the business.",
        "suggested_alternative": "Consider adding clear notice periods and mutual consent requirements."
    }
