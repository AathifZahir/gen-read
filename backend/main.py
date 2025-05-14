# main.py
from fastapi import FastAPI, File, UploadFile
from controllers.zip_file import zipper
from controllers.repo_file import repoFile
from controllers.ai_transform import gemini_transform
import os
import aiofiles
from datetime import datetime

CHUNK_SIZE = 1024 * 1024


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/zip")
async def zipfile(file: UploadFile = File(...)):
    filepath = os.path.join(
        "./temp/zips",
        os.path.basename(datetime.now().strftime("%Y%m%d%H%M%S") + file.filename),
    )
    async with aiofiles.open(filepath, "wb") as f:
        while chunk := await file.read(CHUNK_SIZE):
            await f.write(chunk)
    filepath = filepath.replace("\\", "/")
    print(filepath)
    txt = zipper(filepath)
    print(txt)
    return gemini_transform(txt)


@app.post("/repo")
async def repofile(url):
    txt = repoFile(url)
    print(txt)
    return gemini_transform(txt)


@app.post("/gemini")
async def geminiapi(txt):
    return gemini_transform(txt)


# add a method for custom input by user
