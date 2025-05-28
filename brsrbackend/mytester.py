import pdfplumber

def  Does_the_entity_have_an_equal(pdf_path):
    question_keywords = [
        "Does the entity have an equal opportunity policy as per the Rights of Persons with Disabilities Act, 2016",
        "Does the entity have an equal",
        "web-link to the policy"
    ]

    stop_keywords = [
        "Return to work and Retention rates of permanent employees and workers that took parental leave",
        "Return to work and Retention",
        "employees and workers that took parental leave"
    ]

    # Convert to lowercase for faster comparisons
    question_keywords = [q.lower() for q in question_keywords]
    stop_keywords = [s.lower() for s in stop_keywords]

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue

            lines = text.splitlines()
            lower_lines = [line.lower() for line in lines]

            # Find start of relevant section
            for i, line in enumerate(lower_lines):
                if any(q in line for q in question_keywords):
                    start_index = i
                    # Now find end
                    for j in range(i + 1, len(lower_lines)):
                        if any(s in lower_lines[j] for s in stop_keywords):
                            return lines[start_index:j]
                    return lines[start_index:]  # If no stop marker found
    return []  # If no matching section found

print(Does_the_entity_have_an_equal("C:/Users/coda/Documents/deigeo.pdf"))
