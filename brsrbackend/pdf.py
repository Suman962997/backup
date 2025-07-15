from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
import json,random

def random_number():
    list1 = [32 ,20, 38, 47, 59, 96]
    ram_num=random.choice(list1)
    return ram_num

def get_entity_name(data: dict) -> str:
    # print("Received data $$$$$", data)
    filename = None

    sections = data.get("sections", [])
    for section in sections:
        categories = section.get("Categories", [])
        for category in categories:
            questions = category.get("questions", [])
            for q in questions:
                if q.get("question", "").strip().lower() == "name of the listed entity":
                    filename = q.get("questionAnswer", "new_brsr")
                    break
            if filename:
                break
        if filename:
            break

    if filename is None:
        filename = "new_brsr"
    elif not filename:
        filename="new_brsr"

    return filename


def create_pdf(json_data: list, pdf_name: str):
    print("json data$$$$",json_data)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Question', fontSize=11, spaceAfter=6, leading=14))
    styles.add(ParagraphStyle(name='Answer', fontSize=11, textColor=colors.darkblue, leftIndent=10, leading=14))
    styles.add(ParagraphStyle(name='TableCell', fontSize=9, leading=12))

    output_path = f"{pdf_name}.pdf"
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=60,
        bottomMargin=40
    )

    elements = []

    # Title Page
    elements.append(Paragraph("Aeiforo", styles['Heading2']))
    elements.append(Paragraph("BUSINESS RESPONSIBILITY & SUSTAINABILITY REPORT", styles['Title']))
    elements.append(Spacer(1, 20))

    # Process in original order
    ordered_data = json_data
    current_section = current_title = current_subtitle = None

    for item in ordered_data:
        section = item.get("section", "").strip()
        title = item.get("title", "").strip()
        subtitle = item.get("subtitle", "").strip()
        question_no = item.get("question_no", "").strip()
        question_text = item.get("question", "").strip()
        answer = item.get("answer", "")

        # Add section heading if changed
        if section != current_section:
            current_section = section
            elements.append(Spacer(1, 16))
            elements.append(Paragraph(f"{section}", styles['Heading2']))

        # Add title heading if changed
        if title != current_title:
            current_title = title
            elements.append(Spacer(1, 12))
            elements.append(Paragraph(f"{title}", styles['Heading3']))

        # Add subtitle heading if changed
        if subtitle != current_subtitle:
            current_subtitle = subtitle
            elements.append(Spacer(1, 8))
            elements.append(Paragraph(f"{subtitle}", styles['Heading4']))

        # Question + Answer
        elements.append(Paragraph(f"<b>{question_no}. {question_text}</b>", styles['Question']))

        try:
            parsed_answer = json.loads(answer) if isinstance(answer, str) and answer.strip().startswith("[") else answer
        except Exception:
            parsed_answer = answer

        if isinstance(parsed_answer, list) and all(isinstance(row, dict) for row in parsed_answer):
            # Render table
            headers = list(parsed_answer[0].keys())
            table_data = [[Paragraph(h, styles['TableCell']) for h in headers]]
            for row in parsed_answer:
                table_data.append([Paragraph(str(row.get(col, "")), styles['TableCell']) for col in headers])

            col_width = 480 / len(headers)
            t = Table(table_data, colWidths=[col_width]*len(headers), repeatRows=1)
            t.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#69A0E4")),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('FONTSIZE', (0, 0), (-1, -1), 9),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
                ('TOPPADDING', (0, 0), (-1, -1), 4),
            ]))
            elements.append(t)
        elif isinstance(parsed_answer, list):
            for line in parsed_answer:
                elements.append(Paragraph(str(line), styles['Answer']))
        elif isinstance(parsed_answer, str):
            elements.append(Paragraph(parsed_answer.strip() or "N/A", styles['Answer']))
        else:
            elements.append(Paragraph(str(parsed_answer), styles['Answer']))

        elements.append(Spacer(1, 8))

    doc.build(elements)
    print(f"✅ PDF created successfully at: {output_path}")
    # c=canvas.Canvas(filename=pdf_name)
    # c.save()

