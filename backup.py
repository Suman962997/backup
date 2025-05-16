import pdfplumber
import pytesseract
from PIL import Image
import io
import re


                            #  PRINCIPLE I 

def Percentage_coverage_training(pdf_path,question):
    found = False

    with pdfplumber.open(pdf_path) as pdf:
       print("file opend")
       question_2="Percentage coverage by training and awareness programmes"
       question_3="Percentage coverage by training"
       for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Details of fines / penalties /punishment/ award"
                sec_quest_2="Details of fines / penalties /punishment" 
                sec_quest_3="Details of fines / penalties"
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

                print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
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

print(Percentage_coverage_training("C:/Users/coda/Documents/deigeo.pdf","Percentage coverage by training and awareness programmes on any of the"))
print("************")



def  Monetary(pdf_path,question):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Details of fines/penalties/punishment/award/compounding"
        question_3="Details of fines/penalties"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Non-Monetary"
                sec_quest_2="Of the instances disclosed in Question" 
                sec_quest_3="Of the instances"
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

                print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist-list[:i]
                    else:
                        finallist=list
                print("finallist",finallist)
                
    
                return [
                    {
                        "Category": "Penalty/Fine",
                        "NGRBC Principle":"",
                        "Name of the regulatory/enforcement agencies/judicial institutions": "",
                        "Amount (In ₹)":"",
                        "Brief of the Case": "Non-compliance with disclosure norms.",
                        "Has an appeal been preferred? (Yes/No)": ""
                    },
                    {
                        "Category": "Settlement",
                        "NGRBC Principle": "",
                        "Name of the regulatory/enforcement agencies/judicial institutions": "",
                        "Amount (In ₹)":"",
                        "Brief of the Case": "",
                        "Has an appeal been preferred? (Yes/No)":""
                    },
                    {
                        "Category": "Compounding Fee",
                        "NGRBC Principle": "",
                        "Name of the regulatory/enforcement agencies/judicial institutions": "",
                        "Amount (In ₹)":"",
                        "Brief of the Case": "",
                        "Has an appeal been preferred? (Yes/No)": "",
                    }
                    ]
        
            
    if not found:
        return None

print(Monetary("C:/Users/coda/Documents/deigeo.pdf","Details of fines/penalties/punishment/award"))
print("************")





def Penalty_Fines(pdf_path,question):
    found = False
    with pdfplumber.open(pdf_path) as pdf:
       print("file opend")
        question_2="Penalty/Fines"
        question_3="Penalty"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            print(text)
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
               print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Settlement"
                sec_quest_2="Settlement" 
                sec_quest_3="Compounding fee"
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
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:1+i]
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

print(Penalty_Fines("C:/Users/coda/Documents/deigeo.pdf","Penalty/Fines"))
print("************")

def Settlement(pdf_path,question):

    found = False
    with pdfplumber.open(pdf_path) as pdf:
       print("file opend")
        question_2="Penalty/Fines"
        question_3="Penalty"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            print(text)
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
               print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Settlement"
                sec_quest_2="Settlement" 
                sec_quest_3="Compounding fee"
                list=[]     
                for i, line in enumerate(lines):
                    print(i,line)
                    if question.lower() in line.lower():
                        print("***q1")
                        list=lines[i+1:]
                        break
                    elif question_2.lower() in line.lower():
                        print("***q2")
                        list=lines[i+1:]
                        break
                    elif question_3.lower() in line.lower():
                        list=lines[i+1:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                   print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                     print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:1+i]
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

print(Settlement("C:/Users/coda/Documents/deigeo.pdf","Penalty/Fines"))
print("************")



def Compounding_Fee(pdf_path,question):

    found = False
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Penalty/Fines"
         question_3=""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
             print(text)
            if text and question in text or question_2 in text: or question_3 in text:
                found = True
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Non-Monetary"
                sec_quest_2="Non-Monetary" 
                sec_quest_3="Non-Monetary"
                list=[]     
                for i, line in enumerate(lines):
                     print(i,line)
                    if question.lower() in line.lower():
                        print("***q1",i)
                        list=lines[i+2:]
                        break
                    elif question_2.lower() in line.lower():
                        print("***q2",i)
                        list=lines[i+2:]
                        break
                     elif question_3.lower() in line.lower():
                         print("**q3",i,line)
                         list=lines[i-1:]
                         break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:1+i]
                        break
                    else:
                        finallist=list
                print("finallist",finallist)
    if not found:
        return None

