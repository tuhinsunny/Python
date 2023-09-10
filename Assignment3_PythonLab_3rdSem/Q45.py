tup = ()
mean =0
n = int(input("Enter the number of elements to insert: "))
print("Enter the elements :")
for i in range(n):
    ele=int(input())
    tup += (ele,)
    mean = mean + ele
print("Mean : ", mean/len(tup))