import pdfplumber

question_1 = "Employees and workers (including differently abled)"
question_2 = "Differently abled employees and workers:"
def extract_table_between_questions(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if not text:
                continue

            if question_1 in text and question_2 in text:
                # Case: both questions on the same page
                tables = page.extract_tables()
                # Split text around the questions
                q1_index = text.find(question_1) + len(question_1)
                q2_index = text.find(question_2)
                between_text = text[q1_index:q2_index]
                # print("between text",between_text)

                print("Extracted text between questions:")
                print(between_text.strip())

                if tables:
                    for table in tables:
                        # Simple filter: check if any table row text appears in between_text
                        if any(cell and cell in between_text for row in table for cell in row if cell):
                            print("\n✅ Found matching table between questions:")
                            for row in table:
                                print(row)
                            return table
                print("No table found directly between the two questions.")
                return None

            elif question_1 in text:
                # Record that we found the first question, check next page
                start_page = i
            elif question_2 in text and 'start_page' in locals():
                # Case: table is likely on the page between these two
                for j in range(start_page + 1, i):
                    mid_tables = pdf.pages[j].extract_tables()
                    if mid_tables:
                        print("\n✅ Found table between pages:")
                        for table in mid_tables:
                            for row in table:
                                print(row)
                        return mid_tables[0]
                print("No table found on intermediate pages.")
                return None

    print("Could not find both questions in expected range.")
    return None

# Run the function
# extract_table_between_questions("your_report.pdf")

extract_table_between_questions("C:/Users/coda/Documents/siemens.pdf")