print(Compounding_Fee("C:/Users/coda/Documents/deigeo.pdf","Details of fines/penalties/punishment/award"))
print("************")


def  Non_Monetary(pdf_path,question):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2=""
        question_3=""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                found = True
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                 print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=""
                sec_quest_2="" 
                sec_quest_3=""
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

                print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist-list[:i]
                    else:
                        finallist=list
                print("finallist",finallist)
                
    
                return [
                    {
                        "Category": "Penalty/Fine",
                        "NGRBC Principle":"",
                        "Name of the regulatory/enforcement agencies/judicial institutions": "",
                        "Amount (In ₹)":"",
                        "Brief of the Case": "Non-compliance with disclosure norms.",
                        "Has an appeal been preferred? (Yes/No)": ""
                    },
                    {
                        "Category": "Settlement",
                        "NGRBC Principle": "",
                        "Name of the regulatory/enforcement agencies/judicial institutions": "",
                        "Amount (In ₹)":"",
                        "Brief of the Case": "",
                        "Has an appeal been preferred? (Yes/No)":""
                    },
                    {
                        "Category": "Compounding Fee",
                        "NGRBC Principle": "",
                        "Name of the regulatory/enforcement agencies/judicial institutions": "",
                        "Amount (In ₹)":"",
                        "Brief of the Case": "",
                        "Has an appeal been preferred? (Yes/No)": "",
                    }
                    ]
        
            
    if not found:
        return None

print(Non_Monetary("C:/Users/coda/Documents/deigeo.pdf","Details of fines/penalties/punishment/award"))
print("************")


def Of_the_instances_disclosed(pdf_path,question):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Of the instances disclosed in Question 2"
        question_3="Of the instances disclosed"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
             print(text)
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Does the entity have an anti-corruption or anti-bribery policy? If yes,"
                sec_quest_2="Does the entity have an anti-corruption or" 
                sec_quest_3="Does the entity have an"
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
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else:
                        finallist=list
                print("finallist",finallist)
                            
print(Of_the_instances_disclosed("C:/Users/coda/Documents/deigeo.pdf","Of the instances disclosed in Question 2 above, details of the Appeal/ Revision "))
print("************")



def anti_corruption_or_anti_bribery_policy(pdf_path,question):
    
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Does the entity have an anti-corruption or anti-bribery"
        question_3="Does the entity have an"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=" Number of Directors/KMPs/employees/workers against "
                sec_quest_2="Number of Directors/KMPs" 
                sec_quest_3="/KMPs/employees/workers"
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
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                    
                 print("finallist",finallist)
                return finallist             

print(anti_corruption_or_anti_bribery_policy("C:/Users/coda/Documents/deigeo.pdf","Does the entity have an anti-corruption or anti-bribery policy? If yes, provide "))
print("************")


