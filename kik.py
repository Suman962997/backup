import pdfplumber
import re

question_1 = "Details of business activities (accounting for 90% of the turnover)"
question_2 = "Products/Services sold by the entity"

def extract_text_between_questions(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        pages = []

        # Extract text from all pages
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                full_text += f"\n--- Page {i} ---\n{text}"
                pages.append((i, text))

        # Find positions of the questions
        start_idx = full_text.find(question_1)
        end_idx = full_text.find(question_2)

        if start_idx == -1 or end_idx == -1:
            print("One or both questions not found.")
            return None

        # Extract the content between the questions
        between_text = full_text[start_idx + len(question_1):end_idx]
        return between_text

pdf_path = "C:/Users/coda/Documents/deigeo.pdf"
text_between = extract_text_between_questions(pdf_path)

if text_between:
    print("Text between the questions:")
    print(text_between)
