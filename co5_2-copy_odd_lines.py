f=open("file.txt","r")
f1=open("files.txt","w")
count=0
for x in f:
    count+=1
    if(count%2==0):
        f1.write(x)
f1=open("files.txt","r")
print(f1.read())