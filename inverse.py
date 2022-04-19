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

#transpose of matrix1
Tmatrix1 = []
print("Transpose of first matrix")
for i in range(R1):
    list1 = []
    for j in range(C1):
        list1.append(matrix1[j][i])
    Tmatrix1.append(list1)

for i in range(R1):
    for j in range(C1):
        print(Tmatrix1[i][j],end=" ")
    print()

#transpose of matrix2
Tmatrix2 = []
print("Transpose of second matrix")
for i in range(R2):
    list2 = []
    for j in range(C2):
        list2.append(matrix2[j][i])
    Tmatrix2.append(list2)

for i in range(R2):
    for j in range(C2):
        print(Tmatrix2[i][j],end=" ")
    print()


#Inverse of matrix 1
print("\n")
if(len(matrix1) == 2):
    data = matrix1[0][0]
    matrix1[0][0] = matrix1[1][1]
    matrix1[1][1] = data
    
    determinant = ((matrix1[0][0] * matrix1[1][1]) - (matrix1[1][0] * matrix1[0][1]))
    print("Determinant of matrix 1",determinant, "\n")

    cofactor = []
    for i in range(R1):
        n = []
        for j in range(C1):
            data = pow(-1,(i+j)) * matrix1[i][j]
            data*=(1//determinant)
            n.append(data)
        cofactor.append(n)
    print("Inverse of Matrix 1 is ", cofactor, "\n")

#for matrix 2
print("\n")
if(len(matrix2) == 2):
    data1 = matrix2[0][0]
    matrix2[0][0] = matrix2[1][1]
    matrix2[1][1] = data1
    
    determinant = ((matrix2[0][0] * matrix2[1][1]) - (matrix2[1][0] * matrix2[0][1]))
    print("Determinant of matrix 2 ",determinant, "\n")

    cofactor = []
    for i in range(R2):
        n = []
        for j in range(C2):
            data1 = pow(-1,(i+j)) * matrix2[i][j]
            data1*=(1//determinant)
            n.append(data1)
        cofactor.append(n)

    print("Cofactor of Matrix 2 is ",cofactor, "\n")


#inveerse for matrix1 of 3x3
print("\n")
if(len(matrix1) == 3):
    Dmatrix=0
    Dmatrix=(matrix1[0][0]*((matrix1[1][1]*matrix1[2][2] )- (matrix1[1][2]*matrix1[2][1]))
                - matrix1[0][1]*((matrix1[1][0]*matrix1[2][2] )- (matrix1[1][2]*matrix1[2][0]))
                + matrix1[0][2]*((matrix1[1][0]*matrix1[2][1] )- (matrix1[1][1]*matrix1[2][0])))
    print("The Determinant of 3x3 matrix 1 is :", Dmatrix, "\n")

    cofactor1 = []
    data2=0
    for i in range(R1):
        cofac1 = []
        for j in range(C1):
            data2 = pow(-1,(i+j)) * matrix1[i][j]
            data2*=(1/Dmatrix)
            cofac1.append(data2)
        cofactor1.append(cofac1)
    print("The Cofactor of the matrix is:")
    for i in range(R1):
        for j in range(C1):
            print(cofactor1[i][j],end=" ")
        print()

#for matrix 2 3x3
print("\n")
if(len(matrix2)==3):
    Dmatrix1=0
    Dmatrix1=(matrix2[0][0]*((matrix2[1][1]*matrix2[2][2] )- (matrix2[1][2]*matrix2[2][1]))
                - matrix2[0][1]*((matrix2[1][0]*matrix2[2][2] )- (matrix2[1][2]*matrix2[2][0]))
                + matrix2[0][2]*((matrix2[1][0]*matrix2[2][1] )- (matrix2[1][1]*matrix2[2][0])))
    print("The Determinant of 3x3 matrix 2 is :", Dmatrix1, "\n")

    cofactor1 = []
    data3=0
    for i in range(R2):
        cofac1 = []
        for j in range(C2):
            data3 = pow(-1,(i+j)) * matrix2[i][j]
            data3*=(1/Dmatrix1)
            cofac1.append(data3)
        cofactor1.append(cofac1)

        
    print("The Cofactor of the matrix is:")
    for i in range(R2):
        for j in range(C2):
            print(cofactor1[i][j],end=" ")
        print()
            
























