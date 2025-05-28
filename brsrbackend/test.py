import json
import pdfplumber
import docx
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import os
from Extract_keys import KEYS_TO_EXTRACT_A,KEYS_TO_EXTRACT_B,KEYS_TO_EXTRACT_C
# Configure Gemini
import fitz  # PyMuPDF
# from kik import *
# from section_a import *
import section_a
import section_b

import principle_1
import principle_2
import principle_3
import principle_4
import principle_5
import principle_6
import principle_7
import principle_8
import principle_9


genai.configure(api_key="AIzaSyAZ7GTHvo3ttXPQtEHVtEsRemUMuXzTpTI" )




app = FastAPI()
app = FastAPI(title="Document Extractor API" )
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://192.168.2.72:3000","http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def extract_json_from_text(text):
    brace_stack = []
    start_index = None
    for i, char in enumerate(text):
        if char == '{':
            if start_index is None:
                start_index = i
            brace_stack.append('{')
        elif char == '}':
            if brace_stack:
                brace_stack.pop()
                if not brace_stack:
                    json_str = text[start_index:i + 1]
                    try:
                        return json.loads(json_str)
                    except json.JSONDecodeError:
                        continue
    return None

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])


def chunk_text(text,max_tokens=1500):
    paragraphs = text.split("\n" )
    chunks, current_chunk = [], ""
    for para in paragraphs:
        if len(current_chunk) + len(para) < max_tokens:
            current_chunk += para + "\n"
        else:
            chunks.append(current_chunk)
            # print("else part",len(current_chunk),current_chunk)
            current_chunk = para + "\n"
    if current_chunk:
        chunks.append(current_chunk)
    return chunks




# def extract_fields_with_gemini_a(text_chunk: str) -> dict:
    # print(text_chunk)
    model = genai.GenerativeModel("gemini-2.0-flash" )
    prompt = f"""
You are an expert in information extraction. Extract the following details from the provided text and return them in valid JSON format with keys exactly as listed below. Only return the JSON — no extra commentary.

{KEYS_TO_EXTRACT_A}

TEXT:
{text_chunk}
"""
    try:
        response = model.generate_content(prompt)
        # print(response.text)
        parsed = extract_json_from_text(response.text)
        return parsed if parsed else {}
    except ResourceExhausted:
        raise HTTPException(status_code=429, detail="Gemini API quota exceeded." )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



def extract_fields_with_gemini_a(text_chunk: str) -> dict:
    # print(text_chunk)
    model = genai.GenerativeModel("gemini-2.0-flash" )
    prompt = f"""
You are an expert in information extraction. Extract the following details from the provided text and return them in valid JSON format with keys exactly as listed below. Only return the JSON — no extra commentary.

{KEYS_TO_EXTRACT_A}

TEXT:
{text_chunk}
"""
    try:
        response = model.generate_content(prompt)
        # print(response.text)
        parsed = extract_json_from_text(response.text)
        return parsed if parsed else {}
    except ResourceExhausted:
        raise HTTPException(status_code=429, detail="Gemini API quota exceeded." )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def extract_fields_with_gemini_b(text_chunk: str) -> dict:
    # print(text_chunk)
    model = genai.GenerativeModel("gemini-2.0-flash" )
    prompt = f"""
You are an expert in information extraction. Extract the following details from the provided text and return them in valid JSON format with keys exactly as listed below. Only return the JSON — no extra commentary.

{KEYS_TO_EXTRACT_B}

TEXT:
{text_chunk}
"""
    try:
        response = model.generate_content(prompt)
        # print(response.text)
        parsed = extract_json_from_text(response.text)
        return parsed if parsed else {}
    except ResourceExhausted:
        raise HTTPException(status_code=429, detail="Gemini API quota exceeded." )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def extract_fields_with_gemini_c(text_chunk: str) -> dict:
    # print(text_chunk)
    model = genai.GenerativeModel("gemini-2.0-flash" )
    prompt = f"""
You are an expert in information extraction. Extract the following details from the provided text and return them in valid JSON format with keys exactly as listed below. Only return the JSON — no extra commentary.

{KEYS_TO_EXTRACT_C}

TEXT:
{text_chunk}
"""
    try:
        response = model.generate_content(prompt)
        # print(response.text)
        parsed = extract_json_from_text(response.text)
        return parsed if parsed else {}
    except ResourceExhausted:
        raise HTTPException(status_code=429, detail="Gemini API quota exceeded." )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




def merge_results(results):
    final = {}
    for result in results:
        for k, v in result.items():
            if k not in final or not final[k]:
                final[k] = v
    return final


    
