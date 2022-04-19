def trans(T_matrix,vec,equi):
    res=vec_to_my_space(equi.copy(),vec.copy())
    res2=[]
    for i in range(2):
        sum1=0
        for j in range(1):
            for k in range(2):
                sum1+=T_matrix[i][k]*res[k][j]
        res2.append([sum1])
    equi1=inverse(equi)    
    final_res=[]
    for i in range(2):
        sum1=0
        for j in range(1):
            for k in range(2):
                sum1+=equi1[i][k]*res2[k][j]
        final_res.append(sum1)
    return final_res.copy()

def inverse(matrix):
    matrix1 = [[0, 0], [0, 0]]
    temp=matrix[0][0]
    matrix1[0][0]=matrix[1][1]
    matrix1[1][1]=matrix[0][0]
    matrix1[1][0]=-matrix[1][0]
    matrix1[0][1]=-matrix[0][1]
    deter=(matrix[0][0]*matrix[1][1])-(matrix[1][0]*matrix[0][1])
    for i in range(2):
        for j in range(2):
            matrix1[i][j]/=deter
    return matrix1

def vec_to_my_space(equi,vec):
    res=[]
    for i in range(2):
        sum1=0
        for j in range(1):
            for k in range(2):
                sum1+=equi[i][k]*vec[k][j]
        res.append([sum1])
    return res.copy()

def my_space_to_vect(equil1,my_space):
    equil=equil1.copy()
    equi1=inverse(equil)
    res=[]
    for i in range(2):
        sum1=0
        for j in range(1):
            for k in range(2):
                sum1+=equi1[i][k]*my_space[k][j]
        res.append(sum1)
    return res.copy()
    
V1=[]
equivalent=[]
V2=[]
transformation=[]
print("Enter values for vector 1 ")
for i in range(2):
    V1.append([int(input())])
print("Enter values for vector 2")
for i in range(2):
    V2.append([int(input())])
print("Enter vector 1 basis equivalent to vector 2 basis")
for i in range(2):
    temp=[]
    for j in range(2):
        temp.append(int(input()))
    equivalent.append(temp)
print("Enter Transformation vector")
for i in range(2):
    temp=[]
    for j in range(2):
        temp.append(int(input()))
    transformation.append(temp)

res=vec_to_my_space(equivalent.copy(),V1.copy())
print("Vector 1 in Vector 2's co-ordinates will be")
print(res)
res=my_space_to_vect(equivalent.copy(),V2.copy())
print("Vector 2 in Vector 1 co-ordinates will be")
print(res)
print("The transformation in vector 1's co-ordinate system is: ")
transformed=trans(transformation.copy(),V1.copy(),equivalent.copy()).copy()
print(transformed)
