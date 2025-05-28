import pdfplumber
import pytesseract
from PIL import Image
import io
import re


                            #  PRINCIPLE I 

def  Percentage_coverage_by_training(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Percentage coverage by training and awareness programmes",
        "Percentage coverage by training and awareness",
        "Percentage coverage by training"

    ]
    q_ends = [
        "Details of fines / penalties /punishment/ award/ compounding fees/ settlement amount paid in proceedings",
        "Details of fines / penalties /punishment",
        "settlement amount paid in proceedings"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[7:16]:
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
    output_rows = []
    for line in lines_between:
        output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

    final_4 = []
    final_5 = []
    for f in output_rows:
        if len(f) == 4:
            final_4.append(f)
        elif len(f) == 5:
            final_5.append(f)

    keys = [
        "Segment",
        "Total number of training and awareness programmes held",
        "Topics / principles covered under the training and its impact",
        "%age of persons in respective category covered by the awareness programmes"
    ]

    keys_3 = [
        "S.no",
        "Segment",
        "Total number of training and awareness programmes held",
        "Topics / principles covered under the training and its impact",
        "%age of persons in respective category covered by the awareness programmes"
    ]
    
    myout = []
    if len(final_4) > len(final_5):
        for row in final_4:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_5) > len(final_4):
        for row in final_5:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return lines_between



    if not myout:
        return None


    return myout

#@print(Percentage_coverage_by_training("C:/Users/coda/Documents/praxis.pdf"))
#@print("************")



def  Monetary(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Details of fines / penalties /punishment/ award/ compounding fees/ settlement amount paid in proceedings",
        "Details of fines / penalties /punishment/ award/ compounding fees",
        "law enforcement agencies/ judicial institutions"

    ]
    q_ends = [
        "Non-Monetary",
        "Non Monetary",
        "Non Monetary"
        
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[7:16]:
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
        "Category",
        "NGRBC Principle",
        "Name of the regulatory/ enforcement agencies/ judicial institutions",
        "Amount (In INR)",
        "Brief of the Case",
        "Has an appeal been preferred? (Yes/No)"
    ]

    keys_3 = [
        "S.no",
        "Category",
        "NGRBC Principle",
        "Name of the regulatory/ enforcement agencies/ judicial institutions",
        "Amount (In INR)",
        "Brief of the Case",
        "Has an appeal been preferred? (Yes/No)"        
        
    ]
    
    myout = []
    if len(final_6) > len(final_7):
        for row in final_6:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_7) > len(final_6):
        for row in final_7:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return lines_between



    if not myout:
        return None


    return myout

#@print(Monetary("C:/Users/coda/Documents/praxis.pdf"))
#@print("************")


def  Non_Monetary(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Non-Monetary",
        "Non Monetary",
        "Non Monetary"

    ]
    q_ends = [
     "Of the instances disclosed in Question 2 above, details of the Appeal/ Revision preferred in cases where monetary or non-monetary action has been appealed"   
     "Of the instances disclosed in Question 2 above",
     "Revision preferred in cases where monetary or non-monetary"   
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[7:16]:
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
    output_rows = []
    for line in lines_between:
        output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

    final_5 = []
    final_6 = []
    for f in output_rows:
        if len(f) == 5:
            final_5.append(f)
        elif len(f) == 6:
            final_6.append(f)

    keys = [
        "Category",
        "NGRBC Principle",
        "Name of the regulatory/ enforcement agencies/ judicial institutions",
        "Brief of the Case",
        "Has an appeal been preferred? (Yes/No)"
    ]

    keys_3 = [
        "S.no",
        "Category",
        "NGRBC Principle",
        "Name of the regulatory/ enforcement agencies/ judicial institutions",
        "Brief of the Case",
        "Has an appeal been preferred? (Yes/No)"        
        
    ]
    
    myout = []

    if len(final_5) > len(final_6):
        for row in final_5:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_6) > len(final_5):
        for row in final_6:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return lines_between



    if not myout:
        return None


    return myout

