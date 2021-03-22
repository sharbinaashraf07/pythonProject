def Merge(dict1, dict2):
    return dict2.update(dict1)


dict1 = {'n1': 10, 'n2': 8}
dict2 = {'m1': 6, 'm2': 4}

Merge(dict1, dict2)
print("Merge done \n ", dict2)