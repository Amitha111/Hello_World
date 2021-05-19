import os
from typing import Counter

srcDirectory = r"C:\Users\13148\Desktop\Python_Final"
i = 1
for f, in os.scandir(srcDirectory):
    print(f.path)
    split_tup = os.path.splitext(f.path)
    print(split_tup)
  
# extract the file name and extension
    file_name = split_tup[0]
    file_extension = split_tup[1]
  
    print("File Name: ", file_name)
    print("File Extension: ", file_extension)

    #srcFileNamme =  srcDirectory+f.path
    destFileName  = file_name+'_new'+str(i) + file_extension
    print("DEST FILE NAME = ",destFileName)
    os.rename(f.path,destFileName)
    i += 1
    
      
print('done !!!')

    