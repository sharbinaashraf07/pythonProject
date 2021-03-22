#Create a single string separated with space from two strings by swapping the
#character at position 1.
a="hai world"
s=a.split(" ")
q=s[0]
n=q[0]
e=s[1]

m=e[0]


j=q.replace(n,m)
k=e.replace(m,n)

print(j+" "+k)