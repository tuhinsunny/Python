tup = ()
n = int(input("Enter the number of elements to add: "))
print("Enter the elements :")
for i in range(n):
    ele=int(input())
    tup += (ele,)
print(tup)