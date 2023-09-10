tup = ()
pairs = []
n = int(input("Enter the number of elements to insert: "))
print("Enter the elements :")
for i in range(n):
    ele=int(input())
    tup += (ele,)
for i in range(n):
    for j in range(i+1, n):
        if (tup[i]*tup[j])%2 == 0:
            pairs.append((tup[i],tup[j]))
for i in pairs:
    print(i)