import pdfplumber
import pytesseract
from PIL import Image
import io
import re




                    ####### PRINCIPL VII ########
                    
                    
                    
def a(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2=""
        question_3=""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=""
                sec_quest_2="" 
                sec_quest_3=""
                list=[]     
                for i, line in enumerate(lines):
                    # #(i,line)
                    if question.lower() in line.lower():
                        #("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        #("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        #("****q3")
                        list=lines[i:]
                        break
                # #("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        #("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        #("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        #("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #("finallist",finallist)
                return finallist                       

#(a("C:/Users/coda/Documents/HUL.pdf",""))
#("************")


def a(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2=""
        question_3=""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=""
                sec_quest_2="" 
                sec_quest_3=""
                list=[]     
                for i, line in enumerate(lines):
                    # #(i,line)
                    if question.lower() in line.lower():
                        #("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        #("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        #("****q3")
                        list=lines[i:]
                        break
                # #("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        #("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        #("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        #("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #("finallist",finallist)
                return finallist                       

#(a("C:/Users/coda/Documents/HUL.pdf",""))
#("************")


def a(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2=""
        question_3=""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=""
                sec_quest_2="" 
                sec_quest_3=""
                list=[]     
                for i, line in enumerate(lines):
                    # #(i,line)
                    if question.lower() in line.lower():
                        #("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        #("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        #("****q3")
                        list=lines[i:]
                        break
                # #("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        #("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        #("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        #("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #("finallist",finallist)
                return finallist                       

#(a("C:/Users/coda/Documents/HUL.pdf",""))
#("************")



def a(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2=""
        question_3=""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=""
                sec_quest_2="" 
                sec_quest_3=""
                list=[]     
                for i, line in enumerate(lines):
                    # #(i,line)
                    if question.lower() in line.lower():
                        #("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        #("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        #("****q3")
                        list=lines[i:]
                        break
                # #("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        #("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        #("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        #("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #("finallist",finallist)
                return finallist                       

#(a("C:/Users/coda/Documents/HUL.pdf",""))
#("************")




def a(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2=""
        question_3=""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=""
                sec_quest_2="" 
                sec_quest_3=""
                list=[]     
                for i, line in enumerate(lines):
                    # #(i,line)
                    if question.lower() in line.lower():
                        #("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        #("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        #("****q3")
                        list=lines[i:]
                        break
                # #("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        #("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        #("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        #("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #("finallist",finallist)
                return finallist                       

#(a("C:/Users/coda/Documents/HUL.pdf",""))
#("************")



def a(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2=""
        question_3=""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=""
                sec_quest_2="" 
                sec_quest_3=""
                list=[]     
                for i, line in enumerate(lines):
                    # #(i,line)
                    if question.lower() in line.lower():
                        #("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        #("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        #("****q3")
                        list=lines[i:]
                        break
                # #("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        #("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        #("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        #("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #("finallist",finallist)
                return finallist                       

#(a("C:/Users/coda/Documents/HUL.pdf",""))
#("************")




                ###### PRINCIPLE VIII #######


def SIA(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2="Details of Social Impact Assessments (SIA) of projects"
        question_3="in the current financial year"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Provide information on project(s) for which ongoing Rehabilitation and Resettlement (R&R) is being undertaken by your"
                sec_quest_2="Provide information on project(s) for" 
                sec_quest_3=" entity, in the following format"
                list=[]     
                for i, line in enumerate(lines):
                    # #(i,line)
                    if question.lower() in line.lower():
                        #("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        #("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        #("****q3")
                        list=lines[i:]
                        break
                # #("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        #("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        #("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        #("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #("finallist",finallist)
                return finallist                       

#(SIA("C:/Users/coda/Documents/HUL.pdf","Details of Social Impact Assessments (SIA)"))
#("************")




def Provide_information(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2="Provide information on project(s)"
        question_3="entity, in the following format"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Describe the mechanisms to receive and redress grievances of the community"
                sec_quest_2="Describe the mechanisms to" 
                sec_quest_3="grievances of the community"
                list=[]     
                for i, line in enumerate(lines):
                    # #(i,line)
                    if question.lower() in line.lower():
                        #("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        #("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        #("****q3")
                        list=lines[i:]
                        break
                # #("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        #("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        #("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        #("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #("finallist",finallist)
                return finallist                       

#(Provide_information("C:/Users/coda/Documents/HUL.pdf","Provide information on project(s) for which ongoing"))
#("************")





def Percentage_input(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2="Describe the mechanisms"
        question_3="grievances of the community"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Percentage of input material (inputs to total inputs by value) sourced from suppliers"
                sec_quest_2="Percentage of input material" 
                sec_quest_3=" sourced from suppliers"
                list=[]     
                for i, line in enumerate(lines):
                    # #(i,line)
                    if question.lower() in line.lower():
                        #("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        #("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        #("****q3")
                        list=lines[i:]
                        break
                # #("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        #("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        #("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        #("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #("finallist",finallist)
                return finallist                       

#(Percentage_input("C:/Users/coda/Documents/HUL.pdf","Describe the mechanisms to receive and redress grievances of the community"))
#("************")




def Job_creation(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2="Job creation in smaller towns – Disclose wages paid to persons employed (including employees or workers employed "
        question_3="locations, as % of total wage cost"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Provide details of actions taken to mitigate any negative social impacts identified in the Social Impact Assessments "
                sec_quest_2="Provide details of actions taken to mitigate any negative" 
                sec_quest_3="(Reference: Question 1 of Essential Indicators above)"
                list=[]     
                for i, line in enumerate(lines):
                    # #(i,line)
                    if question.lower() in line.lower():
                        #("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        #("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        #("****q3")
                        list=lines[i:]
                        break
                # #("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        #("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        #("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        #("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #("finallist",finallist)
                return finallist                       

#(Job_creation("C:/Users/coda/Documents/HUL.pdf","Job creation in smaller towns – Disclose wages "))
#("************")




def a(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2=""
        question_3=""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=""
                sec_quest_2="" 
                sec_quest_3=""
                list=[]     
                for i, line in enumerate(lines):
                    # #(i,line)
                    if question.lower() in line.lower():
                        #("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        #("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        #("****q3")
                        list=lines[i:]
                        break
                # #("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        #("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        #("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        #("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #("finallist",finallist)
                return finallist                       

#(a("C:/Users/coda/Documents/HUL.pdf",""))
#("************")





def a(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2=""
        question_3=""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=""
                sec_quest_2="" 
                sec_quest_3=""
                list=[]     
                for i, line in enumerate(lines):
                    # #(i,line)
                    if question.lower() in line.lower():
                        #("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        #("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        #("****q3")
                        list=lines[i:]
                        break
                # #("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        #("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        #("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        #("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #("finallist",finallist)
                return finallist                       

#(a("C:/Users/coda/Documents/HUL.pdf",""))
#("************")




def a(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2=""
        question_3=""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=""
                sec_quest_2="" 
                sec_quest_3=""
                list=[]     
                for i, line in enumerate(lines):
                    # #(i,line)
                    if question.lower() in line.lower():
                        #("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        #("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        #("****q3")
                        list=lines[i:]
                        break
                # #("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        #("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        #("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        #("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #("finallist",finallist)
                return finallist                       

#(a("C:/Users/coda/Documents/HUL.pdf",""))
#("************")




def a(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2=""
        question_3=""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=""
                sec_quest_2="" 
                sec_quest_3=""
                list=[]     
                for i, line in enumerate(lines):
                    # #(i,line)
                    if question.lower() in line.lower():
                        #("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        #("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        #("****q3")
                        list=lines[i:]
                        break
                # #("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        #("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        #("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        #("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #("finallist",finallist)
                return finallist                       

#(a("C:/Users/coda/Documents/HUL.pdf",""))
#("************")





def a(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2=""
        question_3=""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=""
                sec_quest_2="" 
                sec_quest_3=""
                list=[]     
                for i, line in enumerate(lines):
                    # #(i,line)
                    if question.lower() in line.lower():
                        #("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        #("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        #("****q3")
                        list=lines[i:]
                        break
                # #("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        #("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        #("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        #("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #("finallist",finallist)
                return finallist                       

#(a("C:/Users/coda/Documents/HUL.pdf",""))
#("************")




def a(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2=""
        question_3=""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=""
                sec_quest_2="" 
                sec_quest_3=""
                list=[]     
                for i, line in enumerate(lines):
                    # #(i,line)
                    if question.lower() in line.lower():
                        #("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        #("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        #("****q3")
                        list=lines[i:]
                        break
                # #("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        #("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        #("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        #("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #("finallist",finallist)
                return finallist                       

#(a("C:/Users/coda/Documents/HUL.pdf",""))
#("************")




def a(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2=""
        question_3=""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=""
                sec_quest_2="" 
                sec_quest_3=""
                list=[]     
                for i, line in enumerate(lines):
                    # #(i,line)
                    if question.lower() in line.lower():
                        #("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        #("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        #("****q3")
                        list=lines[i:]
                        break
                # #("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        #("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        #("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        #("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #("finallist",finallist)
                return finallist                       

#(a("C:/Users/coda/Documents/HUL.pdf",""))
#("************")




def a(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2=""
        question_3=""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=""
                sec_quest_2="" 
                sec_quest_3=""
                list=[]     
                for i, line in enumerate(lines):
                    # #(i,line)
                    if question.lower() in line.lower():
                        #("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        #("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        #("****q3")
                        list=lines[i:]
                        break
                # #("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        #("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        #("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        #("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #("finallist",finallist)
                return finallist                       

#(a("C:/Users/coda/Documents/HUL.pdf",""))
#("************")




def a(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2=""
        question_3=""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=""
                sec_quest_2="" 
                sec_quest_3=""
                list=[]     
                for i, line in enumerate(lines):
                    # #(i,line)
                    if question.lower() in line.lower():
                        #("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        #("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        #("****q3")
                        list=lines[i:]
                        break
                # #("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        #("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        #("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        #("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #("finallist",finallist)
                return finallist                       

#(a("C:/Users/coda/Documents/HUL.pdf",""))
#("************")




def a(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2=""
        question_3=""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=""
                sec_quest_2="" 
                sec_quest_3=""
                list=[]     
                for i, line in enumerate(lines):
                    # #(i,line)
                    if question.lower() in line.lower():
                        #("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        #("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        #("****q3")
                        list=lines[i:]
                        break
                # #("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    # #("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        #("#########",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        #("### sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        #("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                # #("finallist",finallist)
                return finallist                       

#(a("C:/Users/coda/Documents/HUL.pdf",""))
#("************")



