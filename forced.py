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




                        ###### PRINCIPLE IX #########
                        
                        


def  complaints_feedback(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2="Describe the mechanisms in"
        question_3="consumer complaints and feedback"
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
                sec_quest="Turnover of products and/ services"
                sec_quest_2="all products/service that carry information about" 
                sec_quest_3="carry information about"
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

# print(complaints_feedback("C:/Users/coda/Documents/HUL.pdf","Describe the mechanisms in place to receive and respond to consumer complaints and feedback"))
# print("************")




def Turnover_products(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2="Turnover of products and/ services"
        question_3="service that carry information about"
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
                sec_quest="Number of consumer complaints in respect of the following"
                sec_quest_2="Number of consumer complaints " 
                sec_quest_3="respect of the following"
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

# print(Turnover_products("C:/Users/coda/Documents/HUL.pdf","Turnover of products and/ services as a percentage of turnover from all products/service that carry information about"))
# print("************")




def Number_consumer(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2="Number of consumer complaints"
        question_3="respect of the following"
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
                sec_quest="Details of instances of product recalls on account of safety issues"
                sec_quest_2="Details of instances of product" 
                sec_quest_3="account of safety issues"
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

# print(Number_consumer("C:/Users/coda/Documents/HUL.pdf","Number of consumer complaints in respect of the following"))
# print("************")




def account_safety_issues(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2="Details of instances of product"
        question_3="recalls on account of safety issues:"
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
                sec_quest="Does the entity have a framework/ policy"
                sec_quest_2="provide weblink of the policy" 
                sec_quest_3="weblink of the policy."
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

# print(account_safety_issues("C:/Users/coda/Documents/HUL.pdf","Details of instances of product recalls on account of safety issues"))
# print("************")




def weblink_the_policy(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        # print("file opend")
        question_2="Does the entity have a framework/ policy"
        question_3="weblink of the policy"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                (f"Question found on page {i}")
                image = page.to_image(resolution=300).original  # 300 DPI is usually enough

                # Run Tesseract with config to preserve whitespaces
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                # # #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Provide details of any corrective actions taken"
                sec_quest_2="Provide details of any corrective" 
                sec_quest_3="safety of products / services"
                list=[]     
                for i, line in enumerate(lines):
                    # #(i,line)
                    if question.lower() in line.lower():
                        ("***q1")
                        list=lines[i:]
                        break
                    elif question_2.lower() in line.lower():
                        ("***q2")
                        list=lines[i:]
                        break
                    elif question_3.lower() in line.lower():
                        ("****q3")
                        list=lines[i:]
                        break
                ("405 **",list)
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

# print(weblink_the_policy("C:/Users/coda/Documents/HUL.pdf","Does the entity have a framework/ policy on cyber security and"))
# print("************")



def  issues_relating(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2="cyber security and data privacy of customers; re-occurrence of instances"
        question_3="penalty / action taken by regulatory authorities on safety of products / services."
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
                sec_quest="Channels / platforms where information"
                sec_quest_2="accessed (provide web link" 
                sec_quest_3="Leadership Indicators"
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

# print(issues_relating("C:/Users/coda/Documents/HUL.pdf","Provide details of any corrective actions taken or underway on issues relating to advertising"))
# print("************")



def Channels_platforms(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2="Channels / platforms where information on products"
        question_3="services of the entity can be accessed"
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
                sec_quest=" Steps taken to inform and educate consumers about safe and responsible usage of products and/or services"
                sec_quest_2="Steps taken to inform and educate" 
                sec_quest_3="products and/or services"
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

# print(Channels_platforms("C:/Users/coda/Documents/HUL.pdf","Channels / platforms where information on products and services of the entity can be accessed (provide web"))
# print("************")



def Steps_taken(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2="Steps taken to inform and"
        question_3="products and/or services"
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
                sec_quest="Mechanisms in place to inform consumers of any risk of disruption/discontinuation of essential services"
                sec_quest_2="Mechanisms in place to inform" 
                sec_quest_3="discontinuation of essential services"
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

# print(Steps_taken("C:/Users/coda/Documents/HUL.pdf","Steps taken to inform and educate consumers about safe and responsible usage of products and/or services"))
# print("************")



def Mechanisms_place(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2="Mechanisms in place to inform consumers"
        question_3="discontinuation of essential services"
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
                sec_quest="Does the entity display product information on the product over and above what is mandated as per local laws"
                sec_quest_2="Does the entity display " 
                sec_quest_3="mandated as per local laws"
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

# print(Mechanisms_place("C:/Users/coda/Documents/HUL.pdf","Mechanisms in place to inform consumers of any risk of disruption/discontinuation of essential services"))
# print("************")



def entity_display_product(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2="Does the entity display product information on the product over and above what is "
        question_3="mandated as per local laws"
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
                sec_quest="Provide the following information relating to data breaches"
                sec_quest_2="Provide the following information " 
                sec_quest_3="relating to data breaches"
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

# print(entity_display_product("C:/Users/coda/Documents/HUL.pdf","Does the entity display product information on the product over and above what is mandated as per local laws"))
# print("************")


def data_breaches(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2="Provide the following information relating"
        question_3="data breaches"
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
                sec_quest="Number of instances of data breaches along-with impact"
                sec_quest_2="Number of instances " 
                sec_quest_3="along-with impact"
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

# print(data_breaches("C:/Users/coda/Documents/HUL.pdf","Provide the following information relating to data breaches"))
# print("************")



def instances_data_breaches (pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2="Number of instances of data breaches "
        question_3="along-with impact"
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
                sec_quest="Percentage of data breaches involving personally identifiable information of customers"
                sec_quest_2="Percentage of data breaches " 
                sec_quest_3="information of customers"
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

# print(instances_data_breaches("C:/Users/coda/Documents/HUL.pdf","Number of instances of data breaches along-with impact"))
# print("************")




def Percentage_data_breaches(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question_2="Percentage of data breaches involving "
        question_3="identifiable information of customers"
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
                sec_quest="last"
                sec_quest_2="dc d" 
                sec_quest_3="cdcd"
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

# print(Percentage_data_breaches("C:/Users/coda/Documents/HUL.pdf","Percentage of data breaches involving personally identifiable information of customers"))
# print("************")
