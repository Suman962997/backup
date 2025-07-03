from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
def get_entity_name(data):
    filename=None
    for section in data.get("sections", []):
        for part in section.get("parts", []):
            for question in part.get("questions", []):
                if question.get("question", "").strip().lower() == "name of the listed entity":
                    filename=question.get("questionAnswer","Not Applicable")
    if filename is None:
        filename="new_brsr"
            
    return filename

def create_pdf(json_data: dict, pdf_name):
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Question', fontSize=11, spaceAfter=6, leading=14))
    styles.add(ParagraphStyle(name='Answer', fontSize=11, textColor=colors.darkblue, leftIndent=10, leading=14))
    styles.add(ParagraphStyle(name='TableCell', fontSize=9, leading=12))  # For table wrapping

    output_path=pdf_name+'.pdf'
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=60,
        bottomMargin=40
    )

    elements = []

    # Title page header
    elements.append(Paragraph("Aeiforo", styles['Heading2']))
    elements.append(Paragraph("BUSINESS RESPONSIBILITY & SUSTAINABILITY REPORT", styles['Title']))
    elements.append(Spacer(1, 20))

    # Loop through each section
    for section in json_data.get("sections", []):
        section_title = f"{section['section'].upper()} - {section['title'].upper()}"
        elements.append(Paragraph(section_title, styles['Heading3']))
        elements.append(Spacer(1, 12))

        for part in section.get("parts", []):
            subtitle = part.get("subtitle", "")
            part_no = part.get("partRoman", part.get("partNo", "")).upper()

            elements.append(Paragraph(f"{part_no}. {subtitle}", styles['Heading4']))
            elements.append(Spacer(1, 6))

            for q in part.get("questions", []):
                question = Paragraph(f"<b>{q['questionNo']}. {q['question']}</b>", styles['Question'])
                answer = q.get('questionAnswer', "")

                elements.append(question)

                if isinstance(answer, list) and len(answer) > 0 and isinstance(answer[0], dict):
                    # Table format for list of dicts
                    headers = list(answer[0].keys())
                    table_data = [[Paragraph(h, styles['TableCell']) for h in headers]]

                    for item in answer:
                        row = [Paragraph(str(item.get(col, "")), styles['TableCell']) for col in headers]
                        table_data.append(row)

                    # Set column widths – smaller widths to allow wrapping
                    col_count = len(headers)
                    max_width = 480  # Total width for table
                    col_width = max_width / col_count

                    row_height = None  # Let ReportLab auto-adjust row height

                    t = Table(table_data, colWidths=[col_width]*col_count, repeatRows=1)

                    t.setStyle(TableStyle([
                        ('BACKGROUND', (0, 0), (-1, 0), colors.Color(red=105.0/255,green=160.0/255,blue=228.0/255)),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                        ('FONTSIZE', (0, 0), (-1, -1), 9),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
                        ('TOPPADDING', (0, 0), (-1, -1), 4),
                    ]))
                    elements.append(t)

                elif isinstance(answer, str):
                    elements.append(Paragraph(answer.strip() or "N/A", styles['Answer']))
                else:
                    elements.append(Paragraph(str(answer), styles['Answer']))

                elements.append(Spacer(1, 8))

    doc.build(elements)
    print(f"✅ PDF created successfully at: {output_path}")