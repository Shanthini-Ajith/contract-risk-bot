import streamlit as st
import tempfile

# -------------------- NLP IMPORTS --------------------
from nlp.clause_splitter import extract_clauses
from nlp.obligation_classifier import classify_obligation
from nlp.risk_rules import assess_risk
from nlp.contract_risk import calculate_contract_risk

# -------------------- LLM (MOCK) --------------------
from llm.explain import explain_clause_with_llm

# -------------------- PDF EXPORT --------------------
from utils.pdf_export import generate_contract_pdf


# -------------------- STREAMLIT CONFIG --------------------
st.set_page_config(page_title="Contract Risk Analysis Bot", layout="wide")
st.title("📄 Contract Risk Analysis Bot")


# -------------------- SESSION STATE INIT --------------------
if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

if "clauses" not in st.session_state:
    st.session_state.clauses = None

if "contract_risk_result" not in st.session_state:
    st.session_state.contract_risk_result = None

if "pdf_bytes" not in st.session_state:
    st.session_state.pdf_bytes = None


# -------------------- INPUT --------------------
st.subheader("Paste Contract Text")
contract_text = st.text_area(
    "Paste your contract content below:",
    height=300
)


# -------------------- ANALYZE BUTTON --------------------
if st.button("Analyze Contract"):
    if not contract_text.strip():
        st.warning("Please paste contract text before analyzing.")
        st.session_state.analysis_done = False
    else:
        # STEP 4: Clause Extraction
        clauses = extract_clauses(contract_text)

        if not clauses:
            st.error("No clauses detected. Use numbered clauses like '1. Title'.")
            st.session_state.analysis_done = False
        else:
            # STEP 7: Obligation / Right / Prohibition
            for clause in clauses:
                clause.update(classify_obligation(clause))

            # STEP 9.2: Clause-level Risk
            for clause in clauses:
                clause.update(assess_risk(clause))

            # STEP 8: LLM Explanation (Mocked)
            for clause in clauses:
                clause.update(explain_clause_with_llm(clause))

            # STEP 9.3: Contract-level Risk
            contract_risk_result = calculate_contract_risk(clauses)

            # Save to session state
            st.session_state.clauses = clauses
            st.session_state.contract_risk_result = contract_risk_result
            st.session_state.analysis_done = True
            st.session_state.pdf_bytes = None


# -------------------- DISPLAY RESULTS --------------------
if st.session_state.analysis_done:

    clauses = st.session_state.clauses
    contract_risk_result = st.session_state.contract_risk_result

    st.success(f"{len(clauses)} clauses analyzed successfully")

    # -------------------- CONTRACT RISK SUMMARY --------------------
    st.subheader("📊 Contract Risk Summary")

    risk_icon = {
        "Low": "🟢",
        "Medium": "🟡",
        "High": "🔴"
    }

    st.markdown(
        f"""
### Overall Contract Risk: {risk_icon[contract_risk_result['contract_risk']]} {contract_risk_result['contract_risk']}
**Average Risk Score:** {contract_risk_result['average_score']}
"""
    )

    # -------------------- CLAUSE DETAILS --------------------
    st.subheader("📑 Clause-by-Clause Analysis")

    for clause in clauses:
        with st.expander(f"Clause {clause['clause_id']}: {clause['title']}"):

            st.markdown("### 📌 Clause Type")
            st.write(clause["clause_type"])

            st.markdown("### ⚠️ Risk Level")
            st.write(clause["risk_level"])

            st.markdown("### 🧾 Risk Reason")
            st.write(clause["risk_reason"])

            st.markdown("### 📄 Original Clause Text")
            st.write(clause["text"])

            st.markdown("### 🧠 Simple Explanation")
            st.write(clause["plain_explanation"])

            st.markdown("### ✅ Suggested Alternative")
            st.write(clause["suggested_alternative"])

    # -------------------- PDF EXPORT (ALWAYS VISIBLE) --------------------
    st.subheader("📥 Download Report")

    if st.button("Generate PDF Report"):
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp_file:
            pdf_path = tmp_file.name

        generate_contract_pdf(
            pdf_path,
            st.session_state.contract_risk_result,
            st.session_state.clauses
        )

        with open(pdf_path, "rb") as f:
            st.session_state.pdf_bytes = f.read()

        st.success("PDF generated successfully. Click below to download.")

    if st.session_state.pdf_bytes:
        st.download_button(
            label="⬇️ Download Contract Analysis PDF",
            data=st.session_state.pdf_bytes,
            file_name="contract_risk_report.pdf",
            mime="application/pdf"
        )
