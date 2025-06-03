import pdfplumber
import pytesseract
from PIL import Image
import io
import re



                                #  PRINICIPLE II 


def Percentage_of_R_and_D(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")\
        print("PRINCIPLE 2")
        question="Percentage of R&D and capital expenditure (capex) investments in specific"
        question_2="Percentage of R&D and capital "
        question_3="Percentage of R&D"
        for i, page in enumerate(pdf.pages[7:16]):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                #(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                #  #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  #(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Does the entity have procedures in place for sustainable sourcing? (Yes/No)"
                sec_quest_2="Does the entity have procedures"
                sec_quest_3="for sustainable sourcing? (Yes/No)"
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
                        #("****q3")
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

#@print(Percentage_of_R_and_D("C:/Users/coda/Documents/praxis.pdf"))
#@print("************")


def  Does_the_entity_have_procedures(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question="Does the entity have procedures in place for sustainable sourcing"
        question_2="Does the entity have procedures"
        question_3="for sustainable sourcing"
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
                sec_quest="If yes, what percentage of inputs were sourced sustainably?"
                sec_quest_2="If yes, what percentage of inputs " 
                sec_quest_3="If yes, what percentage"
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
                        #("****q3")
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

#@print(Does_the_entity_have_procedures("C:/Users/coda/Documents/praxis.pdf"))
#@print("************")

def  b_If_yes_what_percentage(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question="If yes, what percentage of inputs were sourced sustainably"
        question_2="If yes, what percentage"
        question_3="were sourced sustainably"
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
                sec_quest="Describe the processes in place to safely reclaim your products"
                sec_quest_2="Describe the processes in place" 
                sec_quest_3="products for reusing"
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
                        #("****q3")
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

#@print(b_If_yes_what_percentage("C:/Users/coda/Documents/praxis.pdf"))
#@print("************")


def  Describe_the_processes_in_place(pdf_path,):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question="Does the entity have procedures in place for sustainable sourcing"
        question_2="Does the entity have procedures in place for"
        question_3="place for sustainable sourcing"
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
                sec_quest="If yes, what percentage of inputs were sourced"
                sec_quest_2="If yes, what percentage of inputs" 
                sec_quest_3="Describe the processes in place to safely reclaim your products for reusing"
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
                        #("****q3")
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

#@print(Describe_the_processes_in_place("C:/Users/coda/Documents/praxis.pdf"))
#@print("************")

def Whether_Extended_Producer_Responsibility_EPR(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question="Whether Extended Producer Responsibility (EPR) is applicable"
        question_2="Whether Extended Producer"
        question_3="Whether Extended Producer Responsibility (EPR)"
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
                sec_quest="Has the entity conducted Life Cycle Perspective / Assessments (LCA) for any of its products (for manufacturing"
                sec_quest_2="Has the entity conducted Life Cycle Perspective / Assessments" 
                sec_quest_3="Has the entity conducted Life Cycle"
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
                        #("****q3")
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

#@print(Whether_Extended_Producer_Responsibility_EPR("C:/Users/coda/Documents/praxis.pdf"))
#@print("************")


def Has_the_entity_conducted_Life(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question="Has the entity conducted Life Cycle Perspective"
        question_2="Has the entity conducted Life Cycle "
        question_3="Has the entity conducted"
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
                sec_quest="If there are any significant social or environmental "
                sec_quest_2="If there are any significant social" 
                sec_quest_3="If there are any significant social "
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
                        #("****q3")
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

#@print(Has_the_entity_conducted_Life("C:/Users/coda/Documents/praxis.pdf"))
#@print("************")

def If_there_are_any_significant_social(pdf_path):

    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question="If there are any significant social or environmental"
        question_2="If there are any significant"
        question_3="If there are any significant social or environmental concerns"
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
                sec_quest="Percentage of recycled or reused input material to total"
                sec_quest_2="Percentage of recycled or reused input" 
                sec_quest_3="Percentage of recycled or reused"
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
                        #("****q3")
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

#@print(If_there_are_any_significant_social("C:/Users/coda/Documents/praxis.pdf"))
#@print("************")


def Percentage_of_recycled(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question="Percentage of recycled or reused input material to total material (by value)"
        question_2="material to total material (by value) used in production"
        question_3="Percentage of recycled or reused "
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
                sec_quest="Of the products and packaging reclaimed at end of life of products, amount (in metric tonnes) reused,"
                sec_quest_2="Of the products and packaging reclaimed at end of" 
                sec_quest_3="Of the products and packaging"
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
                        #("****q3")
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

#@print(Percentage_of_recycled("C:/Users/coda/Documents/praxis.pdf"))
#@print("************")


def Of_the_products_and_packaging(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question="Of the products and packaging reclaimed at end of life of products"
        question_2="Of the products and packaging reclaimed"
        question_3="Of the products and "
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
                sec_quest="Reclaimed products and their packaging materials (as percentage of products sold) "
                sec_quest_2="Reclaimed products and their packaging materials" 
                sec_quest_3="Reclaimed products and"
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
                        #("****q3")
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

#@print(Of_the_products_and_packaging("C:/Users/coda/Documents/praxis.pdf"))
#@print("************")


def Reclaimed_products(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        #("file opend")
        question="Reclaimed products and their packaging materials"
        question_2="Reclaimed products and their packaging materials (as percentage of products sold)"
        question_3="Reclaimed products and their"
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
                sec_quest="Principle 3"
                sec_quest_2="Businesses should respect and promote the well-being of all employees, including those in their value chain" 
                sec_quest_3="Businesses should respect and promote"
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
                        #("****q3")
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

#@print(Reclaimed_products("C:/Users/coda/Documents/praxis.pdf"))
#@print("************")

