list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 12, 13, 14]
for i in list:
    if i % 2 == 0:
        list.remove(i)

print(list)
