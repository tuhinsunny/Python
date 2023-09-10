r1 = int(input("Enter the number of rows of first matrix : "))
c1 = int(input("Enter the number of columns of first matrix : "))
r2 = int(input("Enter the number of rows of second matrix : "))
c2 = int(input("Enter the number of columns of second matrix : "))
mat1 = []
mat2 = []
print("Enter the elements of the first matrix : ")
for i in range(r1):
    row = []
    for j in range(c1):
        ele = int(input())
        row.append(ele)
    mat1.append(row)

print("Enter the elements of the second matrix : ")
for i in range(r2):
    row = []
    for j in range(c2):
        ele = int(input())
        row.append(ele)
    mat2.append(row)
#checking whether multiplication is possible
if c1 != r2 :
    print("Multiplication is not possible")
else :
    #creating a result matrix filled with 0s
    result = [[0 for i in range(c2)] for i in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += mat1[i][k]*mat2[k][j]

print("The product of the matrices :")
for i in result:
    print(i)