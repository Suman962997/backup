import pdfplumber
import pytesseract
from PIL import Image
import io
import re
import fun




def Whether_your_entity(pdf_path):
    found = False
    #@ print("PART A")
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        for i, page in enumerate(pdf.pages[3:16]):
            text = page.extract_text()
            # # #@ print(text)
            question="Whether your entity’s policy"
            question_2="Policy and management processes"
            question_3="entity's policy/policies"
            # sec_quest_2=""
            if text and question in text or question_2 in text or question_3 in text:
                found = True
                # #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Has the policy been approved by the Board" 
                sec_quest_2="Has the policy been" 
                sec_quest_3="approved by the Board" 

                list=[]     
                for i, line in enumerate(lines):
                    # # #@ print(line)
                    if question.lower() in line.lower():
                        list=lines[i-1:]
                    elif  question_2.lower() in line.lower():
                        list=lines[i-1:]

                # # #@ print(list)
                finallist=[]
                for i,selist in enumerate(list):
                    # # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("#########",i,selist)
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
                # #@ print("finallist",finallist)
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # #@ print("51",output_9,len(output_9))
                # #@ print("54",output_10,len(output_10))                
                if output_9:
                    # #@ print("output-9 is exist",output_9,len(output_9))
                    # getlast=output_9[-10:]
                    # # #@ print(getlast)
                    princ=[]
                    for i in output_9:
                        # #@ print(len(i),i)
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                        else:
                            return "Not Applicable"

                    # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

                else:
                    return "Not Applicable"


                    
            
    if not found:
        return "Not Applicable"

#@ print(Whether_your_entity("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")

