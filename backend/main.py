from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import JSONResponse
from utils.file_handler import handle_uploaded_zip
from utils.repo_handler import handle_github_clone
from schemas.schemas import RepoCloneRequest


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI README Generator backend running"}

@app.post("/upload-zip")
async def upload_zip(file: UploadFile = File(...)):
    result = await handle_uploaded_zip(file)
    return JSONResponse(content=result)

@app.post("/repo-clone")
async def repo_clone(body: RepoCloneRequest):
    result = handle_github_clone(body.url)
    return JSONResponse(content=result)