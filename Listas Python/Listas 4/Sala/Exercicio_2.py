import math
A=[]
print("Entre com os valores de uma lista A com 6 valores")
for i in range(0,6):
    A.append(int(input(f"Valor {i+1}: ")))

print("Os respectivos valores de B para a lista A é: ")
B=[0]*6
for i in range(0,6):
    B[i]=math.factorial(A[i])
    print(f"Valor {i+1}: {B[i]}")