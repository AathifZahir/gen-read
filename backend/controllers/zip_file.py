import zipfile
import os

exclude_list = ["node_modules", ".git"]


def zipper(url):
    try:
        txt = ""
        if zipfile.is_zipfile(url):
            with zipfile.ZipFile(url, "r") as file:
                for filename in file.namelist():
                    if any(exclude in filename for exclude in exclude_list):
                        continue
                    else:
                        txt += filename
                        txt += file.read(filename)

        else:
            print("File is not a zip file")

        print(txt)
        return txt

    except zipfile.BadZipFile:
        print("Error: Zip file is corrupted")
    except zipfile.LargeZipFile:
        print("Error: Large file")
