n=int(input("Enter the value of n : "))
if n==0:
    print("The factorial of 0 is 1")
else:
    fact=1
    for i in range (1,n+1):
        fact=fact*i
    print("The factorial of",n,"is", fact)