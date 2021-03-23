#Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly.
n=input("enter a text:")
b=n[-3:]
if b=='ing':
    y=n.replace(b,'ly')
    print(y)
else:
    z=n.replace(b,'ing')
    print(z)
