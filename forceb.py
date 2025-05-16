import pdfplumber
import pytesseract
from PIL import Image
import io
import re


def Whether_your_entity(pdf_path,question):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # print("file opend")
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            # # print(text)
            question_2="Policy and management processes"
            question_3="entity's policy/policies"
            # sec_quest_2=""
            if text and question in text or question_2 in text or question_3 in text:
                found = True
                # print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Has the policy" 
                list=[]     
                for i, line in enumerate(lines):
                    # # print(line)
                    if question.lower() in line.lower():
                        list=lines[i:]
                    elif  question_2.lower() in line.lower():
                        list=lines[i+1:]

                # # print(list)
                finallist=[]
                for i,selist in enumerate(list):
                    # # print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # print("#########",i,selist)
                        finallist=list[:i]
                    # elif sec_quest_2.lower() in selist.lower():
                    #     finallist=list[:i]
                        break
                        
                    else:
                        finallist=list
                # print("finallist",finallist)
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # print("51",output_9,len(output_9))
                # print("54",output_10,len(output_10))                
                if output_9:
                    # print("output-9 is exist",output_9,len(output_9))
                    # getlast=output_9[-10:]
                    # # print(getlast)
                    princ=[]
                    for i in output_9:
                        # print(len(i),i)
                        if len(i)<=3:
                            princ.append(i)
                    # print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                        else:
                            return None

                    # print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

                else:
                    return None


                    
            
    if not found:
        return None

# print(Whether_your_entity("C:/Users/coda/Documents/deigeo.pdf","Whether your entity"))
# print("************")

def Has_the_policy(pdf_path,question):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # print("file opend")
        question_2="Has the policy been approved"
        question_3="Has the policy been"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # # print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Web Link of the Policies" 
                list=[]     
                for i, line in enumerate(lines):
                    # # print(line)
                    if question.lower() in line.lower():
                        list=lines[i:]
                    elif  question_2.lower() in line.lower():
                        list=lines[i+1:]

                finallist=[]
                
                for i,selist in enumerate(list):
                    # # print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # print("#########",i,selist)
                        finallist=list[:i]
                        break
                        
                    else:
                        finallist=list
                # print("finallist",finallist)
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # print("51",output_9,len(output_9))
                # print("54",output_10,len(output_10))                
                if output_9:
                    # print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return None


                    
            
    if not found:
        return None

# print(Has_the_policy("C:/Users/coda/Documents/deigeo.pdf","Has the policy been approved by the Board?"))
# print("************")

def Web_Link_of_Policies(pdf_path,question):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # print("file opend")
        question_2="Web Link of the Policies"
        question_3="Web Link of the"

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
                sec_quest="Whether the entity has translated" 
                list=[]     
                for i, line in enumerate(lines):
                    # # print(line)
                    if question.lower() in line.lower():
                        list=lines[i:]
                    elif question_2.lower() in line.lower():
                        list=lines[i:]
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # # print("#########",i,selist)
                        finallist=list[:i]
                        break     
                    else:
                        finallist=list
                # print("finallist",len(finallist))
                
                
                if finallist:
                    url_pattern = r'https?://[^\s,)"]+'
                    res=[]
                    for t in finallist:
                        matches=re.findall(url_pattern,t)
                        res.extend(matches)
                    # print(res)
                    return res
                else:
                    return None                    
            
    if not found:
        return None

# print(Web_Link_of_Policies("C:/Users/coda/Documents/deigeo.pdf","Web Link of the Policies, if available"))
# print("************")

def Whether_entity_translated(pdf_path,question):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # print("file opend")
        question_2="the entity has"
        question_3="Whether the entity has translated"
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
                list=[]     
                for i, line in enumerate(lines):
                    # # print(line)
                    if question.lower() in line.lower():
                        list=lines[i:]
                    elif  question_2.lower() in line.lower():
                        list=lines[i+1:]

                finallist=[]
                sec_quest="Do the enlisted policies extend to your" 
                sec_2="enlisted policies"                
                for i,selist in enumerate(list):
                    # # print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # # print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_2.lower() in selist.lower():
                        finallist=list[:1+i]
                        break
                    else:
                        finallist=list
                # print("finallist",finallist)
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # print("51",output_9,len(output_9))
                # print("54",output_10,len(output_10))                
                if output_9:
                    # print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return None


                    
            
    if not found:
        return None

# print(Whether_entity_translated("C:/Users/coda/Documents/deigeo.pdf","Whether the entity has translated thepolicy intoprocedures.(Yes/No)"))
# print("************")


