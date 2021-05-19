infile = open("reptiles.txt", "r")

replist = []

pstring = infile.readline()
while pstring:
    replist.append(pstring)
    pstring = infile.readline()
    print(len(replist))
