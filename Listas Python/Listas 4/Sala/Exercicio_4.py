A=[]
print("Valores de uma lista A: ")
for i in range(0,5):
    A.append(int(input(f"Valor {i+1}: ")))

B=[]
print("Valores de uma lista B: ")
for i in range(0,5):
    B.append(int(input(f"Valor {i+1}: ")))

C=[0]*10
print("Valores de uma lista C: ")
for i in range(0,10):
    if i<5:
        C[i]=A[i]
    else:
        C[i]=B[i-5]
    print(f"Valor {i+1}: {C[i]}")

