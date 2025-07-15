# from fastapi import FastAPI, Request,HTTPException,Depends,APIRouter
# from fastapi.middleware.cors import CORSMiddleware
# from typing import Dict, Any
# from pydantic import BaseModel
# from sqlalchemy.orm import declarative_base, relationship,Session
# from sqlalchemy import Column, Integer, String, ForeignKey, Text,text,inspect
# from typing import Dict,List,Optional  
# import json
# import uvicorn
# from database import engine, SessionLocal
# from models import Base,create_pdf_model,TableRegistry  # Import if not already done
# import pdf
# import re
# import random



# class ReportListResponse(BaseModel):
#     name: List[Any]=None
#     created_date: List[Any] = None
#     period: List[Any] = None
#     progress: List[Any] = None
#     status: List[Any] = None





# app = FastAPI()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://192.168.2.72:3000","http://localhost:3000"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # @app.post("/create_pdf/" )
# # async def extract_document(texts: Dict[str, Any], db: Session = Depends(get_db)):
# #     if texts:
# #         print("datas####")
# #         texts = {k.lower(): v for k, v in texts.items()}
    
# #         # print(texts)
# #         data= {
# #   "sections":[
# #     { 
# #      "title": "GENERAL DISCLOSURES",
# #      "section": "SECTION A",
# #      "Categories": [
# #           { "partRoman":"I",
# #         "categoryNo": "one",
# #         "subtitle": "Details of the listed entity",
# #         "questions": [
# #           {
# #             "questionNo": "1",
# #             "question": "Corporate Identity Number (CIN) of the Listed Entity",
# #             "questionAnswer":texts.get("corporate identity number (cin) of the listed entity","Not Applicable")
# #           },
# #           {
# #             "questionNo": "2",
# #             "question": "Name of the Listed Entity",
# #             "questionAnswer":texts.get("name of the listed entity","Not Applicable")
# #           },
# #           {
# #             "questionNo": "3",
# #             "question": "Year of incorporation",
# #             "questionAnswer":texts.get("year of incorporation","Not Applicable")
# #           },
# #           {
# #             "questionNo": "4",
# #             "question": "Registered office address",
# #             "questionAnswer":texts.get("registered office address","Not Applicable")
# #           },
# #           {
# #             "questionNo": "5",
# #             "question": "Corporate address",
# #             "questionAnswer":texts.get("corporate address","Not Applicable")
# #             },
# #           {
# #             "questionNo": "6",
# #             "question": "E-mail",
# #             "questionAnswer":texts.get("Email","Not Applicable")
# #           },

# #           {
# #             "questionNo": "7",
# #             "question": "Telephone",
# #             "questionAnswer":texts.get("telephone","Not Applicable")
# #           },
# #           {
# #             "questionNo": "8",
# #             "question": "Website",
# #             "questionAnswer":texts.get("website","Not Applicable")
# #           },
# #           {
# #             "questionNo": "9",
# #             "question": "Financial year for which reporting is being done",
# #             "questionAnswer":texts.get("financial year for which reporting is being done","Not Applicable")
# #           },
# #           {
# #             "questionNo": "10",
# #             "question": "Name of the Stock Exchange(s) where shares are listed",
# #             "questionAnswer":texts.get("name of the stock exchange(s) where shares are listed","Not Applicable")
# #           },
# #           {
# #             "questionNo": "11",
# #             "question": "Paid-up Capital",
# #             "questionAnswer":texts.get("paid-up capital","Not Applicable")
# #           },
# #           {
# #             "questionNo": "12",
# #             "question": "Name and contact details (telephone, email address) of the person who may be contacted in case of any queries on the brsr report",
# #             "questionAnswer":texts.get("Name and contact details (telephone, email address) of the person who may be contacted in case of any queries on the BRSR report","Not Applicable")
# #           },
# #           {
# #             "questionNo": "13",
# #             "question": "Reporting boundary - Are the disclosures under this report made on a standalone basis (i.e. only for the entity) or on a consolidated basis (i.e. for the entity and all the entities which form a part of its consolidated financial statements, taken together)",
# #             "questionAnswer":texts.get("Reporting boundary - Are the disclosures under this report made on a standalone basis (i.e. only for the entity) or on a consolidated basis (i.e. for the entity and all the entities which form a part of its consolidated financial statements, taken together).","Not Applicable")
# #           },
# #           {
# #             "questionNo": "14",
# #             "question": "Name of assurance provider",
# #             "questionAnswer":texts.get("name of assurance provider","Not Applicable")
# #           },
# #           {
# #             "questionNo": "15",
# #             "question": "Type of assurance obtained",
# #             "questionAnswer":texts.get("type of assurance obtained","Not Applicable")
# #           }]
# #       },
# #           { "partRoman":"II",
# #             "categoryNo": "two",
# #             "subtitle": "Products / Services",
# #             "questions": [
# #               {
# #                 "questionNo": "1",
# #                 "question":"Details of business activities (accounting for 90% of the turnover):",
# #                 "questionAnswer":texts.get("details of business activities (accounting for 90% of the turnover):","Not Applicable"),

# #               },
# #               {
# #                 "questionNo": "2",
# #                 "question": "Products/Services sold by the entity (accounting for 90% of the entity’s Turnover):",
# #                 "questionAnswer":texts.get("products/services sold by the entity (accounting for 90% of the entity’s turnover):","Not Applicable")
# #               }]
# #             },
# #           { "partRoman":"III",
# #             "categoryNo": "three",
# #             "subtitle": "Operations",
# #             "questions": [
# #               {
# #                 "questionNo": "1",
# #                 "question": "Number of locations where plants and offices of the entity are situated:",
# #                 "questionAnswer":texts.get("number of locations where plants and offices of the entity are situated:","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "2",
# #                 "question": "Number of locations",
# #                 "questionAnswer":texts.get("number of locations","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "3",
# #                 "question": "What is the contribution of exports as a percentage of the total turnover of the entity?",
# #                 "questionAnswer":texts.get("what is the contribution of exports as a percentage of the total turnover of the entity?","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "4",
# #                 "question":"A brief on types of customers",
# #                 "questionAnswer":texts.get("a brief on types of customers","Not Applicable"),
# #               },
# #             ]
# #           },
# #           { "partRoman":"IV",
# #             "categoryNo": "four",
# #             "subtitle": "Employees",
# #             "questions": [
# #               {
# #               "questionNo": "1",
# #               "question": "Employees and workers (including differently abled):",
# #               "questionAnswer":texts.get("employees and workers (including differently abled):","Not Applicable"),
# #               },
# #               {
# #               "questionNo": "2",
# #               "question": "Differently abled Employees and workers:",
# #               "questionAnswer":texts.get("differently abled employees and workers:","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "3",
# #                 "question": "Participation/Inclusion/Representation of women",
# #                 "questionAnswer":texts.get("participation/inclusion/representation of women","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "4",
# #                 "question": "Turnover rate for permanent employees and workers (Disclose trends for the past 3 years)",
# #                 "questionAnswer":texts.get("turnover rate for permanent employees and workers (disclose trends for the past 3 years)","Not Applicable"),
# #               }
# #             ]
# #           },
# #           { "partRoman":"V",
# #             "categoryNo": "five",
# #             "subtitle": "Holding, Subsidiary and Associate Companies (including joint ventures)",
# #             "questions": [
# #               {
# #                 "questionNo": "1",
# #                 "question": "How many products have undergone a carbon footprint assessment?",
# #                 "questionAnswer":texts.get("how many products have undergone a carbon footprint assessment?","Not Applicable"),
# #               }
# #             ]
# #           },
# #           {"partRoman":"VI",
# #             "categoryNo": "six",
# #             "subtitle": "CSR Details",
# #             "questions": [
# #             {
# #             "questionNo": "1",
# #             "question": "Whether CSR is applicable as per section 135 of Companies Act, 2013: (Yes/No)",
# #             "questionAnswer":texts.get("whether csr is applicable as per section 135 of companies act, 2013: (yes/no)","Not Applicable"),
# #             },
# #                         {
# #             "questionNo": "2",
# #             "question": "Turnover (in Rs.)",
# #             "questionAnswer":texts.get("turnover (in rs.)","Not Applicable"),
# #             },
# #             {
# #             "questionNo": "3",
# #             "question": "Net worth (in Rs.)",
# #             "questionAnswer":texts.get("net worth (in rs.)","Not Applicable"),
# #             },
# #             ]
# #           },
# #           { "partRoman":"VII",
# #             "categoryNo": "seven",
# #             "subtitle": "Transparency and Disclosures Compliances",
# #             "questions": [
# #               {
# #                 "questionNo": "1",
# #                 "question": "Complaints/Grievances on any of the principles (Principles 1 to 9) under the National Guidelines on Responsible Business Conduct:",
# #                 "questionAnswer":texts.get("complaints/grievances on any of the principles (principles 1 to 9) under the national guidelines on responsible business conduct:","Not Applicable"),
# #               },
# #               {
# #             "questionNo": "2",
# #             "question": "Please indicate material responsible business conduct and sustainability issues pertaining to environmental and social matters that present a risk or an opportunity to your business, rationale for identifying the same, approach to adapt or mitigate the risk along-with its financial implications, as per the following format.",
# #             "questionAnswer":texts.get("please indicate material responsible business conduct and sustainability issues pertaining to environmental and social matters that present a risk or an opportunity to your business, rationale for identifying the same, approach to adapt or mitigate the risk along-with its financial implications, as per the following format.","Not Applicable"),
# #             },

