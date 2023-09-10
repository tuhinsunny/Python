str1 = input("Enter the items of list1 : ")
str2 = input("Enter the items of list2 : ")
list1 = str1.split()
list2 = str2.split()
concatList = [x for sublist in [list1, list2] for x in sublist]
print(concatList)