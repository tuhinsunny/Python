"""
n=input("Enter a number : ")
num=n[::-1]
if n==num:
    print("Number is palindrome")
else:
    print("Number is not palindrome")
"""
n=int(input("Enter a number : "))
rev=0
num=n
while(num>0):
    rev=(rev*10)+(num%10)
    num=num//10
if n==rev:
    print("Palindrome")
else:
    print("Not Palindrome")