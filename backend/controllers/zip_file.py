import zipfile
import os

exclude_list = [
    "node_modules",
    ".git",
    ".vscode",
    "__MACOSX",
    ".DS_Store",
]
include_list = [
    ".py",
    ".js",
    ".ts",
    ".html",
    ".css",
    ".java",
    ".c",
    ".cpp",
    ".cs",  # Code files
    ".go",
    ".rb",
    ".php",
    ".swift",
    ".kt",
    ".rs",
    ".sh",
    ".bat",  # More code files
    ".md",  # Markdown files
]


def zipper(url):
    try:
        print(url)
        txt = ""
        if zipfile.is_zipfile(url):
            with zipfile.ZipFile(url, "r") as file:
                for filename in file.namelist():
                    # Exclude files or folders in the exclude list
                    if any(exclude in filename for exclude in exclude_list):
                        continue

                    # Include only files with extensions in the include list
                    if any(filename.lower().endswith(ext) for ext in include_list):
                        try:
                            # Read and decode the file content
                            content = file.read(filename).decode(
                                "utf-8", errors="ignore"
                            )
                            txt += f"--- {filename} ---\n"  # Add filename as a header
                            txt += content + "\n\n"  # Add file content
                        except Exception as e:
                            print(f"Error reading file {filename}: {e}")
                    else:
                        continue

        else:
            print("File is not a zip file")
            return "File is not a zip file"

        print(txt)
        return txt

    except zipfile.BadZipFile:
        print("Error: Zip file is corrupted")
        return "Error: Zip file is corrupted"
    except zipfile.LargeZipFile:
        print("Error: Large file")
        return "Error: Large file"