def parse_brsr_text_section_a(file_path,json_merge):
  print("sucessfully file sent",file_path)
  
  
  return {
        
    "data": 
      {
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
                "questionOptions": [],
                "questionAnswer":  json_merge["Corporate Identity Number (CIN) of the Listed Entity"]
              },
              {
                "questionNo": "2",
                "question": "Name of the Listed Entity",
                "questionOptions": [],
                "questionAnswer":json_merge["Name of the Listed Entity"]
              },
              {
                "questionNo": "3",
                "question": "Year of incorporation",
                "questionOptions": [],
                "questionAnswer":json_merge["Year of incorporation"]
              },
              {
                "questionNo": "4",
                "question": "Registered office address",
                "questionOptions": [],
                "questionAnswer":json_merge["Registered office address"]
              },
              {
                "questionNo": "5",
                "question": "Corporate address",
                "questionOptions": [],
                "questionAnswer":json_merge["Corporate address"]
              },
              {
                "questionNo": "6",
                "question": "Email",
                "questionOptions": [],
                "questionAnswer":json_merge["Email"]
              },
              {
                "questionNo": "7",
                "question": "Telephone",
                "questionOptions": [],
                "questionAnswer":json_merge["Telephone"]
              },
              {
                "questionNo": "8",
                "question": "Website",
                "questionOptions": [],
                "questionAnswer":json_merge["Website"]
              },
              {
                "questionNo": "9",
                "question": "Financial year for which reporting is being done",
                "questionOptions": [],
                "questionAnswer":json_merge["Financial year for which reporting is being done"]
              },
              {
                "questionNo": "10",
                "question": "Name of the Stock Exchange(s) where shares are listed",
                "questionOptions": [],
                "questionAnswer":json_merge["Name of the Stock Exchange(s) where shares are listed"]
              },
              {
                "questionNo": "11",
                "question": "Paid-up Capital",
                "questionOptions": [],
                "questionAnswer":json_merge["Paid-up Capital"]
              },
              {
                "questionNo": "12",
                "question": "Name and contact details of the person who may be contacted",
                "questionOptions": [],
                "questionAnswer":json_merge["Name and contact details"]
              },
              {
                "questionNo": "13",
                "question": "Reporting boundary - Are the disclosures under this report made on a standalone basis (i.e. only for the entity) or on a consolidated basis (i.e. for the entity and all the entities which form a part of its consolidated financial statements, taken together)",
                "questionOptions": [],
                "questionAnswer":json_merge["Reporting boundary - Are the disclosures under this report made on a standalone basis (i.e. only for the entity) or on a consolidated basis (i.e. for the entity and all the entities which form a part of its consolidated financial statements, taken together)"]
              },
              {
                "questionNo": "14",
                "question": "Name of assurance provider",
                "questionOptions": [],
                "questionAnswer":json_merge["Name of assurance provider"]
              },
              {
                "questionNo": "15",
                "question": "Type of assurance obtained",
                "questionOptions": [],
                "questionAnswer":json_merge["Type of assurance obtained"]
              }
            ]
          },

          {
            "partNo": "two",
            "subtitle": "Products / Services",
            "questions": [
              {
                "questionNo": "1",
                "question": "Details of business activities (accounting for 90% of the turnover)",
                "questionOptions": [],
                "questionAnswer":section_a.Details_of_business(file_path),
                # "questionAnswer":json_merge["Details of business activities (accounting for 90% of the turnover)"]

              },
              {
                "questionNo": "2",
                "question": "Products/Services sold by the entity (accounting for 90% of the entity’s Turnover):",
                "questionOptions": [],
                # "questionAnswer":json_merge["Products/Services sold by the entity (accounting for 90% of the entity’s Turnover):"]
                "questionAnswer":section_a.Products_Services(file_path)

              }
            ]
          },
          {
            "partNo": "three",
            "subtitle": "Operations",
            "questions": [
              {
                "questionNo": "1",
                "question": "No. of locations where plants and/or operations/ offices of the entity are situated:",
                "questionOptions": [],
                "questionAnswer":section_a.Number_of_locations_where(file_path),#json_merge["No. of locations where plants and/or operations/ offices of the entity are situated:"],
              },
              {
                "questionNo": "2",
                "question": "Markets served by the entity",
                "questionOptions": [
                  {
                    "option": "a",
                    "questionAnswer":section_a.Number_of_locations(file_path),#json_merge["No. of Locations"]
                  },
                  {
                    "option": "b",
                    "questionAnswer":section_a.What_is_the_contribution(file_path),#json_merge["What is the contribution of exports as a percentage of the total turnover of the entity?"]
                  },
                    {
                    "option": "c",
                    "questionAnswer":section_a.A_brief_on_types(file_path),#json_merge["What is the contribution of exports as a percentage of the total turnover of the entity?"]
                  }

                ],
              }
            ]
          },
          {
            "partNo": "four",
            "subtitle": "Employees",
            "questions": [
              {
                "questionNo": "1",
                "question": "Details as at the end of Financial Year",
                "questionOptions": [
                  {
                    "option": "a",
                    "questionAnswer":section_a.Employees_and_workers(file_path),#section_a.Employees_and_workers(file_path),#json_merge["Employees and workers (including differently abled):"]
                  },
                  {
                    "option": "b",
                    "questionAnswer":section_a.Differently_abled_employees(file_path),#json_merge["Differently abled Employees and workers:"]
                  }
                ],
              },
              {
                "questionNo": "2",
                "question": "Participation/Inclusion/Representation of women",
                "questionOptions": [],
                "questionAnswer":section_a.Participation_Inclusion(file_path),#json_merge["Participation/Inclusion/Representation of women"]
              },
              {
                "questionNo": "3",
                "question": "Turnover rate for permanent employees and workers (Disclose trends for the past 3 years)",
                "questionOptions": [],
                "questionAnswer":section_a.Turnover_rate(file_path),#json_merge["Turnover rate for permanent employees and workers (Disclose trends for the past 3 years)"]
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
                "questionOptions": [],
                "questionAnswer":section_a.Names_of_holding(file_path),#json_merge["How many products have undergone a carbon footprint assessment?"]
              }
            ]
          },
          {
            "partNo": "six",
            "subtitle": "CSR Details",
            "questions": [
              {
                "questionNo": "1",
                "question": "CSR_details",
                "questionOptions": [
                  {
                    "option": "a",
                    "questionAnswer":section_a.Whether_CSR(file_path),#json_merge["Whether CSR is applicable as per section 135 of Companies Act, 2013: (Yes/No)"]
                  },
                  {
                    "option": "b",
                    "questionAnswer":section_a.Turnover(file_path),#json_merge["Turnover (in Rs.)"]
                  },
                  {
                    "option": "c",
                    "questionAnswer":section_a.Net_worth(file_path),#json_merge["Net worth (in Rs.)"]
                  }
                ],
              }
            ]
          },
          {
            "partNo": "seven",
            "subtitle": "Transparency and Disclosures Compliances",
            "questions": [
              {
                "questionNo": "1",
                "question": "Complaints/Grievances on any of the principles (Principles 1 to 9) under the National Guidelines on Responsible Business Conduct:",
                "questionOptions": [],
                "questionAnswer":section_a.Complaints_Grievances(file_path),#json_merge["Complaints/Grievances on any of the principles (Principles 1 to 9) under the National Guidelines on Responsible Business Conduct:"]
              },
              {
                "questionNo": "2",
                "question": "Overview of the entity’s material responsible business conduct issues",
                "questionOptions": [
                  {
                    "option": "a",
                    "questionAnswer":section_a.Overview_of_the_entity(file_path),#json_merge["Please indicate material responsible business conduct and sustainability issues pertaining to environmental and social matters that present a risk or an opportunity to your business, rationale for identifying the same, approach to adapt or mitigate the risk along-with its financial implications, as per the following format."]
                  }
                ],
              }
            ]
          }
        ]
      },
  
 }



def parse_brsr_text_section_b(file_path,json_merge):
    print("sucessfully file sent",file_path)

    return{
      "data":
            {
        "title": "MANAGEMENT AND PROCESS DISCLOSURES",
        "section": "section_b",
        "parts": [
          {
            "partNo": "one",
            "subtitle": "Policy and management processes",
            "questions": [
              {
                "questionNo": "1",
                "question": "Disclosure Questions",
                "questionOptions":[
                  {
                    "option": "a",
                    "questionAnswer":section_b.Whether_your_entity(file_path),
                  },
                  {
                    "option": "b",
                    "questionAnswer":section_b.Has_the_policy(file_path),
                  }, 
                  {
                    "option": "c",
                    "questionAnswer":section_b.Web_Link_of_Policies(file_path),
                  }],},
                  {
                "questionNo": "2",
                "question": "Whether the entity has translated the policy into procedures. (Yes / No)",
                "questionOptions": [],
                "questionAnswer":section_b.Whether_entity_translated(file_path),
              },
              {
                "questionNo": "3",
                "question": "Do the enlisted policies extend to your value chain partners? (Yes/No)",
                "questionOptions": [],
                "questionAnswer":section_b.Do_the_enlisted(file_path),
              },
              {
                "questionNo": "4",
                "question": "Name of the national and international codes/ certifications/labels/ standards (e.g. Forest Stewardship Council, Fairtrade, Rainforest Alliance,Trustea) standards (e.g. SA 8000, OHSAS, ISO, BIS) adopted by your entity and mapped to each principle.",
                "questionOptions": [],
                "questionAnswer":section_b.Name_of_the_national(file_path),
              },
              {
                "questionNo": "5",
                "question": "Specific commitments, goals and targets set by the entity with defined timelines, if any.",
                "questionOptions": [],
                "questionAnswer":section_b.Specific_commitments(file_path),
              },
              {
                "questionNo": "6",
                "question": "Performance of the entity against the specific commitments, goals and targets along-with reasons in case the same are not met.",
                "questionOptions": [],
                "questionAnswer":section_b.Performance_of_the_entity(file_path),
              },

            ]
          },
          {
            "partNo":"two",
            "subtitle": "Governance, leadership and oversight",
            "questions": [
              {
                "questionNo": "1",
                "question": "Statement by director responsible for the business responsibility report, highlighting ESG related challenges, targets and achievements (listed entity has flexibility regarding the placement of this disclosure)",
                "questionOptions": [],
                "questionAnswer":section_b.Statement_by_director(file_path),
              },
              {
                "questionNo": "2",
                "question": "Details of the highest authority responsible for implementation and oversight of the Business Responsibility policy (ies).",
                "questionOptions": [],
                # "questionAnswer":json_merge["Details of the highest authority responsible for implementation and oversight of the Business Responsibility policy (ies)."]
                "questionAnswer":section_b.Details_of_the_highest(file_path),

              },
              {
                "questionNo": "3",
                "question": "Does the entity have a specified Committee of the Board/ Director responsible for decision making on sustainability related issues? (Yes / No). If yes, provide details.",
                "questionOptions": [],
                # "questionAnswer":json_merge["Does the entity have a specified Committee of the Board/ Director responsible for decision making on sustainability related issues? (Yes / No). If yes, provide details."]
                "questionAnswer":section_b.Specific_commitments(file_path),
              },
              {
                "questionNo": "4",
                "question": "Details of Review of NGRBCs by the Company:",
                "questionOptions": [
                {
                    "option": "a",
                    "questionAnswer":section_b.Indicate_whether_review(file_path),
                    # "questionAnswer":json_merge["Indicate whether review was undertaken by Director / Committee of the Board/ Any other Committee"]
                  },
                  {
                    "option": "b",
                    "questionAnswer":section_b.Frequency_Annually(file_path),
                    # "questionAnswer":json_merge["Frequency(Annually/ Half yearly/ Quarterly/ Any other – please specify)"]
                  }
                ],
                # "questionAnswer":"",#json_merge["Details of Review of NGRBCs by the Company"],
              },
              {
                "questionNo": "5",
                "question": "Has the entity carried out independent assessment/ evaluation of the working of its policies by an external agency? (Yes/No). If yes, provide name of the agency.",
                "questionOptions": [],
                "questionAnswer":section_b.Has_the_entity_carried(file_path),
                # "questionAnswer":json_merge["Has the entity carried out independent assessment/ evaluation of the working of its policies by an external agency? (Yes/No). If yes, provide name of the agency."]
              },
              {
                "questionNo": "6",
                "question": "If answer to question (1) above is “No” i.e. not all Principles are covered by a policy, reasons to be stated, as below:",
                "questionOptions": [],
                # "questionAnswer":json_merge["If answer to question (1) above is “No” i.e. not all Principles are covered by a policy, reasons to be stated, as below:"]
                "questionAnswer":section_b.If_answer_to_question(file_path),
              },
              {
                "questionNo": "7",
                "question": "Supply Chain Management",
                "questionOptions": [
                                    {
                    "option": "a",
                    "questionAnswer":{
                      "The entity does not consider the principles material to its business (Yes/No)":section_b.consider_the_Principles(file_path),
                      "The entity is not at a stage where it is in a position to formulate and implement the policies on specified principles (Yes/No)":section_b.formulate_and_implement(file_path),
                      "The entity does not have the financial or/human and technical resources available for the task (Yes/No)":section_b.human_and_technical(file_path),
                      "It is planned to be done in the next financial year (Yes/No)":section_b.It_is_planned_to_be_done(file_path),
                      "Any other reason (please specify)":section_b.Any_other_reason(file_path),
                    }
                  },
                  {
                    "option": "b",
                    "questionAnswer":""#json_merge["Downstream (Distributors & Customers)"]
                  }
                  ],
                },
            ] # questions
          }# parts
        ]# part
      } #section        
    
}