def Do_the_enlisted(pdf_path,question):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # print("file opend")
        question_2="enlisted policies extend"
        question_3="Do the enlisted"
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
                sec_quest="national and international" 
                list=[]     
                for i, line in enumerate(lines):
                    # # print(line)
                    if question.lower() in line.lower():
                        list=lines[i:]
                    elif question_2.lower() in line.lower():
                        # # print("ELIF")
                        list=lines[i+1:]
                # # print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # # print("#########",i,selist)
                        finallist=list[:i]
                        break
                        
                    else:
                        finallist=list
                # # print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # # print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # # print("51",output_9,len(output_9))
                # # print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    # # print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # # print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # # print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # # print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # # print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4                
           
                else:
                    return None


                    
            
    if not found:
        return None

# print(Do_the_enlisted("C:/Users/coda/Documents/deigeo.pdf","Do the enlisted policies"))
# print("************")


def national_and_international(pdf_path,question):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # print("file opend")
        question_2="Name of the national"
        question_3="national and international codes/certifications/labels/"
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
                sec_quest="Specific commitments," 
                list=[]     
                for i, line in enumerate(lines):
                    # # print(line)
                    if question.lower() in line.lower():
                        list=lines[i:]
                    elif question_2.lower() in line.lower():
                        # # print("ELIF")
                        list=lines[i+1:]
                # # print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # # print("#########",i,selist)
                        finallist=list[:i]
                        break
                        
                    else:
                        finallist=list
                # # print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # # print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # # print("51",output_9,len(output_9))
                # # print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    # # print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # # print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # # print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # # print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # # print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4
           
                else:
                    return None 
            
    if not found:
        return None

# print(national_and_international("C:/Users/coda/Documents/deigeo.pdf","national and international codes/certifications/labels/ standards"))
# print("************")

def Specific_commitments(pdf_path,question):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # print("file opend")
        question_2="Specific commitments"
        question_3=" by the entity with defined timelines, if any"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Performance of the entity against" 
                sec_quest_2="Performance against"
                list=[]     
                for i, line in enumerate(lines):
                    # # print(line)
                    if question.lower() in line.lower():
                        print("***q1")
                        list=lines[i:]
                    elif question_2.lower() in line.lower():
                        print("***q2")
                        list=lines[i+1:]
                # print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print("### sec_2")
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # # print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # # print("51",output_9,len(output_9))
                # # print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    # # print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # # print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # # print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # # print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # # print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4
           
                else:
                    return None 
            
    if not found:
        return None

# print(Specific_commitments("C:/Users/coda/Documents/deigeo.pdf","Specific commitments, goals and targets"))
# print("************")


def Performance_of_the_entity(pdf_path,question):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # print("file opend")
        question_2="Performance of the entity"
        question_3=" reasons in case the same are not met."
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Statement by director responsible" 
                sec_quest_2="Statement by director"
                list=[]     
                for i, line in enumerate(lines):
                    # # print(line)
                    if question.lower() in line.lower():
                        list=lines[i:]
                    elif question_2.lower() in line.lower():
                        # # print("ELIF")
                        list=lines[i+1:]
                # # print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # print("#########",i,selist)
                        finallist=list[:i]
                    elif sec_quest_2.lower() in selist.lower():
                        finallist=list[:i]
                        break
                        
                    else:
                        finallist=list
                # print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # # print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # # print("51",output_9,len(output_9))
                # # print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    # # print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # # print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # # print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # # print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # # print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return None 
            
    if not found:
        return None

# print(Performance_of_the_entity("C:/Users/coda/Documents/deigeo.pdf","Performance of the entity against the specific commitments"))
# print("************")

                                    ###### second part #####
 
 
 
def Statement_by_director(pdf_path,question):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # print("file opend")
        question_2="Statement by director responsible for the business responsibility"
        question_3="Statement by director responsible"

        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text or question_3 in text:
                found = True
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Details of the highest authority"
                sec_quest_2="Details of the highest" 
                list=[]     
                for i, line in enumerate(lines):
                    # print(line)
                    if question.lower() in line.lower():
                        list=lines[i:]
                    elif question_2.lower() in line.lower():
                        # # print("ELIF")
                        list=lines[i+1:]
                # # print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # # print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        finallist=list[:i]
                    else:
                        finallist=list
                # # print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # # print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # # print("51",output_9,len(output_9))
                # # print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    # # print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # # print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # # print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # # print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # # print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return None
    if not found:
        return None

# print(Statement_by_director("C:/Users/coda/Documents/HUL.pdf","Statement by director responsible for the business"))
# print("************")


