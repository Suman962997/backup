
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
    
    keys = [
    ]

    keys_3 = [
        "S.no",
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
\
    
    def  Details_of_fines(pdf_file):
    start_found = False
    end_found = False
    lines_between = []
    custom_config = r'--oem 3 --psm 6 -c preserve_interword_spaces=1'

    # Define multiple possible start and end strings
    q_starts = [
        "Details of fines / penalties /punishment/ award/ compounding fees/ settlement amount paid in proceedings",
        "Details of fines / penalties /punishment",
        "settlement amount paid in proceedings"

    ]
    q_ends = [
        "Monetary",
        "Non-Monetary",
        "Of the instances disclosed in Question 2 above, details"
    ]
    
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages[6:16]:
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

    if lines_between:
        return str(lines_between)
    else:
        return None

print(Details_of_fines("C:/Users/coda/Documents/bse.pdf"))
print("************")

