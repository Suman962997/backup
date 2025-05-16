from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import os
import force
app = FastAPI()

# Define the path where you want to store the uploaded file
UPLOAD_DIR = "uploads"

# Make sure the upload directory exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    
    with open(file_location, "wb") as f:
        f.write(await file.read())  # Write the content of the uploaded file to the location
    print(force.Details_of_business(file_location,"Details of business activities"))
    return JSONResponse(content={"file_path": file_location})

