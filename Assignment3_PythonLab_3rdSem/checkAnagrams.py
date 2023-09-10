str1 = input("Enter 1st Sentence : ")
str2 = input("Enter 2nd sentence : ")
#replacing the spaces with nothing
str1 = str1.lower().replace(' ','')
str2 = str2.lower().replace(' ','')
#checking if lenghts are same
if len(str1) != len(str2):
    print("Not Anagrams ")
    exit()
#converting the strings to lists and sorting the list
list1 = sorted(list(str1))
list2 = sorted(list(str2))
if list1 == list2:
    print("Anagrams")
else :
    print("Not Anagrams")