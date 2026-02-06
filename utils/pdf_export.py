from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_contract_pdf(file_path, contract_risk_result, clauses):
    """
    Generate a PDF summary of contract analysis.
    """

    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(file_path, pagesize=A4)

    story = []

    # ---- TITLE ----
    story.append(Paragraph("<b>Contract Risk Analysis Report</b>", styles["Title"]))
    story.append(Spacer(1, 12))

    # ---- CONTRACT SUMMARY ----
    story.append(Paragraph("<b>Overall Contract Risk</b>", styles["Heading2"]))
    story.append(
        Paragraph(
            f"Risk Level: <b>{contract_risk_result['contract_risk']}</b><br/>"
            f"Average Risk Score: {contract_risk_result['average_score']}",
            styles["Normal"]
        )
    )
    story.append(Spacer(1, 12))

    # ---- CLAUSE DETAILS ----
    story.append(Paragraph("<b>Clause-by-Clause Analysis</b>", styles["Heading2"]))
    story.append(Spacer(1, 12))

    for clause in clauses:
        story.append(
            Paragraph(
                f"<b>Clause {clause['clause_id']}: {clause['title']}</b>",
                styles["Heading3"]
            )
        )

        story.append(Paragraph(f"<b>Clause Type:</b> {clause['clause_type']}", styles["Normal"]))
        story.append(Paragraph(f"<b>Risk Level:</b> {clause['risk_level']}", styles["Normal"]))
        story.append(Paragraph(f"<b>Risk Reason:</b> {clause['risk_reason']}", styles["Normal"]))
        story.append(Spacer(1, 6))

        story.append(Paragraph("<b>Original Clause</b>", styles["Italic"]))
        story.append(Paragraph(clause["text"], styles["Normal"]))
        story.append(Spacer(1, 6))

        story.append(Paragraph("<b>Simple Explanation</b>", styles["Italic"]))
        story.append(Paragraph(clause["plain_explanation"], styles["Normal"]))
        story.append(Spacer(1, 6))

        story.append(Paragraph("<b>Suggested Alternative</b>", styles["Italic"]))
        story.append(Paragraph(clause["suggested_alternative"], styles["Normal"]))
        story.append(Spacer(1, 18))

    doc.build(story)
