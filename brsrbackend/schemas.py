from typing import List
from pydantic import BaseModel

# Pydantic schema for response
class PDFDataSchema(BaseModel):
    id: int
    section: str
    title: str
    categoryNo: str
    subtitle: str
    question_no: str
    question: str
    answer: str
    created_at: datetime

    class Config:
        orm_mode = True
