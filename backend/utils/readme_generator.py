# utils/readme_generator.py
import os
from utils.config import IGNORE_EXTENSIONS, IGNORE_DIRS

def collect_code_files(directory):
    code_files = []
    for root, dirs, files in os.walk(directory):
        # Remove ignored directories from walk
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            ext = os.path.splitext(file)[1]
            if ext in IGNORE_EXTENSIONS:
                continue

            filepath = os.path.join(root, file)
            code_files.append(filepath)

    return code_files


def summarize_code(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
        return f"### {os.path.basename(filepath)}\n\nThis file contains code that needs summarizing.\n"
    except Exception as e:
        return f"### {os.path.basename(filepath)}\n\nError reading file: {e}\n"


def generate_readme_summary(code_dir):
    files = collect_code_files(code_dir)
    readme_sections = [f"# Project Summary\n\nFound {len(files)} relevant files.\n"]

    for f in files:
        summary = summarize_code(f)
        readme_sections.append(summary)

    return "\n".join(readme_sections)
