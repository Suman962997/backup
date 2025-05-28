import pdfplumber
from itertools import product

def Has_the_entity(pdf_path):
    questions = [
        "Has the entity conducted",
        "eNumber of locations where plants and/or ",
        "operations/offices of the entity are situated"
    ]

    sections = [
        "cdcdc",
        "If there are any significant social",
        "Markets served by the entity - No of locations"
    ]

    result = {
        "matched_pair": None,
        "extracted_text": "",
        "table": [],
        "message": "No matching question pairs found."
    }

    with pdfplumber.open(pdf_path) as pdf:
        for q_start, q_end in product(questions, sections):
            start_page = None

            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if not text:
                    continue

                if q_start in text and q_end in text:
                    # Both on same page
                    tables = page.extract_tables()
                    q1_index = text.find(q_start) + len(q_start)
                    q2_index = text.find(q_end)
                    between_text = text[q1_index:q2_index].strip()

                    result["matched_pair"] = {"start": q_start, "end": q_end}
                    result["extracted_text"] = between_text
                    result["message"] = "Matched on same page."

                    if tables:
                        for table in tables:
                            if any(cell and cell in between_text for row in table for cell in row if cell):
                                result["table"] = table
                                result["message"] += " Table found between questions."
                                return result
                    return result

                elif q_start in text:
                    start_page = i
                elif q_end in text and start_page is not None:
                    for j in range(start_page + 1, i):
                        mid_tables = pdf.pages[j].extract_tables()
                        if mid_tables:
                            result["matched_pair"] = {"start": q_start, "end": q_end}
                            result["extracted_text"] = f"Table found between pages {start_page + 1} and {i}."
                            result["table"] = mid_tables[0]
                            result["message"] = "Matched across pages. Table found."
                            return result
                    return result

    return result

print(Has_the_entity("C:/Users/coda/Documents/ppap.pdf"))
