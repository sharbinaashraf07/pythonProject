#Enter 2 lists of integers. Check (a) Whether list are of same length (b) whether list sums
#to same value (c) whether any value occur in both

list1=[4,5,12,10,11,13]
list2=[11,23,24,4,3]
list3=[]
print(len(list1))
print(len(list2))

if len(list1)==len(list2):
      print("both list are of same length")
else:
  print("both list are diffrent length")


print("the sum of list1=",sum(list1))
print("the sum of list2=",sum(list2))
if sum(list1)==sum(list2):
    print(sum(list1))
else:
    print("differnt sums")

for i in list1:
  for i in list2:
    if i not in list3:
      list3.append(i)
print(list3)      