def Details_of_the_highest(pdf_path,question):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # print("file opend")
        question_2="Details of the highest"
        question_3="Details of the highest authority responsible"
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
                sec_quest="Does the entity have a "
                sec_quest_2="Committee of the " 
                list=[]     
                for i, line in enumerate(lines):
                    # # print(line)
                    if question.lower() in line.lower():
                        list=lines[i:]
                    elif question_2.lower() in line.lower():
                        # # print("ELIF")
                        list=lines[i+1:]
                # # print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # # print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        finallist=list[:i]
                    else:
                        finallist=list
                # # print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # # print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # # print("51",output_9,len(output_9))
                # # print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    # # print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # # print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # # print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # # print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # # print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4
           
                else:
                    return None


                    
            
    if not found:
        return None

# print(Details_of_the_highest("C:/Users/coda/Documents/deigeo.pdf","Details of the highest authority responsible"))
# print("************")



def Does_the_entity(pdf_path,question):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # print("file opend")
        question_2="specified Committee of"
        question_3="Director responsible for decision"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Details of Review of NGRBCs by the Company"
                sec_quest_2="Details of Review" 
                sec_quest_3="Review of NGRBCs"
                list=[]     
                for i, line in enumerate(lines):
                    # print(i,line)
                    if question.lower() in line.lower():
                        # print("***q1")
                        list=lines[i:]
                    elif question_2.lower() in line.lower():
                        # print("***q2")
                        list=lines[i:]
                    elif question_3.lower() in line.lower():
                        list=lines[i:]
                # # print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # print("&& sec3")
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                # print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # print("51",output_9,len(output_9))
                # print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    # print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return None


                    
            
    if not found:
        return None

# print(Does_the_entity("C:/Users/coda/Documents/deigeo.pdf","Does the entity have a specified Committee "))
print("************")


def Indicate_whether_review(pdf_path,question):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Indicate whether review was undertaken by Director / Committee"
        question_3="Indicate whether review"
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
                sec_quest=" Has the entity carried out independent assessment"
                sec_quest_2=" Has the entity carried out independent" 
                sec_quest_3=" Has the entity carried"
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
                        list=lines[i:]
                        break
                # # print("405 **",list)
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
                    else:
                        finallist=list
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

# print(Indicate_whether_review("C:/Users/coda/Documents/deigeo.pdf","Indicate whether review was undertaken by Director / Committee"))
# print("************")



def Frequency_Annually(pdf_path,question):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # print("file opend")
        question_2="Frequency (Annually/ Half yearly/ Quarterly/"
        question_3="Frequency (Annually/"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                lines = ocr_text.splitlines()
                # print(lines)
                sec_quest=" Has the entity carried out independent assessment"
                sec_quest_2=" Has the entity carried out independent" 
                sec_quest_3=" Has the entity carried"
                list=[]     
                for i, line in enumerate(lines):
                    # print(i,line)
                    if question.lower() in line.lower():
                        # print("***q1")
                        list=lines[i:]
                    elif question_2.lower() in line.lower():
                        # print("***q2")
                        list=lines[i:]
                    elif question_3.lower() in line.lower():
                        # print("***q3")
                        list=lines[i:]
                    else:
                        finallist=list
                # # print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # print("&& sec3")
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                # print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # print("51",output_9,len(output_9))
                # print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    # print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return None


                    
            
    if not found:
        return None

# print(Frequency_Annually("C:/Users/coda/Documents/deigeo.pdf","Frequency (Annually/ Half yearly/ Quarterly Any other"))
# print("************")


def Has_the_entity_carried(pdf_path,question):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # print("file opend")
        question_2="Has the entity"
        question_3="If yes, provide name of the agency"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="If answer to question (1) above"
                sec_quest_2="If answer to question" 
                list=[]     
                for i, line in enumerate(lines):
                    # # print(line)
                    if question.lower() in line.lower():
                        list=lines[i:]
                    elif question_2.lower() in line.lower():
                        # # print("ELIF")
                        list=lines[i+1:]
                # # print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        finallist=list[:i]
                    else:
                        finallist=list
                # # print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # print("51",output_9,len(output_9))
                # print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    # print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return None


                    
            
    if not found:
        return None

# print(Has_the_entity_carried("C:/Users/coda/Documents/deigeo.pdf","Has the entity carried out independent"))
# print("************")


  ##### 12-th