# #             ]
# #           }
# #         ]},
# #     {
# #       "title": "MANAGEMENT AND PROCESS DISCLOSURES",
# #         "section": "SECTION B",
# #         "Categories": [
# #           { "partRoman":"I",
# #             "categoryNo": "one",
# #             "subtitle": "Policy and management processes",
# #             "questions": [
# #               {
# #                 "questionNo": "1",
# #                 "question": "Whether your entity’s policy/policies cover each principle and its core elements of the NGRBCs. (Yes/No)",
# #                 "questionAnswer":texts.get("whether your entity’s policy/policies cover each principle and its core elements of the ngrbcs. (yes/no)","Not Applicable"),

# #               },
# #               {
# #                 "questionNo": "2",
# #                 "question": "Has the policy been approved by the Board? (Yes/No)",
# #                 "questionAnswer":texts.get("has the policy been approved by the board? (yes/no)","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "3",
# #                 "question": "Web Link of the Policies, if available.",                
# #                 "questionAnswer":texts.get("web link of the policies, if available.","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "4",
# #                 "question": "Whether the entity has translated the policy into procedures. (Yes / No)",
                
# #                 "questionAnswer":texts.get("whether the entity has translated the policy into procedures. (yes / no)","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "5",
# #                 "question": "Do the enlisted policies extend to your value chain partners? (Yes/No)",
                
# #                 "questionAnswer":texts.get("do the enlisted policies extend to your value chain partners? (yes/no)","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "6",
# #                 "question": "Name of the national and international codes/ certifications/labels/ standards (e.g. Forest Stewardship Council, Fairtrade, Rainforest Alliance,Trustea) standards (e.g. SA 8000, OHSAS, ISO, BIS) adopted by your entity and mapped to each principle.",
                
# #                 "questionAnswer":texts.get("name of the national and international codes/ certifications/labels/ standards (e.g. forest stewardship council, fairtrade, rainforest alliance,trustea) standards (e.g. sa 8000, ohsas, iso, bis) adopted by your entity and mapped to each principle.","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "7",
# #                 "question": "Specific commitments, goals and targets set by the entity with defined timelines, if any.",
                
# #                 "questionAnswer":texts.get("specific commitments, goals and targets set by the entity with defined timelines, if any.","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "8",
# #                 "question": "Performance of the entity against the specific commitments, goals and targets along-with reasons in case the same are not met.",
                
# #                 "questionAnswer":texts.get("performance of the entity against the specific commitments, goals and targets along-with reasons in case the same are not met.","Not Applicable"),
# #               },

# #             ]
# #           },
# #           {  "partRoman":"II",
# #             "categoryNo":"two",
# #             "subtitle": "Governance, leadership and oversight",
# #             "questions": [
# #               {
# #                 "questionNo": "1",
# #                 "question": "Statement by director responsible for the business responsibility report, highlighting ESG related challenges, targets and achievements (listed entity has flexibility regarding the placement of this disclosure)",
                
# #                 "questionAnswer":texts.get("statement by director responsible for the business responsibility report, highlighting esg related challenges, targets and achievements (listed entity has flexibility regarding the placement of this disclosure)","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "2",
# #                 "question": "Details of the highest authority responsible for implementation and oversight of the Business Responsibility policy (ies).",
                
# #                 "questionAnswer":texts.get("details of the highest authority responsible for implementation and oversight of the business responsibility policy (ies).","Not Applicable"),

# #               },
# #               {
# #                 "questionNo": "3",
# #                 "question": "Does the entity have a specified Committee of the Board/ Director responsible for decision making on sustainability related issues? (Yes / No). If yes, provide details.",
                
# #                 "questionAnswer":texts.get("does the entity have a specified committee of the board/ director responsible for decision making on sustainability related issues? (yes / no). if yes, provide details.","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "4",
# #                 "question": "Indicate whether review was undertaken by Director / Committee of the Board/ Any other Committee",
# #                 "questionAnswer":texts.get("indicate whether review was undertaken by director / committee of the board/ any other committee","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "5",
# #                 "question": "Frequency(Annually/ Half yearly/ Quarterly/ Any other – please specify)",
# #                 "questionAnswer":texts.get("frequency(annually/ half yearly/ quarterly/ any other – please specify)","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "6",
# #                 "question": "Has the entity carried out independent assessment/ evaluation of the working of its policies by an external agency? (Yes/No). If yes, provide name of the agency.",
                
