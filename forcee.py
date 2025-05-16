import pdfplumber
import pytesseract
from PIL import Image
import io
import re

                                                    ###### PRINCIPLE IV #########



def Describe_processes(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Describe the processes for identifying key stakeholder groups of the entity"
        question_3="stakeholder groups of the entity"
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
                sec_quest="List stakeholder groups identified as key for your entity and the frequency of engagement with each stakeholder group"
                sec_quest_2="List stakeholder groups identified as key for " 
                sec_quest_3=" engagement with each stakeholder group"
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

# print(Describe_processes("C:/Users/coda/Documents/deigeo.pdf","Describe the processes for identifying key stakeholder groups of the entity."))
# print("************")


def List_stakeholder (pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="List stakeholder groups identified as key for your entity and the frequency of engagement"
        question_3="each stakeholder group"
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
                sec_quest="Provide the processes for consultation between stakeholders and the Board on economic, environmental, and social topics or if consultation is delegated, how is feedback from such consultations provided to the Board"
                sec_quest_2="Provide the processes for consultation between stakeholders and the Board " 
                sec_quest_3=" feedback from such consultations provided to the Board"
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

# print(List_stakeholder("C:/Users/coda/Documents/deigeo.pdf","List stakeholder groups identified as key for your entity and the frequency of engagement with"))
# print("************")


def consultation_between_stakeholders(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Provide the processes for consultation between stakeholders and the Board on economic" 
        question_3="how is feedback from such consultations provided to the Board"
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
                sec_quest="Whether stakeholder consultation is used to support the identification and management of environmental, and social topics (Yes / No). If so, provide details of instances as to how the inputs received from stakeholders on these topics were incorporated into policies and activities of the entity"
                sec_quest_2="Whether stakeholder consultation is used to support the identification"
                sec_quest_3="stakeholders on these topics were incorporated into policies and activities"
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

# print(consultation_between_stakeholders("C:/Users/coda/Documents/deigeo.pdf","Provide the processes for consultation between stakeholders and the Board on economic, environmental, and social topics or if consultation is delegated, how is feedback from such consultations provided"))
# print("************")




def Whether_stakeholder_consultation(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Whether stakeholder consultation is used to support the identification and management of environmental"
        question_3="incorporated into policies and activities of the entity"
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
                sec_quest="Provide details of instances of engagement with, and actions taken to, address the concerns of vulnerable/ marginalized stakeholder groups"
                sec_quest_2="Provide details of instances of engagement" 
                sec_quest_3=" address the concerns of vulnerable/ marginalized stakeholder groups"
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

# print(Whether_stakeholder_consultation("C:/Users/coda/Documents/deigeo.pdf","Whether stakeholder consultation is used to support the identification and management of environmental, and social topics (Yes / No). If so, provide details of instances as to how the inputs received from stakeholders on these topics were incorporated into policies"))
# print("************")




def concerns_vulnerable(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Provide details of instances of engagement with, and actions taken to"
        question_3="vulnerable/ marginalized stakeholder groups"
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
                sec_quest="Principle 5:"
                sec_quest_2="Businesses should respect and promote human rights." 
                sec_quest_3="Businesses should respect"
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

# print(concerns_vulnerable("C:/Users/coda/Documents/deigeo.pdf","Provide details of instances of engagement with, and actions taken to, address the concerns of vulnerable/ marginalized stakeholder groups"))






                            ######### PRINCIPLE V ##########
                            



def employees_workers(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Employees and workers who have been provided"
        question_3="human rights issues and policy(ies) of the entity, in the following format"
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
                sec_quest="Details of minimum wages paid to employees and workers, in the following format"
                sec_quest_2="Details of minimum wages paid to employees " 
                sec_quest_3="workers, in the following format"
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

# print(employees_workers("C:/Users/coda/Documents/deigeo.pdf","Employees and workers who have been provided training on human rights issues and policy(ies) of the entity, in the following format:"))
# print("************")




def  minimum_wages_paid(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Details of minimum wages paid to employees and workers, in the following format"
        question_3="minimum wages paid"
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
                sec_quest="Details of remuneration/salary/wages"
                sec_quest_2="remuneration/salary/wages" 
                sec_quest_3="salary/wages"
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

# print(minimum_wages_paid("C:/Users/coda/Documents/deigeo.pdf","Details of minimum wages paid to employees and workers, in the following format:"))
# print("************")





def Median_remuneration(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Median remuneration / wages"
        question_3="remuneration / wages"
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
                sec_quest="Gross wages paid to females as % of total wages paid by the entity, in the following format"
                sec_quest_2="Gross wages paid to females as % of total " 
                sec_quest_3="paid by the entity, in the following format"
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

# print(Median_remuneration("C:/Users/coda/Documents/deigeo.pdf","Median remuneration / wages"))
# print("************")





def Gross_wages(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Gross wages paid to females as % of total"
        question_3="total wages paid by the entity, in the following format"
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
                sec_quest="Do you have a focal point (Individual/ Committee) responsible for addressing human rights impacts or issues caused or contributed to by the business"
                sec_quest_2="Do you have a focal point (Individual/ Committee)" 
                sec_quest_3="rights impacts or issues caused or contributed to by the business"
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

# print(Gross_wages("C:/Users/coda/Documents/deigeo.pdf","Gross wages paid to females as % of total wages paid by the entity, in the following format:"))
# print("************")




def focal_point(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Do you have a focal point (Individual/ Committee)"
        question_3="issues caused or contributed to by the business"
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
                sec_quest="Describe the internal mechanisms in place to redress grievances related to human rights issues"
                sec_quest_2="Describe the internal mechanisms " 
                sec_quest_3="grievances related to human rights issues"
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

# print(focal_point("C:/Users/coda/Documents/deigeo.pdf","Do you have a focal point (Individual/ Committee) responsible for addressing human"))
# print("************")




def human_rights_issues(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Describe the internal mechanisms in place to redress "
        question_3="grievances related to human rights issues"
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
                sec_quest="Number of Complaints on the following made by employees and workers"
                sec_quest_2="Number of Complaints on the following made by employees and workers" 
                sec_quest_3="following made by employees and workers"
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

# print(human_rights_issues("C:/Users/coda/Documents/deigeo.pdf","Describe the internal mechanisms in place to redress grievances related to human rights issues."))
# print("************")




def Number_Complaints(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Number of Complaints on the following made by employees and workers"
        question_3="Number of Complaints"
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
                sec_quest="Complaints filed under the Sexual Harassment of>>> Women at Workplace"
                sec_quest_2="Complaints filed under the Sexual Harassment" 
                sec_quest_3="2013, in the following format"
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

# print(Number_Complaints("C:/Users/coda/Documents/deigeo.pdf","Number of Complaints on the following made by employees and workers:"))
# print("************")




def Complaints_filed(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Complaints filed under the Sexual Harassment"
        question_3=" 2013, in the following format"
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
                sec_quest="Mechanisms to prevent adverse consequences to the complainant in discrimination and harassment cases"
                sec_quest_2="Mechanisms to prevent adverse consequences" 
                sec_quest_3="complainant in discrimination and harassment cases"
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

# print(Complaints_filed("C:/Users/coda/Documents/deigeo.pdf","Complaints filed under the Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013, in the following format"))
# print("************")




def Mechanisms_prevent(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Mechanisms to prevent adverse consequences "
        question_3="discrimination and harassment cases"
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
                sec_quest="Do human rights requirements form part of your business agreements and contracts"
                sec_quest_2="Do human rights requirements" 
                sec_quest_3="your business agreements and contracts"
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

# print(Mechanisms_prevent("C:/Users/coda/Documents/deigeo.pdf","Mechanisms to prevent adverse consequences to the complainant in discrimination and harassment cases"))
# print("************")





def human_rights_requirements(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Do human rights requirements form part of your business agreements and contracts"
        question_3="your business agreements and contracts"
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
                sec_quest="Assessments for the year"
                sec_quest_2="Assessments for the year" 
                sec_quest_3="Assessments"
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

# print(human_rights_requirements("C:/Users/coda/Documents/deigeo.pdf","Do human rights requirements form part of your business agreements and contracts? (Yes/ No)"))
# print("************")




def corrective_actions_taken(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Provide details of any corrective actions taken or underway to address significant risks / concerns arising from the assessments at Question 10 above"
        question_3="assessments at Question 10 above"
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
                sec_quest="Details of a business process being modified / introduced as a result of addressing human rights grievances/complaints"
                sec_quest_2="Details of a business process being modified" 
                sec_quest_3=" addressing human rights grievances/complaints"
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

# print(a("C:/Users/coda/Documents/deigeo.pdf","Provide details of any corrective actions taken or underway to address significant risks / concerns arising from the assessments at Question 10 above."))
# print("************")



def business_process(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Details of a business process being modified / introduced"
        question_3="result of addressing human rights grievances/complaints"
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
                sec_quest="Details of the scope and coverage of any Human rights due-diligence conducted"
                sec_quest_2="Details of the scope and coverage " 
                sec_quest_3="Human rights due-diligence conducted"
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

# print(business_process("C:/Users/coda/Documents/deigeo.pdf","Details of a business process being modified / introduced as a result of addressing human rights grievances/complaints"))
# print("************")




def scope_coverage(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Details of the scope and coverage"
        question_3="Human rights due-diligence conducted"
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
                sec_quest="Is the premise/office of the entity accessible to differently abled visitors, as per the requirements of the Rights of Persons with Disabilities Act, 2016?"
                sec_quest_2="Is the premise/office of the entity accessible to differently" 
                sec_quest_3="Rights of Persons with Disabilities Act, 2016"
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

# print(scope_coverage("C:/Users/coda/Documents/deigeo.pdf","Details of the scope and coverage of any Human rights due-diligence conducted"))
# print("************")




def Rights_Persons(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Is the premise/office of the entity accessible"
        question_3=" Rights of Persons with Disabilities Act, 2016?"
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
                sec_quest="Details on assessment of value chain partners"
                sec_quest_2="Details on assessment of value chain partners" 
                sec_quest_3="Details on assessment of"
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

# print(Rights_Persons("C:/Users/coda/Documents/deigeo.pdf","Is the premise/office of the entity accessible to differently abled visitors, as per the requirements of the Rights of Persons with Disabilities Act, 2016?"))
# print("************")



def value_chain_partners(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Details on assessment of value chain partners:"
        question_3="Details on assessment of value"
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
                sec_quest="Provide details of any corrective actions taken or underway to address significant risks / concerns arising from the assessments at Question 4 above"
                sec_quest_2="Provide details of any corrective actions taken or underway to address" 
                sec_quest_3="arising from the assessments at Question 4 above"
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

# print(value_chain_partners("C:/Users/coda/Documents/deigeo.pdf","Details on assessment of value chain partners:"))
# print("************")


def Question_4_above(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Provide details of any corrective actions taken"
        question_3="arising from the assessments at Question 4 above"
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
                sec_quest="Principle 6"
                sec_quest_2="Businesses should respect and make efforts to protect and restore the environment" 
                sec_quest_3="Businesses should respect and make"
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

# print(Question_4_above("C:/Users/coda/Documents/deigeo.pdf","Provide details of any corrective actions taken or underway to address significant risks / concerns arising from the assessments at Question 4 above"))
# print("************")


                                ###### PRINCIPLE VI #######
                                


def  total_energy_consumption(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2=" Details of total energy consumption"
        question_3="energy intensity, in the following format"
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
                sec_quest="Does the entity have any sites / facilities identified as designated consumers (DCs) under the Performance"
                sec_quest_2="Does the entity have any sites / facilities identified as " 
                sec_quest_3="designated consumers (DCs) under the Performance"
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

print(total_energy_consumption("C:/Users/coda/Documents/deigeo.pdf","Details of total energy consumption"))
print("************")




def PAT_scheme(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Does the entity have any sites / facilities"
        question_3="Achieve and Trade (PAT) Scheme of the Government of India"
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
                sec_quest=" Provide details of the following disclosures related to water, in the following format"
                sec_quest_2="Provide details of the following disclosures" 
                sec_quest_3="related to water, in the following format"
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

print(PAT_scheme("C:/Users/coda/Documents/deigeo.pdf","Does the entity have any sites / facilities identified as designated consumers (DCs) under the Performance"))
print("************")





def  disclosures_related_water(pdf_path,question):
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

print(disclosures_related_water("C:/Users/coda/Documents/deigeo.pdf",""))
print("************")





def related_water(pdf_path,question):
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

print(related_water("C:/Users/coda/Documents/deigeo.pdf",""))
print("************")






def Zero_Liquid_Discharge(pdf_path,question):
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

print(Zero_Liquid_Discharge("C:/Users/coda/Documents/deigeo.pdf",""))
print("************")






def air_emissions(pdf_path,question):
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

print(air_emissions("C:/Users/coda/Documents/deigeo.pdf",""))
print("************")






def  greenhouse_gas(pdf_path,question):
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

print(greenhouse_gas("C:/Users/coda/Documents/deigeo.pdf",""))
print("************")






def project_related(pdf_path,question):
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

print(project_related("C:/Users/coda/Documents/deigeo.pdf",""))
print("************")





def waste_management(pdf_path,question):
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

print(waste_management("C:/Users/coda/Documents/deigeo.pdf",""))
print("************")





def  waste_management_practices(pdf_path,question):
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

print(waste_management_practices("C:/Users/coda/Documents/deigeo.pdf",""))
print("************")





def entity_has_operations(pdf_path,question):
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

print(entity_has_operations("C:/Users/coda/Documents/deigeo.pdf",""))
print("************")




def assessments_projects(pdf_path,question):
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

print(assessments_projects("C:/Users/coda/Documents/deigeo.pdf",""))
print("************")




def applicable_environmental_law(pdf_path,question):
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

print(applicable_environmental_law("C:/Users/coda/Documents/deigeo.pdf",""))
print("************")



def Water_withdrawal(pdf_path,question):
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

print(Water_withdrawal("C:/Users/coda/Documents/deigeo.pdf",""))
print("************")



def total_Scope(pdf_path,question):
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

print(total_Scope("C:/Users/coda/Documents/deigeo.pdf",""))
print("************")





def independent_assessment(pdf_path,question):
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

print(independent_assessment("C:/Users/coda/Documents/deigeo.pdf",""))
print("************")




def ecologically_sensitive(pdf_path,question):
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

print(ecologically_sensitive("C:/Users/coda/Documents/deigeo.pdf",""))
print("************")





def undertaken_any_specific(pdf_path,question):
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

print(undertaken_any_specific("C:/Users/coda/Documents/deigeo.pdf",""))
print("************")





def business_continuity(pdf_path,question):
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

print(business_continuity("C:/Users/coda/Documents/deigeo.pdf",""))
print("************")





def significant_adverse(pdf_path,question):
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

print(significant_adverse("C:/Users/coda/Documents/deigeo.pdf",""))
print("************")



def  value_chain_partners(pdf_path,question):
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

print(value_chain_partners("C:/Users/coda/Documents/deigeo.pdf",""))
print("************")




def Green_Credits(pdf_path,question):
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

print(Green_Credits("C:/Users/coda/Documents/deigeo.pdf",""))
print("************")





def  listed_entity(pdf_path,question):
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

print(listed_entity("C:/Users/coda/Documents/deigeo.pdf",""))
print("************")





def  top_ten(pdf_path,question):
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

print(top_ten("C:/Users/coda/Documents/deigeo.pdf",""))
print("************")
