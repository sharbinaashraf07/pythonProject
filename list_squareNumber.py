n=int(input("enter the numbers"))
list=[]
for x in range(n):
  x=int(input("enter a number"))
  list.append(x)

print(list)
slist=[x**2 for x in list]
print(slist)