# #                 "questionAnswer":texts.get("has the entity carried out independent assessment/ evaluation of the working of its policies by an external agency? (yes/no). if yes, provide name of the agency.","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "7",
# #                 "question": "If answer to question (1) above is “No” i.e. not all Principles are covered by a policy, reasons to be stated, as below:",
# #                 "questionAnswer":texts.get("if answer to question (1) above is “no” i.e. not all principles are covered by a policy, reasons to be stated, as below:","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "8",
# #                 "question": "Upstream (Suppliers & Logistics Partners)",                
# #                 "questionAnswer":texts.get("upstream (suppliers & logistics partners)","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "9",
# #                 "question": "Downstream (Distributors & Customers)",                
# #                 "questionAnswer":texts.get("downstream (distributors & customers)","Not Applicable"),
# #               },
# #               ]},]
# #         },
# #     {
# #         "title": "PRINCIPLE WISE PERFORMANCE DISCLOSURE ",
# #         "section": "SECTION C",
# #         "Categories": [
# #             {
# #             "partRoman":"PRINCIPLE I",
# #             "categoryNo": "one",
# #             "subtitle": "Businesses should conduct and govern themselves with integrity, and in a manner that is Ethical, Transparent and Accountable",
# #             "questions": [
# #               {
# #                 "questionNo": "1",
# #                 "question": "Percentage coverage by training and awareness programmes on any of the Principles during the financial year:",
# #                 "questionAnswer":texts.get("percentage coverage by training and awareness programmes on any of the principles during the financial year:","Not Applicable"),
# #               },
# #               {
# #               "questionNo":"2",
# #               "question":"Details of fines / penalties /punishment/ award/ compounding fees/ settlement amount paid in proceedings (by the entity or by directors / KMPs) with regulators/ law enforcement agencies/ judicial institutions, in the financial year, in the following format (Note: the entity shall make disclosures on the basis of materiality as specified in Regulation 30 of SEBI (Listing Obligations and Disclosure Obligations) Regulations, 2015 and as disclosed on the entity’s website",
# #               "questionAnswer":texts.get("details of fines / penalties /punishment/ award/ compounding fees/ settlement amount paid in proceedings (by the entity or by directors / kmps) with regulators/ law enforcement agencies/ judicial institutions, in the financial year, in the following format (note: the entity shall make disclosures on the basis of materiality as specified in regulation 30 of sebi (listing obligations and disclosure obligations) regulations, 2015 and as disclosed on the entity’s website","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "3",
# #                 "question":"Monetary",
# #                 "questionAnswer":texts.get("monetary","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "4",
# #                 "question":"Non-Monetary",
# #                 "questionAnswer":texts.get("non-monetary","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "5",
# #                 "question": "Of the instances disclosed in Question 2 above, details of the Appeal/ Revision preferred in cases where monetary or non-monetary action has been appealed.",
# #                 "questionAnswer":texts.get("of the instances disclosed in question 2 above, details of the appeal/ revision preferred in cases where monetary or non-monetary action has been appealed.","Not Applicable"),
# #               },
# #                 {
# #                 "questionNo": "6",
# #                 "question": "Does the entity have an anti-corruption or anti-bribery policy? If yes, provide details in brief and if available, provide a web-link to the policy.",
# #                 "questionAnswer":texts.get("does the entity have an anti-corruption or anti-bribery policy? if yes, provide details in brief and if available, provide a web-link to the policy.","Not Applicable"),
# #               },
# #                 {
# #                 "questionNo": "7",
# #                 "question": "Number of Directors/KMPs/employees/workers against whom disciplinary action was taken by any law enforcement agency for the charges of bribery/ corruption",
# #                 "questionAnswer":texts.get("number of directors/kmps/employees/workers against whom disciplinary action was taken by any law enforcement agency for the charges of bribery/ corruption","Not Applicable"),
# #               },
# #                 {
# #                 "questionNo": "8",
# #                 "question": "Details of complaints with regard to conflict of interest",
# #                 "questionAnswer":texts.get("details of complaints with regard to conflict of interest","Not Applicable"),
# #               },
# #                 {
# #                 "questionNo": "9",
# #                 "question": "Provide details of any corrective action taken or underway on issues related to fines / penalties / action taken by regulators/ law enforcement agencies/ judicial institutions, on cases of corruption and conflicts of interest.",
# #                 "questionAnswer":texts.get("provide details of any corrective action taken or underway on issues related to fines / penalties / action taken by regulators/ law enforcement agencies/ judicial institutions, on cases of corruption and conflicts of interest.","Not Applicable"),
# #               },
# #                 {
# #                 "questionNo": "10",
# #                 "question": "Number of days of accounts payables ((Accounts payable *365) / Cost of goods/services procured) in the following format:",
# #                 "questionAnswer":texts.get("number of days of accounts payables ((accounts payable *365) / cost of goods/services procured) in the following format:","Not Applicable"),
# #               },
# #                 {
# #                 "questionNo": "11",
# #                 "question": "Provide details of concentration of purchases and sales with trading houses, dealers, and related parties along-with loans and advances & investments, with related parties, in the following format:",
# #                 "questionAnswer":texts.get("provide details of concentration of purchases and sales with trading houses, dealers, and related parties along-with loans and advances & investments, with related parties, in the following format:","Not Applicable"),
# #               },
# #                 {
# #                 "questionNo": "12",
# #                 "question": "Awareness programmes conducted for value chain partners on any of the Principles during the financial year:",
# #                 "questionAnswer":texts.get("awareness programmes conducted for value chain partners on any of the principles during the financial year:","Not Applicable"),
# #               },
# #                 {
# #                 "questionNo": "13",
# #                 "question": "Does the entity have processes in place to avoid/ manage conflict of interests involving members of the Board? (Yes/No) If Yes, provide details of the same.",
# #                 "questionAnswer":texts.get("does the entity have processes in place to avoid/ manage conflict of interests involving members of the board? (yes/no) if yes, provide details of the same.","Not Applicable"),
# #               }]},
# #             {
# #             "partRoman":"PRINCIPLE II",
# #             "categoryNo": "two",
# #             "subtitle": "Businesses should provide goods and services in a manner that is sustainable and safe",
# #             "questions": [
# #               {
# #                 "questionNo": "1",
# #                 "question": "Percentage of R&D and capital expenditure (capex) investments in specific technologies to improve the environmental and social impacts of product and processes to total R&D and capex investments made by the entity, respectively.",
# #                 "questionAnswer":texts.get("percentage of r&d and capital expenditure (capex) investments in specific technologies to improve the environmental and social impacts of product and processes to total r&d and capex investments made by the entity, respectively.","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "2",
# #                 "question": "Does the entity have procedures in place for sustainable sourcing? (Yes/No)",
# #                 "questionAnswer":texts.get("does the entity have procedures in place for sustainable sourcing? (yes/no)","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "3",
# #                 "question": "If yes, what percentage of inputs were sourced sustainably?",
# #                 "questionAnswer":texts.get("if there are any significant social or environmental concerns and/or risks arising from production or disposal of your products / services, as identified in the life cycle perspective / assessments (lca) or through any other means, briefly describe the same along-with action taken to mitigate the same.","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "4",
# #                 "question": "Describe the processes in place to safely reclaim your products for reusing, recycling and disposing at the end of life, for :",
# #                 "questionAnswer":texts.get("describe the processes in place to safely reclaim your products for reusing, recycling and disposing at the end of life, for :","Not Applicable"),
# #               },

# #               {
# #                 "questionNo": "5",
# #                 "question": "Whether Extended Producer Responsibility (EPR) is applicable to the entity’s activities (Yes / No). If yes, whether the waste collection plan is in line with the Extended Producer Responsibility (EPR) plan submitted to Pollution Control Boards? If not, provide steps taken to address the same.",
# #                 "questionAnswer":texts.get("whether extended producer responsibility (epr) is applicable to the entity’s activities (yes / no). if yes, whether the waste collection plan is in line with the extended producer responsibility (epr) plan submitted to pollution control boards? if not, provide steps taken to address the same.","Not Applicable"),
# #               },

# #               {
# #                 "questionNo": "6",
# #                 "question": "Has the entity conducted Life Cycle Perspective / Assessments (LCA) for any of its products (for manufacturing industry) or for its services (for service industry)? If yes, provide details in the following format?",
# #                 "questionAnswer":texts.get("has the entity conducted life cycle perspective / assessments (lca) for any of its products (for manufacturing industry) or for its services (for service industry)? if yes, provide details in the following format?","Not Applicable"),
# #               },

