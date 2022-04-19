import math
matrix1 = []
for i in range(2):
    temp = []
    for j in range(2):
        temp.append(int(input("Enter the " + str(i) + str(j) + " coordinate of matrix: ")))
    matrix1.append(temp)

a = 1
b = -(matrix1[0][0] + matrix1[1][1])
c = (matrix1[0][0]*matrix1[1][1]) - (matrix1[0][1]*matrix1[1][0])
temp = math.sqrt(b*b - 4*a*c)
ans1 = -b - temp
ans2 = -b + temp
ans1 /= 2*a
ans2 /= 2*a

if str(ans1).endswith(".0") and str(ans2).endswith(".0"):
    print("Eigen Values are:")
    print(ans1)
    print(ans2)

    eigen1 = [[matrix1[0][0]-ans1, matrix1[0][1]], [matrix1[1][0], ans1 - matrix1[1][1]]]
    eigen2 = [[matrix1[0][0]-ans2, matrix1[0][1]], [matrix1[1][0], ans2 - matrix1[1][1]]]

    x1 = -eigen1[0][1]/eigen1[0][0]
    x2 = (-eigen1[0][0]*x1)/eigen1[0][1]

    print("Updated Vector 1 is : ")
    print(x1)
    print(x2)

    x1 = -eigen2[0][1]/eigen2[0][0]
    x2 = -eigen2[0][0]*x1

    print("Updated Vector 2 is : ")
    print(x1)
    print(x2)
else:
    print("No Eigen Vectors found" )
