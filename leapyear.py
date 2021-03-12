year1=int(input("enter the current year:"))
year2=int(input("enter the last year:"))
for i in range(year1,year2+1):
  if(i%4==0 and i%100!=0 or i%400==0):
    print(i)
  i+=1