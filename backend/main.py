from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from utils.file_handler import handle_uploaded_zip

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI README Generator backend running"}

@app.post("/upload-zip")
async def upload_zip(file: UploadFile = File(...)):
    result = await handle_uploaded_zip(file)
    return JSONResponse(content=result)