#@print(Non_Monetary("C:/Users/coda/Documents/praxis.pdf"))
#@print("************")


def  Of_the_instances_disclosed(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
     "Of the instances disclosed in Question 2 above, details of the Appeal/ Revision preferred in cases where monetary or non-monetary action has been appealed"   
     "Of the instances disclosed in Question 2 above",
     "Revision preferred in cases where monetary or non-monetary"   
    ]
    q_ends = [
        "Does the entity have an anti-corruption or anti-bribery policy? If yes, provide details in brief and if available",
        "Does the entity have an anti-corruption or anti-bribery policy? If yes",
        "provide a web-link to the policy"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[7:16]:
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
        "Case Details",
        "Name of the regulatory/ enforcement agencies/ judicial institutions"

    ]

    keys_3 = [
        "S.No",
        "Case Details",
        "Name of the regulatory/ enforcement agencies/ judicial institutions"

    ]
    
    myout = []

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

#@print(Of_the_instances_disclosed("C:/Users/coda/Documents/praxis.pdf"))
#@print("************")


def  Does_the_entity_have_an_anti(pdf_path):
    
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question="Does the entity have an anti-corruption or anti-bribery policy"
        question_2="Does the entity have an"
        question_3="Does the entity have an"
        for i, page in enumerate(pdf.pages[7:16]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=" Number of Directors/KMPs/employees/workers against "
                sec_quest_2="Number of Directors/KMPs" 
                sec_quest_3="/KMPs/employees/workers"
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

#@print(Does_the_entity_have_an_anti("C:/Users/coda/Documents/praxis.pdf"))
#@print("************")

def  Number_of_Directors(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Number of Directors/KMPs/employees/workers against whom disciplinary",
        "Number of Directors/KMPs/employees/workers against",
        "charges of bribery/ corruption"
    ]
    q_ends = [
        "Details of complaints with regard to conflict of interest",
        "Details of complaints",
        "regard to conflict of interest"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[7:16]:
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
        "catagory",
        "FY 2023-2024",
        "FY 2022-2023"
    ]

    keys_3 = [
        "S.No",
        "catagory",
        "FY 2023-2024",
        "FY 2022-2023"
        
    ]
    
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
        return lines_between



    if not myout:
        return None


    return myout

#@print(Number_of_Directors("C:/Users/coda/Documents/praxis.pdf"))
#@print("************")



def  Details_of_complaints(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Details of complaints with regard to conflict of interest",
        "Details of complaints",
        "regard to conflict of interest"
    ]
    q_ends = [
        "Provide details of any corrective action taken or underway on issues related to fines / penalties",
        "Provide details of any corrective action taken",
        "judicial institutions, on cases of corruption and conflicts of interest"
        
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[7:16]:
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
    output_rows = []
    for line in lines_between:
        output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

    final_5 = []
    final_6 = []
    for f in output_rows:
        if len(f) == 5:
            final_5.append(f)
        elif len(f) == 6:
            final_6.append(f)

    keys = [
        "category",
        "FY 2023-2024 Number",
        "FY 2023-2024 Remarks",
        "FY 2022-2023 numbers",
        "FY 2022-2023 Remarks"

    ]

    keys_3 = [
        "S.No",
        "category",
        "FY 2023-2024 Number",
        "FY 2023-2024 Remarks",
        "FY 2022-2023 numbers",
        "FY 2022-2023 Remarks"

    ]
    
    myout = []

    if len(final_5) > len(final_6):
        for row in final_5:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_6) > len(final_5):
        for row in final_6:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return lines_between



    if not myout:
        return None


    return myout

#@print(Details_of_complaints("C:/Users/coda/Documents/praxis.pdf"))
#@print("************")




def Provide_details_of_any_corrective(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question="Provide details of any corrective action taken or underway"
        question_2="Provide details of any corrective"
        question_3="fines / penalties / action taken"
        for i, page in enumerate(pdf.pages[7:16]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=" Number of days of accounts payables ((Accounts payable *365) / Cost of goods/services"
                sec_quest_2="Number of days of accounts payables ((Accounts payable *365)" 
                sec_quest_3="Cost of goods/services"
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

#@print(Provide_details_of_any_corrective("C:/Users/coda/Documents/praxis.pdf"))
#@print("************")



def  Number_of_days_of_accounts(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Number of days of accounts payables ((Accounts payable *365)",
        "Cost of goods/services procured",
        "Accounts payable *365) / Cost of goods/services procured)"
    ]
    q_ends = [
        "Openness of Business",
        "Openness-Business",
        "Open-ness of business"
        
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[7:16]:
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
        "Particulars",
        "FY 2023 -24 (Current Financial year)",
        "FY 2022 -23 (Previous Financial year)"

    ]

    keys_3 = [
        "S.No",
        "Particulars",
        "FY 2023 -24 (Current Financial year)",
        "FY 2022 -23 (Previous Financial year)"
    ]
    
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
        return lines_between



    if not myout:
        return None


    return myout

#@print(Number_of_days_of_accounts("C:/Users/coda/Documents/praxis.pdf"))
#@print("************")



def  Open_ness_of_business(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Openness of Business",
        "Openness-Business",
        "Open-ness of business"
    ]
    q_ends = [
        "Awareness programmes conducted for value chain partners on any of the Principles",
        "Awareness programmes conducted for value chain partners",
        "Principles during the financial year:"
        
        
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[7:16]:
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
    output_rows = []
    for line in lines_between:
        output_rows.append(re.split(r'\s{2,}|\s*\|\s*', line))

    final_4 = []
    final_5 = []
    for f in output_rows:
        if len(f) == 4:
            final_4.append(f)
        elif len(f) == 5:
            final_5.append(f)

    keys = [
        "Parameter",
        "Metrics",
        "FY 2023-2024",
        "FY 2022-2023"
    ]

    keys_3 = [
        "S.No",
        "Parameter",
        "Metrics",
        "FY 2023-2024",
        "FY 2022-2023"

    ]
    
    myout = []

    if len(final_4) > len(final_5):
        for row in final_4:
            data = dict(zip(keys, row))
            myout.append(data)
    elif len(final_5) > len(final_4):
        for row in final_5:
            data = dict(zip(keys_3, row))
            myout.append(data)
    else:
        return lines_between



    if not myout:
        return None


    return myout

#@print(Open_ness_of_business("C:/Users/coda/Documents/praxis.pdf"))
#@print("************")



def  Awareness_programmes_conducted(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Awareness programmes conducted for value chain partners on any of the Principles",
        "Awareness programmes conducted for value chain partners",
        "Principles during the financial year"
    ]
    q_ends = [
        "Does the entity have processes in place to avoid/ manage conflict",
        "Does the entity have processes in place to avoid",
        "provide details of the same"
        
        
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[7:16]:
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
        "Total no of awareness programs held",
        "Topics / principles covered under the training",
        "% of value chain partners covered (by value of business done withsuch partners) under the awarenessprogrammes"
    ]

    keys_3 = [
        "S.No",
        "Total no of awareness programs held",
        "Topics / principles covered under the training",
        "% of value chain partners covered (by value of business done withsuch partners) under the awarenessprogrammes"
        
    ]
    
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
        return lines_between



    if not myout:
        return None


    return myout

#@print(Awareness_programmes_conducted("C:/Users/coda/Documents/praxis.pdf"))
#@print("************")



def   Does_the_entity_have_processes(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Does the entity have processes in place to avoid/ manage conflict",
        "Does the entity have processes in place to avoid",
        "provide details of the same"    
        ]
    q_ends = [
        "PRINCIPLE 2: BUSINESSES SHOULD PROVIDE GOODS AND SERVICES IN A MANNER THAT IS SUSTAINABLE AND SAFE",
        "PRINCIPLE 2",
        "BUSINESSES SHOULD PROVIDE GOODS"
                
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[7:16]:
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
    else:
        return None

#@print(Does_the_entity_have_processes("C:/Users/coda/Documents/praxis.pdf"))
#@print("************")