def Has_the_policy(pdf_path,):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Has the policy been approved by the Board"
        question_2="Has the policy been approved"
        question_3="Has the policy been"
        for i, page in enumerate(pdf.pages[3:16]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Web Link of the Policies" 
                sec_quest_2="Web Link"
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(line)
                    if question.lower() in line.lower():
                        list=lines[i:]
                    elif  question_2.lower() in line.lower():
                        list=lines[i:]

                finallist=[]
                
                for i,selist in enumerate(list):
                    # # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                # #@ print("finallist",finallist)
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # #@ print("51",output_9,len(output_9))
                # #@ print("54",output_10,len(output_10))                
                if output_9:
                    # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return "Not Applicable"


                    
            
    if not found:
        return "Not Applicable"

#@ print(Has_the_policy("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")



def Web_Link_of_Policies(pdf_path):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Web Link of the Policies, if available"
        question_2="Web Link of the Policies"
        question_3="Web Link"
        for i, page in enumerate(pdf.pages[3:16]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # # #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Whether the entity has translated" 
                sec_quest_2="has translated"
                sec_quest_3="procedures"
                list=[]     
                for i, line in enumerate(lines):
                    # # #@ print(line)
                    if question.lower() in line.lower():
                        list=lines[i-1:]
                        break
                    elif question_2.lower() in line.lower():
                        list=lines[i-1:]
                        break
                    elif question_3.lower() in line.lower():
                        list=lines[i-1:]
                # #@ print(list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("#########",i,selist)
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
                # #@ print("finallist",finallist)

                if finallist:
                    return finallist
                
                # else:
                #     return "Not Applicable"

            else:
                found=True
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                res=[]
                url_pattern = r'https?://[^\s,)"]+'
                for l in lines:
                    matches=re.findall(url_pattern,l)
                    res.extend(matches)
                return res
            
    if not found:
        return "Not Applicable"

#@ print(Web_Link_of_Policies("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")

def Whether_entity_translated(pdf_path):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Whether the entity has translated the"
        question_2="the entity has"
        question_3="Whether the entity has translated"
        for i, page in enumerate(pdf.pages[3:16]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # # #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                list=[]     
                for i, line in enumerate(lines):
                    # # #@ print(line)
                    if question.lower() in line.lower():
                        list=lines[i:]
                    elif  question_2.lower() in line.lower():
                        list=lines[i+1:]

                finallist=[]
                sec_quest="Do the enlisted policies extend to your" 
                sec_2="enlisted policies"                
                for i,selist in enumerate(list):
                    # # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_2.lower() in selist.lower():
                        finallist=list[:1+i]
                        break
                    else:
                        finallist=list
                # #@ print("finallist",finallist)
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # #@ print("51",output_9,len(output_9))
                # #@ print("54",output_10,len(output_10))                
                if output_9:
                    # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return "Not Applicable"


                    
            
    if not found:
        return "Not Applicable"

#@ print(Whether_entity_translated("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")


def Do_the_enlisted(pdf_path,):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Do the enlisted policies"
        question_2="enlisted policies extend"
        question_3="Do the enlisted"
        
        for i, page in enumerate(pdf.pages[3:16]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # # #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="national and international" 
                sec_quest_2="Name of the national and"
                sec_quest_3="international codes"
                list=[]     
                for i, line in enumerate(lines):
                    # # #@ print(line)
                    if question.lower() in line.lower():
                        list=lines[i-1:]
                    elif question_2.lower() in line.lower():
                        # # #@ print("ELIF")
                        list=lines[i-1:]
                    elif question_3.lower() in line.lower():
                        # # #@ print("ELIF")
                        list=lines[i-1:]
                # # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    if sec_quest_2.lower() in selist.lower():
                        # # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    if sec_quest_3.lower() in selist.lower():
                        # # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                # # #@ print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # # #@ print("51",output_9,len(output_9))
                # # #@ print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    # # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4                
           
                else:
                    return "Not Applicable"


                    
            
    if not found:
        return "Not Applicable"

#@ print(Do_the_enlisted("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")


def Name_of_the_national(pdf_path):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="national and international codes/certifications/labels/ standards"
        question_2="Name of the national"
        question_3="national and international codes/certifications/labels/"
        for i, page in enumerate(pdf.pages[3:16]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # # #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Specific commitments," 
                list=[]     
                for i, line in enumerate(lines):
                    # # #@ print(line)
                    if question.lower() in line.lower():
                        list=lines[i:]
                    elif question_2.lower() in line.lower():
                        # # #@ print("ELIF")
                        list=lines[i+1:]
                # # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                        
                    else:
                        finallist=list
                # # #@ print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # # #@ print("51",output_9,len(output_9))
                # # #@ print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    # # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4
           
                else:
                    return "Not Applicable" 
            
    if not found:
        return "Not Applicable"

#@ print(Name_of_the_national("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")

def Specific_commitments(pdf_path):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Specific commitments, goals and targets"
        question_2="Specific commitments"
        question_3=" by the entity with defined timelines, if any"
        for i, page in enumerate(pdf.pages[3:16]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Performance of the entity against" 
                sec_quest_2="Performance against"
                sec_quest_3="same are not met."
                list=[]     
                for i, line in enumerate(lines):
                    # # #@ print(line)
                    if question.lower() in line.lower():
                        # #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # #@ print("***q3")
                        list=lines[i:]
                        break
                # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                # #@ print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # # #@ print("51",output_9,len(output_9))
                # # #@ print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    # # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4
           
                else:
                    return "Not Applicable" 
            
    if not found:
        return "Not Applicable"

#@ print(Specific_commitments("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")


def Performance_of_the_entity(pdf_path):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Performance of the entity against the"
        question_2="Performance of the entity"
        question_3=" reasons in case the same are not met."
        for i, page in enumerate(pdf.pages[3:16]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Statement by director responsible" 
                sec_quest_2="Statement by director"
                sec_quest_3="Statement by director responsible"
                list=[]     
                for i, line in enumerate(lines):
                    # # #@ print(line)
                    if question.lower() in line.lower():
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # # #@ print("ELIF")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # # #@ print("ELIF")
                        list=lines[i:]
                        break
                    
                # # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("#########",i,selist)
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
                # #@ print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # # #@ print("51",output_9,len(output_9))
                # # #@ print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    # # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return "Not Applicable" 
            
    if not found:
        return "Not Applicable"

#@ print(Performance_of_the_entity("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")

                                    ###### second part #####
 
 
 
def Statement_by_director(pdf_path):
    #@ print("PART B")
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Statement by director responsible for the business"
        question_2="Statement by director responsible for the business responsibility"
        question_3="Statement by director responsible"

        for i, page in enumerate(pdf.pages[3:16]):
            text = page.extract_text()
            if text and question in text or question_2 in text or question_3 in text:
                found = True
                # #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Details of the highest authority"
                sec_quest_2="Details of the highest" 
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(line)
                    if question.lower() in line.lower():
                        list=lines[i:]
                    elif question_2.lower() in line.lower():
                        # # #@ print("ELIF")
                        list=lines[i+1:]
                # # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        finallist=list[:i]
                    else:
                        finallist=list
                # # #@ print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # # #@ print("51",output_9,len(output_9))
                # # #@ print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    # # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return "Not Applicable"
    if not found:
        return "Not Applicable"

#@ print(Statement_by_director("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")


def Details_of_the_highest(pdf_path):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Details of the highest authority responsible"
        question_2="Details of the highest"
        question_3="Details of the highest authority responsible"
        for i, page in enumerate(pdf.pages[3:16]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # # #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Does the entity have a "
                sec_quest_2="Committee of the " 
                list=[]     
                for i, line in enumerate(lines):
                    # # #@ print(line)
                    if question.lower() in line.lower():
                        list=lines[i:]
                    elif question_2.lower() in line.lower():
                        # # #@ print("ELIF")
                        list=lines[i+1:]
                # # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        finallist=list[:i]
                    else:
                        finallist=list
                # # #@ print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # # #@ print("51",output_9,len(output_9))
                # # #@ print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    # # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4
           
                else:
                    return "Not Applicable"


                    
            
    if not found:
        return "Not Applicable"

#@ print(Details_of_the_highest("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")



def Does_the_entity(pdf_path):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Does the entity have a specified Committee"
        question_2="specified Committee of"
        question_3="Director responsible for decision"
        for i, page in enumerate(pdf.pages[3:16]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Details of Review of NGRBCs by the Company"
                sec_quest_2="Details of Review" 
                sec_quest_3="Review of NGRBCs"
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(i,line)
                    if question.lower() in line.lower():
                        # #@ print("***q1")
                        list=lines[i:]
                    elif question_2.lower() in line.lower():
                        # #@ print("***q2")
                        list=lines[i:]
                    elif question_3.lower() in line.lower():
                        list=lines[i:]
                # # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                # #@ print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # #@ print("51",output_9,len(output_9))
                # #@ print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return "Not Applicable"


                    
            
    if not found:
        return "Not Applicable"

#@ print(Does_the_entity("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")


def Indicate_whether_review(pdf_path):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Indicate whether review was undertaken"
        question_2="undertaken by Director"
        question_3="Indicate whether review"
        for i, page in enumerate(pdf.pages[3:16]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=" Has the entity carried out independent assessment"
                sec_quest_2=" Has the entity carried out independent" 
                sec_quest_3=" Has the entity carried"
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(i,line)
                    if question.lower() in line.lower():
                        # #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        list=lines[i:]
                        break
                # # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                # #@ print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # #@ print("51",output_9,len(output_9))
                # #@ print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return "Not Applicable"


                    
            
    if not found:
        return "Not Applicable"

#@ print(Indicate_whether_review("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")



def Frequency_Annually(pdf_path):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Frequency (Annually/ Half yearly/ Quarterly Any other"
        question_2="Frequency (Annually/ Half yearly/ Quarterly/"
        question_3="Frequency (Annually/"
        for i, page in enumerate(pdf.pages[3:16]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                lines = ocr_text.splitlines()
                # #@ print(lines)
                sec_quest=" Has the entity carried out independent assessment"
                sec_quest_2=" Has the entity carried out independent" 
                sec_quest_3=" Has the entity carried"
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(i,line)
                    if question.lower() in line.lower():
                        # #@ print("***q1")
                        list=lines[i:]
                    elif question_2.lower() in line.lower():
                        # #@ print("***q2")
                        list=lines[i:]
                    elif question_3.lower() in line.lower():
                        # #@ print("***q3")
                        list=lines[i:]
                    else:
                        finallist=list
                # # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                # #@ print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # #@ print("51",output_9,len(output_9))
                # #@ print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return "Not Applicable"


                    
            
    if not found:
        return "Not Applicable"

#@ print(Frequency_Annually("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")


def Compliance_with_statutory(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Compliance with statutory requirements of relevance to the principles",
        "Compliance with statutory",
        "rectification of any non-compliances"

    ]
    q_ends = [
        "Has the entity carried out independent assessment/ evaluation",
        "evaluation of the working of its policies",
        "provide name of the agency"
    ]

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[3:16]:
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

    # #@ print("#######",lines_between)
    if lines_between:
        return lines_between
    else:
        return "Not Applicable"
# #@ print(Compliance_with_statutory("C:/Users/coda/Documents/tata.pdf"))
# #@ print("************")




def Has_the_entity_carried(pdf_path):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Has the entity carried out independent"
        question_2="Has the entity"
        question_3="If yes, provide name of the agency"
        for i, page in enumerate(pdf.pages[3:16]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="If answer to question (1) above"
                sec_quest_2="If answer to question" 
                list=[]     
                for i, line in enumerate(lines):
                    # # #@ print(line)
                    if question.lower() in line.lower():
                        list=lines[i:]
                    elif question_2.lower() in line.lower():
                        # # #@ print("ELIF")
                        list=lines[i+1:]
                # # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        finallist=list[:i]
                    else:
                        finallist=list
                # # #@ print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # #@ print("51",output_9,len(output_9))
                # #@ print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return "Not Applicable"


                    
            
    if not found:
        return "Not Applicable"

#@ print(Has_the_entity_carried("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")


  ##### 12-th

def If_answer_to_question(pdf_path):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="If answer to question (1) above is"
        question_2="If answer to question (1) above is “No”"
        question_3="answer to question"
        for i, page in enumerate(pdf.pages[3:16]):
            text = page.extract_text()
            if text and question in text or question_2 in text or question_3 in text:
                found = True
                # #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Supply Chain Mangement"
                sec_quest_2="SECTION C" 
                sec_quest_3="PRINCIPLE WISE PERFORMANCE DISCLOSURE"
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(line)
                    if question.lower() in line.lower():
                        # #@ print("::")
                        list=lines[i:]
                    elif question_2.lower() in line.lower():
                        # #@ print("ELIF")
                        list=lines[i+1:]
                    elif question_3.lower() in line.lower():
                        list=lines[i+1:]
                # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        # break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print("HBJAS")
                        finallist=list[:i]
                        # break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("KKKKs")
                        finallist=list[:1+i]
                        # break
                    else:
                        finallist=list[i]
                # #@ print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # #@ print("51",output_9,len(output_9))
                # #@ print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return "Not Applicable"


                    
            
    if not found:
        return "Not Applicable"

#@ print(If_answer_to_question("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")


def consider_the_Principles(pdf_path):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="The entity does not consider the Principles"
        question_2="The entity does not consider"
        question_3="The entity does not"
        for i, page in enumerate(pdf.pages[3:16]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="The entity is not at a stage"
                sec_quest_2="The entity is not" 
                sec_quest_3="The entity is"
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(i,line)
                    if question.lower() in line.lower():
                        # #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # #@ print("**q3")
                        list=lines[i:]
                        break
                    else:
                        # #@ print("else")
                        finallist=list
                # # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                # #@ print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # #@ print("51",output_9,len(output_9))
                # #@ print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:
                    finq="The entity does not consider the Principles material to its business (Yes/No)"  
                    # for f in finallist:
                    #     if f == finq:
                    #         # #@ print("ksjdnckjm")
                                              
                    return str(finallist)
                elif output_9:
                    # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return "Not Applicable"


                    
            
    if not found:
        return "Not Applicable"

#@ print( consider_the_Principles("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")


def formulate_and_implement(pdf_path):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="The entity is not at a stage where it is in a position"
        question_2="The entity is not at a stage where "
        question_3="The entity is not"
        for i, page in enumerate(pdf.pages[3:16]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="The entity does not have the financial"
                sec_quest_2="human and technical resources" 
                sec_quest_3="technical resources"
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(i,line)
                    if question.lower() in line.lower():
                        # #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        list=lines[i:]
                        break
                    else:
                        finallist=list
                # # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                # #@ print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # #@ print("51",output_9,len(output_9))
                # #@ print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return "Not Applicable"


                    
            
    if not found:
        return "Not Applicable"

#@ print( formulate_and_implement("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")



def human_and_technical(pdf_path):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="The entity does not have the financial"
        question_2="not have the financial"
        question_3="The entity does not"
        for i, page in enumerate(pdf.pages[3:16]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="It is planned to be done in the next financial"
                sec_quest_2="It is planned to be done" 
                sec_quest_3="the next financial"
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(i,line)
                    if question.lower() in line.lower():
                        # #@ print("***q1")
                        list=lines[i:]
                    elif question_2.lower() in line.lower():
                        # #@ print("***q2")
                        list=lines[i:]
                    elif question_3.lower() in line.lower():
                        list=lines[i:]
                    else:
                        # #@ print("&&&&&&&")
                        finallist=list
                # # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                # #@ print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # #@ print("51",output_9,len(output_9))
                # #@ print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return "Not Applicable"


                    
            
    if not found:
        return "Not Applicable"

#@ print(human_and_technical("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")


def It_is_planned_to_be_done(pdf_path):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="done in the next financial year"
        question_2="It is planned to be done in"
        question_3="next financial year (Yes/No)"
        for i, page in enumerate(pdf.pages[3:16]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # #@ print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Any other reason (please specify)"
                sec_quest_2="Any other reason" 
                sec_quest_3="Section C"
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(i,line)
                    if question.lower() in line.lower():
                        # #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        list=lines[i:]
                        break
                    else:
                        finallist=list
                # # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                # #@ print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # #@ print("51",output_9,len(output_9))
                # #@ print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return "Not Applicable"


                    
            
    if not found:
        return "Not Applicable"

#@ print(It_is_planned_to_be_done("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")

def Any_other_reason(pdf_path):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # #@ print("file opend")
        question="Any other reason (please specify)"
        question_2="Any other reason (please specify)"
        question_3="Any other reason "
        for i, page in enumerate(pdf.pages[3:16]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                # #@ print(f"Question found on page {i + 1}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # #@ print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Section C"
                sec_quest_2="PRINCIPLE WISE PERFORMANCE DISCLOSURE" 
                sec_quest_3="Businesses should conduct"
                list=[]     
                for i, line in enumerate(lines):
                    # #@ print(i,line)
                    if question.lower() in line.lower():
                        # #@ print("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        # #@ print("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        # #@ print("***q3")
                        list=lines[i:]
                        break
                    # else:
                    #     finallist=list
                # #@ print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #@ print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        # #@ print("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        # #@ print("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        # #@ print("&& sec3")
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                # #@ print("finallist",finallist)
                
                output_9=[]
                output_10=[]
                for i in finallist:
                    parts = re.split(r'\s{2,}|\s*\|\s*',i)
                    # #@ print("43",len(parts),parts)
                    if len(parts)>=8:
                        output_9=parts
                    else:
                        output_10=parts
                # #@ print("51",output_9,len(output_9))
                # #@ print("54",output_10,len(output_10))                
                if len(output_9)<3 and len(output_10)<3:                    
                    return str(finallist)
                elif output_9:
                    # #@ print("output-9 is exist",output_9,len(output_9))
                    getlast=output_9[-9:]
                    # #@ print(getlast)
                    princ=[]
                    for i in getlast:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_3 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_3

                
                elif output_10:
                    # #@ print("output-10 is exist",output_10,len(output_10))
                    princ=[]
                    for i in output_10:
                        if len(i)<=3:
                            princ.append(i)
                    # #@ print("prince",princ)
                    data_4 = {
                        f"P{i+1}": princ[i] if i < len(princ) else None
                        for i in range(9)
                    }
                    return data_4

           
                else:
                    return "Not Applicable"


                    
            
    if not found:
        return "Not Applicable"

#@ print(Any_other_reason("C:/Users/coda/Documents/ncc.pdf"))
#@ print("************")




