from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Section(Base):
    __tablename__ = "sections"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    section = Column(String(50))
    Categories = relationship("Category", back_populates="section")

class Category(Base):
    __tablename__ = "Categories"
    id = Column(Integer, primary_key=True, index=True)
    part_no = Column(String(50))
    subtitle = Column(String(255))
    section_id = Column(Integer, ForeignKey("sections.id"))
    section = relationship("Section", back_populates="Categories")
    questions = relationship("Question", back_populates="Category")

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    question_no = Column(String(50))
    question = Column(Text)
    answer = Column(Text)
    part_id = Column(Integer, ForeignKey("Categories.id"))
    Category = relationship("Category", back_populates="questions")
