import csv

with open('anynewtext.csv') as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=",")
    lc=0
    for row in csv_reader:
        if lc==0:
            lc+=1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            lc+=1
    print(f'Processed {lc} lines.')
