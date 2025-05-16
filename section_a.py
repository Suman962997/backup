# from fastapi import FastAPI, UploadFile, File, Form
# from fastapi.responses import JSONResponse
# import fitz  # PyMuPDF
# import tempfile


# async def Details_of_business(file: UploadFile = File(...),search_text:str):
#     if not file.filename.endswith(".pdf"):
#         return JSONResponse(status_code=400, content={"error": "Only PDF files are supported"})

#     found_pages = []
#     print("File sent sucessfully",file.name)
#     print("search sring",search_text)

#     with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
#         tmp.write(await file.read())
#         tmp_path = tmp.name

#     try:
#         doc = fitz.open(tmp_path)
#         for page_num, page in enumerate(doc, start=1):
#             text = page.get_text()
#             if search_text.lower() in text.lower():
#                 start_index = text.lower().find(search_text.lower())
#                 snippet = text[start_index:start_index+200]
#                 found_pages.append({
#                     "page": page_num,
#                     "snippet": snippet.strip()
#                 })
#         doc.close()
#     except Exception as e:
#         return JSONResponse(status_code=500, content={"error": str(e)})

#     return {"matches": found_pages}
