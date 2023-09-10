st = input("Enter a sentence : ")
vowels = "AEIOUaeiou"
cnt = 0
for ch in st :
    if ch in vowels :
        cnt+=1
print("The number of vowels :",cnt)