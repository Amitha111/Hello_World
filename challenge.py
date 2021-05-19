
al1 = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]

bl2 = ["Sarah", "John", "Victor", "Linda", "Sandra", "Lorie", "Elli", "Nora", "Jenny", "Helen"]

for name in bl2:
    print(bl2)

str1 = "This is a challenge which I choose for myself!"
list1 = list(str1.split(" "))
print(list1)

a1 = input("Who took the Challenge? ")
b1 = str(a1)
print(b1 + " took the challenge")
   

diction = (dict(zip(al1, bl2)))
print(diction)

import csv


a_file = open ("python.txt", "r")
txt_li = [(line.strip()).split() for line in a_file]
a_file.close()
print(txt_li)

k1 = txt_li
if any ("Python" in word for word in txt_li):
    print(len("Python"))




    
    
