equ1 = []
equ1.append(int(input("Enter x coordinate of 1st Equation: ")))
equ1.append(int(input("Enter y coordinate of 1st Equation: ")))
equ1.append(int(input("Enter z coordinate of 1st Equation: ")))
equ1.append(int(input("Enter r coordinate of 1st Equation: ")))

equ2 = []
equ2.append(int(input("Enter x coordinate of 2nd Equation: ")))
equ2.append(int(input("Enter y coordinate of 2nd Equation: ")))
equ2.append(int(input("Enter z coordinate of 2nd Equation: ")))
equ2.append(int(input("Enter r coordinate of 2nd Equation: ")))

equ3 = []
equ3.append(int(input("Enter x coordinate of 3rd Equation: ")))
equ3.append(int(input("Enter y coordinate of 3rd Equation: ")))
equ3.append(int(input("Enter z coordinate of 3rd Equation: ")))
equ3.append(int(input("Enter r coordinate of 3rd Equation: ")))

equ4 = []
equ5 = []
for i in range(len(equ1)):
    equ4.append(equ1[i]*equ2[1] - equ2[i]*equ2[1])
    equ5.append(equ1[i]*equ2[1] - equ3[i]*equ1[1])
ans1=[]
for i in range(len(equ1)):
    ans1.append(equ4[i]*equ5[2]- equ5[i]*equ4[2])

equ4 = []
equ5 = []

for i in range(len(equ1)):
    equ4.append(equ1[i]*equ2[i]*equ2[0])
    equ5.append(equ1[i]*equ3[i]*equ1[0])
ans2=[]
for i in range(len(equ1)):
    ans2.append(equ4[i]*equ5[2]- equ5[i]*equ4[2])

equ4 = []
equ5 = []
for i in range(len(equ1)):
    equ4.append(equ1[i]*equ2[0]-equ2[i]*equ1[0])
    equ5.append(equ1[i]*equ3[0]-equ3[i]*equ1[0])
ans3=[]
for i in range(len(equ1)):
    ans3.append(equ4[i]*equ5[1]- equ5[i]*equ4[1])


ans1[3] /= ans1[0]
ans1[0] /= ans1[0]
ans2[3] /= ans2[1]
ans2[1] /= ans2[1]
ans3[3] /= ans3[2]
ans3[2] /= ans3[2]

print("Row canonical form is: ")
print(ans1)
print(ans2)
print(ans3)