# #               {
# #                 "questionNo": "7",
# #                 "question": "If there are any significant social or environmental concerns and/or risks arising from production or disposal of your products / services, as identified in the Life Cycle Perspective / Assessments (LCA) or through any other means, briefly describe the same along-with action taken to mitigate the same.",
# #                 "questionAnswer":texts.get("if there are any significant social or environmental concerns and/or risks arising from production or disposal of your products / services, as identified in the life cycle perspective / assessments (lca) or through any other means, briefly describe the same along-with action taken to mitigate the same.","Not Applicable"),
# #               },

# #               {
# #                 "questionNo": "8",
# #                 "question": "Percentage of recycled or reused input material to total material (by value) used in production (for manufacturing industry) or providing services (for service industry)",
# #                 "questionAnswer":texts.get("percentage of recycled or reused input material to total material (by value) used in production (for manufacturing industry) or providing services (for service industry)","Not Applicable"),
# #               },

# #               {
# #                 "questionNo": "9",
# #                 "question": "Of the products and packaging reclaimed at end of life of products, amount (in metric tonnes) reused, recycled, and safely disposed, as per the following format:",
# #                 "questionAnswer":texts.get("of the products and packaging reclaimed at end of life of products, amount (in metric tonnes) reused, recycled, and safely disposed, as per the following format:","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "10",
# #                 "question": "Reclaimed products and their packaging materials (as percentage of products sold) for each product category.",
# #                 "questionAnswer":texts.get("reclaimed products and their packaging materials (as percentage of products sold) for each product category.","Not Applicable"),
# #               },]
# #             },
# #             {
# #             "partRoman":"PRINCIPLE III",
# #             "categoryNo": "three",
# #             "subtitle": "Businesses should respect and promote the well-being of all employees, including those in their value chains",
# #             "questions": [
# #               {
# #                 "questionNo": "1",
# #                 "question":"Details of measures for the well-being of employees:",
# #                 "questionAnswer":texts.get("details of measures for the well-being of employees:","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "2",
# #                 "question":"Details of measures for the well-being of workers:",
# #                 "questionAnswer":texts.get("details of measures for the well-being of workers:","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "3",
# #                 "question": "Details of retirement benefits, for Current and Previous FY",
# #                 "questionAnswer":texts.get("details of retirement benefits, for current and previous fy","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "4",
# #                 "question": "Accessibility of workplaces",
# #                 "questionAnswer":texts.get("accessibility of workplaces","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "5",
# #                 "question": "Does the entity have an equal opportunity policy as per the Rights of Persons with Disabilities Act, 2016? If so, provide a web-link to the policy.",
# #                 "questionAnswer":texts.get("does the entity have an equal opportunity policy as per the rights of persons with disabilities act, 2016? if so, provide a web-link to the policy.","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "6",
# #                 "question": "Return to work and Retention rates of permanent employees and workers that took parental leave.",
# #                 "questionAnswer":texts.get("return to work and retention rates of permanent employees and workers that took parental leave.","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "7",
# #                 "question": "Is there a mechanism available to receive and redress grievances for the following categories of employees and worker? If yes, give details of the mechanism in brief",
# #                 "questionAnswer":texts.get("is there a mechanism available to receive and redress grievances for the following categories of employees and worker? if yes, give details of the mechanism in brief","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "8",
# #                 "question": "Membership of employees and worker in association(s) or Unions recognised by the listed entity:",
# #                 "questionAnswer":texts.get("membership of employees and worker in association(s) or unions recognised by the listed entity:","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "9",
# #                 "question": "Details of training given to employees and workers:",
# #                 "questionAnswer":texts.get("details of training given to employees and workers:","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "10",
# #                 "question": "Details of performance and career development reviews of employees and workers:",
# #                 "questionAnswer":texts.get("details of performance and career development reviews of employees and workers:","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "11",
# #                 "question":"Whether an occupational health and safety management system has been implemented by the entity? (Yes/ No). If yes, the coverage such system?",
# #                 "questionAnswer":texts.get("whether an occupational health and safety management system has been implemented by the entity? (yes/ no). if yes, the coverage such system?","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "12",
# #                 "question":"What are the processes used to identify work-related hazards and assess risks on a routine and non-routine basis by the entity?",
# #                 "questionAnswer":texts.get("what are the processes used to identify work-related hazards and assess risks on a routine and non-routine basis by the entity?","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "13",
# #                 "question":"Whether you have processes for workers to report the work related hazards and to remove themselves from such risks. (Y/N)",
# #                 "questionAnswer":texts.get("whether you have processes for workers to report the work related hazards and to remove themselves from such risks. (y/n)","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "14",
# #                 "question":"Do the employees/ worker of the entity have access to non-occupational medical and healthcare services? (Yes/ No)",
# #                 "questionAnswer":texts.get("do the employees/ worker of the entity have access to non-occupational medical and healthcare services? (yes/ no)","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "15",
# #                 "question": "Details of safety related incidents, in the following format:",
# #                 "questionAnswer":texts.get("details of safety related incidents, in the following format:","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "16",
# #                 "question": "Describe the measures taken by the entity to ensure a safe and healthy work place",
# #                 "questionAnswer":texts.get("describe the measures taken by the entity to ensure a safe and healthy work place","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "17",
# #                 "question": "Number of Complaints on the following made by employees and workers:",
# #                 "questionAnswer":texts.get("number of complaints on the following made by employees and workers:","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "18",
# #                 "question": "Assessments for the year:",
# #                 "questionAnswer":texts.get("assessments for the year:","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "19",
# #                 "question": "Provide details of any corrective action taken or underway to address safety-related incidents (if any) and on significant risks / concerns arising from assessments of health & safety practices and working conditions.",
# #                 "questionAnswer":texts.get("provide details of any corrective action taken or underway to address safety-related incidents (if any) and on significant risks / concerns arising from assessments of health & safety practices and working conditions.","Not Applicable"),
# #               },
# #                 {
# #                 "questionNo": "20",
# #                 "question": "Does the entity extend any life insurance or any compensatory package in the event of death of (A) Employees (Y/N)",
# #                 "questionAnswer":texts.get("does the entity extend any life insurance or any compensatory package in the event of death of (a) employees (y/n)","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "21",
# #                 "question": "Provide the measures undertaken by the entity to ensure that statutory dues have been deducted and deposited by the value chain partners",
# #                 "questionAnswer":texts.get("provide the measures undertaken by the entity to ensure that statutory dues have been deducted and deposited by the value chain partners","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "22",
# #                 "question": "Provide the number of employees / workers having suffered high consequence work-related injury / ill-health / fatalities (as reported in Q11 of Essential Indicators above), who have been are rehabilitated and placed in suitable employment or whose family members have been placed in suitable employment:",
# #                 "questionAnswer":texts.get("provide the number of employees / workers having suffered high consequence work-related injury / ill-health / fatalities (as reported in q11 of essential indicators above), who have been are rehabilitated and placed in suitable employment or whose family members have been placed in suitable employment:","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "23",
# #                 "question": "Does the entity provide transition assistance programs to facilitate continued employability and the management of career endings resulting from retirement or termination of employment? (Yes/ No)",
# #                 "questionAnswer":texts.get("does the entity provide transition assistance programs to facilitate continued employability and the management of career endings resulting from retirement or termination of employment? (yes/ no)","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "24",
# #                 "question": "Details on assessment of value chain partners:",
# #                 "questionAnswer":texts.get("details on assessment of value chain partners:","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "25",
# #                 "question": "Provide details of any corrective actions taken or underway to address significant risks / concerns arising from assessments of health and safety practices and working conditions of value chain partners.",
# #                 "questionAnswer":texts.get("provide details of any corrective actions taken or underway to address significant risks / concerns arising from assessments of health and safety practices and working conditions of value chain partners.","Not Applicable"),
# #               },]
# #             },
# #             {
# #             "partRoman":"PRINCIPLE IV",
# #             "categoryNo": "four",
# #             "subtitle": "Businesses should respect the interests of and be responsive to all its stakeholders",
# #             "questions": [
# #               {
# #                 "questionNo": "1",
# #                 "question": "Describe the processes for identifying key stakeholder groups of the entity.",
# #                 "questionAnswer":texts.get("describe the processes for identifying key stakeholder groups of the entity.","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "2",
# #                 "question": "List stakeholder groups identified as key for your entity and the frequency of engagement with each stakeholder group.",
# #                 "questionAnswer":texts.get("list stakeholder groups identified as key for your entity and the frequency of engagement with each stakeholder group.","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "3",
# #                 "question": "Provide the processes for consultation between stakeholders and the Board on economic, environmental, and social topics or if consultation is delegated, how is feedback from such consultations provided to the Board.",
# #                 "questionAnswer":texts.get("provide the processes for consultation between stakeholders and the board on economic, environmental, and social topics or if consultation is delegated, how is feedback from such consultations provided to the board.","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "4",
# #                 "question": "Whether stakeholder consultation is used to support the identification and management of environmental, and social topics (Yes / No). If so, provide details of instances as to how the inputs received from stakeholders on these topics were incorporated into policies and activities of the entity",
# #                 "questionAnswer":texts.get("whether stakeholder consultation is used to support the identification and management of environmental, and social topics (yes / no). if so, provide details of instances as to how the inputs received from stakeholders on these topics were incorporated into policies and activities of the entity","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "5",
# #                 "question": "Provide details of instances of engagement with, and actions taken to, address the concerns of vulnerable/ marginalized stakeholder groups.",
# #                 "questionAnswer":texts.get("provide details of instances of engagement with, and actions taken to, address the concerns of vulnerable/ marginalized stakeholder groups.","Not Applicable"),
# #               },]
# #             },
# #             {
# #             "partRoman":"PRINCIPLE V",
# #             "categoryNo": "five",
# #             "subtitle": " Businesses should respect and promote human rights",
# #             "questions": [
# #               {
# #                 "questionNo": "1",
# #                 "question": "Employees and workers who have been provided training on human rights issues and policy(ies) of the entity, in the following format:",
# #                 "questionAnswer":texts.get("employees and workers who have been provided training on human rights issues and policy(ies) of the entity, in the following format:","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "2",
# #                 "question": "Details of minimum wages paid to employees and workers, in the following format:",
# #                 "questionAnswer":texts.get("details of minimum wages paid to employees and workers, in the following format:","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "3",
# #                 "question": "Details of remuneration/salary/wages, in the following format:",
# #                 "questionAnswer":texts.get("details of remuneration/salary/wages","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "4",
# #                 "question": "Do you have a focal point (Individual/ Committee) responsible for addressing human rights impacts or issues caused or contributed to by the business? (Yes/ No)",
# #                 "questionAnswer":texts.get("do you have a focal point (individual/ committee) responsible for addressing human rights impacts or issues caused or contributed to by the business? (yes/ no)","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "5",
# #                 "question": "Describe the internal mechanisms in place to redress grievances related to human rights issues.",
# #                 "questionAnswer":texts.get("","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "6",
# #                 "question": "Number of Complaints on the following made by employees and workers:",
# #                 "questionAnswer":texts.get("number of complaints on the following made by employees and workers:","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "7",
# #                 "question":"Complaints filed under the Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013, in the following format:",
# #                 "questionAnswer":texts.get("complaints filed under the sexual harassment of women at workplace (prevention, prohibition and redressal) act, 2013, in the following format:","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "8",
# #                 "question": "Mechanisms to prevent adverse consequences to the complainant in discrimination and harassment cases.",
# #                 "questionAnswer":texts.get("mechanisms to prevent adverse consequences to the complainant in discrimination and harassment cases.","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "9",
# #                 "question": "Do human rights requirements form part of your business agreements and contracts? (Yes/ No)",
# #                 "questionAnswer":texts.get("do human rights requirements form part of your business agreements and contracts? (yes/ no)","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "10",
# #                 "question": "Assessments for the year:",
# #                 "questionAnswer":texts.get("assessments for the year:","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "11",
# #                 "question": "Provide details of any corrective actions taken or underway to address significant risks / concerns arising from the assessments at Question 10 above.",
# #                 "questionAnswer":texts.get("provide details of any corrective actions taken or underway to address significant risks / concerns arising from the assessments at question 10 above.","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "12",
# #                 "question": "Details of a business process being modified / introduced as a result of addressing human rights grievances/complaints.",
# #                 "questionAnswer":texts.get("details of a business process being modified / introduced as a result of addressing human rights grievances/complaints.","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "13",
# #                 "question": "Details of the scope and coverage of any Human rights due-diligence conducted",
# #                 "questionAnswer":texts.get("details of the scope and coverage of any human rights due-diligence conducted","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "14",
# #                 "question": "Is the premise/office of the entity accessible to differently abled visitors, as per the requirements of the Rights of Persons with Disabilities Act, 2016?",
# #                 "questionAnswer":texts.get("is the premise/office of the entity accessible to differently abled visitors, as per the requirements of the rights of persons with disabilities act, 2016?","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "15",
# #                 "question": "Details on assessment of value chain partners:",
# #                 "questionAnswer":texts.get("details on assessment of value chain partners:","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "16",
# #                 "question": "Provide details of any corrective actions taken or underway to address significant risks / concerns arising from the assessments at Question 4 above.",
# #                 "questionAnswer":texts.get("provide details of any corrective actions taken or underway to address significant risks / concerns arising from the assessments at question 4 above.","Not Applicable"),
# #               },]
# #             },
# #             {  
# #           "partRoman":"PRINCIPLE VI",
# #           "categoryNo": "six",
# #           "subtitle": "Businesses should respect and make efforts to protect and restore",
# #           "questions": [
# #             {
# #               "questionNo": "1",
# #               "question": "Details of total energy consumption (in Joules or multiples) and energy intensity, in the following format:",
# #               "questionAnswer":texts.get("details of total energy consumption (in joules or multiples) and energy intensity, in the following format:","Not Applicable"),
# #             },
# #             {
# #               "questionNo": "2",
# #               "question": "Does the entity have any sites / facilities identified as designated consumers (DCs) under the Performance, Achieve and Trade (PAT) Scheme of the Government of India? (Y/N) If yes, disclose whether targets set under the PAT scheme have been achieved. In case targets have not been achieved, provide the remedial action taken, if any.",
# #               "questionAnswer":texts.get("does the entity have any sites / facilities identified as designated consumers (dcs) under the performance, achieve and trade (pat) scheme of the government of india? (y/n) if yes, disclose whether targets set under the pat scheme have been achieved. in case targets have not been achieved, provide the remedial action taken, if any.","Not Applicable"),
# #             },
# #             {
# #               "questionNo": "3",
# #               "question": "Provide details of the following disclosures related to water, in the following format:",
# #               "questionAnswer":texts.get("provide details of the following disclosures related to water, in the following format:","Not Applicable"),
# #             },

