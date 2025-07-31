import os
import re
import json
from typing import List, Dict
from fastapi import FastAPI
from dotenv import load_dotenv
from llama_parse import LlamaParse
import uvicorn
from difflib import SequenceMatcher
import time
import sec_a

app = FastAPI()
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



def fuzzy_get(result: Dict[str, List[Dict[str, str]]], target_question: str, threshold: float = 0.5):
    best_key = None
    best_score = 0.0
    for key in result.keys():
        score = similarity(key, target_question)
        if score > best_score:
            best_score = score
            best_key = key
    if best_score >= threshold:
        return result.get(best_key)
    return None


##################################QUESTIONS#############################################


def table(result: Dict[str, List[Dict[str, str]]],qdict:Dict):
    question=qdict.get("question",None)
    column=qdict.get("columns",None)
    # print("result",result)
    print("question",question)
    print("column",column)
    
    table_json =result.get(question, None)
    column =column

    if not table_json:
        return []

    filtered_table = []
    for row in table_json:
        filtered_row = {}
        for canonical_col, aliases in column.items():
            for alias in aliases:
                if alias in row:
                    filtered_row[canonical_col] = row[alias]
                    break
            else:
                filtered_row[canonical_col] = ""  # default if none found
        filtered_table.append(filtered_row)

    return filtered_table

# def Products_Services(result: Dict[str, List[Dict[str, str]]]):
#     table_json = result.get("Products/Services sold by the entity (accounting for 90% of the entity’s Turnover)", None)

#     column = {
#     "Product/Service": ["Product/Service", "Product-Service"],
#     "NIC Code":["NIC Code"],
#     "% of total Turnover contributed":["% of total Turnover contributed"],
#     }

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

# def Number_of_locations_where(result: Dict[str, List[Dict[str, str]]]):
#     table_json = result.get("Number of locations where plants and/or operations/offices of the entity are situated", None)

#     column = {
#         "Location": ["Location", "Locations"],
#         "No. of plants": ["No. of plants", "Number of plants"],
#         "No. of offices": ["No. of offices", "Number of offices"],
#         "Total": ["Total", "Total*"]
#     }

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

# def Number_of_locations(result: Dict[str, List[Dict[str, str]]]):
#     table_json = result.get("Number of locations", None)

#     column = {
#         "Location": ["Location", "Locations"],
#         "Number": ["Total", "Total*","Number"]
#     }

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



# @app.get("/llama_parse/")
def llama_parse_function(pdf_path:str):
    start_time = time.time()  # ⏱ Start time 
    
    questions = [
        "Details of business activities, products and services (accounting for 90% of the turnover)",
        "Products/Services sold by the entity (accounting for 90% of the entity’s Turnover)",
        "Number of locations where plants and/or operations/offices of the entity are situated",
        "Number of locations",
        "Employees and workers (including differently abled):",
        "Differently abled Employees and workers:",
        "Participation/Inclusion/Representation of women",
        "Turnover rate for permanent employees and workers (Disclose trends for the past 3 years)",
        "Names of holding / subsidiary / associate companies / joint ventures",
        "Complaints/Grievances on any of the principles (Principles 1 to 9) under the National Guidelines on Responsible Business Conduct:",
        "Please indicate material responsible business conduct and sustainability issues pertaining to environmental and social matters that present a risk or an opportunity to your business, rationale for identifying the same, approach to adapt or mitigate the risk along-with its financial implications, as per the following format."
    ]

    # pdf_path = r"C:\Users\coda\Documents\titan.pdf"

    text = extract_text_from_pdf(pdf_path)
    tables = extract_tables_with_questions(text)
    results = match_questions_to_tables(tables, questions)

    # print(Details_of_business(results))
    # print('******************')
    # print(Products_Services(results))
    # print('******************')
    # print(Number_of_locations_where(results))
    # print('******************')
    # print(Number_of_locations(results))
    # print('******************')

    end_time = time.time()  # End time
    total_seconds = end_time - start_time
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)
    print(f"\n⏱ Execution Time: {minutes} minutes, {seconds} seconds")        # if os.path.exists(temp_path):

    return results



    
        
        




# if __name__ == "__main__":
#     uvicorn.run("table_1:app", host="0.0.0.0", port=2000, reload=False)
