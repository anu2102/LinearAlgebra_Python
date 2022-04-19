import math
n=3
def cross_product(vectorA,vectorB,cross_P):
    cross_P.append(vectorA[1]*vectorB[2]-vectorA[2]*vectorB[1])
    cross_P.append(vectorA[2]*vectorB[0]-vectorA[0]*vectorB[2])
    cross_P.append(vectorA[0]*vectorB[1]-vectorA[1]*vectorB[0])

if __name__=='__main__':
    vectorA=[1,2,3]
    vectorB=[4,5,6]:
    cross_P=[]

print("Cross product: ",end=" ")
cross_product(vectorA,vectorB,cross_P)

for i in range(0,n):
    print(cross_P[i],end=" ")
print("\n")

def conjugate(s):
    z=s
    l=len(s)
    i=0
    if(s.find('+') != -1):
        i=s.find('+')
        s=s.replace('+','-')
    else:
        i=s.find('-')
        s=s.replace('-','+',1)

    print("Conjugate of ",z," = ",s)

def conjugate(s):
    conju = s.conjugate()
    print("Conjugate of complex number: ")
    print(conju)
    
def mod(x):
    modulus = abs(x)
    print("Modulus of complex number: ")
    print(modulus)
    
def add(a,b):
    complex1 = (a) + (b)
    print("Addition of two complex numbers: ")
    print(complex1)
    
def mul(a,b):
    complex2 = (a) * (b)
    print("Multiplication of two complex numbers: ")
    print(complex2)

def div(a,b):
    complex3 = (a) / (b)
    print("Division of two complex numbers:  ")
    print(complex3)
    
comp = complex(input("Enter a number in (a +bj) form: "))
conjugate(comp)
comp1= complex(input("Enter a number in (a +bj) form: "))
conjugate(comp1)


add(comp1,comp)
mul(comp1,comp)
div(comp1,comp)

x=complex(3,4)
mod(x)

print("Conjugate ",x.conjugate())
