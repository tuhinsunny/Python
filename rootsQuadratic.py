import math
print("Enter the values of coefficients a,b and c : ")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
det = b*b - 4*a*c
if det>0:
    root1 = (-b + math.sqrt(det))/(2*a)
    root2 = (-b - math.sqrt(det))/(2*a)
    print("Root1 :",root1)
    print("Root2 :",root2)
    print("Roots are real and distinct")
elif det==0:
    root1 = -b/(2*a)
    print("Roots are :",root1,"and",root1)
    print("Roots are real and equal")
else:
    r = -b/(2*a)
    img = math.sqrt(-det)/(2*a)
    print("Roots are real and imaginary")
    print("Roots are :\n",r,"+",img,end ="i ")
    print("and",r,"+",img,end ="i")