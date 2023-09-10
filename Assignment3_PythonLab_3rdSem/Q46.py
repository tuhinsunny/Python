tup = ()
n = int(input("Enter the number of elements to insert: "))
print("Enter the elements :")
for i in range(n):
    ele=int(input())
    tup += (ele,)
unique = []
duplicate = []
for i in tup:
    if tup.count(i) == 1:
        unique.append(i)
    else:
        if i not in duplicate:
            duplicate.append(i)
print("Unique elements:", unique)
print("Duplicate elements:", duplicate)