def parse_brsr_text_section_c(file_path,json_merge):
  return {
    "data":[
      {
        "title": "Principle wise performance disclosure",
        "section": "section_c",
        "parts": [
            {
            "partNo": "one",
            "subtitle": "Businesses should conduct and govern themselves with integrity, and in a manner that is Ethical, Transparent and Accountable",
            "questions": [
              {
                "questionNo": "1",
                "question": "Percentage coverage by training and awareness programmes on any of the Principles during the financial year:",
                "questionOptions": [],
                # "questionAnswer": "",#json_merge["Percentage coverage by training and awareness programmes on any of the Principles during the financial year:"],
                "questionAnswer":principle_1.Percentage_coverage_by_training(file_path)#"Percentage coverage by training and awareness programmes on"),
              },
                {
                "questionNo": "2",
                "question": "Details of fines / penalties /punishment/ award/ compounding fees/ settlement amount paid in proceedings (by the entity or by directors / KMPs) with regulators/ law enforcement agencies/ judicial institutions, in the financial year, in the following format (Note: the entity shall make disclosures on the basis of materiality as specified in Regulation 30 of SEBI (Listing Obligations and Disclosure Obligations) Regulations, 2015 and as disclosed on the entity’s website",
                "questionOptions": [
                {
                    "option": "a",
                    "questionAnswer":"",
                      
                  },
                  {
                    "option": "b",
                    "questionAnswer":"",#principle_1.Non_Monetary(file_path)
                  }
                ],
                "questionAnswer":"",
              },
                {
                "questionNo": "3",
                "question": "Of the instances disclosed in Question 2 above, details of the Appeal/ Revision preferred in cases where monetary or non-monetary action has been appealed.",
                "questionOptions": [],
                "questionAnswer":principle_1.Of_the_instances_disclosed(file_path),#"Of the instances disclosed in Question 2 above, details of the Appeal/ Revision")
              },
                {
                "questionNo": "4",
                "question": "Does the entity have an anti-corruption or anti-bribery policy? If yes, provide details in brief and if available, provide a web-link to the policy.",
                "questionOptions": [],
                "questionAnswer":principle_1.Does_the_entity_have_an_anti(file_path),#"Does the entity have an anti-corruption or anti-bribery policy? If yes, provide"),
              },
                {
                "questionNo": "5",
                "question": "Number of Directors/KMPs/employees/workers against whom disciplinary action was taken by any law enforcement agency for the charges of bribery/ corruption",
                "questionOptions": [],
                "questionAnswer":principle_1.Number_of_Directors(file_path),#"Number of Directors/KMPs/employees/workers against whom disciplinary action was taken by any law enforcement"),
              },
                {
                "questionNo": "6",
                "question": "Details of complaints with regard to conflict of interest",
                "questionOptions": [],
                "questionAnswer":principle_1.Details_of_complaints(file_path),#"Details of complaints with regard to conflict of interest"),
              },
                {
                "questionNo": "7",
                "question": "Provide details of any corrective action taken or underway on issues related to fines / penalties / action taken by regulators/ law enforcement agencies/ judicial institutions, on cases of corruption and conflicts of interest.",
                "questionOptions": [],
                "questionAnswer":principle_1.Provide_details_of_any_corrective(file_path),#"Provide details of any corrective action taken or underway on issues related to fines / penalties / action taken by regulators/"),
              },
                {
                "questionNo": "8",
                "question": "Number of days of accounts payables ((Accounts payable *365) / Cost of goods/services procured) in the following format:",
                "questionOptions": [],
                "questionAnswer":principle_1.Number_of_days_of_accounts(file_path),#"Number of days of accounts payables ((Accounts payable *365) / Cost of goods/services procured)"),
              },
                {
                "questionNo": "9",
                "question": "Open-ness of business",
                "questionOptions": [
                {
                    "option": "a",
                    "questionAnswer":principle_1.Open_ness_of_business(file_path),#"Provide details of concentration of purchases"),
                  },
                ],
                "questionAnswer":"",
              },
                {
                "questionNo": "10",
                "question": "Awareness programmes conducted for value chain partners on any of the Principles during the financial year:",
                "questionOptions": [],
                "questionAnswer":principle_1.Awareness_programmes_conducted(file_path),#"Awareness programmes conducted for value chain partners on any"),
              },
                {
                "questionNo": "11",
                "question": "Does the entity have processes in place to avoid/ manage conflict of interests involving members of the Board? (Yes/No) If Yes, provide details of the same.",
                "questionOptions": [],
                "questionAnswer":principle_1.Does_the_entity_have_processes(file_path),#"Does the entity have processes in place"),
              }

            ]
          },
            {
            "partNo": "two",
            "subtitle": "Businesses should provide goods and services in a manner that is sustainable and safe",
            "questions": [
              {
                "questionNo": "1",
                "question": "Percentage of R&D and capital expenditure (capex) investments in specific technologies to improve the environmental and social impacts of product and processes to total R&D and capex investments made by the entity, respectively.",
                "questionOptions": [],
                "questionAnswer":principle_2.Percentage_of_R_and_D(file_path),
              },
              {
                "questionNo": "2",
                "question": "Does the entity have procedures in place for sustainable sourcing? (Yes/No)",
                "questionOptions": [
                   {
                    "option": "b",
                    "questionAnswer":principle_2.b_If_yes_what_percentage(file_path)
                  },
                  ],
                    "questionAnswer":principle_2.Does_the_entity_have_procedures(file_path)
              },
              {
                "questionNo": "3",
                "question": "Describe the processes in place to safely reclaim your products for reusing, recycling and disposing at the end of life, for :",
                "questionOptions": [],
                "questionAnswer": principle_2.place_to_safely_reclaim_your_products(file_path),
              },

              {
                "questionNo": "4",
                "question": "Whether Extended Producer Responsibility (EPR) is applicable to the entity’s activities (Yes / No). If yes, whether the waste collection plan is in line with the Extended Producer Responsibility (EPR) plan submitted to Pollution Control Boards? If not, provide steps taken to address the same.",
                "questionOptions": [],
                "questionAnswer":principle_2.Whether_Extended_Producer_Responsibility_EPR(file_path),#json_merge["Whether Extended Producer Responsibility (EPR) is applicable to the entity’s activities (Yes / No). If yes, whether the waste collection plan is in line with the Extended Producer Responsibility (EPR) plan submitted to Pollution Control Boards? If not, provide steps taken to address the same."],
              },

              {
                "questionNo": "5",
                "question": "Has the entity conducted Life Cycle Perspective / Assessments (LCA) for any of its products (for manufacturing industry) or for its services (for service industry)? If yes, provide details in the following format?",
                "questionOptions": [],
                "questionAnswer": principle_2.Has_the_entity_conducted_Life(file_path),
              },

              {
                "questionNo": "6",
                "question": "If there are any significant social or environmental concerns and/or risks arising from production or disposal of your products / services, as identified in the Life Cycle Perspective / Assessments (LCA) or through any other means, briefly describe the same along-with action taken to mitigate the same.",
                "questionOptions": [],
                "questionAnswer":principle_2.If_there_are_any_significant_social(file_path),#json_merge["If there are any significant social or environmental concerns and/or risks arising from production or disposal of your products / services, as identified in the Life Cycle Perspective / Assessments (LCA) or through any other means, briefly describe the same along-with action taken to mitigate the same."],
              },

              {
                "questionNo": "7",
                "question": "Percentage of recycled or reused input material to total material (by value) used in production (for manufacturing industry) or providing services (for service industry)",
                "questionOptions": [],
                "questionAnswer":principle_2.Percentage_of_recycled(file_path),#json_merge["Percentage of recycled or reused input material to total material (by value) used in production (for manufacturing industry) or providing services (for service industry)"],
              },

              {
                "questionNo": "8",
                "question": "Of the products and packaging reclaimed at end of life of products, amount (in metric tonnes) reused, recycled, and safely disposed, as per the following format:",
                "questionOptions": [],
                "questionAnswer":principle_2.Of_the_products_and_packaging(file_path),#json_merge["Of the products and packaging reclaimed at end of life of products, amount (in metric tonnes) reused, recycled, and safely disposed, as per the following format:"],
              },
              {
                "questionNo": "9",
                "question": "Reclaimed products and their packaging materials (as percentage of products sold) for each product category.",
                "questionOptions": [],
                "questionAnswer": principle_2.Reclaimed_products(file_path),#json_merge["Reclaimed products and their packaging materials (as percentage of products sold) for each product category."],
              },
        ]
      },
            {
            "partNo": "three",
            "subtitle": "Businesses should respect and promote the well-being of all employees, including those in their value chains",
            "questions": [
              {
                "questionNo": "1",
                "question": "Details of measures ",
                "questionOptions": [
                  {
                    "option": "a",
                    "questionAnswer":principle_3.well_being_of_employees(file_path),#json_merge["Details of measures for the well-being of employees:"]
                  },
                  {
                    "option": "b",
                    "questionAnswer":principle_3.well_being_of_Workers(file_path),#json_merge["Details of measures for the well-being of workers:"]
                  },
                  {
                    "option": "c",
                    "questionAnswer":principle_3.Spending_on_measures_towards(file_path),#json_merge["Spending on measures towards well-being of employees and workers (including permanent and other than permanent) in the following format –"]
                  },

                  ],
              },
              {
                "questionNo": "2",
                "question": "Details of retirement benefits, for Current and Previous FY",
                "questionOptions": [],
                "questionAnswer":principle_3.Details_retirement_benefits(file_path),#json_merge["Details of retirement benefits, for Current and Previous FY"],
              },
              {
                "questionNo": "3",
                "question": "Accessibility of workplaces",
                "questionOptions": [],
                "questionAnswer":"",#json_merge["Accessibility of workplaces"],
              },
              {
                "questionNo": "4",
                "question": "Does the entity have an equal opportunity policy as per the Rights of Persons with Disabilities Act, 2016? If so, provide a web-link to the policy.",
                "questionOptions": [],
                "questionAnswer":principle_3.Does_the_entity_have_an_equal(file_path),#json_merge["Does the entity have an equal opportunity policy as per the Rights of Persons with Disabilities Act, 2016? If so, provide a web-link to the policy."],
              },
              {
                "questionNo": "5",
                "question": "Return to work and Retention rates of permanent employees and workers that took parental leave.",
                "questionOptions": [],
                "questionAnswer":principle_3.Return_to_work(file_path),#json_merge["Return to work and Retention rates of permanent employees and workers that took parental leave."],
              },
              {
                "questionNo": "6",
                "question": "Is there a mechanism available to receive and redress grievances for the following categories of employees and worker? If yes, give details of the mechanism in brief",
                "questionOptions": [],
                "questionAnswer":principle_3.Is_there_mechanism(file_path),#json_merge["Is there a mechanism available to receive and redress grievances for the following categories of employees and worker? If yes, give details of the mechanism in brief"],
              },
              {
                "questionNo": "7",
                "question": "Membership of employees and worker in association(s) or Unions recognised by the listed entity:",
                "questionOptions": [],
                "questionAnswer":principle_3.Membership_of_employees(file_path),#json_merge["Membership of employees and worker in association(s) or Unions recognised by the listed entity:"],
              },
              {
                "questionNo": "8",
                "question": "Details of training given to employees and workers:",
                "questionOptions": [],
                "questionAnswer":principle_3.Details_of_training(file_path),#json_merge["Details of training given to employees and workers:"],
              },
              {
                "questionNo": "9",
                "question": "Details of performance and career development reviews of employees and workers:",
                "questionOptions": [],
                "questionAnswer":principle_3.Details_of_performance(file_path),#json_merge["Details of performance and career development reviews of employees and workers:"],
              },
              {
                "questionNo": "10",
                "question": "Health and safety management system:",
                "questionOptions": [
                  {
                    "option": "a",
                    "questionAnswer":principle_3.a_Whether_an_occupational(file_path),#json_merge["Whether an occupational health and safety management system has been implemented by the entity? (Yes/ No). If yes, the coverage such system?"]
                  },
                  {
                    "option": "b",
                    "questionAnswer":principle_3.b_What_are_the_processes(file_path),#json_merge["What are the processes used to identify work-related hazards and assess risks on a routine and non-routine basis by the entity?"]
                  },
                  {
                    "option": "c",
                    "questionAnswer":principle_3.c_Whether_you_have_processes_for_workers(file_path),#json_merge["Whether you have processes for workers to report the work related hazards and to remove themselves from such risks. (Y/N)"]
                  },
                  {
                    "option": "d",
                    "questionAnswer":principle_3.d_Do_the_employees_workers(file_path),#json_merge["Do the employees/ worker of the entity have access to non-occupational medical and healthcare services? (Yes/ No)"]
                  }
                ],
              },
              {
                "questionNo": "11",
                "question": "Details of safety related incidents, in the following format:",
                "questionOptions": [],
                "questionAnswer":principle_3.Details_safety_related(file_path),#json_merge["Details of safety related incidents, in the following format:"],
              },
              {
                "questionNo": "12",
                "question": "Describe the measures taken by the entity to ensure a safe and healthy work place",
                "questionOptions": [],
                "questionAnswer":principle_3.Describe_the_measures(file_path),#json_merge["Describe the measures taken by the entity to ensure a safe and healthy work place"],
              },
              {
                "questionNo": "13",
                "question": "Number of Complaints on the following made by employees and workers:",
                "questionOptions": [],
                "questionAnswer":principle_3.Number_of_Complaints(file_path),#json_merge["Number of Complaints on the following made by employees and workers:"],
              },
              {
                "questionNo": "14",
                "question": "Assessments for the year:",
                "questionOptions": [],
                "questionAnswer":principle_3.Assessments_for_the_year(file_path),#json_merge["Assessments for the year:"],
              },
              {
                "questionNo": "15",
                "question": "Provide details of any corrective action taken or underway to address safety-related incidents (if any) and on significant risks / concerns arising from assessments of health & safety practices and working conditions.",
                "questionOptions": [],
                "questionAnswer":principle_3.Provide_details_of_any_corrective(file_path),#json_merge["Provide details of any corrective action taken or underway to address safety-related incidents (if any) and on significant risks / concerns arising from assessments of health & safety practices and working conditions."],
              },
              {
                "questionNo": "16",
                "question": "Does the entity extend any life insurance or any compensatory package in the event of death of (A) Employees (Y/N)",
                "questionOptions": [
                     {
                    "option": "a",
                    "questionAnswer":"",#json_merge["(A) Employees (Y/N)"]
                  },
                  {
                    "option": "b",
                    "questionAnswer":"",#json_merge["(B) Workers (Y/N)"]
                  }],
                "questionAnswer":principle_3.Does_the_entity_extend(file_path),#json_merge["Does the entity extend any life insurance or any compensatory package in the event of death of (A) Employees (Y/N)"],
              },
              {
                "questionNo": "17",
                "question": "Provide the measures undertaken by the entity to ensure that statutory dues have been deducted and deposited by the value chain partners",
                "questionOptions": [],
                "questionAnswer":principle_3.Provide_the_measures_undertaken(file_path),#json_merge["Provide the measures undertaken by the entity to ensure that statutory dues have been deducted and deposited by the value chain partners"],
              },
              {
                "questionNo": "18",
                "question": "Provide the number of employees / workers having suffered high consequence work-related injury / ill-health / fatalities (as reported in Q11 of Essential Indicators above), who have been are rehabilitated and placed in suitable employment or whose family members have been placed in suitable employment:",
                "questionOptions": [],
                "questionAnswer":principle_3.Provide_the_number_of_employees(file_path),#json_merge["Provide the number of employees / workers having suffered high consequence work-related injury / ill-health / fatalities (as reported in Q11 of Essential Indicators above), who have been are rehabilitated and placed in suitable employment or whose family members have been placed in suitable employment:"],
              },
              {
                "questionNo": "19",
                "question": "Does the entity provide transition assistance programs to facilitate continued employability and the management of career endings resulting from retirement or termination of employment? (Yes/ No)",
                "questionOptions": [],
                "questionAnswer":principle_3.Does_the_entity_provide_transition(file_path),#json_merge["Does the entity provide transition assistance programs to facilitate continued employability and the management of career endings resulting from retirement or termination of employment? (Yes/ No)"],
              },
              {
                "questionNo": "20",
                "question": "Details on assessment of value chain partners:",
                "questionOptions": [],
                "questionAnswer":principle_3.Details_on_assessment(file_path),#json_merge["Details on assessment of value chain partners:"],
              },
              {
                "questionNo": "21",
                "question": "Provide details of any corrective actions taken or underway to address significant risks / concerns arising from assessments of health and safety practices and working conditions of value chain partners.",
                "questionOptions": [],
                "questionAnswer":principle_3.Provide_details_of_any_corrective(file_path),#json_merge["Provide details of any corrective actions taken or underway to address significant risks / concerns arising from assessments of health and safety practices and working conditions of value chain partners."],
              },
        ]
      },
            {
            "partNo": "four",
            "subtitle": "Businesses should respect the interests of and be responsive to all its stakeholders",
            "questions": [
              {
                "questionNo": "1",
                "question": "Describe the processes for identifying key stakeholder groups of the entity.",
                "questionOptions": [],
                "questionAnswer":principle_4.Describe_the_processes(file_path),#json_merge["Describe the processes for identifying key stakeholder groups of the entity."],
              },
              {
                "questionNo": "2",
                "question": "List stakeholder groups identified as key for your entity and the frequency of engagement with each stakeholder group.",
                "questionOptions": [],
                "questionAnswer":principle_4.List_stakeholder(file_path),#json_merge["List stakeholder groups identified as key for your entity and the frequency of engagement with each stakeholder group."],
              },
              {
                "questionNo": "3",
                "question": "Provide the processes for consultation between stakeholders and the Board on economic, environmental, and social topics or if consultation is delegated, how is feedback from such consultations provided to the Board.",
                "questionOptions": [],
                "questionAnswer":principle_4.Provide_the_processes(file_path),#json_merge["Provide the processes for consultation between stakeholders and the Board on economic, environmental, and social topics or if consultation is delegated, how is feedback from such consultations provided to the Board."],
              },
              {
                "questionNo": "4",
                "question": "Whether stakeholder consultation is used to support the identification and management of environmental, and social topics (Yes / No). If so, provide details of instances as to how the inputs received from stakeholders on these topics were incorporated into policies and activities of the entity",
                "questionOptions": [],
                "questionAnswer":principle_4.Whether_stakeholder_consultation(file_path),#json_merge["Whether stakeholder consultation is used to support the identification and management of environmental, and social topics (Yes / No). If so, provide details of instances as to how the inputs received from stakeholders on these topics were incorporated into policies and activities of the entity"],
              },
              {
                "questionNo": "5",
                "question": "Provide details of instances of engagement with, and actions taken to, address the concerns of vulnerable/ marginalized stakeholder groups.",
                "questionOptions": [],
                "questionAnswer":principle_4.Provide_details_of_instances(file_path),#json_merge["Provide details of instances of engagement with, and actions taken to, address the concerns of vulnerable/ marginalized stakeholder groups."],
              },


        ]
      },
            {
            "partNo": "five",
            "subtitle": " Businesses should respect and promote human rights",
            "questions": [
              {
                "questionNo": "1",
                "question": "Employees and workers who have been provided training on human rights issues and policy(ies) of the entity, in the following format:",
                "questionOptions": [],
                "questionAnswer":principle_5.Employees_and_workers(file_path),#json_merge["Employees and workers who have been provided training on human rights issues and policy(ies) of the entity, in the following format:"],
              },
              {
                "questionNo": "2",
                "question": "Details of minimum wages paid to employees and workers, in the following format:",
                "questionOptions": [],
                "questionAnswer":principle_5.Details_of_minimum(file_path),#json_merge["Details of minimum wages paid to employees and workers, in the following format:"],
              },
              {
                "questionNo": "3",
                "question": "Details of remuneration/salary/wages",
                "questionOptions": [
                                  {
                    "option": "a",
                    "questionAnswer":principle_5.Details_of_remuneration(file_path),#json_merge["Median remuneration / wages:"]
                  },
                  {
                    "option": "b",
                    "questionAnswer":principle_5.Gross_wages_paid(file_path),#json_merge["Gross wages paid to females as % of total wages paid by the entity, in the following format:"]
                  }

                  ],
              },
              {
                "questionNo": "4",
                "question": "Do you have a focal point (Individual/ Committee) responsible for addressing human rights impacts or issues caused or contributed to by the business? (Yes/ No)",
                "questionOptions": [],
                "questionAnswer":principle_5.Do_you_have_a_focal_point(file_path),#json_merge["Do you have a focal point (Individual/ Committee) responsible for addressing human rights impacts or issues caused or contributed to by the business? (Yes/ No)"],
              },
              {
                "questionNo": "5",
                "question": "Describe the internal mechanisms in place to redress grievances related to human rights issues.",
                "questionOptions": [],
                "questionAnswer":principle_5.Describe_the_internal_mechanisms(file_path),#json_merge["Describe the internal mechanisms in place to redress grievances related to human rights issues."],
              },
              {
                "questionNo": "6",
                "question": "Number of Complaints on the following made by employees and workers:",
                "questionOptions": [],
                "questionAnswer":principle_5.Number_of_Complaints(file_path),#json_merge["Number of Complaints on the following made by employees and workers:"],
              },
              {
                "questionNo": "7",
                "question": "Complaints filed under the Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013, in the following format:",
                "questionOptions": [],
                "questionAnswer":principle_5.Complaints_filed_under(file_path),#json_merge["Complaints filed under the Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013, in the following format:"],
              },
              {
                "questionNo": "8",
                "question": "Mechanisms to prevent adverse consequences to the complainant in discrimination and harassment cases.",
                "questionOptions": [],
                "questionAnswer":principle_5.Mechanisms_prevent(file_path),#json_merge["Mechanisms to prevent adverse consequences to the complainant in discrimination and harassment cases."],
              },
              {
                "questionNo": "9",
                "question": "Do human rights requirements form part of your business agreements and contracts? (Yes/ No)",
                "questionOptions": [],
                "questionAnswer":principle_5.Do_human_rights_requirements(file_path),#json_merge["Do human rights requirements form part of your business agreements and contracts? (Yes/ No)"],
              },
              {
                "questionNo": "10",
                "question": "Assessments for the year:",
                "questionOptions": [],
                "questionAnswer":principle_5.Assessments(file_path),#json_merge["Assessments for the year:"],
              },
              {
                "questionNo": "11",
                "question": "Provide details of any corrective actions taken or underway to address significant risks / concerns arising from the assessments at Question 10 above.",
                "questionOptions": [],
                "questionAnswer":principle_5.Provide_details_of_any(file_path),#json_merge["Provide details of any corrective actions taken or underway to address significant risks / concerns arising from the assessments at Question 10 above."],
              },
              {
                "questionNo": "12",
                "question": "Details of a business process being modified / introduced as a result of addressing human rights grievances/complaints.",
                "questionOptions": [],
                "questionAnswer":principle_5.Details_of_a_business_process(file_path),#json_merge["Details of a business process being modified / introduced as a result of addressing human rights grievances/complaints."],
              },
              {
                "questionNo": "13",
                "question": "Details of the scope and coverage of any Human rights due-diligence conducted",
                "questionOptions": [],
                "questionAnswer":principle_5.Details_of_the_scope(file_path),#json_merge["Details of the scope and coverage of any Human rights due-diligence conducted"],
              },
              {
                "questionNo": "14",
                "question": "Is the premise/office of the entity accessible to differently abled visitors, as per the requirements of the Rights of Persons with Disabilities Act, 2016?",
                "questionOptions": [],
                "questionAnswer":principle_5.Is_the_premise(file_path),#json_merge["Is the premise/office of the entity accessible to differently abled visitors, as per the requirements of the Rights of Persons with Disabilities Act, 2016?"],
              },
              {
                "questionNo": "15",
                "question": "Details on assessment of value chain partners:",
                "questionOptions": [],
                "questionAnswer":principle_5.Details_on_assessment_value_chain(file_path),#json_merge["Details on assessment of value chain partners:"],
              },
              {
                "questionNo": "16",
                "question": "Provide details of any corrective actions taken or underway to address significant risks / concerns arising from the assessments at Question 4 above.",
                "questionOptions": [],
                "questionAnswer":principle_5.Provide_details_of_any_corrective(file_path),#json_merge["Provide details of any corrective actions taken or underway to address significant risks / concerns arising from the assessments at Question 4 above."],
              },

        ]
      },
            {
            "partNo": "six",
            "subtitle": "Businesses should respect and make efforts to protect and restore",
            "questions": [
              {
                "questionNo": "1",
                "question": "Details of total energy consumption (in Joules or multiples) and energy intensity, in the following format:",
                "questionOptions": [],
                "questionAnswer":principle_6.Details_of_total_energy(file_path),#json_merge["Details of total energy consumption (in Joules or multiples) and energy intensity, in the following format:"],
              },
              {
                "questionNo": "2",
                "question": "Does the entity have any sites / facilities identified as designated consumers (DCs) under the Performance, Achieve and Trade (PAT) Scheme of the Government of India? (Y/N) If yes, disclose whether targets set under the PAT scheme have been achieved. In case targets have not been achieved, provide the remedial action taken, if any.",
                "questionOptions": [],
                "questionAnswer":principle_6.Does_the_entity_have_any_sites(file_path),#json_merge["Does the entity have any sites / facilities identified as designated consumers (DCs) under the Performance, Achieve and Trade (PAT) Scheme of the Government of India? (Y/N) If yes, disclose whether targets set under the PAT scheme have been achieved. In case targets have not been achieved, provide the remedial action taken, if any."],
              },
              {
                "questionNo": "3",
                "question": "Provide details of the following disclosures related to water, in the following format:",
                "questionOptions": [],
                "questionAnswer":principle_6.Provide_details_of_the_following(file_path),#json_merge["Provide details of the following disclosures related to water, in the following format:"],
              },

              {
                "questionNo": "4",
                "question": "Provide the following details related to water discharged:",
                "questionOptions": [],
                "questionAnswer":principle_6.Provide_the_following_details(file_path),#json_merge["Provide the following details related to water discharged:"],
              },

              {
                "questionNo": "5",
                "question": "Has the entity implemented a mechanism for Zero Liquid Discharge? If yes, provide details of its coverage and implementation",
                "questionOptions": [],
                "questionAnswer":principle_6.Has_the_entity_implemented(file_path),#json_merge["Has the entity implemented a mechanism for Zero Liquid Discharge? If yes, provide details of its coverage and implementation"],
              },

              {
                "questionNo": "6",
                "question": "Please provide details of air emissions (other than GHG emissions) by the entity, in the following format:",
                "questionOptions": [],
                "questionAnswer":principle_6.Please_provide_details(file_path),#json_merge["Please provide details of air emissions (other than GHG emissions) by the entity, in the following format:"],
              },

              {
                "questionNo": "7",
                "question": "Provide details of greenhouse gas emissions (Scope 1 and Scope 2 emissions) & its intensity, in the following format:",
                "questionOptions": [],
                "questionAnswer":principle_6.Provide_details_of_greenhouse(file_path),#json_merge["Provide details of greenhouse gas emissions (Scope 1 and Scope 2 emissions) & its intensity, in the following format:"],
              },

              {
                "questionNo": "8",
                "question": "Does the entity have any project related to reducing Green House Gas emission? If Yes, then provide details.",
                "questionOptions": [],
                "questionAnswer":principle_6.Does_the_entity_have_any_project(file_path),#json_merge["Does the entity have any project related to reducing Green House Gas emission? If Yes, then provide details."],
              },

              {
                "questionNo": "9",
                "question": "Provide details related to waste management by the entity, in the following format:",
                "questionOptions": [],
                "questionAnswer":principle_6.Provide_details_related(file_path),#json_merge["Provide details related to waste management by the entity, in the following format:"],
              },

              {
                "questionNo": "10",
                "question": "Briefly describe the waste management practices adopted in your establishments. Describe the strategy adopted by your company to reduce usage of hazardous and toxic chemicals in your products and processes and the practices adopted to manage such wastes.",
                "questionOptions": [],
                "questionAnswer":principle_6.Briefly_describe_the_waste(file_path),#json_merge["Briefly describe the waste management practices adopted in your establishments. Describe the strategy adopted by your company to reduce usage of hazardous and toxic chemicals in your products and processes and the practices adopted to manage such wastes."],
              },

              {
                "questionNo": "11",
                "question": "If the entity has operations/offices in/around ecologically sensitive areas (such as national parks, wildlife sanctuaries, biosphere reserves, wetlands, biodiversity hotspots, forests, coastal regulation zones etc.) where environmental approvals / clearances are required, please specify details in the following format:",
                "questionOptions": [],
                "questionAnswer":principle_6.If_the_entity_has_operations(file_path),#json_merge["If the entity has operations/offices in/around ecologically sensitive areas (such as national parks, wildlife sanctuaries, biosphere reserves, wetlands, biodiversity hotspots, forests, coastal regulation zones etc.) where environmental approvals / clearances are required, please specify details in the following format:"],
              },

              {
                "questionNo": "12",
                "question": "Details of environmental impact assessments of projects undertaken by the entity based on applicable laws, in the current financial year:",
                "questionOptions": [],
                "questionAnswer":principle_6.Details_of_environmental(file_path),#json_merge["Details of environmental impact assessments of projects undertaken by the entity based on applicable laws, in the current financial year:"],
              },

              {
                "questionNo": "13",
                "question": "Is the entity compliant with the applicable environmental law/ regulations/ guidelines in India; such as the Water (Prevention and Control of Pollution) Act, Air (Prevention and Control of Pollution) Act, Environment protection act and rules thereunder (Y/N). If not, provide details of all such non-compliances, in the following format:",
                "questionOptions": [],
                "questionAnswer":principle_6.Is_the_entity_compliant(file_path),#json_merge["Is the entity compliant with the applicable environmental law/ regulations/ guidelines in India; such as the Water (Prevention and Control of Pollution) Act, Air (Prevention and Control of Pollution) Act, Environment protection act and rules thereunder (Y/N). If not, provide details of all such non-compliances, in the following format:"],
              },

              {
                "questionNo": "14",
                "question": "Water withdrawal, consumption and discharge in areas of water stress (in kilolitres):",
                "questionOptions": [],
                "questionAnswer":principle_6.Water_withdrawal(file_path),#json_merge["Water withdrawal, consumption and discharge in areas of water stress (in kilolitres):"],
              },

              {
                "questionNo": "15",
                "question": "Please provide details of total Scope 3 emissions & its intensity, in the following format",
                "questionOptions": [
                                  {
                    "option": "a",
                    "questionAnswer":"",#json_merge["Note: Indicate if any independent assessment/ evaluation/assurance has been carried out by an external agency? (Y/N) If yes, name of the external agency"]
                  },
],
                "questionAnswer":principle_6.Please_provide_details(file_path),#json_merge["Please provide details of total Scope 3 emissions & its intensity, in the following format"],
              },

              {
                "questionNo": "16",
                "question": "With respect to the ecologically sensitive areas reported at Question 10 of Essential Indicators above, provide details of significant direct & indirect impact of the entity on biodiversity in such areas along-with prevention and remediation activities",
                "questionOptions": [],
                "questionAnswer":principle_6.With_respect_to_the_ecologically(file_path),#json_merge["With respect to the ecologically sensitive areas reported at Question 10 of Essential Indicators above, provide details of significant direct & indirect impact of the entity on biodiversity in such areas along-with prevention and remediation activities"],
              },

              {
                "questionNo": "17",
                "question": "If the entity has undertaken any specific initiatives or used innovative technology or solutions to improve resource efficiency, or reduce impact due to emissions / effluent discharge / waste generated, please provide details of the same as well as outcome of such initiatives, as per the following format:",
                "questionOptions": [],
                "questionAnswer":principle_6.If_the_entity_has_undertaken(file_path),#json_merge["If the entity has undertaken any specific initiatives or used innovative technology or solutions to improve resource efficiency, or reduce impact due to emissions / effluent discharge / waste generated, please provide details of the same as well as outcome of such initiatives, as per the following format:"],
              },

              {
                "questionNo": "18",
                "question": "Does the entity have a business continuity and disaster management plan? Give details in 100 words/ web link.",
                "questionOptions": [],
                "questionAnswer":principle_6.Does_the_entity_have_a_business(file_path),#json_merge["Does the entity have a business continuity and disaster management plan? Give details in 100 words/ web link."],
              },

              {
                "questionNo": "19",
                "question": "Disclose any significant adverse impact to the environment, arising from the value chain of the entity. What mitigation or adaptation measures have been taken by the entity in this regard.",
                "questionOptions": [],
                "questionAnswer":principle_6.Disclose_any_significant(file_path),#json_merge["Disclose any significant adverse impact to the environment, arising from the value chain of the entity. What mitigation or adaptation measures have been taken by the entity in this regard."],
              },
              {
                "questionNo": "20",
                "question": "Percentage of value chain partners (by value of business done with such partners) that were assessed for environmental impacts.",
                "questionOptions": [],
                "questionAnswer":principle_6.Percentage_of_value_chain(file_path),#json_merge["Percentage of value chain partners (by value of business done with such partners) that were assessed for environmental impacts."],
              },
              {
                "questionNo": "21",
                "question":"How many Green Credits have been generated or procured:",
                "questionOptions": [
                    {
                    "option": "a",
                    "questionAnswer": "",#json_merge["By the listed entity"]
                  },
                  {
                    "option": "b",
                    "questionAnswer":"",#json_merge["By the top ten (in terms of value of purchases and sales,respectively) value chain partners”"]
                  }
                  ],
                "questionAnswer":"",#json_merge["How many Green Credits have been generated or procured:"],
              },



        ]
      },
            {
            "partNo": "seven",
            "subtitle": " Businesses, when engaging in influencing public and regulatory policy, should do so in a manner that is responsible and transparent",
            "questions": [
              {
                "questionNo": "1",
                "question": "Trade and industry",
                "questionOptions": [
                  {
                    "option": "a",
                    "questionAnswer":principle_7.Number_of_affiliations(file_path),#json_merge["Number of affiliations with trade and industry chambers/ associations."],
                  },
                  {
                    "option": "b",
                    "questionAnswer":principle_7.List_the_top_10_trade(file_path),#json_merge["List the top 10 trade and industry chambers/ associations (determined based on the total members of such body) the entity is a member of/ affiliated to, in the following format"]
                  }                    
                    ],
              },
              {
                "questionNo": "2",
                "question": "Provide details of corrective action taken or underway on any issues related to anti-competitive conduct by the entity, based on adverse orders from regulatory authorities.",
                "questionOptions": [],
                "questionAnswer":principle_7.Provide_details_of_corrective_action(file_path),#json_merge["Provide details of corrective action taken or underway on any issues related to anti-competitive conduct by the entity, based on adverse orders from regulatory authorities."],
              },
              {
                "questionNo": "3",
                "question": "Details of public policy positions advocated by the entity:",
                "questionOptions": [],
                "questionAnswer":principle_7.Details_of_public_policy(file_path),#json_merge["Details of public policy positions advocated by the entity:"],
              },

        ]
      },
            {
            "partNo": "eight",
            "subtitle": "Businesses should promote inclusive growth and equitable development",
            "questions": [
              {
                "questionNo": "1",
                "question": "Details of Social Impact Assessments (SIA) of projects undertaken by the entity based on applicable laws, in the current financial year.",
                "questionOptions": [],
                "questionAnswer":principle_8.Details_of_Social_Impact(file_path),#json_merge["Details of Social Impact Assessments (SIA) of projects undertaken by the entity based on applicable laws, in the current financial year."],
              },
              {
                "questionNo": "2",
                "question": "Provide information on project(s) for which ongoing Rehabilitation and Resettlement (R&R) is being undertaken by your entity, in the following format",
                "questionOptions": [],
                "questionAnswer":principle_8.Provide_information_on_project(file_path),#json_merge["Provide information on project(s) for which ongoing Rehabilitation and Resettlement (R&R) is being undertaken by your entity, in the following format"],
              },

              {
                "questionNo": "3",
                "question": "Describe the mechanisms to receive and redress grievances of the community.",
                "questionOptions": [],
                "questionAnswer":principle_8.Describe_the_mechanisms(file_path),#json_merge["Describe the mechanisms to receive and redress grievances of the community."],
              },

              {
                "questionNo": "4",
                "question": "Percentage of input material (inputs to total inputs by value) sourced from suppliers",
                "questionOptions": [],
                "questionAnswer":principle_8.Percentage_of_input_material(file_path),#json_merge["Percentage of input material (inputs to total inputs by value) sourced from suppliers"],
              },

              {
                "questionNo": "5",
                "question": "Job creation in smaller towns – Disclose wages paid to persons employed (including employees or workers employed on a permanent or non-permanent / on contract basis) in the following locations, as % of total wage cost",
                "questionOptions": [],
                "questionAnswer":principle_8.Job_creation_in_smaller_towns(file_path),#json_merge["Job creation in smaller towns – Disclose wages paid to persons employed (including employees or workers employed on a permanent or non-permanent / on contract basis) in the following locations, as % of total wage cost"],
              },

              {
                "questionNo": "6",
                "question": "Provide details of actions taken to mitigate any negative social impacts identified in the Social Impact Assessments (Reference: Question 1 of Essential Indicators above):",
                "questionOptions": [],
                "questionAnswer":principle_8.Provide_details_of_actions_taken(file_path),#json_merge["Provide details of actions taken to mitigate any negative social impacts identified in the Social Impact Assessments (Reference: Question 1 of Essential Indicators above):"],
              },

              {
                "questionNo": "7",
                "question": "Provide the following information on CSR projects undertaken by your entity in designated aspirational districts as identified by government bodies",
                "questionOptions": [],
                "questionAnswer":"",#json_merge["Provide the following information on CSR projects undertaken by your entity in designated aspirational districts as identified by government bodies"],
              },

              {
                "questionNo": "8",
                "question": "Do you have a preferential procurement policy where you give preference to purchase from suppliers comprising marginalized /vulnerable groups? (Yes/No)",
                "questionOptions": [
                                         {
                    "option": "a",
                    "questionAnswer":"",#json_merge["From which marginalized /vulnerable groups do you procure?"]
                  },
                  {
                    "option": "b",
                    "questionAnswer":"",#json_merge["What percentage of total procurement (by value) does it constitute?"]
                  }
                    
                    ],
                "questionAnswer":"",#json_merge["Do you have a preferential procurement policy where you give preference to purchase from suppliers comprising marginalized /vulnerable groups? (Yes/No)"],
              },

              {
                "questionNo": "9",
                "question": "Details of the benefits derived and shared from the intellectual properties owned or acquired by your entity (in the current financial year), based on traditional knowledge:",
                "questionOptions": [],
                "questionAnswer":"",#json_merge["Details of the benefits derived and shared from the intellectual properties owned or acquired by your entity (in the current financial year), based on traditional knowledge:"],
              },

              {
                "questionNo": "10",
                "question": "Details of corrective actions taken or underway, based on any adverse order in intellectual property related disputes wherein usage of traditional knowledge is involved.",
                "questionOptions": [],
                "questionAnswer":"",#json_merge["Details of corrective actions taken or underway, based on any adverse order in intellectual property related disputes wherein usage of traditional knowledge is involved."],
              },

              {
                "questionNo": "11",
                "question": "Details of beneficiaries of CSR Projects:",
                "questionOptions": [],
                "questionAnswer":"",#json_merge["Details of beneficiaries of CSR Projects:"],
              },


        ]
      },
            {
            "partNo": "nine",
            "subtitle": "",
            "questions": [
              {
                "questionNo": "1",
                "question": "Describe the mechanisms in place to receive and respond to consumer complaints and feedback.",
                "questionOptions": [],
                "questionAnswer":principle_9.Describe_the_mechanisms(file_path),
                },
              {
                "questionNo": "2",
                "question": "Turnover of products and/ services as a percentage of turnover from all products/service that carry information about:",
                "questionOptions": [],
                "questionAnswer":principle_9.Turnover_products(file_path),
              },
              {
                "questionNo": "3",
                "question": "Number of consumer complaints in respect of the following:",
                "questionOptions": [],
                "questionAnswer":principle_9.Number_consumer(file_path),
              },

              {
                "questionNo": "4",
                "question": "Details of instances of product recalls on account of safety issues:",
                "questionOptions": [],
                "questionAnswer":principle_9.Details_of_instances_of_product(file_path),
              },
              {
                "questionNo": "5",
                "question": "Does the entity have a framework/policy on cyber security and risks related to data privacy? (Yes/No). If available, provide weblink of the policy.",
                "questionOptions": [],
                "questionAnswer":principle_9.Does_the_entity_have_a_framework(file_path),
              },

              {
                "questionNo": "6",
                "question": "Provide details of any corrective actions taken or underway on issues relating to advertising, and delivery of essential services; cyber security and data privacy of customers; re-occurrence of instances of product recalls; penalty / action taken by regulatory authorities on safety of products / services.",
                "questionOptions": [],
                "questionAnswer":principle_9.Provide_details_of_any_corrective(file_path),
              },
              {
                "questionNo": "7",
                "question": "Channels / platforms where information on products and services of the entity can be accessed (provide web link, if available).",
                "questionOptions": [],
                "questionAnswer":principle_9.Channels_platforms(file_path),
              },

              {
                "questionNo": "8",
                "question": "Steps taken to inform and educate consumers about safe and responsible usage of products and/or services.",
                "questionOptions": [],
                "questionAnswer":principle_9.Steps_taken(file_path),
              },

              {
                "questionNo": "9",
                "question": "Mechanisms in place to inform consumers of any risk of disruption/discontinuation of essential services.",
                "questionOptions": [],
                "questionAnswer":principle_9.Mechanisms_place(file_path),
              },

              {
                "questionNo": "10",
                "question": "Does the entity display product information on the product over and above what is mandated as per local laws? (Yes/No/Not Applicable) If yes, provide details in brief. Did your entity carry out any survey with regard to consumer satisfaction relating to the major products / services of the entity, significant locations of operation of the entity or the entity as a whole? (Yes/No)",
                "questionOptions": [],
                "questionAnswer":principle_9.Does_the_entity_display_product_information(file_path),
              },
              {
                "questionNo": "11",
                "question":"Provide the following information relating to data breaches:",
                "questionOptions":[
                                         {
                    "option": "a",
                    "questionAnswer":principle_9.Number_of_instances(file_path),
                  },
                  {
                    "option": "b",
                    "questionAnswer":principle_9.Percentage_data_breaches(file_path),
                  }],
              }
          ]  }
                ]
      }]}




