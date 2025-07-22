import pdfplumber
import pytesseract
from PIL import Image
import io
import re
import pandas as pd
import sec_a



# def  Textarea(pdf_file):

#     start_found = False
#     end_found = False
#     lines_between = []
#     custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

#     # Define multiple possible start and end strings
#     q_starts = [
#         "Details of business activities (accounting for 90% of the turnover)",
#         "Details of business activities",
#         "accounting for 90% of the turnover"

#     ]
#     q_ends = [
#         "Products/Services sold by the entity (accounting for 90% of the entity’s Turnover)",
#         "Products/Services sold by the",
#         "accounting for 90% of the entity’s Turnover"
        
#     ]
#     keys = [
#         "Description of Main Activity",
#         "Description of Business Activity",
#         "% of Turnover of the entity",

#     ]

#     keys_3 = [
#         "S.No",
#         "Description of Main Activity",
#         "Description of Business Activity",
#         "% of Turnover of the entity",
#     ]
#     with pdfplumber.open(pdf_file) as pdf:
#         for page in pdf.pages[:10]:
#             pil_image = page.to_image(resolution=300).original
#             text = pytesseract.image_to_string(pil_image, config=custom_config)

#             if not text:
#                 continue

#             for line in text.splitlines():
#                 # Check if line matches any start phrase
#                 if not start_found and any(start.lower() in line.lower() for start in q_starts):
#                     start_found = True
#                     continue  # skip the line containing start phrase

#                 # Check if line matches any end phrase
#                 if start_found and any(end.lower() in line.lower() for end in q_ends):
#                     end_found = True
#                     break

#                 if start_found:
#                     lines_between.append(line)

#             if end_found:
#                 break

#     if not start_found:
#         return [f"Start question not found:{q_starts[0]}"]
#     if not end_found:
#         return None
#     if not lines_between:
#         return {"error": "No content found between start and end questions."}

#     output_rows = []
#     for line in lines_between:
#         output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

#     final_3 = []
#     final_4 = []
#     for f in output_rows:
#         if len(f) == 3:
#             final_3.append(f)
#         elif len(f) == 4:
#             final_4.append(f)


    
#     myout = []

#     if len(final_3) > len(final_4):
#         for row in final_3:
#             data = dict(zip(keys, row))
#             myout.append(data)
#     elif len(final_4) > len(final_3):
#         for row in final_4:
#             data = dict(zip(keys_3, row))
#             myout.append(data)
#     else:
#         return "\n".join(lines_between)



#     if not myout:
#         return "Not Applicable"


#     return myout

# print(Textarea("C:/Users/coda/Documents/narendra.pdf"))
# print("************")




def  Table(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Details of business activities (accounting for 90% of the turnover)",
        "Details of business activities",
        "accounting for 90% of the turnover"

    ]
    q_ends = [
        "Products/Services sold by the entity (accounting for 90% of the entity’s Turnover)",
        "Products/Services sold by the",
        "accounting for 90% of the entity’s Turnover"
        
    ]
    keys = [
        "Description of Main Activity",
        "Description of Business Activity",
        "% of Turnover of the entity",

    ]

    keys_3 = [
        "S.No",
        "Description of Main Activity",
        "Description of Business Activity",
        "% of Turnover of the entity",
    ]
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            pil_image = page.to_image(resolution=300).original
            text = pytesseract.image_to_string(pil_image, config=custom_config)

            if not text:
                continue

            for line in text.splitlines():
                # Check if line matches any start phrase
                if not start_found and any(start.lower() in line.lower() for start in q_starts):
                    start_found = True
                    continue  # skip the line containing start phrase

                # Check if line matches any end phrase
                if start_found and any(end.lower() in line.lower() for end in q_ends):
                    end_found = True
                    break

                if start_found:
                    lines_between.append(line)

            if end_found:
                break

    if not start_found:
        return [f"Start question not found:{q_starts[0]}"]
    if not end_found:
        return None
    if not lines_between:
        return {"error": "No content found between start and end questions."}

    output_rows = []
    for line in lines_between:
        output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

    final_3 = []
    final_4 = []
    for f in output_rows:
        if len(f) == 3:
            final_3.append(f)
        elif len(f) == 4:
            final_4.append(f)


    
    myout = []

    if len(final_3) > len(final_4):
        for row in final_3:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_4) > len(final_3):
        for row in final_4:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return "\n".join(lines_between)



    if not myout:
        return "Not Applicable"


    return myout

print(Table("C:/Users/coda/Documents/narendra.pdf"))
print("************")



def  Radio(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Turnover rate for permanent employees and workers",
        "Turnover rate for permanent",
        "employees and workers"

    ]
    q_ends = [
        "Holding, Subsidiary and Associate Companies (including joint ventures)",
        "Holding, Subsidiary and Associate Companies",
        "including joint ventures"

    ]

    keys = [
    "Category",
    " FY (2024-25) Male",
    " FY (2024-25) Female",
    " FY (2024-25) Total",
    " FY (2023-24) Male",
    " FY (2023-24) Female",
    " FY (2023-24) Total",
    " FY (2022-23) Male",
    " FY (2022-23) Female",
    " FY (2022-23) Total",

    ]

    keys_3 = [
    "S.no",
    "Category",
    " FY (2024-25) Male",
    " FY (2024-25) Female",
    " FY (2024-25) Total",
    " FY (2023-24) Male",
    " FY (2023-24) Female",
    " FY (2023-24) Total",
    " FY (2022-23) Male",
    " FY (2022-23) Female",
    " FY (2022-23) Total",        
    ]
    

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[:10]:
            pil_image = page.to_image(resolution=300).original
            text = pytesseract.image_to_string(pil_image, config=custom_config)

            if not text:
                continue

            for line in text.splitlines():
                # Check if line matches any start phrase
                if not start_found and any(start.lower() in line.lower() for start in q_starts):
                    start_found = True
                    continue  # skip the line containing start phrase

                # Check if line matches any end phrase
                if start_found and any(end.lower() in line.lower() for end in q_ends):
                    end_found = True
                    break

                if start_found:
                    lines_between.append(line)

            if end_found:
                break


    if not start_found:
        return [f"Start question not found:{q_starts[0]}"]
    if not end_found:
        return None
    if not lines_between:
        return {"error": "No content found between start and end questions."}

    output_rows = []
    for line in lines_between:
        output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

    final_10 = []
    final_11 = []
    for f in output_rows:
        if len(f) == 10:
            final_10.append(f)
        elif len(f) == 11:
            final_11.append(f)

    myout = []
    # for row in output_rows:
    #     data = dict(zip(keys, row))
    #     myout.append(data)

    if len(final_10) > len(final_11):
        for row in final_10:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_11) > len(final_10):
        for row in final_11:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return "\n".join(lines_between)



    if not myout:
        return "Not Applicable"


    return myout

print(Radio("C:/Users/coda/Documents/narendra.pdf"))
print("************")



