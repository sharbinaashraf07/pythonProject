#Sort dictionary in ascending and descending order.
m1={
    "n[1]":50,
    "n[5]":15,
    "n[3]":30

}
print("Ascending")
for i in sorted(m1.items()):

    print({i})
print("descending")
for x in sorted(m1.items(),reverse=True):
    print({x})