# #             {
# #               "questionNo": "4",
# #               "question": "Provide the following details related to water discharged:",
# #               "questionAnswer":texts.get("provide the following details related to water discharged:","Not Applicable"),
# #             },

# #             {
# #               "questionNo": "5",
# #               "question": "Has the entity implemented a mechanism for Zero Liquid Discharge? If yes, provide details of its coverage and implementation",
# #               "questionAnswer":texts.get("has the entity implemented a mechanism for zero liquid discharge? if yes, provide details of its coverage and implementation","Not Applicable"),
# #             },

# #             {
# #               "questionNo": "6",
# #               "question": "Please provide details of air emissions (other than GHG emissions) by the entity, in the following format:",
# #               "questionAnswer":texts.get("please provide details of air emissions (other than ghg emissions) by the entity, in the following format:","Not Applicable"),
# #             },

# #             {
# #               "questionNo": "7",
# #               "question": "Provide details of greenhouse gas emissions (Scope 1 and Scope 2 emissions) & its intensity, in the following format:",
# #               "questionAnswer":texts.get("provide details of greenhouse gas emissions (scope 1 and scope 2 emissions) & its intensity, in the following format:","Not Applicable"),
# #             },

# #             {
# #               "questionNo": "8",
# #               "question": "Does the entity have any project related to reducing Green House Gas emission? If Yes, then provide details.",
# #               "questionAnswer":texts.get("does the entity have any project related to reducing green house gas emission? if yes, then provide details.","Not Applicable"),
# #             },

