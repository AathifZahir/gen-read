import zipfile
import tempfile
import os

IGNORE_LIST = ['.env', 'node_modules', '.git', '__pycache__', 'dist', 'build']

async def handle_uploaded_zip(file):
    with tempfile.TemporaryDirectory() as tmpdir:
        zip_path = os.path.join(tmpdir, file.filename)
        with open(zip_path, "wb") as buffer:
            buffer.write(await file.read())

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(tmpdir)

        files = []
        for root, dirs, filenames in os.walk(tmpdir):
            dirs[:] = [d for d in dirs if d not in IGNORE_LIST]
            for name in filenames:
                if any(ignored in name for ignored in IGNORE_LIST):
                    continue
                full_path = os.path.join(root, name)
                rel_path = os.path.relpath(full_path, tmpdir)
                if not rel_path.endswith(".zip"):
                    files.append(rel_path)


        return {"extracted_files": files}