def If_answer_to_question(pdf_path,question):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # print("file opend")
        question_2="If answer to question (1) above is “No”"
        question_3="answer to question"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text or question_3 in text:
                found = True
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Supply Chain Mangement"
                sec_quest_2="SECTION C" 
                sec_quest_3="PRINCIPLE WISE PERFORMANCE DISCLOSURE"
                list=[]     
                for i, line in enumerate(lines):
                    print(line)
                    if question.lower() in line.lower():
                        print("::")
                        list=lines[i:]
                    elif question_2.lower() in line.lower():
                        print("ELIF")
                        list=lines[i+1:]
                    elif question_3.lower() in line.lower():
                        list=lines[i+1:]
                # print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        print("#########",i,selist)
                        finallist=list[:i]
                        # break
                    elif sec_quest_2.lower() in selist.lower():
                        print("HBJAS")
                        finallist=list[:i]
                        # break
                    elif sec_quest_3.lower() in selist.lower():
                        print("KKKKs")
                        finallist=list[:1+i]
                        # break
                    else:
                        finallist=list[i]
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

# print(If_answer_to_question("C:/Users/coda/Documents/deigeo.pdf","If answer to question (1) above is"))
# print("************")


def consider_the_Principles(pdf_path,question):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="The entity does not consider"
        question_3="The entity does not"
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
                sec_quest="The entity is not at a stage"
                sec_quest_2="The entity is not" 
                sec_quest_3="The entity is"
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
                        print("**q3")
                        list=lines[i:]
                        break
                    else:
                        print("else")
                        finallist=list
                # # print("405 **",list)
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
                    else:
                        finallist=list
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
                # print("51",output_9,len(output_9))
                # print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:
                    finq="The entity does not consider the Principles material to its business (Yes/No)"  
                    # for f in finallist:
                    #     if f == finq:
                    #         print("ksjdnckjm")
                                              
                    return str(finallist)
                elif output_9:
                    print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # print("prince",princ)
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
                    # print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return None


                    
            
    if not found:
        return None

# print( consider_the_Principles("C:/Users/coda/Documents/HUL.pdf","The entity does not consider the Principles"))
# print("************")



def formulate_and_implement(pdf_path,question):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # print("file opend")
        question_2="The entity is not at a stage where "
        question_3="The entity is not"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="The entity does not have the financial"
                sec_quest_2="human and technical resources" 
                sec_quest_3="technical resources"
                list=[]     
                for i, line in enumerate(lines):
                    # print(i,line)
                    if question.lower() in line.lower():
                        # print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        list=lines[i:]
                        break
                    else:
                        finallist=list
                # # print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # print("&& sec3")
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                # print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # print("51",output_9,len(output_9))
                # print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    # print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return None


                    
            
    if not found:
        return None

# print( formulate_and_implement("C:/Users/coda/Documents/deigeo.pdf","The entity is not at a stage where it is in a position to"))
# print("************")



def human_and_technical(pdf_path,question):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="The entity does not have the financial"
        question_3="The entity does not"
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
                sec_quest="It is planned to be done in the next financial"
                sec_quest_2="It is planned to be done" 
                sec_quest_3="the next financial"
                list=[]     
                for i, line in enumerate(lines):
                    print(i,line)
                    if question.lower() in line.lower():
                        print("***q1")
                        list=lines[i:]
                    elif question_2.lower() in line.lower():
                        print("***q2")
                        list=lines[i:]
                    elif question_3.lower() in line.lower():
                        list=lines[i:]
                    else:
                        print("&&&&&&&")
                        finallist=list
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
                        finallist=list
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

# print(human_and_technical("C:/Users/coda/Documents/deigeo.pdf","The entity does not have the financial or/human"))
# print("************")


def It_is_planned_to_be_done(pdf_path,question):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="It is planned to be done in"
        question_3="next financial year (Yes/No)"
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
                sec_quest="Any other reason (please specify)"
                sec_quest_2="Any other reason" 
                sec_quest_3="Section C"
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
                    else:
                        finallist=list
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
                        finallist=list
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

# print(It_is_planned_to_be_done("C:/Users/coda/Documents/deigeo.pdf","It is planned to be done in the next financial year (Yes/No)"))
# print("************")

def Any_other_reason(pdf_path,question):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # print("file opend")
        question_2="Any other reason (please specify)"
        question_3="Any other reason "
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Section C"
                sec_quest_2="PRINCIPLE WISE PERFORMANCE DISCLOSURE" 
                sec_quest_3="Businesses should conduct"
                list=[]     
                for i, line in enumerate(lines):
                    # print(i,line)
                    if question.lower() in line.lower():
                        # print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # print("***q3")
                        list=lines[i:]
                        break
                    # else:
                    #     finallist=list
                # print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # print("&& sec3")
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                # print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # print("51",output_9,len(output_9))
                # print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    # print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return None


                    
            
    if not found:
        return None

# print(Any_other_reason("C:/Users/coda/Documents/deigeo.pdf","Any other reason (please specify)"))
# print("************")




