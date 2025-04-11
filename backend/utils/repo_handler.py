# repo_handler.py
import os
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

# Refactored function for handling GitHub repo clone
def handle_github_clone(repo_url: str) -> dict:
    # Clone the repo to a temporary folder
    repo_name = repo_url.split("/")[-1]
    temp_dir = f"/tmp/{repo_name}"
    
    os.system(f"git clone {repo_url} {temp_dir}")
    
    # Filter out ignored files in the cloned repository
    cloned_files = []
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if not should_ignore(file_path):
                cloned_files.append(file_path)
    
    return {"cloned_files": cloned_files}
