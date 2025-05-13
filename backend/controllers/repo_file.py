import os
from git import Repo
import shortuuid

exclude_list = ["package-lock.json", "README.md"]

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

txt = ""


def print_repo_files(repo_url):
    repo_name = repo_url.split("/")[-1].split(".")[0]
    temp_id = shortuuid.random(length=4)
    os.makedirs("./backend/temp/repos/" + repo_name + temp_id, exist_ok=True)
    local_dir = "./backend/temp/repos/" + repo_name + temp_id
    repo = Repo.clone_from(repo_url, local_dir)
    """
    Prints all files in a Git repository.

    Args:
        repo_path (str): Path to the Git repository.
    """
    try:
        # Get the latest commit
        head_commit = repo.head.commit
        # Traverse the repository tree
        print_tree(head_commit.tree)
    except Exception as e:
        print(f"An error occurred: {e}")


def print_tree(tree, indent=""):
    """
    Recursively prints files and directories in a Git tree.

    Args:
        tree (git.objects.tree.Tree): Git tree object.
        indent (str): Indentation for printing.
    """
    global txt
    for item in tree:
        txt += item.abspath.split("repos\\")[-1]
        print(f"{item.abspath.split('repos\\')[-1]}")
        if any(exclude in item.name for exclude in exclude_list):
            continue
        if item.type == "tree":
            print_tree(item, indent + "  ")
        elif item.type == "blob":
            # If it's a file (blob), read and print content
            blob = item.data_stream.read().decode("utf-8")
            print(f"{blob}")
            txt += blob


def repoFile(url):
    print_repo_files(url)
    return txt