def Directors_KMPs_employees_workers (pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Number of Directors/KMPs/employees/workers against "
        question_3="/KMPs/employees/workers"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Details of complaints with regard to conflict of interest"
                sec_quest_2="conflict of interest" 
                sec_quest_3="Details of complaints with "
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
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list

                 print("finallist",finallist)
                return finallist                       

print(Directors_KMPs_employees_workers("C:/Users/coda/Documents/deigeo.pdf","Number of Directors/KMPs/employees/workers against whom disciplinary action was taken by any law enforcement"))
print("************")

def  Details_of_complaints_with(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Details of complaints with regard to conflict of interest"
        question_3="conflict of interest"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=" Provide details of any corrective action taken or underway on issues related to fines"
                sec_quest_2=" Provide details of any corrective action taken or" 
                sec_quest_3=" Provide details of any corrective"
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
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(Details_of_complaints_with("C:/Users/coda/Documents/deigeo.pdf","Details of complaints with regard to conflict of interest"))
print("************")

def taken_or_underway_on_issues(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Provide details of any corrective action taken or underway on issues related to fines / penalties / action taken"
        question_3="fines / penalties / action taken"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=" Number of days of accounts payables ((Accounts payable *365) / Cost of goods/services"
                sec_quest_2="Number of days of accounts payables ((Accounts payable *365)" 
                sec_quest_3="Cost of goods/services"
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
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(taken_or_underway_on_issues("C:/Users/coda/Documents/deigeo.pdf","Provide details of any corrective action taken or underway on issues related to fines / penalties / action taken by regulators/"))
print("************")



def  Number_of_days_of_accounts_payables(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2=" Number of days of accounts payables"
        question_3="Accounts payable *365"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Open-ness of business"
                sec_quest_2="Openness of business" 
                sec_quest_3="Open ness of business"
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
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(Number_of_days_of_accounts_payables("C:/Users/coda/Documents/deigeo.pdf"," Number of days of accounts payables ((Accounts payable *365) / Cost of goods/services"))
print("************")


def concentration_of_purchases(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Provide details of concentration of purchases and sales"
        question_3="Provide details of concentration"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Awareness programmes conducted for value chain partners on any of the Principles during the financial year:"
                sec_quest_2="Awareness programmes conducted for value chain " 
                sec_quest_3="Awareness programmes conducted"
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
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(concentration_of_purchases("C:/Users/coda/Documents/deigeo.pdf","Provide details of concentration of purchases"))
print("************")


def Awareness_programmes_conducted(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Awareness programmes conducted for value chain"
        question_3="Awareness programmes conducted"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Does the entity have processes in place to avoid/ manage conflict"
                sec_quest_2="Does the entity have processes in place " 
                sec_quest_3="Does the entity have"
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
                print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                print("finallist",finallist)
                return finallist                       

print(Awareness_programmes_conducted("C:/Users/coda/Documents/deigeo.pdf","Awareness programmes conducted for value chain partners on any of the Principles"))
print("************")


def place_to_avoid_manage_conflict(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Does the entity have processes in place to"
        question_3="avoid/ manage conflict"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Businesses should provide"
                sec_quest_2="Businesses should provide goods and services" 
                sec_quest_3="PRINCIPLE 2"
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
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(place_to_avoid_manage_conflict("C:/Users/coda/Documents/deigeo.pdf"," Does the entity have processes in place to avoid/ manage conflict of interests involving members of the Board"))
print("************")



                                #  PRINICIPLE II 


def Percentage_of_R_and_D(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Percentage of R&D and capital expenditure (capex) investments in specific"
        question_3="Percentage of R&D and capital expenditure"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                #  #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Does the entity have procedures in place for sustainable sourcing? (Yes/No)"
                sec_quest_2="Does the entity have procedures"
                sec_quest_3="for sustainable sourcing? (Yes/No)"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(Percentage_of_R_and_D("C:/Users/coda/Documents/deigeo.pdf","Percentage of R&D and capital expenditure (capex) investments in specific technologies to improve the environmental and social"))
print("************")




def place_for_sustainable_sourcing(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Does the entity have procedures in place for sustainable sourcing"
        question_3="for sustainable sourcing?"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="If yes, what percentage of inputs were sourced sustainably?"
                sec_quest_2="If yes, what percentage of inputs " 
                sec_quest_3="If yes, what percentage"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(place_for_sustainable_sourcing("C:/Users/coda/Documents/deigeo.pdf","Does the entity have procedures in place for sustainable sourcing? (Yes/No)"))
print("************")


def procedures_in_place(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Does the entity have procedures in place for"
        question_3="place for sustainable sourcing"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="If yes, what percentage of inputs were sourced"
                sec_quest_2="If yes, what percentage of inputs" 
                sec_quest_3="Describe the processes in place to safely reclaim your products for reusing"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(procedures_in_place("C:/Users/coda/Documents/deigeo.pdf","Does the entity have procedures in place for sustainable sourcing? (Yes/No)"))
print("************")


def place_to_safely_reclaim_your_products(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Describe the processes in place to safely reclaim your products for reusing, recycling "
        question_3="Describe the processes in place to safely"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest=" Whether Extended Producer Responsibility (EPR) is applicable to the entity’s activities (Yes / No). If yes, whether the waste collection"
                sec_quest_2=" Whether Extended Producer Responsibility (EPR) is applicable to the entity’s activities (Yes / No)" 
                sec_quest_3=" Whether Extended Producer Responsibility (EPR)"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist              
                     
print(place_to_safely_reclaim_your_products("C:/Users/coda/Documents/deigeo.pdf","Describe the processes in place to safely reclaim your products for reusing"))
print("************")

def Whether_Extended_Producer_Responsibility_EPR(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Whether Extended Producer Responsibility (EPR) is applicable to the entity’s activities "
        question_3="Whether Extended Producer Responsibility (EPR)"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Has the entity conducted Life Cycle Perspective / Assessments (LCA) for any of its products (for manufacturing"
                sec_quest_2="Has the entity conducted Life Cycle Perspective / Assessments" 
                sec_quest_3="Has the entity conducted Life Cycle"
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
                        print("****q3")
                        list=lines[i:]
                        break
                print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                    print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                        print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(Whether_Extended_Producer_Responsibility_EPR("C:/Users/coda/Documents/deigeo.pdf","Whether Extended Producer Responsibility (EPR) is applicable to the entity’s activities (Yes / No). If yes, whether the waste collection plan is in line with the "))
print("************")


def Life_Cycle_Perspective(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Has the entity conducted Life Cycle Perspective / Assessments (LCA) for any of its products "
        question_3="Has the entity conducted Life Cycle"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="If there are any significant social or environmental concerns and/or risks arising from production or disposal of "
                sec_quest_2="If there are any significant social or environmental concerns and/or " 
                sec_quest_3="If there are any significant social or"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(Life_Cycle_Perspective("C:/Users/coda/Documents/deigeo.pdf","Has the entity conducted Life Cycle Perspective / Assessments (LCA) for any of its products (for manufacturing industry) or for its services"))
print("************")

def significant_social_or_environmental(pdf_path,question):

    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="If there are any significant social or environmental concerns and/or risks arising "
        question_3="If there are any significant social or environmental concerns"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Percentage of recycled or reused input material to total material (by value) used in production (for"
                sec_quest_2="Percentage of recycled or reused input material to " 
                sec_quest_3="Percentage of recycled or reused"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(significant_social_or_environmental("C:/Users/coda/Documents/deigeo.pdf","If there are any significant social or environmental concerns and/or risks arising fro+D28m production or disposal of your products / services, as"))
print("************")

def Percentage_of_recycled(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Percentage of recycled or reused input material to total material (by value) used in production"
        question_3="Percentage of recycled or reused "
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Of the products and packaging reclaimed at end of life of products, amount (in metric tonnes) reused,"
                sec_quest_2="Of the products and packaging reclaimed at end of" 
                sec_quest_3="Of the products and packaging"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(Percentage_of_recycled("C:/Users/coda/Documents/deigeo.pdf","Percentage of recycled or reused input material to total material (by value) used in production (for manufacturing industry) or providing services (for service industry)"))
print("************")


def Of_the_products_and_packaging(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Of the products and packaging reclaimed at end of life of products, amount (in metric tons)"
        question_3="Of the products and packaging reclaimed at end"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Reclaimed products and their packaging materials (as percentage of products sold) "
                sec_quest_2="Reclaimed products and their packaging materials" 
                sec_quest_3="Reclaimed products and"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(Of_the_products_and_packaging("C:/Users/coda/Documents/deigeo.pdf","Of the products and packaging reclaimed at end of life of products, amount (in metric tons) reused, recycled, and safely disposed"))
print("************")


def Reclaimed_products(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Reclaimed products and their packaging materials (as percentage of products sold)"
        question_3="Reclaimed products and their"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Principle 3"
                sec_quest_2="Businesses should respect and promote the well-being of all employees, including those in their value chain" 
                sec_quest_3="Businesses should respect and promote"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(Reclaimed_products("C:/Users/coda/Documents/deigeo.pdf","Reclaimed products and their packaging materials (as percentage of products sold)"))
print("************")


                             PRINCIPLE III 
                         
                         
def well_being_of_employees(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Details of measures for the well-being of employees"
        question_3="Details of measures for the well-being of employees"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Details of measures for the well-being of Workers"
                sec_quest_2="well-being of Workers" 
                sec_quest_3="Spending on measures towards well-being"
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
                        print("****q3")
                        list=lines[i:]
                        break
                print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(well_being_of_employees("C:/Users/coda/Documents/deigeo.pdf","Details of measures for the well-being of employees"))
print("************")
   
   
def well_being_of_Workers(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Details of measures for the well-being of Workers"
        question_3="well-being of Workers"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="on measures towards well-being of employees and workers (including permanent and other than permanent) in the"
                sec_quest_2="on measures towards well-being of employees and workers" 
                sec_quest_3="(including permanent and other than permanent)"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(well_being_of_Workers("C:/Users/coda/Documents/deigeo.pdf","Details of measures for the well-being of Workers"))
print("************")


def towards_well_being_of_employees(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Spending on measures towards well-being of employees and workers (including"
        question_3="(including permanent and other than permanent)"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Details of retirement benefits, for Current Financial Year and Previous Financial Year"
                sec_quest_2="Details of retirement benefits, for Current" 
                sec_quest_3="Financial Year and Previous Financial Year"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(towards_well_being_of_employees("C:/Users/coda/Documents/deigeo.pdf","Spending on measures towards well-being of employees and workers (including permanent and other than permanent) in the"))
print("************")


def Details_of_retirement_benefits(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Details of retirement benefits, for Current Financial Year and Previous Financial Year"
        question_3="Year and Previous Financial Year"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Are the premises / offices of the entity accessible to differently abled employees and workers, as per the requirements of the Rights"
                sec_quest_2="Are the premises / offices of the entity accessible to differently abled employees and workers" 
                sec_quest_3="Are the premises / offices of the entity accessible to differently"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(Details_of_retirement_benefits("C:/Users/coda/Documents/deigeo.pdf","Details of retirement benefits, for Current Financial Year and Previous Financial Year"))
print("************")

def Accessibility(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Accessibility of workplaces"
        question_3="Accessibility of workplaces"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Does the entity have an equal opportunity policy as per the Rights of Persons with Disabilities"
                sec_quest_2="Does the entity have an equal opportunity" 
                sec_quest_3=" Rights of Persons with Disabilities Act, 2016?"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(Accessibility("C:/Users/coda/Documents/deigeo.pdf","Accessibility of workplaces"))
print("************")


def Return_to_work(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Return to work and Retention rates of permanent employees and workers that took parental leave"
        question_3="Return to work and Retention rates of permanent"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Is there a mechanism available to receive and redress grievances for the following categories of employees "
                sec_quest_2="Is there a mechanism available to receive" 
                sec_quest_3="for the following categories of employees "
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(Return_to_work("C:/Users/coda/Documents/deigeo.pdf","Return to work and Retention rates of permanent employees and workers that took parental leave"))
print("************")



def Is_there_mechanism(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Is there a mechanism available to receive and redress"
        question_3="categories of employees and worker"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Membership of employees and worker in association(s) or Unions recognised by the listed entity"
                sec_quest_2="Membership of employees and worker in association" 
                sec_quest_3="Unions recognised by the listed entity"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(Is_there_mechanism("C:/Users/coda/Documents/deigeo.pdf","Is there a mechanism available to receive and redress grievances for the following categories of employees and worker"))
print("************")


def Membership_of_employees(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2=" Membership of employees and worker in association(s) or Unions recognised by the listed entity"
        question_3=" Membership of employees and worker "
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Details of training given to employees and workers"
                sec_quest_2="Details of training given to " 
                sec_quest_3="to employees and workers"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("fin
                 
                 allist",finallist)
                return finallist                       

print(Membership_of_employees("C:/Users/coda/Documents/deigeo.pdf"," Membership of employees and worker in association(s) or Unions recognised by the listed entity"))
print("************")



def Details_of_training(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Details of training given to employees and workers:"
        question_3="Details of training given to employees and workers"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Details of performance and career development reviews of employees and workers:"
                sec_quest_2="Details of performance and career development" 
                sec_quest_3=" reviews of employees and workers"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(Details_of_training("C:/Users/coda/Documents/deigeo.pdf","Details of training given to employees and workers"))
print("************")




def Details_of_performance(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Details of performance and career development reviews of employees and workers:"
        question_3="Details of performance and career development"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Health and safety management system:"
                sec_quest_2="safety management system:" 
                sec_quest_3="Health and safety"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(Details_of_performance("C:/Users/coda/Documents/deigeo.pdf","Details of performance and career development reviews of employees and workers:"))
print("************")



def Health_safety_management(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Health and safety management system:"
        question_3="Health and safety management system"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Whether an occupational health and safety management system has been implemented by the entity"
                sec_quest_2="Whether an occupational health and safety" 
                sec_quest_3="system has been implemented by the entity"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(Health_safety_management("C:/Users/coda/Documents/deigeo.pdf","Health and safety management system:"))
print("************")



def processes_used_to_identify(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="What are the processes used to identify"
        question_3="risks on a routine and non-routine basis by the entity"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Whether you have processes for workers to report the work related hazards and to remove themselves from such risks"
                sec_quest_2="Whether you have processes for workers to report" 
                sec_quest_3=" the work related hazards and to remove themselves from such risks. (Y/N)"
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
                        print("****q3")
                        list=lines[i:]
                        break
                print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(processes_used_to_identify("C:/Users/coda/Documents/deigeo.pdf","What are the processes used to identify work-related hazards and assess risks on a routine and non-routine basis by the entity"))
print("************")



def  workers_report_work(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Whether you have processes for workers to report the work"
        question_3=" related hazards and to remove themselves from such risks"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Do the employees/ worker of the entity have access to non-occupational medical and healthcare services? (Yes/ No)"
                sec_quest_2="Do the employees/ worker of the entity have" 
                sec_quest_3=" non-occupational medical and healthcare services"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(workers_report_work("C:/Users/coda/Documents/deigeo.pdf","Whether you have processes for workers to report the work related hazards and to remove themselves from such risks"))
print("************")


def  non_occupational_medical_and_healthcare(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Do the employees/ worker of the entity have access to non-occupational medical and healthcare services"
        question_3="non-occupational medical and healthcare services"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Details of safety related incidents, in the following format"
                sec_quest_2="Details of safety related incidents" 
                sec_quest_3="incidents, in the following format"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(non_occupational_medical_and_healthcare("C:/Users/coda/Documents/deigeo.pdf","Do the employees/ worker of the entity have access to non-occupational"))
print("************")

def Details_safety_related(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Details of safety related incidents, in the following format:"
        question_3="Details of safety related incidents"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Describe the measures taken by the entity to ensure a safe and healthy work place"
                sec_quest_2="Describe the measures taken by " 
                sec_quest_3="a safe and healthy work place"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(Details_safety_related("C:/Users/coda/Documents/deigeo.pdf","Details of safety related incidents, in the following format"))
print("************")


def safe_and_healthy_work_place(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Describe the measures taken by the entity to ensure a safe and healthy workplace"
        question_3="safe and healthy work place"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Number of Complaints on the following made by employees and workers:"
                sec_quest_2="Number of Complaints on the " 
                sec_quest_3=" made by employees and workers:"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(safe_and_healthy_work_place("C:/Users/coda/Documents/deigeo.pdf","Describe the measures taken by the entity to ensure a safe and healthy work place"))
print("************")


def Number_of_Complaints(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Number of Complaints on the following"
        question_3="made by employees and workers:"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Assessments for the year"
                sec_quest_2="Assessments for the year" 
                sec_quest_3="Assessments for the year"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(Number_of_Complaints("C:/Users/coda/Documents/deigeo.pdf","Number of Complaints on the following made by employees and workers"))
print("************")

def Assessments_for_the_year(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Assessments for the year"
        question_3="Assessments for the year:"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Provide details of any corrective action taken or underway to address safety-related incidents (if any) and on significant risks / concerns arising from assessments of health & safety practices"
                sec_quest_2="Provide details of any corrective action taken or underway to address safety-related incidents (if any) and on significant" 
                sec_quest_3=" risks / concerns arising from assessments of health & safety practices"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(Assessments_for_the_year("C:/Users/coda/Documents/deigeo.pdf","Assessments for the year:"))
print("************")


def safety_practices_and_working_conditions(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Provide details of any corrective action taken or underway to address safety-related incidents (if any) and on significant risks / concerns"
        question_3=" arising from assessments of health & safety practices and working conditions"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Does the entity extend any life insurance or any compensatory Package in the event of death"
                sec_quest_2="Package in the event of death" 
                sec_quest_3="Does the entity extend any life insurance"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(safety_practices_and_working_conditions("C:/Users/coda/Documents/deigeo.pdf","Provide details of any corrective action taken or underway to address safety-related incidents (if any) and on significant risks / concerns arising from assessments of health & safety practices and working conditions."))
print("************")


def  compensatory_package(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Does the entity extend any life insurance or any compensatory package in the event"
        question_3="event of death of (A) Employees (Y / N); (B) Workers (Y / N)"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Provide the measures undertaken by the entity to ensure that statutory dues have been deducted and deposited by the value chain partners"
                sec_quest_2="Provide the measures undertaken by the entity to ensure" 
                sec_quest_3="have been deducted and deposited by the value chain partners"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print( compensatory_package("C:/Users/coda/Documents/deigeo.pdf","Does the entity extend any life insurance or any compensatory package in the event of death of (A) Employees"))
print("************")



def Provide_measures_undertaken(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Provide the number of employees / workers having suffered "
        question_3="Provide the number of employees / workers"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Provide the number of employees / workers having suffered high consequence work- related injury / ill-health /"
                sec_quest_2="Provide the number of employees / workers having suffered" 
                sec_quest_3="members have been placed in suitable employment"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(Provide_measures_undertaken("C:/Users/coda/Documents/deigeo.pdf","Provide the number of employees / workers having suffered high consequence work- related injury / ill-health"))
print("************")

def transition_assistance_programs(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Does the entity provide transition assistance programs to facilitate continued employability and the management of career endings resulting"
        question_3="retirement or termination of employment? (Yes/ No)"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Details on assessment of value chain partners:"
                sec_quest_2="Details on assessment of value chain partners" 
                sec_quest_3="Details on assessment"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(transition_assistance_programs("C:/Users/coda/Documents/deigeo.pdf","Does the entity provide transition assistance programs to facilitate continued employability and the management of career endings resulting from retirement or termination of employment"))
print("************")


def Details_on_assessment(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Details on assessment of value chain partners"
        question_3="Details on assessment of value chain"
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Provide details of any corrective actions taken or underway to address significant risks / concerns arising from assessments of health"
                sec_quest_2="Provide details of any corrective actions taken or underway to address significant risks" 
                sec_quest_3="arising from assessments of health"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(Details_on_assessment("C:/Users/coda/Documents/deigeo.pdf","Details on assessment of value chain partners"))
print("************")


def conditions_value_chain_partners(pdf_path,question):
    with pdfplumber.open(pdf_path) as pdf:
        print("file opend")
        question_2="Provide details of any corrective actions taken or underway to address significant risks / concerns arising from assessments of health and safety practices"
        question_3="health and safety practices and working conditions of value chain partners."
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text and question in text or question_2 in text  or question_3 in text:
                print(f"Question found on page {i}")
                image = page.to_image(resolution=300).original  #

                 #
                custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'
                ocr_text = pytesseract.image_to_string(image, config=custom_config)
                  print(ocr_text)
                lines = ocr_text.splitlines()
                sec_quest="Principle 4:"
                sec_quest_2="Businesses should respect the interests of and be responsive to all its stakeholders." 
                sec_quest_3="Businesses should respect the interests"
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
                        print("****q3")
                        list=lines[i:]
                        break
                 print("405 **",list)
                finallist=[]
                
                for i,selist in enumerate(list):
                     print("*",i,selist)
                    if sec_quest.lower() in selist.lower():
                                      print("",i,selist)
                        finallist=list[:i]
                        break
                    elif sec_quest_2.lower() in selist.lower():
                        print(" sec_2")
                        finallist=list[:i]
                        break
                    elif sec_quest_3.lower() in selist.lower():
                        print("&& sec3")
                        finallist=list[:i]
                        break
                    else :
                        finallist=list
                 print("finallist",finallist)
                return finallist                       

print(conditions_value_chain_partners("C:/Users/coda/Documents/deigeo.pdf","Provide details of any corrective actions taken or underway to address significant risks / concerns"))
print("************")
