import os
import re
from typing import List, Dict
from dotenv import load_dotenv
from llama_parse import LlamaParse
from difflib import SequenceMatcher
import time


load_dotenv()

def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def extract_text_from_pdf(pdf_path: str) -> str:
    parser = LlamaParse(api_key=os.getenv("llama"), result_type="markdown")
    with open(pdf_path, "rb") as f:
        docs = parser.load_data(f, extra_info={"file_name": os.path.basename(pdf_path)})
    return "\n".join([doc.text for doc in docs])


def extract_tables_with_questions(text: str) -> List[Dict[str, str]]:
    # print(text)
    tables_with_questions = []
    lines = text.splitlines()

    current_question = None
    current_table = []

    for line in lines:
        if re.match(r"^\s*\|.*\|\s*$", line):  # Detect markdown table rows
            current_table.append(line)
        else:
            if current_table:
                if len(current_table) >= 2:  # Minimum: header + 1 row
                    tables_with_questions.append({
                        "question": current_question or "Unknown Question",
                        "answer": "\n".join(current_table)
                    })
                current_table = []

            if line.strip() and not line.strip().startswith("|"):
                current_question = line.strip()
    # Catch any table at EOF
    if current_table and len(current_table) >= 2:
        
        tables_with_questions.append({
            "question": current_question or "Unknown Question",
            "answer": "\n".join(current_table)
        })

    return tables_with_questions


def markdown_table_to_json(table: str) -> List[Dict[str, str]]:
    lines = table.strip().splitlines()
    if len(lines) < 2:
        return []

    headers = [cell.strip() for cell in lines[0].strip("|").split("|")]
    data_rows = lines[2:] if re.match(r'^\s*\|?\s*-+', lines[1]) else lines[1:]

    json_data = []
    for row in data_rows:
        if not row.strip().startswith("|"):
            continue
        values = [cell.strip() for cell in row.strip("|").split("|")]
        if len(values) < len(headers):
            values += [""] * (len(headers) - len(values))
        json_data.append(dict(zip(headers, values)))
    return json_data

def match_questions_to_tables(tables: List[Dict[str, str]], questions: List[str]) -> Dict[str, List[Dict[str, str]]]:
    matched = {}
    for user_question in questions:
        best_match = None
        best_score = 0.0

        for item in tables:
            extracted_question = item["question"]
            score = similarity(user_question, extracted_question)

            if score > best_score:
                best_score = score
                best_match = item

        # Optional threshold to avoid bad matches
        if best_match and best_score > 0.6:
            matched[user_question] = markdown_table_to_json(best_match["answer"])
        else:
            matched[user_question] = [{"error": "No good match found for this question."}]

    return matched



##################################QUESTIONS#############################################


# def table(result: Dict[str, List[Dict[str, str]]],qdict:Dict):
#     question=qdict.get("question",None)
#     column=qdict.get("columns",None)
#     # print("result",result)
#     print("question",question)
#     print("column",column)
    
#     table_json =result.get(question, None)
#     column =column

#     if not table_json:
#         return []

#     filtered_table = []
#     for row in table_json:
#         filtered_row = {}
#         for canonical_col, aliases in column.items():
#             for alias in aliases:
#                 if alias in row:
#                     filtered_row[canonical_col] = row[alias]
#                     break
#             else:
#                 filtered_row[canonical_col] = ""  # default if none found
#         filtered_table.append(filtered_row)

#     return filtered_table

def normalize(text: str) -> str:
    """Lowercase, remove punctuation, extra whitespace."""
    return re.sub(r'\s+', ' ', re.sub(r'[^\w\s]', '', text.lower())).strip()

def fuzzy_match(target: str, candidates: List[str], threshold: float = 0.85) -> str:
    """Return best fuzzy match from candidates based on similarity threshold."""
    target_norm = normalize(target)
    best_match = ""
    best_score = 0.0
    for candidate in candidates:
        score = SequenceMatcher(None, target_norm, normalize(candidate)).ratio()
        if score > best_score and score >= threshold:
            best_match = candidate
            best_score = score
    return best_match if best_match else None

def table(result: Dict[str, List[Dict[str, str]]], qdict: Dict) -> List[Dict[str, str]]:
    question = qdict.get("question", "")
    column = qdict.get("columns", {})

    print("question:", question)
    print("column:", column)

    # Normalize all keys in result to match against normalized question
    normalized_result = {normalize(k): v for k, v in result.items()}
    matched_question_key = fuzzy_match(question, list(result.keys()))

    if not matched_question_key:
        print("❌ No matching question found.")
        return []

    table_json = result[matched_question_key]
    if not table_json or (len(table_json) == 1 and 'error' in table_json[0]):
        print("⚠️ Table not found or contains error.")
        return []

    filtered_table = []
    for row in table_json:
        filtered_row = {}
        row_keys = list(row.keys())
        for canonical_col, aliases in column.items():
            matched_key = None
            for alias in aliases:
                matched_key = fuzzy_match(alias, row_keys)
                if matched_key:
                    break
            filtered_row[canonical_col] = row.get(matched_key, "") if matched_key else ""
        filtered_table.append(filtered_row)

    return filtered_table




def llama_parse_function(pdf_path:str):
    start_time = time.time()  # ⏱ Start time 
    
    
    questions = [
        "Whether your entity’s policy/policies cover each principle and its core elements of the NGRBCs. (Yes/No)",
        "Has the policy been approved by the Board? (Yes/No)",
        "Whether the entity has translated the policy into procedures. (Yes / No)",
        "Do the enlisted policies extend to your value chain partners? (Yes/No)",
        "Name of the national and international codes/ certifications/labels/ standards (e.g. Forest Stewardship Council, Fairtrade, Rainforest Alliance,Trustea) standards (e.g. SA 8000, OHSAS, ISO, BIS) adopted by your entity and mapped to each principle.",
        "Specific commitments, goals and targets set by the entity with defined timelines, if any.",
        "Does the entity have a specified Committee of the Board/ Director responsible for decision making on sustainability related issues? (Yes / No). If yes, provide details."
        "Indicate whether review was undertaken by Director / Committee of the Board/ Any other Committee",
        "Frequency(Annually/ Half yearly/ Quarterly/ Any other – please specify)",
        "Has the entity carried out independent assessment/ evaluation of the working of its policies by an external agency? (Yes/No). If yes, provide name of the agency.",
        "If answer to question (1) above is “No” i.e. not all Principles are covered by a policy, reasons to be stated, as below:",
    ]

    # pdf_path = r"C:\Users\coda\Documents\titan.pdf"

    text = extract_text_from_pdf(pdf_path)
    tables = extract_tables_with_questions(text)
    results = match_questions_to_tables(tables, questions)


    end_time = time.time()  # End time
    total_seconds = end_time - start_time
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)
    print(f"\n⏱ Execution Time: {minutes} minutes, {seconds} seconds")        # if os.path.exists(temp_path):
    print("****",results)
    return results



    
        
        


