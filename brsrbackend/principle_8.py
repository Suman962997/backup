import pdfplumber
import pytesseract
from PIL import Image
import io
import re

                                ###### PRINCIPLE VIII #######

def  Details_of_Social_Impact(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Details of Social Impact Assessments (SIA) of projects undertaken by the entity",
        "Details of Social Impact Assessments",
        "the current financial year"
    ]
    q_ends = [
        "Provide information on project(s) for which ongoing Rehabilitation and Resettlement",
        "Provide information on project",
        "entity, in the following format"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[15:]:
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
        return {"error": f"Start question not found. Tried: {q_starts}"}
    if not end_found:
        return {"error": f"End question not found. Tried: {q_ends}"}
    if not lines_between:
        return {"error": "No content found between start and end questions."}

    # # print("#######",lines_between)
    output_rows = []
    for line in lines_between:
        output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

    final_6 = []
    final_7 = []
    for f in output_rows:
        if len(f) == 6:
            final_6.append(f)
        elif len(f) == 7:
            final_7.append(f)

    keys = [
        "Name and brief details of project",
        "SIA Notification No.",
        "Date of notification",
        "Whether conducted by independent external agency (Yes / No)",
        "Results communicated in public domain (Yes / No)",
        "Relevant Web link"
    ]

    myout = []
    # for row in final_5:
    #     data = dict(zip(keys, row))
    #     myout.append(data)

    if len(final_7) > len(final_6):
        for row in final_7:
            data = dict(zip(keys, row))
            myout.append(data)
    else:
        for row in output_rows:
            data = dict(zip(keys, row))
            myout.append(data)


    if not myout:
        return None


    return myout

# print(Details_of_Social_Impact("C:/Users/coda/Documents/bse.pdf"))
# print("************")


def  Provide_information_on_project(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Provide information on project(s) for which ongoing Rehabilitation and Resettlement",
        "Provide information on project",
        "your entity, in the following format"
    ]
    q_ends = [
        "Describe the mechanisms to receive and redress grievances of the community",
        "Describe the mechanisms to receive and redress grievances of the community",
        "grievances of the community"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[15:]:
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
        return {"error": f"Start question not found. Tried: {q_starts}"}
    if not end_found:
        return {"error": f"End question not found. Tried: {q_ends}"}
    if not lines_between:
        return {"error": "No content found between start and end questions."}

    # # print("#######",lines_between)
    output_rows = []
    for line in lines_between:
        output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

    final_6 = []
    final_7 = []
    for f in output_rows:
        if len(f) == 6:
            final_6.append(f)
        elif len(f) == 7:
            final_7.append(f)

    keys = [
        "S.No.",
        "Name of Project for which R&R is ongoing",
        "State",
        "District",
        "No. of Project Affected Families (PAFs)",
        "% of PAFs covered by R&R",
        "Amounts paid to PAFs in the FY (In INR)",
    ]

    myout = []
    for row in output_rows:
        data = dict(zip(keys, row))
        myout.append(data)

    # if len(final_7) > len(final_6):
    #     for row in final_7:
    #         data = dict(zip(keys, row))
    #         myout.append(data)
    # else:
    #     for row in final_6:
    #         data = dict(zip(keys, row))
    #         myout.append(data)


    if not myout:
        return None


    return myout

# print(Provide_information_on_project("C:/Users/coda/Documents/bse.pdf"))
# print("************")



def Describe_the_mechanisms(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question="Describe the mechanisms to receive and redress grievances of the community"
        question_2="Describe the mechanisms"
        question_3="grievances of the community"
        for i, page in enumerate(pdf.pages[15:]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Percentage of input material (inputs to total inputs by value) sourced from suppliers"
                sec_quest_2="Percentage of input material" 
                sec_quest_3="sourced from suppliers"
                list=[]     
                for i, line in enumerate(lines):
                     #(i,line)
                    if question.lower() in line.lower():
                        #("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        #("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        list=lines[i:]
                        break
                 #("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     #("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      #("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        #(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        #("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 #("finallist",finallist)
                return finallist                       

# print(Describe_the_mechanisms("C:/Users/coda/Documents/bse.pdf"))
# print("************")



def  Provide_information_on_project(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Percentage of input material (inputs to total inputs by value) sourced from suppliers",
        "Percentage of input material",
        " sourced from suppliers"
    ]
    q_ends = [
        "PRINCIPLE 9",
        "Businesses should engage with and provide value to their consumers in a responsible manner",
        "Describe the mechanisms"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[15:]:
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
        return {"error": f"Start question not found. Tried: {q_starts}"}
    if not end_found:
        return {"error": f"End question not found. Tried: {q_ends}"}
    if not lines_between:
        return {"error": "No content found between start and end questions."}

    # # print("#######",lines_between)
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

    keys = [
        "Category",
        "FY 2024-25 Current Financial Year",
        "FY 2023-24 Previous Financial Year"
    ]

    keys_2 = [
        "S.No.",
        "Category",
        "FY 2024-25 Current Financial Year",
        "FY 2023-24 Previous Financial Year"
    ]
    
    

    myout = []
    for row in output_rows:
        data = dict(zip(keys, row))
        myout.append(data)

    if len(final_3) > len(final_4):
        for row in final_3:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_4) > len(final_3):
        for row in final_4:
            data = dict(zip(keys_2, row))
            myout.append(data)
    else:
        return lines_between



    if not myout:
        return None


    return myout

# print(Provide_information_on_project("C:/Users/coda/Documents/bse.pdf"))
# print("************")

def  Describe_the_mechanisms_to_receive(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Describe the mechanisms to receive and redress grievances of the community",
        "Describe the mechanisms to receive",
        "redress grievances of the community"
    ]
    q_ends = [
        "Percentage of input material (inputs to total inputs by value) sourced from suppliers",
        "inputs to total inputs by value",
        "sourced from suppliers"
        
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[15:]:
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
        return {"error": f"Start question not found. Tried: {q_starts}"}
    if not end_found:
        return {"error": f"End question not found. Tried: {q_ends}"}
    if not lines_between:
        return {"error": "No content found between start and end questions."}

    # print("#######",lines_between)
    if lines_between:
        return lines_between
    else :
        return None

# print(Describe_the_mechanisms_to_receive("C:/Users/coda/Documents/bse.pdf"))
# print("************")




def  Percentage_of_input_material(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Percentage of input material (inputs to total inputs by value) sourced from suppliers",
        "inputs to total inputs by value",
        "sourced from suppliers"
    ]
    q_ends = [
        "Job creation in smaller towns – Disclose wages paid to persons employed (including employees or workers",
        "Disclose wages paid to persons employed",
        "following locations, as % of total wage cost"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[15:]:
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
        return {"error": f"Start question not found. Tried: {q_starts}"}
    if not end_found:
        return {"error": f"End question not found. Tried: {q_ends}"}
    if not lines_between:
        return {"error": "No content found between start and end questions."}

    # # print("#######",lines_between)
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

    key = [
        "Particulars",
        "FY 2023-24 (Current Financial Year)",
        "FY 2022-23 (Previous Financial year)"

    ]


    keys = [
        "S.No.",
        "Particulars",
        "FY 2023-24 (Current Financial Year)",
        "FY 2022-23 (Previous Financial year)"
    ]

    myout = []
    for row in output_rows:
        data = dict(zip(keys, row))
        myout.append(data)

    if len(final_3) > len(final_4):
        for row in final_3:
            data = dict(zip(key, row))
            myout.append(data)

    elif len(final_4) > len(final_3):
        for row in final_4:
            data = dict(zip(keys, row))
            myout.append(data)


    if not myout:
        return None


    return myout

# print(Percentage_of_input_material("C:/Users/coda/Documents/bse.pdf"))
# print("************")

def  Job_creation_in_smaller_towns(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Job creation in smaller towns",
        "Job creation",
        "of total wage cost"
    ]
    q_ends = [
        "Provide details of actions taken to mitigate any negative",
        "Provide details of actions",
        "Essential Indicators above"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[-12:]:
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
        return {"error": f"Start question not found. Tried: {q_starts}"}
    if not end_found:
        return {"error": f"End question not found. Tried: {q_ends}"}
    if not lines_between:
        return {"error": "No content found between start and end questions."}

    # # print("#######",lines_between)
    output_rows = []
    for line in lines_between:
        output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

    final_2 = []
    final_3 = []
    for f in output_rows:
        if len(f) == 2:
            final_2.append(f)
        elif len(f) == 3:
            final_3.append(f)

    keys = [
        "Details of negative social impact identified",
        "Corrective action taken"
    ]

    keys_3 = [
        "S.No.",
        "Details of negative social impact identified",
        "Corrective action taken"
    ]
    
    

    myout = []
    for row in output_rows:
        data = dict(zip(keys, row))
        myout.append(data)

    if len(final_2) > len(final_3):
        for row in final_2:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_3) > len(final_2):
        for row in final_3:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return lines_between



    if not myout:
        return None


    return myout
# print(Job_creation_in_smaller_towns("C:/Users/coda/Documents/bse.pdf"))
# print("************")



def  Provide_details_of_actions_taken(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Provide details of actions taken to mitigate any negative social impacts identified in the Social Impact",
        "any negative social impacts"
        "1 of Essential Indicators above"
    ]
    q_ends = [
        "Provide the following information on CSR projects undertaken by your entity in designated aspirational districts",
        "your entity in designated",
        "government bodies"
        
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[-12:]:
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
        return {"error": f"Start question not found. Tried: {q_starts}"}
    if not end_found:
        return {"error": f"End question not found. Tried: {q_ends}"}
    if not lines_between:
        return {"error": "No content found between start and end questions."}

    # # print("#######",lines_between)
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

    keys = [
        "State",
        "Aspirational District",
        "Amount spent (In INR)"
    ]

    keys_4 = [
        "Sl.No",
        "State",
        "Aspirational District",
        "Amount spent (In INR)"

        
    ]
    
    

    myout = []
    for row in output_rows:
        data = dict(zip(keys, row))
        myout.append(data)

    if len(final_3) > len(final_4):
        for row in final_3:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_4) > len(final_3):
        for row in final_3:
            data = dict(zip(keys_4, row))
            myout.append(data)
    else:
        return lines_between



    if not myout:
        return None


    return myout
# print(Provide_details_of_actions_taken("C:/Users/coda/Documents/bse.pdf"))
# print("************")


