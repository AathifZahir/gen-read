# file_handler.py
import os
from zipfile import ZipFile
from utils.config import IGNORE_EXTENSIONS, IGNORE_DIRS

# Function to check if a file should be ignored

def should_ignore(file_path: str) -> bool:
    # Normalize path for cross-platform compatibility
    file_path = file_path.replace("\\", "/")
    
    # Ignore if any parent folder matches
    for folder in file_path.split("/"):
        if folder in IGNORE_DIRS:
            return True

    # Ignore if file has undesired extension
    for ext in IGNORE_EXTENSIONS:
        if file_path.endswith(ext):
            return True

    return False

# Refactored function for handling uploaded ZIP files
async def handle_uploaded_zip(file) -> dict:
    file_path = f"/tmp/{file.filename}"
    
    # Save the uploaded zip file
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    
    # Extract the zip file and filter out ignored files
    extracted_files = []
    with ZipFile(file_path, "r") as zip_ref:
        for zip_file in zip_ref.namelist():
            if not should_ignore(zip_file):
                zip_ref.extract(zip_file, "/tmp/")
                extracted_files.append(zip_file)
    
    return {"extracted_files": extracted_files}
