n=int(input("Enter the value of n : "))
a=0
b=1
if n==1:
    print("0")
elif n==2:
    print("0 1 ")
else:
    print("0 1 ",end="")
    for i in range(3,n+1):
        sum=a+b
        a=b
        b=sum
        print(sum,end=" ")