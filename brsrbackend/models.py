# models.py

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Text

Base = declarative_base()

class Section(Base):
    __tablename__ = "sections"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    section = Column(String(100))
    parts = relationship("Part", back_populates="section")

class Part(Base):
    __tablename__ = "parts"
    id = Column(Integer, primary_key=True, index=True)
    part_no = Column(String(50))
    subtitle = Column(String(255))
    section_id = Column(Integer, ForeignKey("sections.id"))
    section = relationship("Section", back_populates="parts")
    questions = relationship("Question", back_populates="part")

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    question_no = Column(String(50))
    question = Column(Text)
    answer = Column(Text)
    part_id = Column(Integer, ForeignKey("parts.id"))
    part = relationship("Part", back_populates="questions")
