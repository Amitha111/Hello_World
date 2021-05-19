import os
import os.path, time




def rename_file_1(a):  
    i = 0
    print("location is - ",a)
    for files in os.scandir(a):
      
        print(files.path)
        break_up = os.path.splitext(files.path)
        file_name = break_up[0]
        file_ext = break_up[1]
        new_name = file_name + "new"  + str(i) + file_ext
        os.rename(files, new_name)
        i +=1

path = input("Enter your file directory location")
location = str(path)
rename_file_1(location)
print("Done Renaming Please Verify !!!!")
    

    


