str = input("Enter the list of elements of atleast 15 items : ")
lst = str.split()
if len(lst) < 15 : 
    print("Enter atleast 15 items")
    exit()
lst = list(set(lst))
print(lst)