@app.post("/extract/" )
async def extract_document(file: UploadFile = File(...),questionKey: str = Form(...)):
    if not (file.filename.endswith(".pdf" ) or file.filename.endswith(".docx" )):
        raise HTTPException(status_code=400, detail="Only PDF or DOCX files are supported." )
          
    if questionKey=="section_a":
      print(questionKey)
      content = await file.read()
      temp_path =file.filename
      print("file path",temp_path)
      
      with open(temp_path, "wb" ) as f:
          f.write(content)

      try:
          if file.filename.endswith(".pdf" ):
              text = extract_text_from_pdf(temp_path)
          else:
              text = extract_text_from_docx(temp_path)

            
          chunks = chunk_text(text)
          results = [extract_fields_with_gemini_a(chunk) for chunk in chunks[:5]]
          # print(results)
          merged = merge_results(results)          
          res=parse_brsr_text_section_a(temp_path,merged)
          return res

          
          
      finally:
        import os
        # if os.path.exists(temp_path):
        #     os.remove(temp_path)


    elif questionKey=="section_b":
      print(questionKey)
      content = await file.read()
      temp_path =file.filename
      
      with open(temp_path, "wb" ) as f:
          f.write(content)

      try:
          if file.filename.endswith(".pdf" ):
              text = extract_text_from_pdf(temp_path)
          else:
              text = extract_text_from_docx(temp_path)

                    
          chunks = chunk_text(text)
          results = [extract_fields_with_gemini_b(chunk) for chunk in chunks[:5]]

          print(results)
          merged = merge_results(results)
          res=parse_brsr_text_section_b(temp_path,merged)
          return res          

      finally:
        import os
          # if os.path.exists(temp_path):
          #     os.remove(temp_path)
              

    elif questionKey=="section_c":
      print(questionKey)
      content = await file.read()
      temp_path = f"temp_{file.filename}"
      
      with open(temp_path, "wb" ) as f:
          f.write(content)

      try:
          if file.filename.endswith(".pdf" ):
              text = extract_text_from_pdf(temp_path)
          else:
              text = extract_text_from_docx(temp_path)
                    
          chunks = chunk_text(text)
          results = [extract_fields_with_gemini_c(chunk) for chunk in chunks[:5]]

          # print(results)
          merged = merge_results(results)
          print(merged)
          res=parse_brsr_text_section_c(temp_path,merged)
          return res          

      finally:
          import os
          if os.path.exists(temp_path):
              os.remove(temp_path)
              
      

    else:
      return "SECTION NOT FOUND !"



    


if __name__ == "__main__":
    uvicorn.run("test:app", host="0.0.0.0", port=1000, reload=False, log_level="debug" )
