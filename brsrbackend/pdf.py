from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import json
import random

def random_number():
    list1 = [32, 20, 38, 47, 59, 96]
    return random.choice(list1)

def get_entity_name(data: dict) -> str:
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

    return filename or "new_brsr"

def create_pdf(json_data: list, pdf_name: str):
    print("Generating PDF from JSON data...")

    # Styles Setup
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

    # Process Data in Order
    current_section = current_title = current_subtitle = None

    for item in json_data:
        section = item.get("section", "").strip()
        title = item.get("title", "").strip()
        subtitle = item.get("subtitle", "").strip()
        question_no = item.get("question_no", "").strip()
        question_text = item.get("question", "").strip()
        answer = item.get("answer", "")

        # Section Heading
        if section != current_section:
            current_section = section
            elements.append(Spacer(1, 16))
            elements.append(Paragraph(section, styles['Heading2']))

        # Title Heading
        if title != current_title:
            current_title = title
            elements.append(Spacer(1, 12))
            elements.append(Paragraph(title, styles['Heading3']))

        # Subtitle Heading
        if subtitle != current_subtitle:
            current_subtitle = subtitle
            elements.append(Spacer(1, 8))
            elements.append(Paragraph(subtitle, styles['Heading4']))

        # Question
        elements.append(Paragraph(f"<b>{question_no}. {question_text}</b>", styles['Question']))

        # Parse the Answer
        parsed_answer = answer
        if isinstance(answer, str) and answer.strip().startswith("["):
            try:
                parsed_answer = json.loads(answer)
            except json.JSONDecodeError:
                pass  # Leave as string if invalid JSON

        # Render Table if list of dicts
        if isinstance(parsed_answer, list) and all(isinstance(row, dict) for row in parsed_answer):
            if len(parsed_answer) > 0:
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
            else:
                # Empty Table Case
                elements.append(Paragraph("<i>No Data Available</i>", styles['Answer']))
        elif isinstance(parsed_answer, list):
            # List of strings or invalid dict structure
            for line in parsed_answer:
                elements.append(Paragraph(str(line), styles['Answer']))
        elif isinstance(parsed_answer, str):
            elements.append(Paragraph(parsed_answer.strip() or "N/A", styles['Answer']))
        else:
            elements.append(Paragraph(str(parsed_answer), styles['Answer']))

        elements.append(Spacer(1, 8))

    # Build PDF
    doc.build(elements)
    print(f"✅ PDF created successfully: {output_path}")
    return output_path
