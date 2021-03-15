#Store a list of first names. Count the occurrences of ‘a’ within the list

s=["apple","banana","orange"]
count=0
for x in s:
    for i in x:
        if 'a' in i:
            count=count+1
print(count)


