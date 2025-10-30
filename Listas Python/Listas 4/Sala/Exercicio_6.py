A=[]
print("Valores de uma lista A: ")
for i in range(0,8):
    A.append(int(input(f"Valor {i+1}: ")))

B=[0]*8
print("Valores de uma lista B: ")
for i in range(0,8):
    B[i]=A[i]**2
    print(f"Valor {i+1}: {B[i]}")