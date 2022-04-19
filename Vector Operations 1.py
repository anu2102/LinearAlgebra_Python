#Addition of the Vectors
n=int(input("Enter the Dimension of Vectors: "))
v1=[]
v2=[]
res=0
ans=[]
for i in range (n):
    v1.append(int(input("Enter the Element in vector 1: ")))
for i in range (n):
    v2.append(int(input("Enter the Element in vector 2: ")))
for i in range (n):
    res =  v1[i] + v2[i]
    ans.append(res)
print("Vector 1 is ",v1, "\n")
print("Vector 2 is ",v2, "\n")
print("Addition of vector 1 and vector 2 is : ",ans, "\n")

#Scalar Multiplication
res=0
result=[]
snum=int(input("Enter the Scalar number: "))
for i in range (n):
    res = snum * v1[i]
    result.append(res)
print("Scalar Multiplication of vector 1 is: ", result, "\n")

#Dot product
dot=0
for i in range (n):
    dot += v1[i]*v2[i]
print("Dot product of both vectors is: ",dot, "\n" )

# Norm of a Vector
m=0
for i in range (n):
    m +=v1[i]*v1[i]
norm = m**(1/2) 
print("Norm of Vector 1 is: ",norm, "\n")
m2=0
for i in range (n):
    m2 +=v2[i]*v2[i]
norm2 = m2**(1/2)
print("Norm of Vector 2 is: ",norm2, "\n")   

#Distance between  Vectors
p=0
for i in range (n):
    p += ((v1[i] - v2[i] )**2)
dist = p**(1/2)
print("Distance between vector 1 and 2 is : ",dist, "\n")


#Cosin  Angle
angle= dot/(norm * norm2)
print("The Cosin angle between vector 1 and 2 is : ",angle, "\n")


#Projection of a vector on another
proj=0
for i in range (n):
    proj = (dot/(m2))*v1[i]
    print(proj, end=" , ""\n")

# finding unit vector
unit=0
for i in range(n):
    unit = (v1[i]/norm)
print("Unit vector of 1 is: ",unit)

unit2=0
for i in range(n):
    unit2 = (v2[i]/norm2)
print("Unit vector of 2  is: ",unit2)
