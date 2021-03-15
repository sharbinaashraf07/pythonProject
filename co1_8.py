#replace a first character with '$' except first character.
a=input("enter the string")
b=a[0]
a=a.replace(b,'$')
print(b+a[1:])
