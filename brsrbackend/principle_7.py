import pdfplumber
import pytesseract
from PIL import Image
import io
import re



                                ###### PRINCIPLE VII #######
                                
def Number_of_affiliations(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        ## # print("file opend")
        question="Number of affiliations with trade and industry chambers/ associations"
        question_2="Number of affiliations"
        question_3="chambers/ associations"
        for i, page in enumerate(pdf.pages[13:-2]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                ## # print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # ## # print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="List the top 10 trade and industry chambers/ associations"
                sec_quest_2="List the top 10 trade and industry" 
                sec_quest_3="affiliated to, in the following format"
                list=[]     
                for i, line in enumerate(lines):
                    # ## # print(i,line)
                    if question.lower() in line.lower():
                        ## # print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        ## # print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        ## # print("****q3")
                        list=lines[i:]
                        break
                # ## # print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # ## # print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        ## # print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        ## # print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        ## # print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # ## # print("finallist",finallist)
                return finallist                       

#@print(Number_of_affiliations("C:/Users/coda/Documents/ncc.pdf"))
#@print("************")



def  List_the_top_10_trade(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "List the top 10 trade and industry chambers/ associations",
        "List the top 10 trade and industry",
        "member of/ affiliated to"
    ]
    q_ends = [
        "Provide details of corrective action taken or underway on any",
        "Provide details of corrective action",
        "orders from regulatory authorities"
        
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[13:-2]:
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

    # ## # print("#######",lines_between)
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
        "Name of the trade and industry chambers/ associations",
        "Reach of trade and industry chambers/ associations (State/ National)"
    ]
    
    keys_3 = [
        "SI.NO",
        "Name of the trade and industry chambers/ associations",
        "Reach of trade and industry chambers/ associations (State/ National)"
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

#@print(List_the_top_10_trade("C:/Users/coda/Documents/ncc.pdf"))
#@print("************")



def Provide_details_of_corrective_action(pdf_file):
    import pdfplumber, pytesseract, re
    from PIL import Image

    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    q_starts = [
        "Provide details of corrective action taken or underway on any issues related to anticompetitive conduct",
        "Provide details of corrective action taken or",
        "orders from regulatory authorities."
    ]
    q_ends = [
        "Details of public policy positions advocated by the entity",
        "Details of public policy",
        "advocated by the entity"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[10:-2]:  # reduced page range
            text = page.extract_text()
            if not text or len(text.strip()) < 50:
                pil_image = page.to_image(resolution=150).original
                text = pytesseract.image_to_string(pil_image, config=custom_config)

            if not text:
                continue

            for line in text.splitlines():
                if not start_found and any(start.lower() in line.lower() for start in q_starts):
                    start_found = True
                    continue
                if start_found and any(end.lower() in line.lower() for end in q_ends):
                    end_found = True
                    break
                if start_found:
                    lines_between.append(line)

            if end_found:
                break

    if not start_found or not end_found or not lines_between:
        return {"error": "Start or End phrase not found or no content extracted."}

    # Structure parsing
    output_rows = [re.split(r'\s{2,}|\s*\|\s*', line) for line in lines_between]
    keys = ["Name of Authority", "Corrective action taken", "Brief of the case"]
    keys_3 = ["SI.NO", "Name of Authority", "Corrective action taken", "Brief of the case"]

    myout = []
    for row in output_rows:
        if len(row) == 3:
            myout.append(dict(zip(keys, row)))
        elif len(row) == 4:
            myout.append(dict(zip(keys_3, row)))

    return myout if myout else lines_between
#@print(Provide_details_of_corrective_action("C:/Users/coda/Documents/ncc.pdf"))
#@print("************")


def Details_of_public_policy(pdf_file):
    import pdfplumber, pytesseract, re
    from PIL import Image

    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    q_starts = [
        "Details of public policy positions advocated by the entity",
        "Details of public policy",
        "advocated by the entity"

    ]
    q_ends = [
        "Principle 8",
        "Businesses should promote inclusive growth and equitable development",
        "Details of Social Impact Assessments"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[12:-2]:  # reduced page range
            text = page.extract_text()
            if not text or len(text.strip()) < 50:
                pil_image = page.to_image(resolution=150).original
                text = pytesseract.image_to_string(pil_image, config=custom_config)

            if not text:
                continue

            for line in text.splitlines():
                if not start_found and any(start.lower() in line.lower() for start in q_starts):
                    start_found = True
                    continue
                if start_found and any(end.lower() in line.lower() for end in q_ends):
                    end_found = True
                    break
                if start_found:
                    lines_between.append(line)

            if end_found:
                break

    if not start_found or not end_found or not lines_between:
        return {"error": "Start or End phrase not found or no content extracted."}

    # Structure parsing
    output_rows = [re.split(r'\s{2,}|\s*\|\s*', line) for line in lines_between]
    keys = [
            "Public policy advocated",
            "Method resorted for such advocacy",
            "Whether information available in public domain? (Yes/No)"
            "Frequency of Review by Board (Annually/ Half yearly/ Quarterly/ Others – please specify)"
            "Web Link, if available"
            ]

    keys_3 = [
            "S.NO",
            "Public policy advocated",
            "Method resorted for such advocacy",
            "Whether information available in public domain? (Yes/No)"
            "Frequency of Review by Board (Annually/ Half yearly/ Quarterly/ Others – please specify)"
            "Web Link, if available"
              ]

    myout = []
    for row in output_rows:
        if len(row) == 5:
            myout.append(dict(zip(keys, row)))
        elif len(row) == 6:
            myout.append(dict(zip(keys_3, row)))

    return myout if myout else lines_between
#@print(Details_of_public_policy("C:/Users/coda/Documents/ncc.pdf"))
#@print("************")

