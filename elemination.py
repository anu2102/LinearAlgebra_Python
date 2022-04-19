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
equ6 = []

for i in range(len(equ1)):
    equ4.append(equ1[i] / equ1[0])
    equ5.append(equ2[i] / equ2[0])
    equ6.append(equ3[i] / equ3[0])
print("Equation 4 is: ",equ4)
print("Equation 5 is: ",equ5)
print("Equation 6 is: ",equ6)

ans1 = []
ans2 = []
for i in range(len(equ1)):
    ans1.append(equ4[i] - equ5[i])
    ans2.append(equ4[i] - equ6[i])
print("Answer1: ",ans1)
print("Answer 2: ",ans2)

for i in range(1, len(equ1)):
    ans1[i] /= ans1[1]
    ans2[i] /= ans2[1]
print("Answer 1: ",ans1)
print("Answer 2: ",ans2)

fin = []
for i in range(len(equ1)):
    fin.append(ans1[i] - ans2[i])

z = fin[3]/fin[2]
y = -ans2[3] + (ans2[2]*z)
x = equ4[3] - (equ4[1]*y + equ4[2]*z)

print("Value of x = " + str(x))
print("Value of y = " + str(y))
print("Value of z = " + str(z))
