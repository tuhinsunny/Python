str1 = input("Enter the elements of the list1 : ")
str2 = input("Enter the elements of the list2 : ")
list1 = str1.split()
list2 = str2.split()
newList = [i for i in list2 if i not in list1]
print(newList)