A=[]
print("Valores de uma lista A: ")
for i in range(0,5):
    A.append(int(input(f"Valor {i+1}: ")))

B=[]
print("Valores de uma lista B: ")
for i in range(0,5):
    B.append(int(input(f"Valor {i+1}: ")))

C=[0]*5
print("Valores da lista C (A-B):")
for i in range(0,5):
    C[i]=A[i]-B[i]
    print((f"Valor {i+1}: {C[i]}"))