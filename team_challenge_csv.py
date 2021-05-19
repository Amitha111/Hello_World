import csv

with open('employee.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    lin_count = 0
    for row in csv_reader:
        if lin_count == 0:
            print(f'Column Names are {",".join(row)}')
            lin_count+=1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            lin_count+=1
