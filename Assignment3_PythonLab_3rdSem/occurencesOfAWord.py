#accepting a string from the user in a variable
str = input("Enter a sentence from the user: ")
cnt = 0
for ch in str:
    if ch == ' ':
        cnt+=1
print("Number of words :",cnt+1)