#Print out all colors from color-list1 not contained in color-list2.
list1=["orange","red","blue"]
list2=["red","black","brown"]
cr=[]

for x in list1:
    for i in list2:
       if i==x:
            break
    else:
            cr.append(x)
print(cr)