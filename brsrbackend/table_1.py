import os
import re
from typing import List, Dict
from fastapi import FastAPI, Response
from dotenv import load_dotenv
from llama_parse import LlamaParse
import json
import uvicorn

app = FastAPI()
load_dotenv()


def extract_text_from_pdf(pdf_path: str) -> str:
    parser = LlamaParse(api_key=os.getenv("llama"), result_type="markdown")  # preserves table structure
    with open(pdf_path, "rb") as f:
        docs = parser.load_data(f, extra_info={"file_name": os.path.basename(pdf_path)})
    return "\n".join([doc.text for doc in docs])


def extract_tables_with_questions(text: str) -> List[Dict[str, str]]:
    tables_with_questions = []
    lines = text.splitlines()

    current_question = None
    current_table = []

    for i, line in enumerate(lines):
        # Detect table rows
        if re.match(r"^\s*\|.*\|\s*$", line):
            current_table.append(line)

        else:
            # Save the completed table
            if current_table:
                tables_with_questions.append({
                    "question": current_question or "Unknown Question",
                    "answer": "\n".join(current_table)
                })
                current_table = []

            # Detect a new potential question (non-empty and not a table)
            if line.strip() and not line.strip().startswith('|'):
                current_question = line.strip()

    # In case there's a table at the end
    if current_table:
        tables_with_questions.append({
            "question": current_question or "Unknown Question",
            "answer": "\n".join(current_table)
        })

    return tables_with_questions



# Step 3: Convert markdown table to structured JSON
def markdown_table_to_json(table: str) -> List[Dict[str, str]]:
    lines = table.strip().splitlines()
    if len(lines) < 2:
        return []

    headers = [cell.strip() for cell in lines[0].strip("|").split("|")]

    # Skip the markdown separator row
    data_rows = lines[2:] if re.match(r'^\s*\|?\s*-+', lines[1]) else lines[1:]

    json_data = []
    for row in data_rows:
        if not row.strip().startswith("|"):
            continue
        values = [cell.strip() for cell in row.strip("|").split("|")]

        if len(values) < len(headers):
            values += [""] * (len(headers) - len(values))

        row_dict = dict(zip(headers, values))
        json_data.append(row_dict)

    return json_data


# Step 4: Match provided questions to the best table
def match_questions_to_tables(tables: List[Dict[str, str]], questions: List[str]) -> Dict[str, List[Dict[str, str]]]:
    matched = {}
    for question in questions:
        best_table = None
        best_score = 0
        question_words = set(re.findall(r'\w+', question.lower()))

        for item in tables:
            table_question = item["question"]
            table_markdown = item["answer"]

            # Use header words for matching
            lines = table_markdown.strip().splitlines()
            if len(lines) < 2:
                continue

            headers = [h.strip().lower() for h in lines[0].strip("|").split("|")]
            header_words = set(" ".join(headers).split())

            score = len(question_words.intersection(header_words))

            if score > best_score:
                best_score = score
                best_table = table_markdown

        if best_table:
            matched[question] = markdown_table_to_json(best_table)
        else:
            matched[question] = [{"error": "Expected columns not found or no matching table found."}]

    return matched

@app.get("/llama_parse/")
async def llama_parse_function():
    # 📌 Add your questions here
    questions = [
        "Number of locations where plants and/or operations/offices of the entity are situated",
        "Details of business activities, products and services (accounting for 90% of the turnover)",
        "Products/Services sold by the entity (accounting for 90% of the entity’s Turnover)",
    ]

    # 📌 Set your PDF path here
    pdf_path = r"C:\Users\coda\Documents\titan.pdf"

    # ✅ Pipeline
    extracted_text = extract_text_from_pdf(pdf_path)
    tables = extract_tables_with_questions(extracted_text)
    results = match_questions_to_tables(tables, questions)

    return tables


if __name__ == "__main__":
    uvicorn.run("table_1:app", host="0.0.0.0", port=2000, reload=False, log_level="debug")
