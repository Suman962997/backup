from fastapi import FastAPI, Request,HTTPException,Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any
from pydantic import BaseModel
import uvicorn
from pydantic import BaseModel
import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from sqlalchemy.orm import declarative_base, relationship,Session
from sqlalchemy import Column, Integer, String, ForeignKey, Text
import os
import tkinter as tk
from models import Base, Section, Part, Question
from database import engine, SessionLocal
from typing import Dict

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



def create_pdf(json_data:dict):
  filename=None
  parts=json_data["parts"]
  section_a_subtitle=parts[0]["subtitle"]
  section_a_questions=parts[0]["questions"]
  for part in json_data["parts"]:
    for question in part["questions"]:
      if question["question"]=="Name of the Listed Entity":
        filename=question["questionAnswer"]
    if filename:
      break
  print(filename)
  c = canvas.Canvas(filename+'.pdf', pagesize=letter)
  width, height = letter
  # Draw some text
  c.setFont('DarkGardenMK',15)
  c.drawString(520, height -50, "Aeiforo")

  c.setFont("Helvetica",18)
  c.drawString(30, height - 100, "BUSINESS RESPONSIBILITY & SUSTAINABILITY REPORT")

  # Draw a line
  c.line(70, height - 105, 800, height - 105)
  c.drawString(100, height - 150, "SECTION A: GENERAL DISCLOSURES")
  c.setFont("Courier-Bold",15)
  c.drawString(1, height - 180,"I.")    
  c.drawString(14, height - 180,section_a_subtitle)    

  c.setFont("Times-Roman",14)

  for i,q in enumerate(section_a_questions,start=12):    
    c.drawString(1, height - i*20,q["questionNo"]+'.')    
    c.drawString(14, height - i*20,q["question"])
    c.drawString(400, height - i*20,q["questionAnswer"])
    
  # Save the PDF
  c.save()



