import os 
import os.path, time


def rename_files(location):
    i = 0
    for filename, in os.scandir(location):
        print(filename.path)
        rename = "updated" + str(i) + ".docx"
        rename = location +"\\"+ rename
        print("renamed file",rename)
        os.rename(filename.path, rename)
        i += 1
        print("Last Modified: %s" %time.ctime(os.path.getmtime(location)))


path = input("Enter your file directory location")
location = str(path)
rename_files(location)
print("Done Renaming Please Verify !!!!")

