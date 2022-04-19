R1 = int(input("Enter the number of rows in Matrix 1: "))
C1 = int(input("Enter the number of columns in Matrix 1: "))

R2 = int(input("Enter the number of rows in Matrix 2: "))
C2 = int(input("Enter the number of columns in Matrix 2: "))

matrix1=[]
print("Enter the numbers for first matrix:")
for i in range(R1):
    a=[]
    for j in range(C1):
        a.append(int(input()))
    matrix1.append(a)

for i in range(R1):
    for j in range(C1):
        print(matrix1[i][j],end=" ")
    print()


matrix2=[]
print("Enter the numbers for second matrix:")
for i in range(R2):
    b=[]
    for j in range(C2):
        b.append(int(input()))
    matrix2.append(b)

for i in range(R2):
    for j in range(C2):
        print(matrix2[i][j],end=" ") 
    print()

#addition of Matrix
print("Addition of Two matrix")    
addmatrix=[]
for i in range(R1):
    list3=[]
    for j in range(C1):
        list3.append(matrix1[i][j] + matrix2[i][j])
    addmatrix.append(list3)

for i in range(R2):
    for j in range(C2):
        print(addmatrix[i][j],end=" ")
    print()

#multiplication of matrix
i=j=k=0
mul_matrix = []
for i in range(R1):
    c=[]
    for j in range(C1):
        res=0
        for k in range(R2):
            res = res + (matrix1[i][k] * matrix2[k][j])
        c.append(res)
    mul_matrix.append(c)

print("Multiplication of Matrix is: ")
for i in range(R2):
    for j in range(C2):
        print(mul_matrix[i][j],end=" ")
    print()