# #             {
# #               "questionNo": "9",
# #               "question": "Provide details related to waste management by the entity, in the following format:",
# #               "questionAnswer":texts.get("provide details related to waste management by the entity, in the following format:","Not Applicable"),
# #             },

# #             {
# #               "questionNo": "10",
# #               "question": "Briefly describe the waste management practices adopted in your establishments. Describe the strategy adopted by your company to reduce usage of hazardous and toxic chemicals in your products and processes and the practices adopted to manage such wastes.",
# #               "questionAnswer":texts.get("briefly describe the waste management practices adopted in your establishments. describe the strategy adopted by your company to reduce usage of hazardous and toxic chemicals in your products and processes and the practices adopted to manage such wastes.","Not Applicable"),
# #             },

# #             {
# #               "questionNo": "11",
# #               "question": "If the entity has operations/offices in/around ecologically sensitive areas (such as national parks, wildlife sanctuaries, biosphere reserves, wetlands, biodiversity hotspots, forests, coastal regulation zones etc.) where environmental approvals / clearances are required, please specify details in the following format:",
# #               "questionAnswer":texts.get("if the entity has operations/offices in/around ecologically sensitive areas (such as national parks, wildlife sanctuaries, biosphere reserves, wetlands, biodiversity hotspots, forests, coastal regulation zones etc.) where environmental approvals / clearances are required, please specify details in the following format:","Not Applicable"),
# #             },

# #             {
# #               "questionNo": "12",
# #               "question": "Details of environmental impact assessments of projects undertaken by the entity based on applicable laws, in the current financial year:",
# #               "questionAnswer":texts.get("details of environmental impact assessments of projects undertaken by the entity based on applicable laws, in the current financial year:","Not Applicable"),
# #             },

# #             {
# #               "questionNo": "13",
# #               "question": "Is the entity compliant with the applicable environmental law/ regulations/ guidelines in India; such as the Water (Prevention and Control of Pollution) Act, Air (Prevention and Control of Pollution) Act, Environment protection act and rules thereunder (Y/N). If not, provide details of all such non-compliances, in the following format:",
# #               "questionAnswer":texts.get("is the entity compliant with the applicable environmental law/ regulations/ guidelines in india; such as the water (prevention and control of pollution) act, air (prevention and control of pollution) act, environment protection act and rules thereunder (y/n). if not, provide details of all such non-compliances, in the following format:","Not Applicable"),
# #             },

# #             {
# #               "questionNo": "14",
# #               "question": "Water withdrawal, consumption and discharge in areas of water stress (in kilolitres):",
# #               "questionAnswer":texts.get("water withdrawal, consumption and discharge in areas of water stress (in kilolitres):","Not Applicable"),
# #             },
            

# #             {
# #               "questionNo": "15",
# #               "question": "Please provide details of total Scope 3 emissions & its intensity, in the following format",
# #               "questionAnswer":texts.get("please provide details of total scope 3 emissions & its intensity, in the following format","Not Applicable"),
# #             },

# #             {
# #               "questionNo": "16",
# #               "question": "With respect to the ecologically sensitive areas reported at Question 10 of Essential Indicators above, provide details of significant direct & indirect impact of the entity on biodiversity in such areas along-with prevention and remediation activities",
# #               "questionAnswer":texts.get("with respect to the ecologically sensitive areas reported at question 10 of essential indicators above, provide details of significant direct & indirect impact of the entity on biodiversity in such areas along-with prevention and remediation activities","Not Applicable"),
# #             },

# #             {
# #               "questionNo": "17",
# #               "question": "If the entity has undertaken any specific initiatives or used innovative technology or solutions to improve resource efficiency, or reduce impact due to emissions / effluent discharge / waste generated, please provide details of the same as well as outcome of such initiatives, as per the following format:",
# #               "questionAnswer":texts.get("if the entity has undertaken any specific initiatives or used innovative technology or solutions to improve resource efficiency, or reduce impact due to emissions / effluent discharge / waste generated, please provide details of the same as well as outcome of such initiatives, as per the following format:","Not Applicable"),
# #             },

# #             {
# #               "questionNo": "18",
# #               "question": "Does the entity have a business continuity and disaster management plan? Give details in 100 words/ web link.",
# #               "questionAnswer":texts.get("does the entity have a business continuity and disaster management plan? give details in 100 words/ web link.","Not Applicable"),
# #             },

# #             {
# #               "questionNo": "19",
# #               "question": "Disclose any significant adverse impact to the environment, arising from the value chain of the entity. What mitigation or adaptation measures have been taken by the entity in this regard.",
# #               "questionAnswer":texts.get("disclose any significant adverse impact to the environment, arising from the value chain of the entity. what mitigation or adaptation measures have been taken by the entity in this regard.","Not Applicable"),
# #             },
# #             {
# #               "questionNo": "20",
# #               "question": "Percentage of value chain partners (by value of business done with such partners) that were assessed for environmental impacts.",
# #               "questionAnswer":texts.get("percentage of value chain partners (by value of business done with such partners) that were assessed for environmental impacts.","Not Applicable"),
# #             },
# #             {
# #               "questionNo": "21",
# #               "question": "How many Green Credits have been generated or procured:",
# #               "questionAnswer":texts.get("how many green credits have been generated or procured:","Not Applicable"),
# #             },
# #             {
# #               "questionNo": "22",
# #               "question": "By the listed entity",
# #               "questionAnswer":texts.get("by the listed entity","Not Applicable"),
# #             },
# #             {
# #               "questionNo": "23",
# #               "question": "By the top ten (in terms of value of purchases and sales,respectively) value chain partners",
# #               "questionAnswer":texts.get("By the top ten (in terms of value of purchases and sales,respectively) value chain partners","Not Applicable"),
# #             },]
# #           },
# #             {
# #           "partRoman":"PRINCIPLE VII",
# #           "categoryNo": "seven",
# #           "subtitle": " Businesses, when engaging in influencing public and regulatory policy, should do so in a manner that is responsible and transparent",
# #           "questions": [
# #             {
# #               "questionNo": "1",
# #               "question": "Number of affiliations with trade and industry chambers/ associations.",
# #               "questionAnswer":texts.get("number of affiliations with trade and industry chambers/ associations.","Not Applicable")
# #             },
# #             {
# #               "questionNo": "2",
# #               "question": "List the top 10 trade and industry chambers/ associations (determined based on the total members of such body) the entity is a member of/ affiliated to, in the following format",
# #               "questionAnswer":texts.get("list the top 10 trade and industry chambers/ associations (determined based on the total members of such body) the entity is a member of/ affiliated to, in the following format","Not Applicable")
# #             },
            
