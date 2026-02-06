import pdfplumber
from docx import Document

def extract_pdf_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
    return text.strip()

def extract_docx_text(file):
    doc = Document(file)
    return "\n".join([p.text for p in doc.paragraphs]).strip()

def extract_txt_text(file):
    return file.read().decode("utf-8", errors="ignore").strip()

def extract_text(file):
    if file.type == "application/pdf":
        return extract_pdf_text(file)
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return extract_docx_text(file)
    elif file.type == "text/plain":
        return extract_txt_text(file)
    else:
        raise ValueError("Unsupported file format")
