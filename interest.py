p = float(input("Enter the principal amount : "))
t = float(input("Enter the duration : "))
if p<200000:
    r = 10.0
elif p>=200000 and p<1000000 :
    r =12.0
elif p>=1000000:
    r =15.0
si = (p*r*t)/100
print('Simple Interest :',si)