# #             {
# #               "questionNo": "3",
# #               "question": "Provide details of corrective action taken or underway on any issues related to anti-competitive conduct by the entity, based on adverse orders from regulatory authorities.",
# #               "questionAnswer":texts.get("provide details of corrective action taken or underway on any issues related to anti-competitive conduct by the entity, based on adverse orders from regulatory authorities.","Not Applicable")
# #             },
# #             {
# #               "questionNo": "4",
# #               "question": "Details of public policy positions advocated by the entity:",
# #               "questionAnswer":texts.get("details of public policy positions advocated by the entity:","Not Applicable")
# #             },]
# #           },
# #             {
# #             "partRoman":"PRINCIPLE VIII",
# #             "categoryNo": "eight",
# #             "subtitle": "Businesses should promote inclusive growth and equitable development",
# #             "questions": [
# #               {
# #                 "questionNo": "1",
# #                 "question": "Details of Social Impact Assessments (SIA) of projects undertaken by the entity based on applicable laws, in the current financial year.",
# #               "questionAnswer":texts.get("details of social impact assessments (sia) of projects undertaken by the entity based on applicable laws, in the current financial year.","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "2",
# #                 "question": "Provide information on project(s) for which ongoing Rehabilitation and Resettlement (R&R) is being undertaken by your entity, in the following format",
# #               "questionAnswer":texts.get("provide information on project(s) for which ongoing rehabilitation and resettlement (r&r) is being undertaken by your entity, in the following format","Not Applicable"),
# #                 },

# #               {
# #                 "questionNo": "3",
# #                 "question": "Describe the mechanisms to receive and redress grievances of the community.",
# #               "questionAnswer":texts.get("describe the mechanisms to receive and redress grievances of the community.","Not Applicable"),
# #                 },

# #               {
# #                 "questionNo": "4",
# #                 "question": "Percentage of input material (inputs to total inputs by value) sourced from suppliers",
# #               "questionAnswer":texts.get("percentage of input material (inputs to total inputs by value) sourced from suppliers","Not Applicable"),
# #                 },

# #               {
# #                 "questionNo": "5",
# #                 "question": "Job creation in smaller towns – Disclose wages paid to persons employed (including employees or workers employed on a permanent or non-permanent / on contract basis) in the following locations, as % of total wage cost",
# #               "questionAnswer":texts.get("job creation in smaller towns – disclose wages paid to persons employed (including employees or workers employed on a permanent or non-permanent / on contract basis) in the following locations, as % of total wage cost","Not Applicable"),
# #                 },

# #               {
# #                 "questionNo": "6",
# #                 "question": "Provide details of actions taken to mitigate any negative social impacts identified in the Social Impact Assessments (Reference: Question 1 of Essential Indicators above):",
# #               "questionAnswer":texts.get("provide details of actions taken to mitigate any negative social impacts identified in the social impact assessments (reference: question 1 of essential indicators above):","Not Applicable"),
# #                 },

# #               {
# #                 "questionNo": "7",
# #                 "question": "Provide the following information on CSR projects undertaken by your entity in designated aspirational districts as identified by government bodies",
# #               "questionAnswer":texts.get("provide the following information on csr projects undertaken by your entity in designated aspirational districts as identified by government bodies","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "8",
# #                 "question": "Do you have a preferential procurement policy where you give preference to purchase from suppliers comprising marginalized /vulnerable groups? (Yes/No)",
# #               "questionAnswer":texts.get("do you have a preferential procurement policy where you give preference to purchase from suppliers comprising marginalized /vulnerable groups? (yes/no)","Not Applicable"),
# #               },

# #               {
# #                 "questionNo": "9",
# #                 "question": "From which marginalized /vulnerable groups do you procure?",
# #               "questionAnswer":texts.get("from which marginalized /vulnerable groups do you procure?","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "10",
# #                 "question": "What percentage of total procurement (by value) does it constitute?",
# #               "questionAnswer":texts.get("what percentage of total procurement (by value) does it constitute?","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "11",
# #                 "question": "Details of the benefits derived and shared from the intellectual properties owned or acquired by your entity (in the current financial year), based on traditional knowledge:",
# #               "questionAnswer":texts.get("details of the benefits derived and shared from the intellectual properties owned or acquired by your entity (in the current financial year), based on traditional knowledge:","Not Applicable"),
# #               },

# #               {
# #                 "questionNo": "12",
# #                 "question": "Details of corrective actions taken or underway, based on any adverse order in intellectual property related disputes wherein usage of traditional knowledge is involved.",
# #               "questionAnswer":texts.get("details of corrective actions taken or underway, based on any adverse order in intellectual property related disputes wherein usage of traditional knowledge is involved.","Not Applicable"),
# #               },

# #               {
# #                 "questionNo": "13",
# #                 "question": "Details of beneficiaries of CSR Projects:",
# #               "questionAnswer":texts.get("details of beneficiaries of csr projects:","Not Applicable"),
# #               },]
# #             },
# #             {
# #             "partRoman":"PRINCIPLE IX",
# #             "categoryNo": "nine",
# #             "subtitle": "Businesses should engage with and provide value to their consumers in a responsible manner",
# #             "questions": [
# #               {
# #                 "questionNo": "1",
# #                 "question": "Describe the mechanisms in place to receive and respond to consumer complaints and feedback.",
# #               "questionAnswer":texts.get("describe the mechanisms in place to receive and respond to consumer complaints and feedback.","Not Applicable"),
# #                 },
# #               {
# #                 "questionNo": "2",
# #                 "question": "Turnover of products and/ services as a percentage of turnover from all products/service that carry information about:",
# #               "questionAnswer":texts.get("turnover of products and/ services as a percentage of turnover from all products/service that carry information about:","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "3",
# #                 "question": "Number of consumer complaints in respect of the following:",
# #               "questionAnswer":texts.get("number of consumer complaints in respect of the following:","Not Applicable"),
# #               },

# #               {
# #                 "questionNo": "4",
# #                 "question": "Details of instances of product recalls on account of safety issues:",
# #               "questionAnswer":texts.get("details of instances of product recalls on account of safety issues:","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "5",
# #                 "question": "Does the entity have a framework/policy on cyber security and risks related to data privacy? (Yes/No). If available, provide weblink of the policy.",
# #               "questionAnswer":texts.get("does the entity have a framework/policy on cyber security and risks related to data privacy? (yes/no). if available, provide weblink of the policy.","Not Applicable"),
# #               },

