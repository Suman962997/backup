import pdfplumber
import pytesseract
from PIL import Image
import io
import re

                                        ######## PART II #########
def Details_of_business(pdf_path,question):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # print("file opend")
        question_2="Details of business activities (accounting for 90% of the turnover)"
        question_3="Details of business activities"
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
                sec_quest="Products/Service" 
                sec_quest_2="Products/Services sold by the entity"
                sec_quest_3="Products/Services sold by the entity (accounting for 90% of the entity’s turnover)"
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
# print(Details_of_business("C:/Users/coda/Documents/deigeo.pdf","Details of business activities"))
# print("**************")

def Products_Services(pdf_path,question):
    
    found = False
    with pdfplumber.open(pdf_path) as pdf:
        # print("file opend")
        question_2="Products/Services sold by the entity (accounting for 90% of the entity’s turnover)"
        question_3="Products/Services sold by the entity"
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
                sec_quest="Operations" 
                sec_quest_2="Number of locations where plants and/or operations/offices of the entity are situated"
                sec_quest_3="Number of locations where plants"
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
                    "Product/ Service":output_4[-1][1],
                    "NIC Code":output_4[-1][2],
                    "% of Turnoverof the contributed":output_4[-1][3]}]
                    return data_4                    



                elif output_3:
                    # print("output-3 is exist",output_3,len(output_3))
                    data_3=[{
                    "S:No":1,
                    "Product/ Service":output_3[-1][0],
                    "NIC Code":output_3[-1][1],
                    "% of Turnoverof the contributed":output_3[-1][2]}]
                    return data_3

                    
            
    if not found:
        return None
# print(Products_Services("C:/Users/coda/Documents/deigeo.pdf","Products/Services sold by the entity (accounting for 90% of the entity’s turnover)"))
# print("**************")

def Number_of_locations(pdf_path,question):
    
    found = False
    with pdfplumber.open(pdf_path) as pdf:
        # print("file opend")
        question_2="Number of locations where plants"
        question_3="of the entity are situated"
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
                sec_quest="Markets served by" 
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
                finallist=[]
                
                sec_quest="Markets served by the entity - No of locations" 
                sec_quest_2="Markets served by the entity - No of locations"
                sec_quest_3="Markets served by the entity - No of locations"
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
                    "Product/ Service":output_4[-1][1],
                    "NIC Code":output_4[-1][2],
                    "% of Turnoverof the contributed":output_4[-1][3]}]
                    return data_4                    



                elif output_3:
                    # print("output-3 is exist",output_3,len(output_3))
                    data_3=[{
                    "S:No":1,
                    "Product/ Service":output_3[-1][0],
                    "NIC Code":output_3[-1][1],
                    "% of Turnoverof the contributed":output_3[-1][2]}]
                    return data_3

                    
            
    if not found:
        return None
# print(Number_of_locations("C:/Users/coda/Documents/deigeo.pdf","Number of locations where plants and/or operations/offices of the entity are situated"))
# print("**************")




                                        ######## PART III #########








