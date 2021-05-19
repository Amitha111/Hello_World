infile = open("python.txt", "r" )

alist = []

pstring = infile.readline()
print(pstring)
while pstring:
    alist.append(pstring)
#pstring = infile.readline()  

infile.close()

blist = []

for elem in alist:
    elem1 = elem.upper()
    blist.append(elem1)

outfile = open("python1.txt", "w")

for elem2 in blist:
    outfile.write(elem2 + '\n')

outfile.close()
