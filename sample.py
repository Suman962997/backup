import pdfplumber
import pytesseract
import re


def q(pdf_path,question):
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
print(q("C:/Users/coda/Documents/bajaj.pdf","q"))
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


def c(pdf_path,question):
    found = False
    
    with pdfplumber.open(pdf_path) as pdf:
        # print("file opend")
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
print(c("C:/Users/coda/Documents/deigeo.pdf",""))
print("**************")


