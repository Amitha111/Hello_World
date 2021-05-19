import os

def reanameFilesUsingWalk(location):
    i =1
    for root, dirs, files in os.walk(location, topdown = False):
        for name in files:
            print("first for ", os.path.join(root, name))
            realFileName = os.path.join(root, name)
            break_up = os.path.splitext(realFileName)
            file_name = break_up[0]
            file_ext = break_up[1]
            new_name = file_name + "new"  + str(i) + file_ext
            os.rename(realFileName, new_name)
            i +=2
        for name in dirs:
            print("second for ",os.path.join(root, name))

path = input("Enter your file directory location")
location = str(path)
reanameFilesUsingWalk(location)
print("Done Renaming Please Verify !!!!")