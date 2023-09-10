"""
Write a program to find the distinct pair of numbers whose product is odd from a list of integers.
"""
str = input("Enter the elements of the list1 : ")
lst = str.split()
lst = [int(num) for num in lst]
pairs = []
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if (lst[i]*lst[j])%2 == 1:
            pairs.append((lst[i],lst[j]))
for i in pairs:
    print(i)