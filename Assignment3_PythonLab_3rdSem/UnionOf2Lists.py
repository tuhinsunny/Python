str1 = input("Enter the 1st list : ")
str2 = input("Enter the 2nd list : ")
list1 = str1.split()
list2 = str2.split()
union = list(set(list1) | set(list2)) #| is used to union
print("Union of 2 lists : \n")
print(union)