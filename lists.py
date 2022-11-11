list=[1,"Hello",True,2,6]
print(list)
print(type(list))
#extracting elements
print(list[2])
print(list[1:5])
#changing the element
list[0]="Tuhin"
print(list)
#pop the last element
print(list.pop())
#to add a new element
list.append("Sparta")
print(list)
list2=[1,2,3,4,5]
print(list+list2)
list.reverse()
print(list)
#sorting 
list2.sort()
print(list2)
list2.insert(2,"Hello")
print(list2)
#concatenate
print(list+list2)