# #               {
# #                 "questionNo": "6",
# #                 "question": "Provide details of any corrective actions taken or underway on issues relating to advertising, and delivery of essential services; cyber security and data privacy of customers; re-occurrence of instances of product recalls; penalty / action taken by regulatory authorities on safety of products / services.",
# #               "questionAnswer":texts.get("provide details of any corrective actions taken or underway on issues relating to advertising, and delivery of essential services; cyber security and data privacy of customers; re-occurrence of instances of product recalls; penalty / action taken by regulatory authorities on safety of products / services.","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "7",
# #                 "question": "Channels / platforms where information on products and services of the entity can be accessed (provide web link, if available).",
# #               "questionAnswer":texts.get("channels / platforms where information on products and services of the entity can be accessed (provide web link, if available).","Not Applicable"),
# #               },

# #               {
# #                 "questionNo": "8",
# #                 "question": "Steps taken to inform and educate consumers about safe and responsible usage of products and/or services.",
# #               "questionAnswer":texts.get("steps taken to inform and educate consumers about safe and responsible usage of products and/or services.","Not Applicable"),
# #               },

# #               {
# #                 "questionNo": "9",
# #                 "question": "Mechanisms in place to inform consumers of any risk of disruption/discontinuation of essential services.",
# #               "questionAnswer":texts.get("mechanisms in place to inform consumers of any risk of disruption/discontinuation of essential services.","Not Applicable"),
# #               },

# #               {
# #                 "questionNo": "10",
# #                 "question": "Does the entity display product information on the product over and above what is mandated as per local laws? (Yes/No/Not Applicable) If yes, provide details in brief. Did your entity carry out any survey with regard to consumer satisfaction relating to the major products / services of the entity, significant locations of operation of the entity or the entity as a whole? (Yes/No)",
# #               "questionAnswer":texts.get("does the entity display product information on the product over and above what is mandated as per local laws? (yes/no/not applicable) if yes, provide details in brief. did your entity carry out any survey with regard to consumer satisfaction relating to the major products / services of the entity, significant locations of operation of the entity or the entity as a whole? (yes/no)","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "11",
# #                 "question": "Number of instances of data breaches along-with impact",
# #               "questionAnswer":texts.get("number of instances of data breaches along-with impact","Not Applicable"),
# #               },
# #               {
# #                 "questionNo": "12",
# #                 "question": "Percentage of data breaches involving personally identifiable information of customers",
# #               "questionAnswer":texts.get("provide the following information relating to data breaches:","Not Applicable"),
# #               },]
# #             }
# #           ]}
# #     ]}
        
     
     
        
# #           # 1. Save section

# #         filename = pdf.get_entity_name(data)
# #         print("filename", filename)
# #         table_name = filename

# #         PDFTable = create_pdf_model(table_name)

# #         # Track table creation order
# #         Base.metadata.create_all(bind=db.get_bind(), tables=[TableRegistry.__table__])
# #         existing = db.query(TableRegistry).filter_by(table_name=table_name).first()
# #         if not existing:
# #             registry_entry = TableRegistry(table_name=table_name)
# #             db.add(registry_entry)
# #             db.commit()

# #         # Create dynamic table if not exists
# #         PDFTable.__table__.create(bind=db.get_bind(), checkfirst=True)

# #         # Insert records
# #         for section_data in data.get("sections", []):
# #             if not section_data.get("title") or not section_data.get("section"):
# #                 continue

# #             section = section_data["section"]
# #             title = section_data["title"]

# #             for category in section_data.get("Categories", []):
# #                 if not category.get("categoryNo") or not category.get("subtitle"):
# #                     continue

# #                 categoryNo = category["categoryNo"]
# #                 subtitle = category["subtitle"]

# #                 for q in category.get("questions", []):
# #                     if not q.get("questionNo") or not q.get("question") or "questionAnswer" not in q:
# #                         continue

# #                     answer = q["questionAnswer"]
# #                     if isinstance(answer, list):
# #                         answer = json.dumps(answer)

# #                     record = PDFTable(
# #                         section=section,
# #                         title=title,
# #                         categoryNo=categoryNo,
# #                         subtitle=subtitle,
# #                         question_no=q["questionNo"],
# #                         question=q["question"],
# #                         answer=answer
# #                     )
# #                     db.add(record)

# #         db.commit()
# #         return {"status": "DONE"}


# @app.get("/download_pdf/")
# def get_last_table_data(db: Session = Depends(get_db)):
#     # Step 1: Get last registered table name
#     last_entry = db.query(TableRegistry).order_by(TableRegistry.created_at.desc()).first()
#     if not last_entry:
#         return {"message": "No table entries found"}

#     table_name = last_entry.table_name

#     # Step 2: Check if table exists in DB
#     inspector = inspect(db.get_bind())
#     if not inspector.has_table(table_name):
#         return {"message": f"Table '{table_name}' does not exist in the database"}

#     # Step 3: Dynamically create model for the table
#     PDFTable = create_pdf_model(table_name)

#     # Step 4: Query all rows
#     rows = db.query(PDFTable).all()

#     # Step 5: Convert rows to list of dicts
#     data = []
#     for row in rows:
#         row_dict = row.__dict__
#         row_dict.pop("_sa_instance_state", None)
#         data.append(row_dict)
#     # filename=pdf.get_entity_name(data)
#     filename=table_name
#     print("pdf name",filename)
#     pdf.create_pdf(data,filename)
#     # print("@@@@",data)
#     return data


# # router = APIRouter()

# @app.get("/report_list/", response_model=ReportListResponse)
# def get_all_table_datas(db: Session = Depends(get_db)):
#     """
#     Returns all dynamically created table names from table_registry.
#     """
#     tables = db.query(TableRegistry).order_by(TableRegistry.created_at.asc()).all()
#     name = [table.table_name for table in tables]
#     len_table=len(name)
#     created_date = [table.created_at for table in tables]    
#     period = ["FY 2024 -2026" for i in range(0,len_table)]
#     progress = [pdf.random_number() for i in range(0,len_table)]
#     status = ["Saved" for i in range(0,len_table)]
    
    
#     return ReportListResponse(
#         name=name,
#         created_date=created_date,
#         period=period,
#         progress=progress,
#         status=status
#     )

    
#     # return ReportListResponse(
#     #     name=["DEMO","jik"],
#     #     created_date=["27/4/2003","32/9/0989"],
#     #     period=["23233","dw3232"],
#     #     progress=[45,88],
#     #     status=["YES","No"]
#     # )





# @app.get("/download_pdf_report/{raw_table_name}")
# def download_pdf_report(raw_table_name: str, db: Session = Depends(get_db)):

#     # Step 1: Dynamically create model
#     PDFTable = create_pdf_model(raw_table_name)

#     # Step 2: Check if model is in metadata
#     if raw_table_name not in Base.metadata.tables:
#         return {"message": f"Model for table '{raw_table_name}' is not registered"}

#     # Step 3: Check if table exists in the database
#     inspector = inspect(db.get_bind())
#     if not inspector.has_table(raw_table_name):
#         return {"message": f"Table '{raw_table_name}' does not exist in the database"}

#     # Step 4: Query all rows
#     rows = db.query(PDFTable).all()

#     # Step 5: Convert to list of dicts
#     data = []
#     for row in rows:
#         row_dict = row.__dict__.copy()
#         row_dict.pop("_sa_instance_state", None)
#         data.append(row_dict)

#     # Step 6: Create PDF (optional)
#     print("pdf name:", raw_table_name)
#     pdf.create_pdf(data, raw_table_name)

#     return {"table": raw_table_name, "data": data}



# if __name__ == "__main__":
#   uvicorn.run("create:app", host="0.0.0.0", port=5000, reload=False, log_level="debug")