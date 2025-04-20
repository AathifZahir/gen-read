import zipfile
import os

# exclude certain folders like node modules
# so what i have to do is, get the filename, check extension, 
# then if code, add the filename with directory and content to a var or list
# after loop ends, add the content to a txt with unique name
# also invoke ai function by sending unique name
# handle errors

exclude_list = ["node_modules", ".git"]


def main():
    try:
        if zipfile.is_zipfile('./backend/controllers/snap-link.zip'):
            with zipfile.ZipFile('./backend/controllers/snap-link.zip', "r") as file:
                for filename in file.namelist():
                    if any(exclude in filename for exclude in exclude_list):
                        continue
                    else:
                        print(filename)
                        print(file.read(filename))
                        
                        
        else:
            print("File is not a zip file")
       # with zipfile.ZipFile('./backend/controllers/snap-link.zip') as file:                        

            # ZipFile.namelist() returns a list containing all the members with names of an archive file
            #print(file.namelist()[-1])

            #file.printdir()

            # ZipFile.getinfo(path = filepath) returns the information about a member of Zip file.
            # It raises a KeyError if it doesn't contain the mentioned file
           # print(file.getinfo(file.namelist()[-1]))

            # ZipFile.open(path = filepath, mode = mode_type, pwd = password) opens the members of an archive file
            # 'pwd' is optional -> if it has password mention otherwise leave it
           # text_file = file.open(name = file.namelist()[-1], mode = 'r')

            # 'read()' method of the file prints all the content of the file. You see this method in file handling.
            #print(text_file.read())  

            # You must close the file if you don't open a file using 'with' keyword
            # 'close()' method is used to close the file
           #text_file.close()

            # ZipFile.extractall(path = filepath, pwd = password) extracts all the files to current directory
            #file.extractall()
            # after executing check the directory to see extracted files

    except zipfile.BadZipFile:
        print('Error: Zip file is corrupted')
    except zipfile.LargeZipFile:
        print('Error: Large file')

if __name__ == '__main__': main()