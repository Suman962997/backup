import pdfplumber
import pytesseract
import re


def q(pdf_path):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question=""
        question_2=""
        question_3=""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="s"
                sec_quest_2="s" 
                sec_quest_3="s"
                list=[]     
                for i, line in enumerate(lines):
                    print(i,line)
                    if question.lower() in line.lower():
                        print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        list=lines[i:]
                        break
                # # print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else:
                        print("else")
                        finallist=list                  
                        break      
                print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                print("51",output_9,len(output_9))
                print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return None


                    
            
    if not found:
        return None
print(q("C:/Users/coda/Documents/bajaj.pdf"))
print("************")



def a(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2=""
        question_3=""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=""
                sec_quest_2="" 
                sec_quest_3=""
                list=[]     
                for i, line in enumerate(lines):
                    # print(i,line)
                    if question.lower() in line.lower():
                        print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        print("****q3")
                        list=lines[i:]
                        break
                # print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # print("finallist",finallist)
                return finallist                       

print(a("C:/Users/coda/Documents/deigeo.pdf",""))
print("************")




### sample ####


def c(pdf_path):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # print("file opend")
        question=""
        question_2=""
        question_3=""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # # print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="" 
                sec_quest_2=""
                sec_quest_3=""
                list=[]     
                for i, line in enumerate(lines):
                    # # print(line)
                    if question.lower() in line.lower():
                        list=lines[i+1:]
                        break
                    elif question_2.lower() in line.lower():
                        list=lines[i+1:]
                        break
                    elif question_3.lower() in line.lower():
                        list=lines[i+1:]
                # # print(list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                # print("finallist",finallist)
                output_3=[]
                output_4=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # print("43",len(parts),parts)
                    if len(parts)==3:
                        output_3.append(parts)
                    elif len(parts)==4:
                        output_4.append(parts)                
                # print("51",output_3)
                # print("52",output_4)
                
                if output_4 :
                    # print("output-4 is exist",output_4,len(output_4))
                    data_4=[{
                    "S:No":output_4[-1][0],
                    "Description of Main Activity":output_4[-1][1],
                    "Description of Business Activity":output_4[-1][2],
                    "% of Turnoverof the entity":output_4[-1][3]}]
                    return data_4                    



                elif output_3:
                    # print("output-3 is exist",output_3,len(output_3))
                    data_3=[{
                    "S:No":1,
                    "Description of Main Activity":output_3[-1][0],
                    "Description of Business Activity":output_3[-1][1],
                    "% of Turnoverof the entity":output_3[-1][2]}]
                    return data_3

                else:
                    return None

                    
            
    if not found:
        return None
print(c("C:/Users/coda/Documents/deigeo.pdf"))
print("**************")




def A_brief_on_types(pdf_path):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # print("file opend")
        question="What is the contribution of exports as a percentage of the total turnover of the entity?"
        question_2="What is the contribution of exports"
        question_3="of the total turnover of the entity"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # # print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="A brief on types of customers" 
                sec_quest_2="A brief on types"
                sec_quest_3=" of customers"
                list=[]     
                for i, line in enumerate(lines):
                    # # print(line)
                    if question.lower() in line.lower():
                        list=lines[i+1:]
                        break
                    elif question_2.lower() in line.lower():
                        list=lines[i+1:]
                        break
                    elif question_3.lower() in line.lower():
                        list=lines[i+1:]
                # # print(list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                print("finallist",finallist)
                if finallist:
                    return finallist
                else:
                    return None

                    
            
    if not found:
        return None
print(A_brief_on_types("C:/Users/coda/Documents/deigeo.pdf"))
print("**************")



import pdfplumber

def d(pdf_path):
    question_1 = "Number of locations where plants and/or operations/offices of the entity are situated:"
    question_2 = "eNumber of locations where plants and/or "
    question_3 = "operations/offices of the entity are situated"

    sec_1 = "Markets served byd the entity - No of locations"
    sec_2 = "Markets served byd the entity - No of locations"
    sec_3 = "Markets served by the entity - No of locations"

    question_pairs = [
        (question_1, sec_1),
        (question_2, sec_2),
        (question_3, sec_3),
    ]

    with pdfplumber.open(pdf_path) as pdf:
        for q_start, q_end in question_pairs:
            start_page = None

            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if not text:
                    continue

                if q_start in text and q_end in text:
                    # Both questions on same page
                    tables = page.extract_tables()
                    q1_index = text.find(q_start) + len(q_start)
                    q2_index = text.find(q_end)
                    between_text = text[q1_index:q2_index]

                    print(f"✅ Matched pair: {q_start} -> {q_end}")
                    print("Extracted text between questions:")
                    print(between_text.strip())

                    if tables:
                        for table in tables:
                            if any(cell and cell in between_text for row in table for cell in row if cell):
                                print("\n✅ Found matching table between questions:")
                                for row in table:
                                    print(row)
                                return table
                    print("No table found directly between the two questions.")
                    return None

                elif q_start in text:
                    start_page = i
                elif q_end in text and start_page is not None:
                    # Look for tables between pages
                    for j in range(start_page + 1, i):
                        mid_tables = pdf.pages[j].extract_tables()
                        if mid_tables:
                            print(f"\n✅ Matched pair across pages: {q_start} -> {q_end}")
                            for table in mid_tables:
                                for row in table:
                                    print(row)
                            return mid_tables[0]
                    print("No table found on intermediate pages.")
                    return None

    print("Could not find any matching question pairs.")
    return None

# Example usage
d("C:/Users/coda/Documents/deigeo.pdf")









def table_hy(pdf_path):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # print("file opend")
        question="Employees and workers (including differently abled)"
        question_2="Employees and workers"
        question_3="(including differently abled)"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # # print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Differently abled employees and workers" 
                sec_quest_2="Differently abled "
                sec_quest_3="employees and workers"
                list=[]     
                for i, line in enumerate(lines):
                    # # print(line)
                    if question.lower() in line.lower():
                        list=lines[i+1:]
                        break
                    elif question_2.lower() in line.lower():
                        list=lines[i+1:]
                        break
                    elif question_3.lower() in line.lower():
                        list=lines[i+1:]
                # # print(list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                        
                print("finallist",finallist)
                d=I_permanent(finallist)
                return {
                    "S:NO":d[0] if len(d)<=0<len(d) else None,
                    "Particulars":d[1] if len(d)<=1<len(d) else None,
                    "Total (A)":d[2] if len(d)<=2<len(d) else None,
                    "Male (No. (B)":d[3] if len(d)<=3<len(d) else None,
                    "Female (No. (B)":d[5] if len(d)<=5<len(d) else None,
                    "Male % (B/A)":d[4] if len(d)<=4<len(d) else None,
                    "Female % (C/A)":d[6] if len(d)<=6<len(d) else None,
                }    
            
    if not found:
        return None
print(table_hy("C:/Users/coda/Documents/deigeo.pdf"))
print("**************")



####### FILES ###########

print(Whether_CSR("C:/Users/coda/Documents/deigeo.pdf"))
print("********************")
print(Whether_CSR("C:/Users/coda/Documents/siemens.pdf"))
print("********************")
print(Whether_CSR("C:/Users/coda/Documents/HUL.pdf"))
print("********************")
print(Whether_CSR("C:/Users/coda/Documents/praxis.pdf"))
print("********************")
print(Whether_CSR("C:/Users/coda/Documents/reliance.pdf"))
print("********************")
print(Whether_CSR("C:/Users/coda/Documents/vendanta.pdf"))
print("********************")
print(Whether_CSR("C:/Users/coda/Documents/narendra.pdf"))
print("********************")
print(Whether_CSR("C:/Users/coda/Documents/wipro.pdf"))
print("********************")
print(Whether_CSR("C:/Users/coda/Documents/bajaj.pdf"))
print("********************")
print(Whether_CSR("C:/Users/coda/Documents/Persistent Systems.pdf"))

def E(pdf_file):
    import pdfplumber, pytesseract, re
    from PIL import Image

    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    q_starts = [
        "",
        "",
        ""

    ]
    q_ends = [
        "",
        "",
        ""
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[-10:]:  # reduced page range
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
print(E("C:/Users/coda/Documents/deigeo.pdf"))





def  o(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "",
        "",
        ""
    ]
    q_ends = [
        "",
        "",
        ""
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
        "",
        "",
        ""
    ]
    
    keys_3 = [
        "SI.NO",
        "",
        "",
        ""
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

print(o("C:/Users/coda/Documents/deigeo.pdf"))
print("************")


def  p(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "",
        "",
        ""

    ]
    q_ends = [
        "",
        "",
        ""
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
    ]

    keys_3 = [
        "S.no",
    ]
    
    myout = []
    # for row in output_rows:
    #     data = dict(zip(keys, row))
    #     myout.append(data)

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

print(p("C:/Users/coda/Documents/siemens.pdf"))
print("************")



                if finallist:
                    url_pattern = r'https?://[^\s,)"]+'
                    res=[]
                    for t in finallist:
                        matches=re.findall(url_pattern,t)
                        res.extend(matches)
                    # print(res)
