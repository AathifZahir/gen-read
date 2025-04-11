from fastapi import FastAPI, UploadFile, File
from utils.file_utils import handle_zip_upload

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "AI README Generator backend is up!"}

@app.post("/upload-zip")
async def upload_zip(file: UploadFile = File(...)):
    result = await handle_zip_upload(file)
    return {"status": "success", "files": result}
