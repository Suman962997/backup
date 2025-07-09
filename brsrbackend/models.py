from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text

Base = declarative_base()

def create_pdf_model(table_name: str):
    class_attrs = {
        "__tablename__": table_name,
        "id": Column(Integer, primary_key=True, index=True),
        "section": Column(String(50)),
        "title": Column(String(255)),
        "categoryNo": Column(String(50)),
        "subtitle": Column(String(255)),
        "question_no": Column(String(50)),
        "question": Column(Text),
        "answer": Column(Text),
        "__table_args__": {'extend_existing': True},  # Optional: avoids errors if already declared
    }

    return type("PDFTable", (Base,), class_attrs)
