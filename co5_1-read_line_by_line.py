import csv
with open("file.txt","r")as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)