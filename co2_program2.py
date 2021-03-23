#Fibonacci series of N terms .
n=int(input("enter the number"))
coun=1
n1=0
n2=1
sum=0
print("fibanacci series:\n",end='')
while(coun<=n):
    print(sum,end="\n")

    coun+=1
    n1=n2
    n2=sum
    sum=n1+n2
