x=int(input("enter first"))
y=int(input("enter second"))
z=int(input("enter third"))
if (x >= y) and (x >= z):
  largest = x
elif (y >= x) and (y >= z):
  largest = y
else:
  largest = z
print("the largest numbers is",largest)