app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://192.168.2.72:3000","http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/submit/" )
async def extract_document(texts: Dict[str, str], db: Session = Depends(get_db)):
    if texts:
        print("datas####")      
        print(texts)

        data= {
        "title": "GENERAL DISCLOSURES",
        "section": "section_a",
        "parts": [
          {
            "partNo": "one",
            "subtitle": "Details of the listed entity",
            "questions": [
              {
                "questionNo": "1",
                "question": "Corporate Identity Number (CIN) of the Listed Entity",
                "questionAnswer":texts["corporate identity number (cin) of the listed entity"]
              },
              {
                "questionNo": "2",
                "question": "Name of the Listed Entity",
                "questionAnswer":texts["name of the listed entity"]
              },
              {
                "questionNo": "3",
                "question": "Year of incorporation",
                "questionAnswer":texts["year of incorporation"]
              },
              {
                "questionNo": "4",
                "question": "Registered office address",
                "questionAnswer":texts["registered office address"]
              },
              {
                "questionNo": "5",
                "question": "Corporate address",
                "questionAnswer":texts["corporate address"]
                },
              {
                "questionNo": "6",
                "question": "Email",
                "questionAnswer":texts["e-mail"]
              },
              {
                "questionNo": "7",
                "question": "Telephone",
                "questionAnswer":texts["telephone"]
              },
              {
                "questionNo": "8",
                "question": "Website",
                "questionAnswer":texts["website"]
              },
              {
                "questionNo": "9",
                "question": "Financial year for which reporting is being done",
                "questionAnswer":texts["financial year for which reporting is being done"]
              },
              {
                "questionNo": "10",
                "question": "Name of the Stock Exchange(s) where shares are listed",
                "questionAnswer":texts["name of the stock exchange(s) where shares are listed"]
              },
              {
                "questionNo": "11",
                "question": "Paid-up Capital",
                "questionAnswer":texts["paid-up capital"]
              },
              {
                "questionNo": "12",
                "question": "Name and contact details (telephone, email address) of the person who may be contacted in case of any queries on the brsr report",
                "questionAnswer":texts["name and contact details (telephone, email address) of the person who may be contacted in case of any queries on the brsr report"]
              },
              {
                "questionNo": "13",
                "question": "Reporting boundary - Are the disclosures under this report made on a standalone basis (i.e. only for the entity) or on a consolidated basis (i.e. for the entity and all the entities which form a part of its consolidated financial statements, taken together)",
                "questionAnswer":texts["reporting boundary - are the disclosures under this report made on a standalone basis (i.e. only for the entity) or on a consolidated basis (i.e. for the entity and all the entities which form a part of its consolidated financial statements, taken together)."]
              },
              {
                "questionNo": "14",
                "question": "Name of assurance provider",
                "questionAnswer":texts["name of assurance provider"]
              },
              {
                "questionNo": "15",
                "question": "Type of assurance obtained",
                "questionAnswer":texts["type of assurance obtained"]
              }
            ]
          },
          {
            "partNo": "two",
            "subtitle": "Products / Services",
            "questions": [
              {
                "questionNo": "1",
                "question":"Details of business activities (accounting for 90% of the turnover):",
                "questionAnswer":"section_a.Details_of_business(file_path)",

              },
              {
                "questionNo": "2",
                "question": "Products/Services sold by the entity (accounting for 90% of the entity’s Turnover):",
                "questionAnswer":"section_a.Products_Services(file_path)"

              }
            ]
          },
          {
            "partNo": "three",
            "subtitle": "Operations",
            "questions": [
              {
                "questionNo": "1",
                "question": "Number of locations where plants and offices of the entity are situated:",
                "questionAnswer":"section_a.Number_of_locations_where(file_path)",
              },
              {
                "questionNo": "2",
                "question": "Number of locations",
                "questionAnswer":"section_a.Number_of_locations(file_path)",
              },
              {
                "questionNo": "3",
                "question": "What is the contribution of exports as a percentage of the total turnover of the entity?",
                "questionAnswer":"section_a.What_is_the_contribution(file_path)",
              },
              {
                "questionNo": "4",
                "question":"A brief on types of customers",
                "questionAnswer":"section_a.A_brief_on_types(file_path)",
              },
            ]
          },
          {
            "partNo": "four",
            "subtitle": "Employees",
            "questions": [
              {
              "questionNo": "1",
              "question": "Employees and workers (including differently abled):",
              "questionAnswer":"section_a.Employees_and_workers(file_path)",
              },
              {
              "questionNo": "2",
              "question": "Differently abled Employees and workers:",
              "questionAnswer":"section_a.Differently_abled_employees(file_path)",
              },
              {
                "questionNo": "3",
                "question": "Participation/Inclusion/Representation of women",
                "questionAnswer":"section_a.Participation_Inclusion(file_path)",
              },
              {
                "questionNo": "4",
                "question": "Turnover rate for permanent employees and workers (Disclose trends for the past 3 years)",
                "questionAnswer":"section_a.Turnover_rate(file_path)",
              }
            ]
          },
          {
            "partNo": "five",
            "subtitle": "Holding, Subsidiary and Associate Companies (including joint ventures)",
            "questions": [
              {
                "questionNo": "1",
                "question": "How many products have undergone a carbon footprint assessment?",
                "questionAnswer":"section_a.Names_of_holding(file_path)",
              }
            ]
          },
          {
            "partNo": "six",
            "subtitle": "CSR Details",
            "questions": [
            {
            "questionNo": "1",
            "question": "Whether CSR is applicable as per section 135 of Companies Act, 2013: (Yes/No)",
            "questionAnswer":"section_a.Whether_CSR(file_path)",
            },
                        {
            "questionNo": "2",
            "question": "Turnover (in Rs.)",
            "questionAnswer":"section_a.Turnover(file_path)",
            },
            {
            "questionNo": "3",
            "question": "Net worth (in Rs.)",
            "questionAnswer":"section_a.Net_worth(file_path)",
            },
            ]
          },
          {
            "partNo": "seven",
            "subtitle": "Transparency and Disclosures Compliances",
            "questions": [
              {
                "questionNo": "1",
                "question": "Complaints/Grievances on any of the principles (Principles 1 to 9) under the National Guidelines on Responsible Business Conduct:",
                "questionAnswer":"section_a.Complaints_Grievances(file_path)",
              },
              {
            "questionNo": "2",
            "question": "Please indicate material responsible business conduct and sustainability issues pertaining to environmental and social matters that present a risk or an opportunity to your business, rationale for identifying the same, approach to adapt or mitigate the risk along-with its financial implications, as per the following format.",
            "questionAnswer":"section_a.Please_indicate_material(file_path)",
            },

            ]
          }
        ]
      }
          # 1. Save section


        section = Section(title=data["title"], section=data["section"])
        db.add(section)
        db.flush()  # Get section.id before commit

        # 2. Save parts and questions
        for part in data["parts"]:
            db_part = Part(part_no=part["partNo"], subtitle=part["subtitle"], section_id=section.id)
            db.add(db_part)
            db.flush()

            for q in part["questions"]:
                db_question = Question(
                    question_no=q["questionNo"],
                    question=q["question"],
                    answer=q["questionAnswer"],
                    part_id=db_part.id
                )
                db.add(db_question)

        db.commit()
        

        return create_pdf(data)
    

if __name__ == "__main__":
    uvicorn.run("create:app", host="0.0.0.0", port=5000, reload=False, log_level="debug" )
